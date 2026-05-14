# Airspeeder Mk3 — Aerodynamic Workflow Repository

> **Obiettivo:** Ottimizzare la resistenza aerodinamica (drag) del telaio Airspeeder Mk3 tramite un workflow CAD parametrico + analisi CFD iterativa, al fine di massimizzare le prestazioni competitive.

---

## Navigazione rapida

| File / Cartella | Descrizione |
|---|---|
| [`brainstorming.md`](brainstorming.md) | Ragionamenti grezzi da cui nasce il progetto |
| [`execution_pipeline.md`](execution_pipeline.md) | Pipeline di esecuzione per LLM (con diagramma Mermaid) |
| [`tools.md`](tools.md) | Tutti gli strumenti del progetto |
| [`validator.md`](validator.md) | Procedure di validazione dei risultati |
| [`assembly_guide.md`](assembly_guide.md) | Come si assemblano i file nel progetto finale |
| [`cross_references.md`](cross_references.md) | Dipendenze tra file e artifacts |
| [`token_saving_techniques.md`](token_saving_techniques.md) | Tecniche per gestire context window e token |
| [`metrics/evaluation_metrics.md`](metrics/evaluation_metrics.md) | Metrica di valutazione delle configurazioni |
| [`configs/`](configs/) | Configurazioni workflow (3 opzioni) |
| [`prompts/`](prompts/) | Prompt originali e ottimizzati |
| [`sources/sources.md`](sources/sources.md) | Sorgenti con reliability index |
| [`examples/industry_examples.md`](examples/industry_examples.md) | Workflow adottati da aziende leader |
| [`improvements/`](improvements/) | Suggerimenti di miglioramento per iterazione |
| [`execution_logs/`](execution_logs/) | Log di esecuzione dei prompt |
| [`report/report.tex`](report/report.tex) | Report LaTeX completo |

---

## Panoramica del progetto

### Contesto
L'**Airspeeder Mk3** è un veicolo da corsa elettrico volante (eVTOL racing). L'obiettivo è ridurre la resistenza aerodinamica del telaio per migliorare le prestazioni in gara, tramite un ciclo CAD parametrico → analisi CFD → ottimizzazione.

### Configurazioni analizzate

| # | Stack | Fidelity | Costo | Consigliata per |
|---|---|---|---|---|
| 1 | OpenVSP + SU2 | Media-Alta | Free | **Progetto principale** |
| 2 | OpenVSP + OpenFOAM | Alta | Free | Analisi dettagliate |
| 3 | OpenVSP + XFLR5 | Bassa-Media | Free | Fase preliminare |

### Filosofia del workflow
```
CAD Parametrico → Mesh → CFD → Post-processing → Analisi → Ottimizzazione → CAD (iterazione)
```

---

## Come usare questa repo con un LLM

1. Leggi [`execution_pipeline.md`](execution_pipeline.md) per capire l'ordine dei passi
2. Consulta [`cross_references.md`](cross_references.md) per le dipendenze tra file
3. Usa [`token_saving_techniques.md`](token_saving_techniques.md) per gestire la context window
4. Ogni passo produce un file in [`execution_logs/`](execution_logs/)
5. I miglioramenti suggeriti vanno in [`improvements/`](improvements/)

---

## Requisiti

- Python ≥ 3.9
- OpenVSP ≥ 3.40 (Windows/Linux/macOS)
- SU2 ≥ 7.5 **oppure** OpenFOAM ≥ 10
- GMSH ≥ 4.11 (meshing)
- ParaView ≥ 5.11 (post-processing)
- LaTeX (per compilare il report)

---

*Generato con Claude Sonnet 4.6 — iterazione 01*
