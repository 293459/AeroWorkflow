---
title: "Tutorials and Learning Resources"
phase: "Documentation"
status: "ready"
last_updated: "2026-05-20"
iteration: 3
scope: "CAD, meshing, CFD, optimization"
---

# Tutorials and Learning Resources

> Raccolta pratica per imparare i software del progetto. Le risorse ufficiali hanno priorita'; YouTube e risorse community sono incluse come punto di partenza, ma vanno sempre confrontate con la documentazione della versione installata.

---

## Percorso consigliato per i due casi studio

1. **CAD parametrico**: imparare sketch, vincoli, configurazioni e parametri in SOLIDWORKS o NX.
2. **Preparazione CFD**: imparare naming superfici, defeaturing, volume fluido, farfield, symmetry plane e moving/rotating regions.
3. **STAR-CCM+**: partire da import CAD, surface repair/wrapper, mesh automatica, prism layers, physics continua, reports/monitors.
4. **HEEDS**: automatizzare il loop CAD -> STAR-CCM+ -> estrazione risposte, poi definire variabili, vincoli, obiettivi e budget run.
5. **Validazione**: eseguire mesh sensitivity, confronto con caso semplice e controlli di convergenza prima di fidarsi dell'ottimizzazione.

---

## SOLIDWORKS

| Tipo | Risorsa | Link | Uso consigliato |
|---|---|---|---|
| Documentazione | SOLIDWORKS Web Help | https://help.solidworks.com/ | Reference ufficiale per funzioni, API e versione installata |
| Training | MySolidWorks | https://my.solidworks.com/training | Lezioni, learning paths e video con file esempio |
| Video ufficiali | SOLIDWORKS YouTube channel | https://www.youtube.com/@SOLIDWORKS | Tips, workflow base, novita' e demo ufficiali |
| Guida ufficiale | Beginners Guide to SOLIDWORKS | https://blogs.solidworks.com/products/solidworks/beginners-guide-to-solidworks/ | Serie video su sketch, parti, assiemi, fori e cloud services |
| Community video | SolidWorksTutorials | https://www.youtube.com/@SolidWorksTutorials | Buono per pratica su modellazione meccanica e surfacing, da verificare con Web Help |

**Per il progetto droni:** concentrarsi su configurazioni, equazioni, design tables, naming pulito dei corpi e export Parasolid/STEP. Evitare STL come formato CAD principale verso STAR-CCM+ se si vuole preservare superfici e patch.

---

## Siemens NX

| Tipo | Risorsa | Link | Uso consigliato |
|---|---|---|---|
| Prodotto | NX CAD Software | https://www.siemens.com/en-us/products/designcenter/nx-cad-software/ | Panoramica su CAD, PLM, CAE/CAM e digital twin |
| Aerospace | NX CAD for aerospace engineering | https://www.siemens.com/en-us/products/designcenter/nx-cad-software/workflows/aerospace-aircraft-design/ | Surfacing, airframes, UAV, urban air mobility, composites e aerostrutture |
| Interoperabilita' | NX CAD interoperability | https://www.siemens.com/en-us/products/designcenter/nx-cad-software/cad-interoperability/ | Master model, formati, Teamcenter, scambio dati |
| New user | NX design resources | https://www.siemens.com/en-gb/products/designcenter/nx-cad-software/new-user/ | Documenti e video iniziali |
| Video ufficiali | NX Tips and Tricks playlist | https://www.youtube.com/playlist?list=PL1m1vu8_quoDVJfmPp3FL9700HGM_LK9P | Playlist ufficiale linkata dalla pagina Siemens per nuovi utenti |

**Per il progetto droni:** dare priorita' a parametric modeling, synchronous/direct editing, surface modeling, assembly arrangements, expressions e gestione master model. NX e' la scelta piu' naturale se il workflow resta dentro Siemens.

---

## Simcenter STAR-CCM+

