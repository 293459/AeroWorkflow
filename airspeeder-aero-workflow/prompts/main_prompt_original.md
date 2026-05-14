---
title: "Prompt Originale — Airspeeder Mk3 Aero Workflow"
version: "original"
status: "executed"
date: "2026-05-13"
optimized_version: "main_prompt_optimized.md"
---

# Prompt Originale

> File grezzo così come fornito dall'utente. Non modificato.

---

## Testo originale

Devo ragionare su una possibile logica di integrazione di diversi strumenti usati nel team per creare un workflow smooth. L'idea è quella di realizzare il cad parametrico di un telaio per airspeeder mk3 e fare una serie di analisi aerodinamiche e valutando i risultati iterare e modificare il cad per ottenere quello ottimale. La logica è quello di ottimizzare la resistenza al fine di rendere il modello più competitivo dal punto di vista delle prestazioni.

**Output richiesti:**

1. Una rappresentazione grafica della logica del workflow (prima quella generale poi ciascuna delle configurazioni proposte) con i principali dati (formati file I/O, questioni di interoperabilità)
2. Una tabella con i principali parametri di interesse: tipo di analisi, accuratezza, integrabilità, costi licenze, scalabilità, compatibilità OS, supporto formati
3. Una metrica di valutazione personalizzabile (fornita a parole, da trasformare in markdown organizzato)
4. Per ciascuna configurazione un file markdown di riepilogo completo
5. Un report LaTeX dettagliato (con commenti, citazioni, riferimenti web)
6. Un file sorgenti con tutti i riferimenti + indice di attendibilità
7. Un file examples.md con workflow di aziende leader del settore
8. Un file markdown con le istruzioni per ottimizzare i prompt (basato sul prompt optimizer usato)

**Specifiche tecniche della repo:**
- Struttura repo GitHub
- Diagrammi in Mermaid
- Ogni prompt salvato nella cartella `prompts/` (versione originale e ottimizzata)
- Brainstorming in markdown (sequenza di pensieri grezzi)
- `tools.md` con tutti gli strumenti
- Cartella `execution_logs/`
- `cross_references.md`
- `validator.md` con procedure di verifica
- File di assembly guide
- Cartella `improvements/` (1 per iterazione)
- Execution pipeline in markdown + Mermaid (da txt esistente)
- `token_saving_techniques.md` migliorato (da txt esistente)

**Focus:** Primariamente aerodinamico; aeroacustica secondaria.

**Domande aperte nel prompt originale:**
1. Ci sono ulteriori considerazioni progettuali generali di workflow design?
2. Qual è la rappresentazione grafica finale ottimale (file unico aggregato che si aggiorna se cambiano i componenti)?
3. Come trasformare un prompt monolitico in un prompt modulare eseguibile in fasi o chat separate?
