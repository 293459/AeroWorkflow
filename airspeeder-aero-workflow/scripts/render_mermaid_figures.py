"""Extract Mermaid diagrams from a Markdown file and render them as images.

The script prefers a local Mermaid CLI (`mmdc`) when available. If it is not
installed, it falls back to the Kroki Mermaid endpoint and writes both SVG and
PNG files so the diagrams can be used in Markdown previews and LaTeX reports.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import urllib.request
from dataclasses import dataclass, asdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "examples" / "industry_examples.md"
DEFAULT_OUTPUT = ROOT / "report" / "figures" / "industry_examples"


@dataclass
class Diagram:
    index: int
    title: str
    slug: str
    markdown_heading: str
    mmd_path: str
    svg_path: str
    png_path: str


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text[:80] or "diagram"


def extract_blocks(markdown: str) -> list[tuple[str, str]]:
    """Return pairs of (nearest heading, mermaid code block)."""
    pattern = re.compile(r"(^## .+?$)|```mermaid\s*\n(.*?)```", re.MULTILINE | re.DOTALL)
    current_heading = "Untitled Mermaid Diagram"
    blocks: list[tuple[str, str]] = []

    for match in pattern.finditer(markdown):
        heading, block = match.groups()
        if heading:
            current_heading = heading.replace("##", "", 1).strip()
        elif block:
            blocks.append((current_heading, block.strip() + "\n"))

    return blocks


def render_with_mmdc(mmd_path: Path, svg_path: Path, png_path: Path) -> bool:
    mmdc = shutil.which("mmdc")
    if not mmdc:
        return False

    commands = [
        [mmdc, "-i", str(mmd_path), "-o", str(svg_path), "-b", "white"],
        [mmdc, "-i", str(mmd_path), "-o", str(png_path), "-b", "white", "-s", "2"],
    ]

    for command in commands:
        subprocess.run(command, check=True)
    return True


def kroki_render(diagram: str, fmt: str) -> bytes:
    request = urllib.request.Request(
        f"https://kroki.io/mermaid/{fmt}",
        data=diagram.encode("utf-8"),
        method="POST",
        headers={
            "Content-Type": "text/plain",
            "User-Agent": "Mozilla/5.0",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def render_with_kroki(diagram: str, svg_path: Path, png_path: Path) -> None:
    svg_path.write_bytes(kroki_render(diagram, "svg"))
    png_path.write_bytes(kroki_render(diagram, "png"))


def render_all(source: Path, output_dir: Path) -> list[Diagram]:
    markdown = source.read_text(encoding="utf-8")
    blocks = extract_blocks(markdown)
    output_dir.mkdir(parents=True, exist_ok=True)

    diagrams: list[Diagram] = []
    for index, (heading, block) in enumerate(blocks, start=1):
        slug = f"{index:02d}_{slugify(heading)}"
        mmd_path = output_dir / f"{slug}.mmd"
        svg_path = output_dir / f"{slug}.svg"
        png_path = output_dir / f"{slug}.png"

        mmd_path.write_text(block, encoding="utf-8")
        if not render_with_mmdc(mmd_path, svg_path, png_path):
            render_with_kroki(block, svg_path, png_path)

        diagrams.append(
            Diagram(
                index=index,
                title=heading,
                slug=slug,
                markdown_heading=heading,
                mmd_path=str(mmd_path.relative_to(ROOT)),
                svg_path=str(svg_path.relative_to(ROOT)),
                png_path=str(png_path.relative_to(ROOT)),
            )
        )

    manifest_json = output_dir / "manifest.json"
    manifest_json.write_text(
        json.dumps([asdict(diagram) for diagram in diagrams], indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    manifest_md = output_dir / "manifest.md"
    rows = [
        "# Mermaid Figure Manifest",
        "",
        f"Source: `{source.relative_to(ROOT)}`",
        "",
        "| # | Heading | PNG | SVG | MMD |",
        "|---:|---|---|---|---|",
    ]
    for diagram in diagrams:
        rows.append(
            f"| {diagram.index} | {diagram.title} | `{diagram.png_path}` | "
            f"`{diagram.svg_path}` | `{diagram.mmd_path}` |"
        )
    manifest_md.write_text("\n".join(rows) + "\n", encoding="utf-8")

    return diagrams


def main() -> int:
    source = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_SOURCE
    output_dir = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else DEFAULT_OUTPUT

    diagrams = render_all(source, output_dir)
    print(f"Rendered {len(diagrams)} Mermaid diagrams into {output_dir}")
    for diagram in diagrams:
        print(f"- {diagram.index:02d}: {diagram.title} -> {diagram.png_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
