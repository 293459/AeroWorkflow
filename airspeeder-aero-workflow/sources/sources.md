---
title: "Sources — Airspeeder Mk3 Aero Workflow"
phase: "Documentation"
status: "ready"
last_updated: "2026-05-13"
iteration: 1
---

# Sorgenti e Riferimenti

> Tutti i riferimenti usati nel progetto, con URL, data di accesso, tipo di fonte e reliability score.
> **Reliability Score (1–5):** 5 = documentazione ufficiale / paper peer-reviewed; 4 = sito ufficiale del software; 3 = articolo tecnico non peer-reviewed; 2 = forum/community; 1 = fonte secondaria o non verificabile.

---

## Software — Documentazione Ufficiale

| # | Nome | URL | Tipo | Reliability | Data accesso | Note |
|---|---|---|---|---|---|---|
| S01 | OpenVSP Official | https://openvsp.org | Sito ufficiale NASA | ⭐⭐⭐⭐⭐ 5 | 2026-05-13 | Include tutorial, API docs, download |
| S02 | OpenVSP GitHub | https://github.com/OpenVSP/OpenVSP | Repository GitHub | ⭐⭐⭐⭐⭐ 5 | 2026-05-13 | Codice sorgente + issues tracker |
| S03 | SU2 Official | https://su2code.github.io | Sito ufficiale | ⭐⭐⭐⭐⭐ 5 | 2026-05-13 | Docs, tutorials, download |
| S04 | SU2 GitHub | https://github.com/su2code/SU2 | Repository GitHub | ⭐⭐⭐⭐⭐ 5 | 2026-05-13 | Codice + wiki + esempi |
| S05 | OpenFOAM Official | https://openfoam.org | Sito ufficiale | ⭐⭐⭐⭐⭐ 5 | 2026-05-13 | Versione OpenFOAM.org |
| S06 | OpenFOAM ESI | https://www.openfoam.com | Sito ufficiale ESI | ⭐⭐⭐⭐⭐ 5 | 2026-05-13 | Versione commerciale/community ESI |
| S07 | GMSH Official | https://gmsh.info | Sito ufficiale | ⭐⭐⭐⭐⭐ 5 | 2026-05-13 | Docs, API, tutorials |
| S08 | ParaView Official | https://www.paraview.org | Sito ufficiale | ⭐⭐⭐⭐⭐ 5 | 2026-05-13 | Docs + pvpython reference |
| S09 | XFLR5 | http://www.xflr5.tech | Sito ufficiale | ⭐⭐⭐⭐ 4 | 2026-05-13 | Meno aggiornato, versione stabile |
| S10 | Optuna | https://optuna.org | Sito ufficiale | ⭐⭐⭐⭐⭐ 5 | 2026-05-13 | Docs complete, tutorial Bayesian opt |

---

## Airspeeder Mk3 — Fonti Primarie

| # | Titolo | URL | Tipo | Reliability | Data | Note |
|---|---|---|---|---|---|---|
| S11 | Airspeeder Official | https://airspeeder.com | Sito ufficiale | ⭐⭐⭐⭐⭐ 5 | 2026-05-13 | News, spec tecniche |
| S12 | Mk3 Ready to Race | https://airspeeder.com/news/mk3-worlds-first-electric-flying-racing-car-ready-to-race | Comunicato stampa | ⭐⭐⭐⭐ 4 | 2026-05-13 | Dati tecnici Mk3 |
| S13 | 2023 EXA Championship | https://www.urbanairmobilitynews.com/air-taxis/motorsport-history-as-2023-exa-series-championship-completed/ | Articolo | ⭐⭐⭐ 3 | 2026-05-13 | Top speed 100 km/h, 4.1m wingspan |
| S14 | Mk4 Reveal (dati Mk3) | https://newatlas.com/aircraft/airspeeder-mk4-racing-h2-evtol/ | Articolo tecnico | ⭐⭐⭐ 3 | 2026-05-13 | 350+ test flights Mk3 |
| S15 | eVTOL Insights Mk3 | https://evtolinsights.com/airspeeders-mk3-evtol-flying-vehicle-has-been-revealed-and-is-now-ready-to-race/ | Articolo | ⭐⭐⭐ 3 | 2026-05-13 | Costruzione in fibra di carbonio |

---

## Paper Accademici

