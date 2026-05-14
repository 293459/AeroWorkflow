---
title: "Prompt Ottimizzato — Airspeeder Mk3 Aero Workflow"
version: "optimized-v1"
status: "executed"
date: "2026-05-13"
original_version: "main_prompt_original.md"
optimization_technique: "modular decomposition + XML structure + chain-of-thought"
---

# Prompt Ottimizzato — Airspeeder Mk3 Aero Workflow

> Versione ottimizzata del prompt originale. Trasformato da monolitico a modulare, con struttura XML, istruzioni di ragionamento esplicite e separazione per fasi di esecuzione.

---

## MODULO 0 — Context & Setup

```xml
<context>
  <project>Airspeeder Mk3 Aerodynamic Optimization Workflow</project>
  <objective>
    Costruire una repo GitHub strutturata per il workflow:
    CAD parametrico (OpenVSP) → Meshing (GMSH) → CFD (SU2/OpenFOAM) → Ottimizzazione (Optuna)
    con obiettivo di minimizzare il drag del telaio Airspeeder Mk3 per competizione.
  </objective>
  <constraints>
    - Open source preferito
    - Windows compatibile (team lavora su Windows)
    - Focus aerodinamico (aeroacustica secondaria)
    - Interoperabilità formati file critica
    - Tutto in formato leggibile da LLM (markdown + mermaid)
  </constraints>
  <output_format>
    - File markdown per ogni componente
    - Diagrammi in Mermaid (non immagini)
    - Struttura repo GitHub
    - Nessun file monolitico — uno scopo per file
  </output_format>
</context>
```

---

## MODULO 1 — Generazione Configurazioni

```xml
<task id="M1" phase="analysis" produces="configs/">
  <instruction>
    Analizza e confronta 3 configurazioni di workflow CFD per l'Airspeeder Mk3.
    
    Per CIASCUNA configurazione:
    1. Genera un diagramma Mermaid flowchart che mostri:
       - Software utilizzati (nodi)
       - Formati file in transito (label sugli archi)
       - Input/Output principali
    2. Valuta secondo la metrica in metrics/evaluation_metrics.md
    3. Genera il file summary.md in configs/config_N_*/
    
    Configurazioni da analizzare:
    - Config 1: OpenVSP + GMSH + SU2 (raccomandato)
    - Config 2: OpenVSP + GMSH + OpenFOAM (alta fedeltà)  
    - Config 3: OpenVSP + XFLR5 (screening preliminare)
  </instruction>
  
  <chain_of_thought>
    Prima ragiona su:
    - Quali formati file usa ciascun software?
    - Dove ci sono conversioni non banali?
    - Quale stack è più pratico su Windows?
    Poi genera i file.
  </chain_of_thought>
  
  <validation>
    - Ogni config ha un diagramma Mermaid valido
    - La tabella metrica somma a 100%
    - Il punteggio finale è nell'intervallo [1, 5]
  </validation>
</task>
```

---

## MODULO 2 — Documentazione Tecnica

```xml
<task id="M2" phase="documentation" depends_on="M1" produces="sources/ examples/ tools.md">
  <subtask id="M2a">
    Genera sources/sources.md con:
    - Siti ufficiali dei software
    - Forum/community links rilevanti
    - Articoli/paper di riferimento
    - Per ciascuna fonte: URL + data accesso + reliability_score (1-5)
    Cerca informazioni aggiornate prima di scrivere.
  </subtask>
  
  <subtask id="M2b">
    Genera examples/industry_examples.md con:
    - 3-5 aziende aerospaziali/motorsport che usano workflow CFD simili
    - Per ciascuna: stack usato, caso d'uso, link a fonte pubblica
    - Nota: presenza in un'azienda ≠ soluzione ottimale, solo garanzia che funziona
  </subtask>
  
  <subtask id="M2c">
    Genera tools.md con tabella completa di tutti gli strumenti:
    ruolo, versione, licenza, OS, formati I/O, Python API.
  </subtask>
</task>
```

---

## MODULO 3 — Infrastruttura Repo

```xml
<task id="M3" phase="infrastructure" produces="execution_pipeline.md validator.md cross_references.md assembly_guide.md">
  <subtask id="M3a">
    execution_pipeline.md: pipeline a 7 fasi con diagramma Mermaid principale +
    diagrammi dettaglio per ciascuna fase. Include "context modules per fase"
    (quali file caricare in ogni sessione LLM).
  </subtask>
  
  <subtask id="M3b">
    validator.md: per ciascuna fase, definire:
    - Criterio di validazione quantitativo
    - Come verificarlo (comando/script/check manuale)
    - Cosa fare se fallisce
  </subtask>
  
  <subtask id="M3c">
    cross_references.md: matrice di dipendenze tra tutti i file della repo.
    Formato: "File A richiede File B" con motivazione.
  </subtask>
  
  <subtask id="M3d">
    assembly_guide.md: come vengono assemblati i file nel report finale.
    Come fare in modo che modificare un file componente aggiorni l'output finale.
  </subtask>
</task>
```

---

## MODULO 4 — Report LaTeX

```xml
<task id="M4" phase="reporting" depends_on="M1 M2 M3" produces="report/report.tex">
  <instruction>
    Genera un report LaTeX completo con:
    - Introduzione al problema (Airspeeder Mk3, obiettivo drag minimization)
    - Sezione per ciascuna configurazione workflow (con figure Mermaid convertite)
    - Tabella comparativa finale con ranking
    - Appendici: config SU2 template, script GMSH template
    - Bibliografia con tutti i riferimenti da sources.md
    - Commenti LaTeX esplicativi in italiano
  </instruction>
  <format>
    - Classe: article o report
    - Encoding: UTF-8
    - Package richiesti: geometry, hyperref, booktabs, graphicx, listings, biblatex
  </format>
</task>
```

---

## MODULO 5 — Miglioramento Continuo

```xml
<task id="M5" phase="iteration" depends_on="M1 M2 M3 M4" produces="improvements/ prompts/">
  <instruction>
    Al termine di ogni iterazione:
    1. Genera improvements/iteration_NN_improvements.md con:
       - Cosa ha funzionato
       - Cosa non ha funzionato
       - Suggerimenti specifici per la prossima iterazione
    2. Genera un nuovo prompt nella cartella prompts/ con suffisso _NOT_EXECUTED.md
       che incorpori i miglioramenti suggeriti
    3. Aggiorna execution_logs/ con il log della sessione
  </instruction>
</task>
```

---

## Note sull'ottimizzazione applicata

| Tecnica | Applicata come |
|---|---|
| Struttura XML | Ogni modulo ha `<task>`, `<instruction>`, `<validation>` chiari |
| Chain-of-thought | Istruzione "prima ragiona, poi genera" esplicita in M1 |
| Decomposizione modulare | 5 moduli indipendenti eseguibili in sessioni separate |
| Output format esplicito | Ogni task specifica `produces=` |
| Dipendenze esplicite | `depends_on=` tra moduli per sequenziamento |
| Vincoli negativi | "Non fare file monolitici", "aeroacustica secondaria" |
| Formato specifico | Mermaid (non immagini), markdown (non HTML), UTF-8 |
