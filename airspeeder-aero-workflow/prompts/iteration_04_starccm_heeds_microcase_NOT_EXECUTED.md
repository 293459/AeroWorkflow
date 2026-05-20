---
title: "Prompt Iteration 04 NOT EXECUTED - STAR-CCM+ / HEEDS Microcase"
version: "next"
status: "not executed"
date: "2026-05-20"
depends_on: "iteration_03_cad_starccm_heeds"
---

# Prompt Iterazione 04 - NOT EXECUTED

Studia un micro-caso operativo per verificare il workflow NX/SOLIDWORKS -> STAR-CCM+ -> HEEDS senza usare subito la geometria completa Airspeeder.

Obiettivi:

1. Definisci una geometria semplificata: fusoliera ellissoidale, due bracci, fairing rotore semplificati.
2. Definisci 5 variabili CAD robuste e i relativi bounds.
3. Definisci 2 vincoli: clearance rotori e volume/massa proxy.
4. Definisci 2 obiettivi: minimizzare Cd in cruise e limitare momento/pitch proxy.
5. Specifica una mesh STAR-CCM+ coarse/medium/fine con target y+ e criteri di qualita'.
6. Definisci il template HEEDS: input, output, response extraction, failure handling, budget run.
7. Aggiorna `configs/`, `results/`, `report/iterations/iter3_*.tex`, `execution_logs/` e `improvements/`.

Vincolo:

- Non avviare un'ottimizzazione reale senza licenze/tool disponibili; produrre template e processo verificabile.
