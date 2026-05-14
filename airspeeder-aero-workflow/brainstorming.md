# Brainstorming — Airspeeder Mk3 Aero Workflow

> *Non è una guida ordinata. È una sequenza di pensieri, dubbi, intuizioni e ragionamenti grezzi da cui nasce il progetto. Leggerlo è come assistere a una conversazione con sé stessi.*

---

Allora. Ho un telaio Airspeeder Mk3 da ottimizzare aerodinamicamente. L'obiettivo è ridurre il drag per migliorare le prestazioni in gara. Okay, punto di partenza semplice. Ma come si fa?

Prima questione: il CAD deve essere **parametrico**. Non voglio ogni volta rifare tutto da zero — voglio cambiare un parametro (angolo, curvatura, dimensione) e ricalcolare automaticamente. Questo è fondamentale per l'ottimizzazione iterativa. OpenVSP sembra la scelta naturale qui, già lo usiamo nel team.

Poi: quali analisi fare? Aerodinamica sicuro. Aeroacustica? Probabilmente meno urgente per una gara dove conta la resistenza. Ma potrebbe tornare utile in futuro... lasciamo la porta aperta ma non è priorità ora.

Il punto critico è l'interoperabilità. Il CAD produce un file (STL? STEP? VSP3?), il solver CFD ne vuole un altro. Ci sono conversioni di mezzo? Perdite di qualità geometrica? Questo è il collo di bottiglia tipico dei workflow aero.

Pensando agli stack possibili... OpenVSP + SU2 sembra il più "clean" perché SU2 accetta file mesh da GMSH o addirittura ha un mesher interno, e OpenVSP esporta già in formati compatibili. OpenFOAM sarebbe più potente ma ha una curva di apprendimento brutale, soprattutto per chi non l'ha mai usato — e la preparazione della mesh con snappyHexMesh è un'arte in sé. XFLR5 è velocissimo ma usa metodi a pannelli, quindi per geometrie complesse come un telaio Airspeeder (non è esattamente un'ala) potrebbe non essere abbastanza preciso.

Ah, ma aspetta — per la fase preliminare XFLR5 o addirittura AVL potrebbero essere utili. Non per la risposta definitiva ma per capire rapidamente l'ordine di grandezza, orientarsi, scartare configurazioni ovviamente brutte prima di buttarci dentro ore di calcolo SU2.

La questione Windows vs Linux è un problema concreto. OpenFOAM su Windows è un casino (WSL2 funziona ma aggiunge complessità). SU2 gira su Windows nativamente. OpenVSP anche. Quindi Config 1 (OpenVSP+SU2) è molto più facile da installare per il team.

Ottimizzazione: come la faccio? Manuale (cambio parametri a mano, calcolo, guardo) oppure automatica (Optuna/SLSQP che variano i parametri OpenVSP e lanciano automaticamente SU2)? Quella automatica sarebbe bellissima ma richiede che il workflow sia completamente scriptato. Fattibile con Python — OpenVSP ha bindings Python, SU2 ha un'interfaccia a config files...

Budget computazionale: per analisi RANS su una geometria come Airspeeder, quanto tempo ci vuole su una workstation normale? Con SU2 una mesh da ~1M celle potrebbe prendere 30 min - 2h su 8 core. Dipende da quanto raffiniamo. Per l'ottimizzazione automatica bisogna che ogni run sia sotto qualche ora altrimenti non è praticabile in tempi ragionevoli.

Post-processing: ParaView è gratuito e potente, già noto. L'output di SU2 è in VTK, ParaView lo legge nativamente. Perfetto.

Altra cosa: documentazione del workflow. Devo fare in modo che un altro membro del team possa capire e riprendere il lavoro. Quindi README chiari, naming convention stabile, no magic numbers nel codice...

La questione dei format: OpenVSP esporta in .stl, .obj, .stp, .degen (file proprio), .vsp3 (nativo). Per CFD di solito si parte dalla superficie STL o da un file STEP pulito. GMSH può meshare a partire da STL (ma la qualità dipende dalla qualità dell'STL...) oppure da STEP.

Pensando all'Airspeeder Mk3 nello specifico: è un veicolo che vola, quindi ha componenti rotanti (rotori) oltre al telaio statico. Per l'aerodinamica del telaio in volo rettilineo uniforme la simulazione steady state RANS dovrebbe andare bene. Tralasciamo per ora l'interazione rotore-fusoliera che richiede simulazioni più complesse (sliding mesh, etc.).

Ultima cosa: tenere traccia di tutti i run, parametri, risultati. Un database semplice anche in CSV va bene. Così poi posso plottare i risultati, vedere le tendenze, capire quali parametri impattano di più il drag.

Okay, credo di avere abbastanza per strutturare il progetto.

---

## Domande aperte

- Qual è il livello di dettaglio geometrico necessario? Telaio "liscio" o con tutti i dettagli costruttivi?
- Quante iterazioni di ottimizzazione sono realistiche con il budget computazionale disponibile?
- L'ottimizzazione è mono-obiettivo (solo drag) o multi-obiettivo (drag + downforce + stabilità)?
- Il team ha esperienza con SU2 o partiamo da zero?
- C'è una workstation dedicata o si gira tutto su laptop?

---

## Considerazioni generali di workflow design (spesso trascurate)

Queste sono cose che chi si occupa seriamente di workflow CFD tiene sempre in conto:

1. **Reproductibilità**: ogni run deve essere riproducibile. Seeds fissi, versionamento dei file di config, log completi.
2. **Graceful failure**: se un run CFD diverge (capitano!), il sistema deve gestirlo senza bloccare tutto il processo di ottimizzazione.
3. **Mesh sensitivity study**: prima di fare ottimizzazione, verificare che il risultato non dipenda dalla dimensione della mesh. Almeno 3 livelli di raffinamento.
4. **Validazione con dati sperimentali o letteratura**: se non si ha un dato di riferimento, come si sa che il solver sta calcolando correttamente?
5. **Separazione geometria/fisica**: il file CAD non dovrebbe contenere info fisiche; quelle vanno nel config del solver.
6. **Backup automatico**: con workflow lunghi, checkpoint frequenti. Se il calcolo si interrompe dopo 10h, non si ricomincia da zero.
