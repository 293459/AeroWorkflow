---
title: "Prompt Iterazione 02 — Industrial Workflow Report Expansion"
version: "original"
status: "executed"
date: "2026-05-14"
source_context:
  - "examples/industry_examples.md"
  - "sources/sources.md"
  - "report.md"
---

# Prompt Iterazione 02 — Industrial Workflow Report Expansion

> Prompt originale salvato secondo la logica della execution pipeline. Questa richiesta estende la run precedente: usa gli esempi industriali aggiornati, genera figure Mermaid, amplia il report LaTeX, valuta workflow alternativi e aggiunge guidelines operative.

---

## Testo originale

bene sfruttando ora le casistiche che trovi nel file inustry example:

1. genera tutti i grafici mermaid sotto forma di immagini (ho due estensioni per mermaid su vscode quindi non dovrebbe essere un problema)
2. nel report in latex inserisci una spiegazione di tutte gli esempi industriali cn una spiegazione esaustiva che integri ovviamente gli schemi mermaid . Per farlo usa come riferimento un file markdown che ho appena agginutno alla directory, che sostanzialmente è una skill che spiega come fare reporrt.
3. Oltre agli esempi industriali già pressenta valuta possibili combinazioni alternative che tisembrano ragionevoli in funzione dell'ottenere un workflow completo (valuta anche deei workflow un po' dubbi tanto c'è poi la funzione di metricaa che decide quali sono quelli ottimali)
4. compila tutto il latex in modo che ci sia un odf bello e pronto con il report
5. non limitare il numero di configurazioni anzi tienilo più esaustivo possbile così da considerare tutti i casi ma magari inserisci metadata aggiuntivi tipo a quale run appartengono, se sono stati già processati con la meetrica per salutare se hanno senso e altre strategie per evitare poi di allargare la context window quando si fa la comparazione
6. crea un file di guidelines sia a livello ignegneristico su come bisognerebbe gestire i workflow, la logica sottostante etc... (quindi logica di ingegneria di processo) e sia dal punto di vista informatico su come gestire ad esempio i commit, quando fare i commenti etc... ( e usale come reference quando fai le operazioni varie quindi tienile in considerazione anche nell'execution pipeline etc...). Di base vorei che ad ogni modifica si facesse un commit locale commentando opportunamente i cambi

ovviamente seguendo la logica del programma questi prompt che ti mando devono essere salvati nela cartella prompt, deveessere eseguita laa execution pipeline etc...

---

## Interpretazione operativa

- Salvare il prompt prima delle modifiche successive.
- Usare `report.md` come reference di stile per il capitolo LaTeX.
- Generare figure da tutti i blocchi Mermaid presenti in `examples/industry_examples.md`.
- Aggiungere un catalogo workflow più ampio, con metadata utili per filtrare e confrontare senza caricare tutto in context.
- Aggiornare la documentazione infrastrutturale affinché le guidelines diventino riferimento operativo.
- Compilare il report in PDF; se "odf" era intenzionale, il PDF resta comunque l'output naturale della pipeline LaTeX.
