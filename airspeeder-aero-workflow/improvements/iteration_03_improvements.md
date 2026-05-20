---
title: "Suggested Improvements - Iteration 03"
iteration: 3
date: "2026-05-20"
status: "completed"
next_prompt: "prompts/iteration_04_starccm_heeds_microcase_NOT_EXECUTED.md"
---

# Suggested Improvements - Iterazione 03

## Cosa e' stato prodotto

- Aggiornate le fonti per SOLIDWORKS, NX, STAR-CCM+ e HEEDS in `sources/sources.md`.
- Creato `tutorials.md` con documentazione, guide, training e video/playlist per i software principali.
- Aggiunte due configurazioni dedicate:
  - `configs/config_4_solidworks_starccm_heeds/summary.md`
  - `configs/config_5_nx_starccm_heeds/summary.md`
- Aggiornato `configs/workflow_catalog.md` con W25 e W26.
- Creato `results/iteration_03_cad_starccm_heeds_analysis.md` con risposta alle tre domande guida.
- Ristrutturato il report LaTeX in forma modulare:
  - `report/report.tex` entry point compatibile
  - `report/main.tex` assemblatore
  - `report/sections/software_logic.tex`
  - `report/iterations/iter1_solidworks_starccm_heeds.tex`
  - `report/iterations/iter2_nx_starccm_heeds.tex`
  - `report/sections/recommendations.tex`
- Aggiunti prompt originale, prompt ottimizzato e prompt successivo not-executed.

## Cosa ha funzionato

1. Separare SOLIDWORKS e NX ha reso piu' chiara la decisione: NX e' il benchmark proprietario, SOLIDWORKS e' alternativa operativa.
2. Trattare STAR-CCM+ come ambiente mesh+solver, non solo solver, evita una falsa dicotomia con GMSH.
3. La modularizzazione LaTeX rende piu' facile aggiungere nuove iterazioni senza gonfiare un solo file.

## Cosa resta incompleto

| Item | Priorita' | Nota |
|---|---|---|
| Template STAR-CCM+ reale | Alta | Mancano macro Java/simulation operations concrete per un micro-caso |
| Template HEEDS reale | Alta | Mancano file input/output e response extractors |
| Parametri CAD comuni | Alta | Serve un micro-modello condiviso tra SOLIDWORKS/NX e baseline open |
| Validazione mesh | Alta | Serve una matrice coarse/medium/fine con criteri y+ e Cd convergence |
| Fonti video non ufficiali | Media | YouTube e community resources vanno curate periodicamente |

## Suggerimento per iterazione 04

Usare il prompt `prompts/iteration_04_starccm_heeds_microcase_NOT_EXECUTED.md` per costruire un micro-caso verificabile. L'obiettivo non e' ancora lanciare HEEDS, ma definire un template industriale: variabili, bounds, constraints, mesh sensitivity, response extraction e failure handling.
