---
title: "Prompt Ottimizzato - Iteration 03 CAD + STAR-CCM+ + HEEDS"
version: "optimized-v3"
status: "executed"
date: "2026-05-20"
original_version: "iteration_03_cad_starccm_heeds_request.md"
optimization_technique: "scoped research + modular report generation + repository consistency pass"
---

# Prompt Ottimizzato - Iterazione 03

> Versione operativa del prompt originale, organizzata per fasi e output tracciabili.

---

## MODULO 0 - Context

```xml
<context>
  <project>Airspeeder Mk3 aerodynamic workflow repository</project>
  <focus>
    Confrontare due workflow proprietari:
    1. SOLIDWORKS CAD -> Simcenter STAR-CCM+ mesh/CFD -> Simcenter HEEDS optimization
    2. NX CAD -> Simcenter STAR-CCM+ mesh/CFD -> Simcenter HEEDS optimization
  </focus>
  <baseline>
    Mantenere OpenVSP + GMSH + SU2/OpenFOAM + Optuna come baseline open-source replicabile.
  </baseline>
</context>
```

---

## MODULO 1 - Research

```xml
<task id="M1" phase="research">
  <instruction>
    Verifica fonti aggiornate e primarie per:
    SOLIDWORKS, NX, STAR-CCM+, HEEDS, GMSH e strumenti gia' presenti nella repo.
    Aggiorna sources/sources.md con URL, reliability, data accesso e note operative.
  </instruction>
  <validation>
    Ogni software citato nei due workflow deve essere presente in sources.md.
    Le fonti vendor sono affidabili per capability dichiarate, ma non per confronti neutrali tra vendor.
  </validation>
</task>
```

---

## MODULO 2 - Analysis

```xml
<task id="M2" phase="analysis">
  <questions>
    <q>Meglio SOLIDWORKS o NX per droni/eVTOL?</q>
    <q>STAR-CCM+ fa bene le mesh o conviene GMSH?</q>
    <q>Come funziona HEEDS e cosa modifica in un processo industriale?</q>
  </questions>
  <output>
    results/iteration_03_cad_starccm_heeds_analysis.md
  </output>
  <validation>
    La risposta deve separare: raccomandazione operativa, rischi, quando scegliere ciascuna alternativa.
  </validation>
</task>
```

---

## MODULO 3 - Configuration Files

```xml
<task id="M3" phase="configuration">
  <instruction>
    Aggiungi due configurazioni dedicate e aggiorna configs/workflow_catalog.md:
    - configs/config_4_solidworks_starccm_heeds/summary.md
    - configs/config_5_nx_starccm_heeds/summary.md
  </instruction>
  <validation>
    Ogni configurazione include diagramma Mermaid, score, vantaggi, rischi e parametri modificabili.
  </validation>
</task>
```

---

## MODULO 4 - Tutorials

```xml
<task id="M4" phase="learning_resources">
  <instruction>
    Crea tutorials.md con risorse per imparare i software:
    documentazione ufficiale, guide, video YouTube ufficiali/community e percorso consigliato.
  </instruction>
  <validation>
    SOLIDWORKS, NX, STAR-CCM+ e HEEDS devono comparire per primi.
  </validation>
</task>
```

---

## MODULO 5 - Modular LaTeX Report

```xml
<task id="M5" phase="reporting">
  <instruction>
    Ristruttura report/report.tex: non deve piu' essere monolitico.
    Usa report/main.tex come assemblatore e file separati:
    - report/sections/software_logic.tex
    - report/iterations/iter1_solidworks_starccm_heeds.tex
    - report/iterations/iter2_nx_starccm_heeds.tex
    - eventuale report/sections/recommendations.tex
  </instruction>
  <validation>
    report/report.tex deve restare compatibile come entry point e includere main.tex.
  </validation>
</task>
```

---

## MODULO 6 - Continuous Improvement

```xml
<task id="M6" phase="project_update">
  <instruction>
    Aggiorna execution log, improvements, cross references, assembly guide e README se necessario.
  </instruction>
  <output>
    execution_logs/log_20260520_iteration03.md
    improvements/iteration_03_improvements.md
  </output>
</task>
```
