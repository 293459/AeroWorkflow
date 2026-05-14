---
title: "Evaluation Metrics — Airspeeder Mk3 Aero Workflow"
phase: "Setup"
status: "ready"
last_updated: "2026-05-13"
iteration: 1
---

# Metriche di Valutazione — Configurazioni Workflow

> Questo file definisce i criteri e i pesi per ordinare le configurazioni workflow dalla più alla meno adatta al progetto. I pesi riflettono le priorità specificate nel brief di progetto.

---

## Criteri e pesi

| # | Criterio | Peso (%) | Note |
|---|---|---|---|
| 1 | Tipo di analisi supportate | 15% | Focus aerodinamica; aeroacustica è secondaria |
| 2 | Accuratezza delle analisi | 20% | Rilevante nella fase di progetto dettagliato |
| 3 | Integrabilità con altri software | 15% | Interoperabilità dei formati file |
| 4 | Costo delle licenze | 15% | Open source preferito se non sacrifica accuratezza |
| 5 | Scalabilità del workflow | 10% | Per ora analisi leggere; importante in futuro |
| 6 | Compatibilità OS | 10% | Windows primario nel team, Linux per workstation |
| 7 | Supporto formati di calcolo | 15% | Flessibilità per cambiamenti futuri |

**Peso totale: 100%**

---

## Scale di valutazione

Ogni criterio è valutato su scala **1–5**:

| Voto | Significato |
|---|---|
| 5 | Eccellente — nessuna limitazione rilevante |
| 4 | Buono — limitazione minore trascurabile |
| 3 | Sufficiente — limitazione presente ma gestibile |
| 2 | Scarso — limitazione significativa |
| 1 | Inaccettabile — blocca l'uso pratico |

---

## Dettaglio criteri

### 1. Tipo di analisi supportate (15%)

Valuta quali fenomeni fisici il workflow può simulare:

- **5:** RANS steady + unsteady, LES/DES, aeroacustica, multifase
- **4:** RANS steady + unsteady, analisi modale
- **3:** RANS steady, analisi di stabilità
- **2:** Metodi a pannelli (potenziale), solo steady
- **1:** Solo analisi qualitative

*Per questo progetto, RANS steady è il requisito minimo (voto ≥ 3).*

---

### 2. Accuratezza delle analisi (20%)

Valuta l'errore atteso rispetto a dati sperimentali o High-Fidelity:

- **5:** Errore < 2% su Cd/Cl (LES con mesh fine)
- **4:** Errore < 5% su Cd/Cl (RANS con buona mesh)
- **3:** Errore < 10% su Cd/Cl (RANS con mesh media)
- **2:** Errore < 20% (metodi a pannelli su geometria semplice)
- **1:** Errore > 20% o non quantificabile

*Nella fase preliminare si accetta voto ≥ 2; nella fase di design finale si richiede voto ≥ 4.*

---

### 3. Integrabilità con altri software (15%)

Valuta la facilità di scambio dati con OpenVSP e gli altri tool del team:

- **5:** API Python nativa, formati standard (SU2, VTK, CGNS, STEP)
- **4:** Formati standard senza API Python
- **3:** Formati proprietari con converter disponibile
- **2:** Formati proprietari con converter limitato
- **1:** Nessuna integrazione praticabile

---

### 4. Costo licenze (15%)

- **5:** Completamente open source (MIT, GPL, Apache)
- **4:** Open source con alcune dipendenze commerciali opzionali
- **3:** Freemium o accademico gratuito
- **2:** Licenza commerciale < €5.000/anno
- **1:** Licenza commerciale > €5.000/anno

---

### 5. Scalabilità (10%)

Valuta quanto il workflow scala con mesh più grandi, più run paralleli, HPC:

- **5:** Supporto MPI nativo, scalabilità documentata fino a 1000+ core
- **4:** MPI supportato, testato fino a 100 core
- **3:** MPI supportato ma non ottimizzato
- **2:** Solo single-node, multi-thread
- **1:** Single-thread only

---

### 6. Compatibilità OS (10%)

Dato il contesto del team (Windows primario, possibile workstation Linux):

- **5:** Windows nativo + Linux + macOS, installazione semplice
- **4:** Windows nativo + Linux
- **3:** Linux nativo, Windows via WSL2 (funziona con setup)
- **2:** Solo Linux
- **1:** Solo Linux con requisiti HW specifici

---

### 7. Supporto formati di calcolo (15%)

Valuta quanti formati mesh/geometria/risultati il solver accetta/produce:

- **5:** CGNS, SU2, OpenFOAM, VTK, STL, STEP, IGES, Fluent, tecplot
- **4:** CGNS, SU2, VTK, STL, STEP
- **3:** Formato nativo + STL/VTK
- **2:** Solo formato nativo con export limitato
- **1:** Formato proprietario chiuso

---

## Calcolo punteggio

$$S_{config} = \sum_{i=1}^{7} w_i \cdot v_i$$

Dove:
- $w_i$ = peso del criterio $i$ (in percentuale, 0–1)
- $v_i$ = voto del criterio $i$ (1–5)

**Punteggio massimo teorico:** 5.0  
**Soglia minima accettabile:** 3.0

---

## Come aggiornare questa metrica

Per modificare i pesi in base a nuove priorità del team:
1. Cambiare i valori nella colonna "Peso (%)" assicurandosi che la somma sia sempre 100%
2. Ricalcolare i punteggi nelle tabelle comparative dei singoli config
3. Aggiornare `last_updated` e `iteration`
4. Committare con messaggio: `metrics: updated weights - [motivazione]`