| Tipo | Risorsa | Link | Uso consigliato |
|---|---|---|---|
| Prodotto | Simcenter STAR-CCM+ | https://www.siemens.com/en-gb/products/simcenter/fluids-thermal-simulation/star-ccm/ | CAD handling, automated meshing, multiphysics, post-processing, design exploration |
| Training ufficiale | STAR-CCM+ Fundamentals | https://training.plm.automation.siemens.com/ilt/iltdescription.cfm?pID=TR09101-EN____STAR_2020.1_B9 | Corso base-intermedio su workflow, mesh, physics, post e automazione |
| Curriculum | STAR-CCM+ CFD Curriculum | https://resources.sw.siemens.com/en-US/download-computational-fluid-dynamics/ | Tutorial NACA 4412 completo: mesh, run, analisi, validazione |
| Webinar | CFD simulations in STAR-CCM+ | https://webinars.sw.siemens.com/en-US/enabling-simulation-driven-design-simcenter-star-ccm/ | Demo CAD-to-results e design exploration |
| Video | Siemens Software YouTube search: STAR-CCM+ | https://www.youtube.com/@SiemensSoftware/search?query=STAR-CCM%2B | Video ufficiali e webinar caricati sul canale Siemens |
| Community | VOLUPE STAR-CCM+ blog | https://volupe.com/simcenter-star-ccm/ | Articoli pratici su setup, meshing, macro e best practice |

**Per il progetto droni:** imparare bene surface wrapper, local mesh controls, prism layer mesher, rotating/moving reference frames, overset/sliding mesh, force reports e Java macros. La qualita' della mesh va sempre provata con uno studio coarse/medium/fine.

---

## Simcenter HEEDS

| Tipo | Risorsa | Link | Uso consigliato |
|---|---|---|---|
| Prodotto | Simcenter HEEDS | https://www.siemens.com/en-us/products/simcenter/integration-solutions/heeds/ | Workflow automation, SHERPA, distributed execution, AI Simulation Predictor |
| Workflow | Design space exploration and optimization | https://www.siemens.com/en-us/products/simcenter/simulation-test/design-space-exploration-optimization/ | Logica generale di esplorazione e ottimizzazione industriale |
| Case study | Martin UAV V-BAT | https://resources.sw.siemens.com/en-US/case-study-martin-uav/ | Esempio piu' vicino: STAR-CCM+ + HEEDS per ducted-fan VTOL UAV |
| Webinar | Turbine blade simulation and optimization | https://webinars.sw.siemens.com/en-US/simulation-optimization-of-gas-turbine-blades-simcenter/ | Esempio MDAO/HEEDS con workflow template-driven |
| Video | Siemens Software YouTube search: HEEDS | https://www.youtube.com/@SiemensSoftware/search?query=HEEDS | Video e webinar ufficiali disponibili sul canale Siemens |

**Per il progetto droni:** HEEDS va imparato come orchestratore, non come solver. La parte importante e' definire variabili robuste, bounds, constraints, response extraction e criteri di fallimento delle run CFD.

---

## OpenVSP

| Tipo | Risorsa | Link | Uso consigliato |
|---|---|---|---|
| Sito | OpenVSP | https://openvsp.org | Download, docs, wiki e API |
| Video/guide ufficiali | NASA OpenVSP Ground School | https://www.nasa.gov/software/openvsp-ground-school/ | Tutorial video per modellazione parametrica aeronautica |
| Docs | OpenVSP Documentation | https://openvsp.org/docs.shtml | Indice docs, wiki, API C++/AngelScript/Python |
| API | OpenVSP API Docs | https://openvsp.org/api_docs/ | Automazione geometry generation e export |

---

## GMSH

| Tipo | Risorsa | Link | Uso consigliato |
|---|---|---|---|
| Docs | Gmsh documentation | https://gmsh.info/doc/texinfo/ | Tutorial progressivi t1-t21 e API |
| API | Python package | https://gmsh.info/#Download | Automazione mesh via Python |
| Video | YouTube search: Gmsh Python API | https://www.youtube.com/results?search_query=gmsh+python+api+tutorial | Video community da usare dopo i tutorial ufficiali |

