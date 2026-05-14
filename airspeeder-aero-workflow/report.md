---
name: ai-learn-report
description: >
  Use this skill to generate academic/technical report chapters following the
  "Weinig Standard": rigorous, visually scannable, didactic, and coherent.
  Triggers on: "write a report chapter on [TOPIC]", "generate a technical report
  section", "document [TOPIC] in academic style", or any request for a structured
  Markdown/LaTeX academic document. Produces Notion-ready Markdown with LaTeX math,
  symbol tables, image placeholders, and trade-off analyses.
license: MIT
---

# AI LEARN — Report Skill (Weinig Standard)

Generate academic and technical report chapters with a rigorous, visually scannable,
didactic, and internally consistent style.

## Context
- **Source material:** [ATTACH PDF/NOTES/DATA — required]
- **Integration notes:** [ADD STUDENT NOTES — leave blank if none]
- **Output:** Notion-ready Markdown + LaTeX math. Sections will be manually reordered
  and numbered by the student — **do not add section numbers**.
- **Language:** Technical English — formal, precise, "Expert Peer" register.

---

## 1. Content Structure

**Decimal numbering** for all sub-headings when the student requests numbering
(e.g. 3.4, 3.4.1). Default: use `##` and `###` headers only, no numbers.

**Micro-sections:** Keep paragraphs short and focused on a single logical concept.
No "walls of text". Each section answers exactly one question.

**"Why" logic:** For every design choice, parameter selection, or formula introduced,
add a dedicated sub-section or inline justification:
- *"Why this parameter is used: ..."*
- *"Critical note on reference frame choice: ..."*

**Concept order (apply to each concept):**
1. Intuitive explanation — the "why" in simple, discursive prose (no formulas yet)
2. Formal definition — `> blockquote` format for strict academic definitions
3. Mathematical derivation — step by step, justifying every non-trivial passage;
   mark approximations: *(Approximation: [reason it is valid])*
4. Key Takeaways — 3–5 bullets: minimum a student must know for an exam on this topic

---

## 2. Typography and Math

**Strategic bold:** Bold key terms and technical vocabulary on first occurrence only.
No mid-sentence bolding after that. No bold without semantic reason.

**LaTeX (mandatory):**
- All variables, formulas, and units: inline LaTeX `$...$` (e.g. `$C_D$`, `$\rho$`)
- Main equations: display LaTeX `$$...$$` (one equation per block)
- Never write variables as plain text (e.g. write `$k$` not just "k")

**Bullet points:** Use only to list properties, graph observations, or trade-offs.
Never use bullets where prose narrative would be clearer.

---

## 3. Visual Elements and Tables

**Image placeholders:** Every geometry, physical setup, or numerical result that
would benefit from a figure must include a descriptive tag:
```
[Insert Figure: Description of what the plot shows, axis labels, key trends]
[Insert Diagram: Description of the geometry or system]
```

**Definition table** — at the start or end of complex sections:
| Symbol | Definition | Physical meaning |
|--------|-----------|-----------------|
| $C_D$ | Drag coefficient | Ratio of drag force to dynamic pressure × reference area |

**Trade-off / comparison table** — for final commentary sections:
| Scenario A | Scenario B | Criterion |
|-----------|-----------|-----------|
| High solidity | Low solidity | Efficiency |

---

## 4. Scientific Rigour

**Physical interpretation:** Every formula must be followed immediately by a sentence
explaining its physical meaning (e.g. *"This expression measures what fraction of
kinetic energy is converted to pressure."*)

**Limit analysis:** For every key result, verify and state the behaviour at boundary
conditions (e.g. what happens as $k \to 0$ or $k \to 1$).

**Source fidelity:** Reproduce all content from the source material without compression.
A student who reads only this chapter must lose no significant information from the original.

**Handwritten notes in source:** Include if they add non-redundant information.
Transcribe as-is (may be Italian or English). If unclear, reconstruct from context
and flag: *(reconstructed from handwritten note)*.

**URLs:** Include as Markdown links `[text](url)` for automatic Notion embedding.

---

## 5. Calculation Procedure (when applicable)

If the report covers a lab exercise or numerical procedure, structure the core section
as numbered steps:

**Step N — [Step name]**
- *Input:* [what is given]
- *Formula:* `$$[operative formula]$$`
- *Output:* [what is produced, units]

---

## Constraints
- Do not summarise or compress the source — aim for complete information transfer.
- Do not add section numbers unless explicitly requested.
- Spell-check Italian syntax if any Italian appears in the source notes.
- If output is too long, split into parts labelled: *"Part N/M — [section name]"*
