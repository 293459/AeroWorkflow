---
title: "Workflow Catalog — Airspeeder Mk3 CFD Pipeline Candidates"
phase: "Configuration Expansion"
status: "updated"
last_updated: "2026-05-20"
iteration: 3
run_id: "iteration_03_cad_starccm_heeds"
metric_profile: "proprietary_tolerant"
metric_status: "pending_batch_evaluation"
context_strategy: "load summary table first; load detailed notes only for shortlisted workflows"
---

# Workflow Catalog — Candidate Pipeline Esaustive

> Catalogo compatto delle configurazioni possibili. Serve a non limitare artificialmente il numero di workflow e a mantenere metadata minimi per filtrare i candidati prima di applicare la metrica completa.

## Metadata usati

| Campo | Significato |
|---|---|
| `run_id` | Iterazione o run in cui il candidato è stato introdotto |
| `source_class` | `existing`, `industrial`, `derived`, `speculative`, `dubious` |
| `metric_status` | `evaluated_legacy`, `pending_evaluation`, `needs_tool_access`, `reject_likely` |
| `context_load` | `low`, `medium`, `high`; indica quanto pesa caricare il candidato in context |
| `fit_intent` | Perché esiste il candidato: baseline, benchmark commerciale, eVTOL, racing, validazione, esplorazione |

---

## Tabella sintetica

| ID | Workflow | Source class | Metric status | Context | Fit intent | Prima valutazione |
|---|---|---|---|---|---|---|
| W01 | OpenVSP + GMSH + SU2 + ParaView + Optuna | existing | evaluated_legacy | low | baseline open | Fortissimo come baseline replicabile |
| W02 | OpenVSP + GMSH/snappyHexMesh + OpenFOAM + ParaView | existing | evaluated_legacy | low | high fidelity open | Forte per rotori/futuro, più complesso |
| W03 | OpenVSP + XFLR5/AVL + SU2 | derived | pending_evaluation | low | multi-fidelity open | Utile screening, debole su geometria complessa |
| W04 | CATIA/NX + ANSA + Ansys Fluent + EnSight | industrial | needs_tool_access | medium | racing benchmark | Molto credibile, costoso |
| W05 | SpaceClaim/Discovery + Fluent Meshing + Ansys Fluent + optiSLang | industrial | needs_tool_access | medium | commercial end-to-end | Ottimo se si vuole ecosistema Ansys |
| W06 | NX/CATIA + Simcenter STAR-CCM+ + HEEDS | industrial | needs_tool_access | medium | eVTOL optimization | Molto forte per esplorazione automatica |
| W07 | STAR-CCM+ only workflow: clean CAD + mesh + CFD + post | industrial | needs_tool_access | low | single-suite CFD | Riduce attrito tra tool |
| W08 | Cadence Fidelity CFD end-to-end | industrial | needs_tool_access | low | eVTOL/EV benchmark | Forte su geometrie complesse |
| W09 | Pointwise/Fidelity Pointwise + SU2/OpenFOAM | derived | pending_evaluation | medium | premium mesh + open solver | Buon compromesso se solo meshing commerciale |
| W10 | SIMULIA PowerFLOW + PowerACOUSTICS + PowerVIZ | industrial | needs_tool_access | medium | aeroacoustic future | Forte su transient/aeroacustica |
| W11 | 3DEXPERIENCE/CATIA + SIMULIA PowerFLOW/Abaqus | industrial | needs_tool_access | high | full PLM + multiphysics | Pesante ma coerente per azienda strutturata |
| W12 | NASA CAPE + Cart3D + FUN3D + OVERFLOW | industrial | needs_tool_access | high | run matrix/HPC | Ottimo modello logico, accesso/tooling difficile |
| W13 | OpenVSP + Cart3D + SU2 | derived | pending_evaluation | medium | NASA-like open/academic | Screening veloce + RANS dettagliato |
| W14 | FreeCAD/Salome + GMSH + Code_Saturne | speculative | pending_evaluation | medium | open alternative | Possibile, meno naturale per eVTOL aero |
| W15 | Rhino/Grasshopper + OpenFOAM/Butterfly | dubious | reject_likely | medium | parametric design | Interessante per concept, fragile per CFD serio |
| W16 | Blender/FreeCAD + OpenFOAM | dubious | reject_likely | medium | low-budget geometry | Rischio geometrie sporche e poco riproducibili |
| W17 | SolidWorks CAD + SolidWorks Flow Simulation | speculative | pending_evaluation | low | quick engineering check | Rapido, ma non ideale per high-fidelity external aero |
| W18 | COMSOL Multiphysics + CAD Import | speculative | pending_evaluation | medium | multiphysics | Utile per coupling termico/strutturale, meno per racing CFD |
| W19 | Onshape/Fusion 360 + SimScale cloud CFD | speculative | pending_evaluation | low | cloud low-friction | Facile da usare, meno controllo numerico |
| W20 | OpenVSP + SU2 adjoint + DAKOTA/Optuna | derived | pending_evaluation | low | optimization-heavy | Molto adatto a design space ampio |
| W21 | OpenVSP + OpenFOAM actuator disk/sliding mesh + SU2 drag loop | derived | pending_evaluation | high | eVTOL hybrid | Buona separazione fusoliera/rotori |
| W22 | CAD commerciale + STAR-CCM+/Fluent + flight telemetry database | speculative | pending_evaluation | high | Alauda-like internal | Ideale se esistono dati reali di volo |
| W23 | OpenVSP + GMSH + SU2 + ML surrogate model | derived | pending_evaluation | medium | many-runs acceleration | Utile dopo prime decine di run CFD |
| W24 | CAD + reduced-order model + final CFD validation | derived | pending_evaluation | medium | fast iteration | Ragionevole se serve esplorazione ampia |
| W25 | SOLIDWORKS + STAR-CCM+ mesh/CFD + HEEDS | industrial | needs_tool_access | medium | commercial CAD benchmark | Valido se il team e' gia' SOLIDWORKS, ma richiede forte disciplina CAD-to-CFD |
| W26 | NX + STAR-CCM+ mesh/CFD + HEEDS | industrial | needs_tool_access | medium | preferred proprietary drone/eVTOL | Miglior fit proprietario per droni/eVTOL complessi dentro ecosistema Siemens |

