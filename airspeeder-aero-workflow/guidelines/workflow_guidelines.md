---
title: "Workflow Guidelines — Engineering and Repository Practice"
phase: "Infrastructure"
status: "ready"
last_updated: "2026-05-14"
iteration: 2
run_id: "iteration_02_industrial_report"
applies_to:
  - "execution_pipeline.md"
  - "configs/workflow_catalog.md"
  - "examples/industry_examples.md"
  - "report/report.tex"
---

# Workflow Guidelines — Engineering and Repository Practice

> Questo file definisce le regole di gestione del workflow aerodinamico e della repo. Deve essere letto insieme a `execution_pipeline.md` prima di modifiche sostanziali.

---

## Principi di ingegneria di processo

### 1. Separare decisioni, dati e automazione

Un workflow CFD è robusto quando distingue chiaramente decisioni progettuali, dati di input e automazione. Questa separazione permette di cambiare un layer senza invalidare tutto il processo: sostituire SU2 con OpenFOAM, per esempio, non dovrebbe richiedere di riscrivere la logica CAD.

### 2. Usare una logica multi-fidelity

Non tutte le geometrie meritano una simulazione costosa. Il workflow dovrebbe procedere per livelli:

| Livello | Scopo | Esempio |
|---|---|---|
| Low fidelity | Scartare rapidamente configurazioni pessime | XFLR5, AVL, Cart3D, surrogate model |
| Medium fidelity | Misurare trend aerodinamici credibili | SU2 RANS, OpenFOAM steady RANS |
| High fidelity | Validare candidati finali | sliding mesh, DES/LES, PowerFLOW, STAR-CCM+ high resolution |
| Experimental/flight | Chiudere il loop con dati reali | telemetria, test flight, wind tunnel |

### 3. Progettare per run matrix, non per singola simulazione

La singola simulazione è solo un campione. Il valore industriale nasce dalla matrice di run: naming stabile, parametri machine-readable, log solver versionati, metriche automatiche e fallimenti classificati invece che cancellati.

### 4. Trattare le divergenze CFD come dati

Una run divergente non è solo un errore: è informazione su geometrie, mesh o condizioni al contorno problematiche. Il workflow deve salvare parametri geometrici, mesh quality summary, residui prima della divergenza, codice di errore e decisione successiva.

### 5. Non mischiare benchmark e produzione

Uno stack proprietario può essere ottimo come benchmark e inadatto alla produzione della repo. Ogni workflow deve essere marcato come `repo baseline`, `industrial benchmark`, `future candidate` o `dubious control`.

### 6. Validare prima di ottimizzare

Prima di lanciare loop ampi:

1. verificare mesh independence su almeno tre livelli;
2. controllare conservazione e residui;
3. confrontare un caso noto o una geometria semplificata;
4. salvare l'intera configurazione di riferimento.

---

## Regole informatiche e repository

### 1. Commit locali per blocchi logici

Ogni modifica sostanziale deve chiudersi con un commit locale. Il commit deve essere piccolo abbastanza da poter essere letto e revertito, ma grande abbastanza da rappresentare un risultato completo.

Pattern consigliato:

```text
<area>: <azione breve>

Perché:
- motivo tecnico o documentale

Cosa cambia:
- file principali toccati
- effetto sulla pipeline
```

### 2. Non committare modifiche non correlate

Se il working tree contiene modifiche preesistenti, lasciarle fuori dal commit salvo richiesta esplicita. Quando una modifica preesistente tocca lo stesso file, leggere il contesto e lavorare sopra senza cancellarla.

### 3. Commentare dove serve davvero

I commenti devono spiegare decisioni non ovvie: soglie, fallback, candidati dubbi, assunzioni fisiche. Evitare commenti che ripetono codice o tabelle.

### 4. Usare metadata per ridurre context window

Ogni nuovo file di catalogo o report dovrebbe avere YAML header con `status`, `last_updated`, `iteration`, `run_id`, `metric_status` se riguarda configurazioni e `context_strategy` se il file può diventare lungo.

### 5. Generare artifact derivati in cartelle dedicate

Artifact generati, come figure Mermaid e PDF, devono vivere in percorsi prevedibili:

```text
report/figures/<topic>/
report/report.pdf
execution_logs/
```

Ogni cartella generata dovrebbe includere un manifest quando contiene molti file.

### 6. Validare prima del commit

Prima di committare:

1. eseguire `git diff --check`;
2. verificare che i file attesi esistano;
3. se si tocca LaTeX, compilare o documentare perché non è possibile;
4. se si generano immagini, controllare manifest e dimensioni non nulle.

---

## Regole specifiche per il report

Le sezioni del report devono seguire lo stile di `report.md`: micro-sezioni leggibili, spiegazione del "perché", tabelle di trade-off, figure vicine al testo che le interpreta, assunzioni e limiti dichiarati esplicitamente.

Per gli esempi industriali, ogni caso deve rispondere a quattro domande:

1. Quale problema industriale risolve?
2. Quale stack usa o suggerisce?
3. Che cosa insegna al caso Airspeeder?
4. Quale limite impedisce di copiarlo direttamente?

---

## Regola di chiusura iterazione

Ogni iterazione sostanziale dovrebbe produrre prompt salvato in `prompts/`, artifact aggiornati, report o log aggiornato, commit locali separati per blocco e nota finale con commit hash e test eseguiti.
