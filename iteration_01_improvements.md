---
title: "Suggested Improvements — Iteration 01"
iteration: 1
date: "2026-05-13"
status: "pending review"
next_prompt: "prompts/iteration_02_NOT_EXECUTED.md"
---

# Suggested Improvements — Iterazione 01

> Analisi di cosa ha funzionato, cosa manca, e suggerimenti concreti per la prossima iterazione.

---

## Cosa è stato prodotto in questa iterazione

- ✅ Struttura repo completa (tutti i file fondamentali)
- ✅ 3 configurazioni workflow con valutazione metrica
- ✅ Diagrammi Mermaid per ogni config e pipeline
- ✅ tools.md, sources.md con reliability index
- ✅ Industry examples con 5 casi aziendali
- ✅ validator.md con check automatizzabili
- ✅ cross_references.md, assembly_guide.md
- ✅ Prompt originale + ottimizzato + optimizer instructions
- ✅ Report LaTeX (struttura e sezioni principali)
- ✅ token_saving_techniques.md migliorato

---

## Cosa manca o è incompleto

| Item | Priorità | Note |
|---|---|---|
| Script Python reali (non solo template) | Alta | `extract_mermaid.py`, `build_comparison_table.py` vanno implementati completamente |
| File `.cfg` SU2 completo per Airspeeder | Alta | Il template è generico, va calibrato per quadricottero |
| Script GMSH `.geo` per geometria telaio | Alta | Non ancora scritto |
| `openvsp_model.py` per parametrizzazione | Alta | Manca completamente |
| Report LaTeX sezioni contenuto (non solo struttura) | Media | Sezioni `config1.tex`, `config2.tex` ecc. vanno popolate |
| Dati tecnici Mk3 più precisi | Media | MTOW, dimensioni esatte telaio non trovate pubblicamente |
| Analisi aeroacustica (anche se secondaria) | Bassa | Non coperta in questa iterazione |

---

## Cosa ha funzionato bene

1. **Struttura modulare per layer** — chiara e scalabile
2. **Mermaid per tutti i diagrammi** — coerente con la richiesta
3. **YAML metadata header** — permette parsing automatico (es. comparison table)
4. **Reliability index nelle sources** — aggiunge valore pratico
5. **Validator con script Python** — immediatamente usabile
6. **Industry examples con contesto critico** — non solo lista ma analisi

---

## Suggerimenti specifici per iterazione 02

### Priorità Alta — Codice funzionante

1. **Implementare `openvsp_model.py`**
   - Classe `AirspeedermK3Model` con parametri geometrici
   - Metodo `export_stl(params) → path`
   - Bounds realistica per spazio di ottimizzazione

2. **Implementare script GMSH**
   - Script `.geo` per geometria esterna del telaio
   - 3 livelli di mesh (coarse/medium/fine)
   - Boundary layer con y+ ≈ 1

3. **Config SU2 calibrata per Mk3**
   - Velocità di riferimento corretta (~28 m/s = 100 km/h)
   - Densità aria a quota operativa
   - Condizioni al contorno realistiche

4. **Script ottimizzazione Optuna**
   - Loop completo: Optuna → OpenVSP → GMSH → SU2 → estrazione Cd
   - Gestione errori (divergenza CFD)
   - Log automatico in `optimization/history.csv`

### Priorità Media — Documentazione

5. **Popolare le sezioni LaTeX** con dati reali dopo i primi run
6. **Aggiungere confronto quantitativo** tra le 3 configs con dati simulati
7. **Aggiungere README in ogni sottocartella** per navigazione rapida

### Priorità Bassa — Miglioramenti futuri

8. **Aggiungere Config 4** (Ansys Fluent per confronto commerciale — solo come benchmark)
9. **Dashboard web** con risultati delle run (Streamlit o HTML statico)
10. **GitHub Actions** per validazione automatica della repo ad ogni commit

---

## Domande aperte per il prossimo prompt

1. Sono disponibili dati geometrici precisi del telaio Mk3 (CAD o specifiche)?
2. Qual è la velocità di riferimento per l'ottimizzazione (100 km/h race speed o altro)?
3. È previsto un budget computazionale specifico (ore di calcolo, n° di run)?
4. Il team ha già esperienza con SU2/OpenFOAM o si parte da zero?
5. L'ottimizzazione è mono-obiettivo (solo Cd) o multi-obiettivo (Cd + stabilità)?