---

## Shortlist iniziale per fase successiva

| Bucket | Candidati | Razionale |
|---|---|---|
| Baseline replicabile | W01, W03, W13, W20 | Mantengono costo basso e automazione Python |
| Benchmark proprietario racing/eVTOL | W04, W05, W06, W07, W08 | Coprono Fluent, STAR-CCM+ e Fidelity CFD |
| Benchmark CAD + STAR-CCM+ + HEEDS | W25, W26 | Separano il confronto tra SOLIDWORKS e NX richiesto in Iterazione 03 |
| Futuro rotor-body/aeroacustica | W02, W10, W21 | Rilevanti quando i rotori entrano nel modello |
| Run matrix e processo industriale | W12, W22, W23, W24 | Più importanti per scalare che per singola simulazione |
| Candidati dubbi da far filtrare alla metrica | W15, W16, W17, W18, W19 | Utili come confronto, probabilmente non vincenti |

---

## Note operative sui candidati

### W01 — OpenVSP + GMSH + SU2 + ParaView + Optuna

È la baseline già emersa come workflow principale. Il suo valore non è solo il costo nullo, ma la possibilità di versionare ogni input e automatizzare il ciclo con script Python. Deve restare il riferimento minimo contro cui confrontare ogni proposta più costosa.

### W06 — NX/CATIA + STAR-CCM+ + HEEDS

È probabilmente il candidato commerciale più coerente con gli esempi Martin UAV e Formula E. HEEDS aggiunge esplorazione automatica del design space e si sposa bene con un problema in cui geometria, hover, cruise e drag possono diventare obiettivi concorrenti.

### W08 — Cadence Fidelity CFD end-to-end

Ha senso quando il rischio principale è l'attrito tra preprocessing, meshing e solver. È interessante per eVTOL e geometrie complesse, ma richiede accesso licenza e una verifica pratica sul caso Airspeeder.

### W10 — SIMULIA PowerFLOW + PowerACOUSTICS

Non è prioritario per il focus attuale, perché l'aeroacustica è secondaria. Diventa però molto interessante se il progetto passa da drag-only a rotor noise, scie transienti e operazioni di gara.

### W15/W16 — Rhino/Blender/FreeCAD + OpenFOAM

Sono inclusi di proposito come candidati dubbi. Possono funzionare per concept e prototipi rapidi, ma rischiano di introdurre geometrie non manifold, naming fragile delle superfici, boundary conditions instabili e bassa riproducibilità.

---

### W25 - SOLIDWORKS + STAR-CCM+ + HEEDS

E' una pipeline praticabile quando il team lavora gia' in SOLIDWORKS e il valore principale sta nella rapidita' di modellazione meccanica. Il punto debole non e' STAR-CCM+ o HEEDS, ma la robustezza del CAD durante centinaia di varianti: fillet, split line, naming superfici e configurazioni devono restare stabili. Per il trasferimento verso STAR-CCM+ usare preferibilmente Parasolid o STEP, non STL, salvo casi di mesh superficiale controllata.

### W26 - NX + STAR-CCM+ + HEEDS

E' il benchmark proprietario piu' coerente per il campo droni/eVTOL. NX e' piu' naturale su superfici aerospace, UAV, compositi, master model e integrazione Simcenter; STAR-CCM+ gestisce mesh/CFD/post e HEEDS orchestra l'esplorazione. Il limite resta il costo licenze e la curva di apprendimento, quindi va mantenuta una baseline open source per replicabilita' e didattica.

---

## Regola di context window

Quando si lavora sulla comparazione, caricare prima solo questa sezione:

1. YAML header.
2. Tabella sintetica.
3. Shortlist iniziale.

Caricare le note operative solo per i candidati selezionati dalla metrica o da una domanda specifica. Questo evita di saturare la context window durante ranking e iterazioni.