**Nota STAR-CCM+:** GMSH e' ottimo per stack open source e per controllare la mesh via script. Se il solver e' STAR-CCM+, normalmente conviene usare il mesher interno STAR-CCM+ per mantenere coerenza regioni, patch, prism layers e adattamento.

---

## SU2

| Tipo | Risorsa | Link | Uso consigliato |
|---|---|---|---|
| Docs | SU2 documentation | https://su2code.github.io/docs_v7/home/ | Concetti, solver, opzioni configurazione |
| Tutorial | SU2 Tutorial Collection | https://su2code.github.io/tutorials/home/ | Esempi ordinati per complessita', con mesh e config |
| GitHub | SU2 Tutorials repository | https://github.com/su2code/Tutorials | File pronti per run locali |
| Ottimizzazione | Shape optimization in SU2 | https://su2code.github.io/documents/Optimization_Using_SU2.pdf | Base per adjoint e shape optimization |

---

## OpenFOAM

| Tipo | Risorsa | Link | Uso consigliato |
|---|---|---|---|
| User Guide | OpenFOAM User Guide | https://www.openfoam.com/documentation/user-guide | Case structure, mesh, solvers, models, post-processing |
| Tutorial wiki | OpenFOAM tutorials | https://wiki.openfoam.com/Tutorials | Casi di esempio e raccolte community |
| Video | Fluid Mechanics 101 YouTube | https://www.youtube.com/@fluidmechanics101 | Fondamenti CFD/OpenFOAM utili per capire SIMPLE/PIMPLE e turbolenza |

---

## ParaView

| Tipo | Risorsa | Link | Uso consigliato |
|---|---|---|---|
| Docs | ParaView Tutorials | https://docs.paraview.org/en/latest/Tutorials/ | Self-directed e classroom tutorials |
| Webinars | ParaView Tutorials and Webinars | https://www.paraview.org/tutorials/ | Include webinar CFD post-processing |
| Video | Kitware YouTube search: ParaView CFD | https://www.youtube.com/@KitwareInc/search?query=ParaView%20CFD | Video ufficiali Kitware e webinar |

---

## XFLR5

| Tipo | Risorsa | Link | Uso consigliato |
|---|---|---|---|
| Sito | XFLR5 official | https://www.xflr5.tech/xflr5.htm | Documentazione, note, video tutorial base |
| Guide | ROSflight XFLR5 guide | https://docs.rosflight.org/latest/user-guide/tutorials/user-manual-xflr5/ | Guida didattica per piccoli velivoli/UAV |
| Tutorial universitari | Notre Dame XFLR5 tutorials | https://prumbach.nd.edu/xflr5/ | Introduzione e stabilita'/dynamic response |
| Video | YouTube search: XFLR5 tutorial | https://www.youtube.com/results?search_query=xflr5+tutorial+uav | Video community per workflow base |

---

## Optuna

| Tipo | Risorsa | Link | Uso consigliato |
|---|---|---|---|
| Docs | Optuna documentation | https://optuna.readthedocs.io/en/stable/ | Study, trial, samplers, pruning, dashboard |
| Tutorial | Optuna tutorial | https://optuna.readthedocs.io/en/stable/tutorial/ | Introduzione e ricette operative |
| Dashboard | Optuna Dashboard | https://optuna-dashboard.readthedocs.io/ | Monitoraggio run e human-in-the-loop optimization |
| Paper | Optuna KDD paper | https://arxiv.org/abs/1907.10902 | Base teorica del framework |

---

## Regola pratica di apprendimento

Per ogni software, completare prima un tutorial "toy" ufficiale e poi replicarlo con un micro-caso Airspeeder:

| Step | Micro-caso |
|---|---|
| CAD | corpo fusoliera semplificato + due bracci + naming superfici |
| Mesh | farfield, refinement locale, prism layers su pareti principali |
| CFD | incompressibile/RANS a 27.8 m/s, estrazione Cd e residual monitors |
| Ottimizzazione | 3-5 variabili geometriche, 20 run iniziali, constraints su volume/clearance |

Solo dopo questo passaggio ha senso scalare verso geometria completa, rotori e multi-obiettivo.
