---
title: "Risultati Analisi Iterazione 03 - CAD + STAR-CCM+ + HEEDS"
phase: "Analysis Results"
status: "completed"
date: "2026-05-20"
iteration: 3
run_id: "iteration_03_cad_starccm_heeds"
sources: ["S37", "S38", "S39", "S40", "S41", "S42", "S43", "S44", "S45", "S46", "S47", "S26"]
---

# Risultati Analisi - Iterazione 03

> Domanda: confronto tra due configurazioni:
> 1. SOLIDWORKS (CAD) -> STAR-CCM+ (mesh + CFD) -> HEEDS (optimization)
> 2. NX (CAD) -> STAR-CCM+ (mesh + CFD) -> HEEDS (optimization)

---

## Executive Summary

| Domanda | Risposta breve |
|---|---|
| Meglio SOLIDWORKS o NX per droni/eVTOL? | **NX**, se licenze e competenze sono disponibili. SOLIDWORKS resta piu' rapido/accessibile per prototipi meccanici e team piccoli. |
| STAR-CCM+ fa bene le mesh? | **Si**, in contesto industriale e soprattutto se si usa anche STAR-CCM+ come solver. GMSH conviene nello stack open source, non come mesher predefinito per STAR-CCM+. |
| Come funziona HEEDS? | Automatizza un workflow CAD/CAE, modifica variabili, lancia simulazioni, legge risposte, applica algoritmi di esplorazione/ottimizzazione e produce trade-off/Pareto/sensitivity. |

---

## 1. SOLIDWORKS vs NX nel campo droni/eVTOL

### Raccomandazione

Per un workflow industriale orientato a droni/eVTOL racing, **NX e' preferibile a SOLIDWORKS**. La motivazione non e' che SOLIDWORKS "non vada bene": e' un CAD parametrico eccellente e molto produttivo. Il punto e' che NX ha un fit piu' diretto con:

- superfici aerodinamiche complesse;
- aerospace/UAV/urban air mobility;
- compositi e aerostrutture;
- master model technology;
- integrazione Simcenter/Teamcenter;
- automazione di parametri e varianti in un digital thread Siemens.

SOLIDWORKS resta una scelta forte se il team e' gia' formato su quello, se la geometria e' prevalentemente meccanica e se la priorita' e' generare rapidamente parti/assiemi producibili. Pero' in ottimizzazione automatica puo' diventare fragile se fillet, feature tree, split lines o nomi delle superfici cambiano tra una variante e l'altra.

### Decisione pratica

| Scenario | Scelta |
|---|---|
| Team piccolo, prototipo veloce, esperienza SOLIDWORKS gia' presente | SOLIDWORKS + STAR-CCM+ + HEEDS |
| Drone/eVTOL complesso, superfici aero, compositi, rotori/fairing, workflow industriale Siemens | NX + STAR-CCM+ + HEEDS |
| Repo didattica/open, zero licenze, massima riproducibilita' | OpenVSP + GMSH + SU2/OpenFOAM + Optuna |

### Implicazione per Airspeeder-like

Per Airspeeder Mk3 il CAD non e' solo "disegnare il telaio": deve sostenere iterazioni automatiche. Questo rende piu' importante la robustezza parametrica che la velocita' di modellazione manuale. NX vince per il benchmark proprietario; SOLIDWORKS e' una valida alternativa operativa.

---

## 2. STAR-CCM+ per le mesh: usarlo o preferire GMSH?

### Risposta breve

**STAR-CCM+ fa mesh molto bene**, specialmente per workflow industriali CFD in cui la mesh deve essere:

- ripetibile;
- associata alle regioni fisiche della simulazione;
- dotata di prism layers robusti;
- controllata localmente;
- adattabile a superfici sporche tramite wrapping/repair;
- integrata con solver, reports, post-processing e design exploration.

Se il solver finale e' STAR-CCM+, conviene quasi sempre **meshare in STAR-CCM+**. Usare GMSH davanti a STAR-CCM+ aggiunge conversioni e rischia di perdere naming, regioni, controlli mesh e ripetibilita' nativa del workflow.

### Quando usare GMSH

GMSH e' preferibile quando:

- si usa SU2 o un altro solver open source;
- si vuole versionare completamente la mesh generation con script `.geo` o Python;
- la repo deve restare eseguibile senza licenze;
- si sta facendo una baseline didattica/accademica.

