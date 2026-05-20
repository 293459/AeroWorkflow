---
title: "Prompt Iteration 03 - CAD + STAR-CCM+ + HEEDS"
version: "original"
status: "executed"
date: "2026-05-20"
optimized_version: "iteration_03_cad_starccm_heeds_optimized.md"
run_id: "iteration_03_cad_starccm_heeds"
---

# Prompt Originale - Iterazione 03

> File grezzo cosi' come fornito dall'utente. Non modificato nei contenuti tecnici.

---

## Testo originale

Facendo riferimento a questa repo https://github.com/293459/AeroWorkflow (che e' la stessa che trovi in locale qui suvsstudio code e a cui puoi accedere traite l'IDE) e in particolare modo al file di possibili configurazioni, voglio che tu vada a studiare in dettaglio le configurazioni di seguito:

1. Solidwork(CAD) -> starccm+(mesh+CFD) -> heeds(optimisation)
2. NX(CAD) -> starccm+(mesh+CFD) -> heeds(optimisation)

Prova a rispondere alle seguenti domande:

1. meglio solidwork o NX nel nostro campo di applicazioni droni?
2. Starcc+ fa bene le mesh? Oppure conviene farle con altri software, che so gmsh?
3. come funziona heeds e i software di ottimizzazione in generale a livello industriale? Cosa permettono di modificare e come funziona il loro processo.

Esegui le seguenti azioni:

1. aggiorna la lista delle fonti (sources.md) verificando che ciascun software sia presente e inserisci tutte le informazioni a riguardo
2. crea un file tutorials.md che contenga per ogni software (in particolare modo questi che cito) dei video tutorial su YouTube, delle guide su internet, della documentazione e in generale risorse che servano ad imparare i software
3. aggiungi al report.tex i due casi studio. Cambia la logica, anziche' avere un unico file latex complessivo produci diversi file latex (che al limite assembli in un main.tex). Fai un primo file che spiega il funzionamento e la logica del software e poi un file per iterazione (tipo chiamandoli iter1,iter2 etc...) che corrisponde ad un diverso caso di studio
4. aggiorna tutto il progetto seguendo la logica solita (crea file di prompt, prompt ottimizzato, risultati dell'analisi, improvements etc..)