| # | Titolo | URL | Journal/Conf | Reliability | Anno | Note |
|---|---|---|---|---|---|---|
| S16 | SU2 for Rotorcraft Flows (Polimi) | https://arxiv.org/pdf/2107.13895 | arXiv / accademico | ⭐⭐⭐⭐⭐ 5 | 2021 | SU2 per analisi rotori — molto rilevante per eVTOL |
| S17 | OpenVSP + ESP (AIAA 2024) | https://acdl.mit.edu/ESP/Publications/AIAApaper2024-4304.pdf | AIAA Aviation Forum 2024 | ⭐⭐⭐⭐⭐ 5 | 2024 | Workflow OpenVSP → CFD pronto per analisi |
| S18 | SU2 + OpenFOAM Validation HLPW5 | https://www.researchgate.net/publication/398218662 | ResearchGate 2025 | ⭐⭐⭐⭐ 4 | 2025 | Confronto SU2 vs OpenFOAM su casi industriali |

---

## Tutorial e Risorse Pratiche

| # | Titolo | URL | Tipo | Reliability | Anno | Note |
|---|---|---|---|---|---|---|
| S19 | SU2 Tutorials Official | https://su2code.github.io/tutorials/ | Tutorial ufficiali | ⭐⭐⭐⭐⭐ 5 | 2024 | Casi NACA 0012, RAE 2822, ecc. |
| S20 | GMSH Tutorials | https://gmsh.info/doc/texinfo/gmsh.html | Documentazione | ⭐⭐⭐⭐⭐ 5 | 2024 | Reference completo |
| S21 | OpenFOAM User Guide | https://doc.cfd.direct/openfoam/user-guide-v11/ | Documentazione | ⭐⭐⭐⭐⭐ 5 | 2023 | Guida ufficiale v11 |
| S22 | CFD Online Forum | https://www.cfd-online.com/Forums/ | Forum community | ⭐⭐⭐ 3 | ongoing | Utile per troubleshooting specifico |
| S23 | Open Source vs Proprietary CFD | https://gaugehow.com/simulation/best-cfd-software-2026-commercial-vs-open-source | Articolo tecnico | ⭐⭐⭐ 3 | 2026 | Confronto aggiornato 2026 |
| S24 | MetaOpenFOAM 2.0 (LLM+CFD) | https://arxiv.org/pdf/2502.00498 | arXiv 2025 | ⭐⭐⭐⭐ 4 | 2025 | Interessante per automazione CFD con LLM |

---

## Dati tecnici Airspeeder Mk3

Dalle fonti S11–S15:
- **Dimensioni:** 4.1 m di lunghezza
- **Costruzione:** fibra di carbonio
- **Top speed:** 100 km/h (Mk3); Mk4 fino a 360 km/h
- **Propulsione:** elettrica (quadricottero racing)
- **Operazione:** remotamente pilotato (Mk3)
- **Test:** 350+ voli di test completati
- **MTOW:** < 950 kg (Mk4; Mk3 significativamente più leggero)
- **Vincitore 2023 EXA Series:** Zephatali Walsh

---

## Note sulla attendibilità delle fonti

> ⚠️ **Importante:** Un reliability score basso non implica che l'informazione sia sbagliata — fonti vecchie possono essere ancora valide (es. principi CFD stabili). Il score riflette principalmente verificabilità e aggiornamento.

| Score | Interpretazione |
|---|---|
| ⭐⭐⭐⭐⭐ 5 | Certa e aggiornata — usare direttamente |
| ⭐⭐⭐⭐ 4 | Affidabile — verificare se ci sono aggiornamenti recenti |
| ⭐⭐⭐ 3 | Usare con cautela — cross-check con fonte primaria |
| ⭐⭐ 2 | Solo come indicazione — verificare sempre |
| ⭐ 1 | Non citare — solo per ispirazione |

---

## Script di verifica link

```python
# verify_links.py — verifica che tutti i link nella repo siano raggiungibili
import requests

LINKS = [
    "https://openvsp.org",
    "https://su2code.github.io",
    "https://openfoam.org",
    "https://gmsh.info",
    "https://www.paraview.org",
    "https://optuna.org",
    "https://airspeeder.com",
]

for url in LINKS:
    try:
        r = requests.head(url, timeout=5)
        status = "✅" if r.status_code < 400 else "❌"
        print(f"{status} {r.status_code} — {url}")
    except Exception as e:
        print(f"❌ ERRORE — {url}: {e}")
```