### Quando usare STAR-CCM+ mesh

STAR-CCM+ e' preferibile quando:

- il solver e' STAR-CCM+;
- la geometria e' CAD industriale, non una mesh superficiale semplice;
- servono wrapper, automatic defeaturing, prism layers e mesh operations replayable;
- si usera' HEEDS/Design Manager per centinaia di varianti;
- ci sono rotori, moving regions, overset/sliding mesh o AMR.

### Regola operativa

Non decidere "GMSH vs STAR mesh" in astratto. Decidere in base al solver e al ciclo di automazione:

```text
OpenVSP/SU2/OpenFOAM baseline -> GMSH o snappyHexMesh
STAR-CCM+ solver industriale   -> STAR-CCM+ automated meshing
```

In entrambi i casi, il risultato valido nasce da mesh sensitivity study: coarse, medium, fine; controllo y+; controllo Cd/Cl; controllo qualità celle; e monitor di convergenza.

---

## 3. Come funziona HEEDS e l'ottimizzazione industriale

### Concetto base

HEEDS non sostituisce CAD o CFD. HEEDS li orchestra.

Un workflow tipico e':

```text
1. Definisci variabili di progetto
2. HEEDS modifica CAD/parametri/input file
3. Il CAD rigenera la geometria
4. STAR-CCM+ importa/prepara/mesha/simula
5. Script o reports estraggono Cd, Cl, power, constraint
6. HEEDS decide il prossimo design da provare
7. I risultati vengono salvati, confrontati e visualizzati
```

### Cosa puo' modificare

| Categoria | Esempi |
|---|---|
| Parametri CAD | raggi, spessori, lunghezze, sweep, sezioni, fairing, duct, posizioni componenti |
| Parametri fisici | velocita', yaw, alpha, RPM, casi hover/cruise, load cases |
| Parametri mesh | base size, refinement, prism layer, AMR; da usare con cautela |
| Parametri solver | criteri convergenza, modelli fisici, iterazioni; da separare dalla fisica finale |
| Vincoli | clearance rotori, volume, massa proxy, stress max, packaging, manufacturability |
| Obiettivi | minimizzare Cd, massimizzare thrust/efficiency, ridurre power, robustezza, Pareto trade-off |

### Processo industriale

1. **DOE iniziale**: campionamento dello spazio per capire sensitivita' e failure modes.
2. **Search adattiva**: algoritmi come SHERPA combinano strategie globali/locali e si adattano mentre imparano il design space.
3. **Parallelizzazione**: run distribuite su workstation, server, cluster o cloud.
4. **Failure handling**: una geometria che non mesha o un solver che diverge non ferma tutto; viene marcata come infeasible.
5. **Result mining**: Pareto front, sensitivity, correlazioni, design families, robustezza rispetto a tolleranze.
6. **Validation run**: le geometrie migliori vengono ricalcolate con mesh piu' fine, fisica piu' completa e controlli indipendenti.

### Cosa non bisogna fare

- Non usare HEEDS come "macchina magica": se il CAD e' fragile o la mesh non converge, l'ottimizzazione amplifica il problema.
- Non ottimizzare parametri numerici per abbassare artificialmente il drag.
- Non accettare il best design senza re-run indipendente.
- Non mescolare obiettivi incompatibili senza Pareto/multi-objective: un drone puo' richiedere compromessi tra cruise drag, hover thrust, cooling, stabilita' e produzione.

---

## Ranking finale dei due casi studio

| Rank | Workflow | Score | Giudizio |
|---|---|---:|---|
| 1 | NX + STAR-CCM+ + HEEDS | 4.20/5 | Miglior fit proprietario per droni/eVTOL complessi |
| 2 | SOLIDWORKS + STAR-CCM+ + HEEDS | 3.90/5 | Buona alternativa se il team e' SOLIDWORKS-first |

---

## Raccomandazione per la repo

Mantenere due livelli:

- **Baseline replicabile**: OpenVSP + GMSH + SU2/OpenFOAM + Optuna.
- **Benchmark industriale proprietario**: NX + STAR-CCM+ + HEEDS.

SOLIDWORKS + STAR-CCM+ + HEEDS va documentato come alternativa pratica, non come target ideale, perche' nel nostro campo l'integrazione aerospace/Simcenter di NX e' un vantaggio reale.
