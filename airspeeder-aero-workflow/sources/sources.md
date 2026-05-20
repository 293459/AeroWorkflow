---
title: "Sources — Airspeeder Mk3 Aero Workflow"
phase: "Documentation"
status: "updated"
last_updated: "2026-05-20"
iteration: 3
research_scope: "solidworks_nx_starccm_heeds_focus"
---

# Sorgenti e Riferimenti

> Tutti i riferimenti usati nel progetto, con URL, data di accesso, tipo di fonte e reliability score.
> **Reliability Score (1-5):** 5 = documentazione ufficiale / paper peer-reviewed; 4 = sito ufficiale o paper non ancora completamente verificato; 3 = articolo tecnico non peer-reviewed; 2 = forum/community; 1 = fonte secondaria o non verificabile.

---

## Software — Documentazione Ufficiale

| # | Nome | URL | Tipo | Reliability | Data accesso | Note |
|---|---|---|---|---|---|---|
| S01 | OpenVSP Official | https://openvsp.org | Sito ufficiale NASA/OpenVSP | 5 | 2026-05-14 | Homepage aggiornata; release OpenVSP 3.50.2 pubblicata il 2026-05-09 |
| S02 | OpenVSP GitHub | https://github.com/OpenVSP/OpenVSP | Repository GitHub | 5 | 2026-05-13 | Codice sorgente + issues tracker |
| S03 | SU2 Official | https://su2code.github.io | Sito ufficiale | 5 | 2026-05-14 | Multiphysics simulation/design, open source LGPL 2.1 |
| S04 | SU2 GitHub | https://github.com/su2code/SU2 | Repository GitHub | 5 | 2026-05-13 | Codice + wiki + esempi |
| S05 | OpenFOAM Official | https://openfoam.org | Sito ufficiale | 5 | 2026-05-13 | Versione OpenFOAM.org |
| S06 | OpenFOAM ESI | https://www.openfoam.com | Sito ufficiale ESI | 5 | 2026-05-13 | Versione commerciale/community ESI |
| S07 | GMSH Official | https://gmsh.info | Sito ufficiale | 5 | 2026-05-13 | Docs, API, tutorials |
| S08 | ParaView Official | https://www.paraview.org | Sito ufficiale | 5 | 2026-05-13 | Docs + pvpython reference |
| S09 | XFLR5 | http://www.xflr5.tech | Sito ufficiale | 4 | 2026-05-13 | Meno aggiornato, versione stabile |
| S10 | Optuna | https://optuna.org | Sito ufficiale | 5 | 2026-05-13 | Docs complete, tutorial Bayesian optimization |

---

## Software Proprietari Verificati per Iterazione 03

| # | Nome | URL | Tipo | Reliability | Data accesso | Note |
|---|---|---|---|---|---|---|
| S37 | SOLIDWORKS Design | https://www.solidworks.com/product/solidworks-design | Sito prodotto ufficiale | 5 | 2026-05-20 | CAD parametrico 3D, forte su parti/assiemi/disegni, collaborazione cloud e strumenti integrati di simulazione/CAM; molto accessibile per team meccanici |
| S38 | SOLIDWORKS Web Help / MySolidWorks | https://help.solidworks.com/ | Documentazione ufficiale | 5 | 2026-05-20 | Help 2026, API Help e accesso a MySolidWorks con training online, file esempio e quiz |
| S39 | Siemens NX CAD | https://www.siemens.com/en-us/products/designcenter/nx-cad-software/ | Sito prodotto ufficiale | 5 | 2026-05-20 | CAD integrato con PLM, CAM, CAE, Simcenter e digital twin; adatto a prodotti complessi |
| S40 | Siemens NX CAD for Aerospace | https://www.siemens.com/en-us/products/designcenter/nx-cad-software/workflows/aerospace-aircraft-design/ | Pagina workflow ufficiale | 5 | 2026-05-20 | Pagina specifica aerospace: UAV, urban air mobility, advanced surfacing, simulation, automation, composites e design aerostrutturale |
| S41 | Siemens NX CAD Interoperability | https://www.siemens.com/en-us/products/designcenter/nx-cad-software/cad-interoperability/ | Documentazione prodotto ufficiale | 5 | 2026-05-20 | Master model technology, traduttori STEP/IGES/JT/STL e integrazione con Teamcenter; utile per mantenere coerenza CAD-simulation |
| S42 | Simcenter STAR-CCM+ | https://www.siemens.com/en-gb/products/simcenter/fluids-thermal-simulation/star-ccm/ | Sito prodotto ufficiale | 5 | 2026-05-20 | CFD multiphysics integrato con CAD handling, surface repair/wrapping, meshing automatico, solver, post-processing e design exploration |
| S43 | STAR-CCM+ Meshing Solutions Fact Sheet | https://resources.sw.siemens.com/en-US/fact-sheet-cad-to-mesh-conversion/ | Fact sheet ufficiale | 5 | 2026-05-20 | Riferimento specifico per CAD-to-mesh, surface wrapper, polyhedral/trimmer/prism layer e mesh motion/adaptation |
| S44 | Simcenter STAR-CCM+ Fundamentals | https://training.plm.automation.siemens.com/ilt/iltdescription.cfm?pID=TR09101-EN____STAR_2020.1_B9 | Training ufficiale | 5 | 2026-05-20 | Corso Siemens Xcelerator Academy: workflow, import, mesh generation, automatic meshing, surface cleanup, post-processing e automazione |
| S45 | STAR-CCM+ CFD Curriculum | https://resources.sw.siemens.com/en-US/download-computational-fluid-dynamics/ | Risorsa didattica ufficiale | 5 | 2026-05-20 | Simulazioni prebuilt; include tutorial completo NACA 4412 su meshing, run, analisi e validazione |
| S46 | Simcenter HEEDS | https://www.siemens.com/en-us/products/simcenter/integration-solutions/heeds/ | Sito prodotto ufficiale | 5 | 2026-05-20 | Design space exploration, workflow automation, distributed execution, SHERPA hybrid adaptive search e AI Simulation Predictor |
| S47 | Simcenter Design Space Exploration and Optimization | https://www.siemens.com/en-us/products/simcenter/simulation-test/design-space-exploration-optimization/ | Pagina workflow ufficiale | 5 | 2026-05-20 | Spiega la logica industriale: esplorare parametricamente lo spazio progetto per prevedere l'effetto delle modifiche su performance reali |
| S48 | SOLIDWORKS Beginners Guide | https://blogs.solidworks.com/products/solidworks/beginners-guide-to-solidworks/ | Tutorial ufficiale | 5 | 2026-05-20 | Serie video ufficiale su basi CAD: sketch, parti, assiemi, fori, comandi quotidiani e cloud services |
| S49 | NX Design Software Resources | https://www.siemens.com/en-gb/products/designcenter/nx-cad-software/new-user/ | Risorsa didattica ufficiale | 5 | 2026-05-20 | Documenti e video per nuovi utenti NX; include playlist YouTube ufficiale NX tips and tricks |

---

## Airspeeder / Alauda — Fonti Primarie e Tecniche

| # | Titolo | URL | Tipo | Reliability | Data | Note |
|---|---|---|---|---|---|---|
| S11 | Airspeeder Official | https://airspeeder.com | Sito ufficiale | 5 | 2026-05-13 | News, serie racing, comunicati |
| S12 | Mk3 Ready to Race | https://airspeeder.com/news/mk3-worlds-first-electric-flying-racing-car-ready-to-race | Comunicato stampa | 4 | 2026-05-13 | Dati tecnici Mk3 dove disponibili |
| S13 | 2023 EXA Championship | https://www.urbanairmobilitynews.com/air-taxis/motorsport-history-as-2023-exa-series-championship-completed/ | Articolo | 3 | 2026-05-13 | Top speed 100 km/h, wingspan riportata |
| S14 | Mk4 Reveal (dati Mk3) | https://newatlas.com/aircraft/airspeeder-mk4-racing-h2-evtol/ | Articolo tecnico | 3 | 2026-05-13 | 350+ test flights Mk3 |
| S15 | eVTOL Insights Mk3 | https://evtolinsights.com/airspeeders-mk3-evtol-flying-vehicle-has-been-revealed-and-is-now-ready-to-race/ | Articolo | 3 | 2026-05-13 | Costruzione in fibra di carbonio |
| S35 | Alauda Aeronautics Official | https://www.alauda.aero/ | Sito ufficiale | 5 | 2026-05-14 | Mk3: all-electric racing powertrain, carbon-fibre chassis, high-speed manoeuvrability |
| S36 | Airspeeder Talent Announcement | https://airspeeder.com/news/airspeeder-attracts-leading-motorsport-and-aerospace-talent | News ufficiale | 4 | 2026-05-14 | Team con competenze Boeing, Renault F1, McLaren, Williams, Vertical Airspace |

---

## Paper Accademici

| # | Titolo | URL | Journal/Conf | Reliability | Anno | Note |
|---|---|---|---|---|---|
| S16 | SU2 for Rotorcraft Flows (Polimi) | https://arxiv.org/pdf/2107.13895 | arXiv / accademico | 5 | 2021 | SU2 per analisi rotori; molto rilevante per eVTOL |
| S17 | OpenVSP + ESP (AIAA 2024) | https://acdl.mit.edu/ESP/Publications/AIAApaper2024-4304.pdf | AIAA Aviation Forum 2024 | 5 | 2024 | Workflow OpenVSP -> CFD per analisi |
| S18 | SU2 + OpenFOAM Validation HLPW5 | https://www.researchgate.net/publication/398218662 | ResearchGate 2025 | 4 | 2025 | Confronto SU2 vs OpenFOAM su casi industriali |

---

## Tutorial e Risorse Pratiche

| # | Titolo | URL | Tipo | Reliability | Anno | Note |
|---|---|---|---|---|---|
| S19 | SU2 Tutorials Official | https://su2code.github.io/tutorials/ | Tutorial ufficiali | 5 | 2024 | Casi NACA 0012, RAE 2822, ecc. |
| S20 | GMSH Tutorials | https://gmsh.info/doc/texinfo/gmsh.html | Documentazione | 5 | 2024 | Reference completo |
| S21 | OpenFOAM User Guide | https://doc.cfd.direct/openfoam/user-guide-v11/ | Documentazione | 5 | 2023 | Guida ufficiale v11 |
| S22 | CFD Online Forum | https://www.cfd-online.com/Forums/ | Forum community | 3 | ongoing | Utile per troubleshooting specifico |
| S23 | Open Source vs Proprietary CFD | https://gaugehow.com/simulation/best-cfd-software-2026-commercial-vs-open-source | Articolo tecnico | 3 | 2026 | Confronto aggiornato 2026 |
| S24 | MetaOpenFOAM 2.0 (LLM+CFD) | https://arxiv.org/pdf/2502.00498 | arXiv 2025 | 4 | 2025 | Automazione CFD con LLM |

---

## Workflow Industriali — Aggiornamento Priorità Altissima

| # | Nome | URL | Tipo | Reliability | Data accesso | Note |
|---|---|---|---|---|---|---|
| S25 | Oracle Red Bull Racing + Ansys | https://www.ansys.com/en-gb/resource-center/case-study/red-bull-racing | Case study ufficiale Ansys | 5 | 2026-05-14 | Fluent Meshing + Fluent CFD come virtual wind tunnel; cooling e materiali nello stesso ecosistema |
| S26 | Martin UAV V-BAT + Siemens | https://resources.sw.siemens.com/en-US/case-study-martin-uav/ | Case study ufficiale Siemens | 5 | 2026-05-14 | STAR-CCM+ + HEEDS; ducted-fan VTOL; BEM/RBM; centinaia di design |
| S27 | TLG Aerospace + Siemens | https://resources.sw.siemens.com/en-US/case-study-tlg-aerospace/ | Case study ufficiale Siemens | 5 | 2026-05-14 | STAR-CCM+ + MSC Nastran per certification by analysis e database aerodinamiche |
| S28 | AOTECH / Spark Racing Technology + Siemens | https://resources.sw.siemens.com/en-US/case-study-aotech/ | Case study ufficiale Siemens | 5 | 2026-05-14 | Formula E front wing; STAR-CCM+; workflow CAD/surface cleaning/meshing/simulation |
| S29 | Cadence Fidelity CFD Platform | https://www.cadence.com/en_US/home/tools/system-analysis/computational-fluid-dynamics/fidelity.html | Sito prodotto ufficiale | 5 | 2026-05-14 | Workflow CFD end-to-end; citazioni Honda/Toyota/Kawasaki; preprocessing e solver integrati |
| S30 | Honda eVTOL + Cadence CFD | https://www.cadence.com/content/cadence-www/global/en_US/home/multimedia.html/content/dam/cadence-www/global/en_US/videos/solutions/honda-cfd-designed-with-cadence.mp4/ | Pagina/video ufficiale Cadence | 4 | 2026-05-14 | Honda usa Cadence CFD per ottimizzare design EV/eVTOL; last modified 2026-02-17 |
| S31 | Dassault SIMULIA PowerFLOW | https://www.3ds.com/products/simulia/powerflow | Sito prodotto ufficiale | 5 | 2026-05-14 | Lattice Boltzmann transient CFD; aero, aeroacoustics, thermal; moving geometry/LRF |
| S32 | NASA CAPE | https://www.nas.nasa.gov/pubs/ams/2023/03-09-23.html | Seminario/software NASA | 5 | 2026-05-14 | Run matrix executive per Cart3D/FUN3D/OVERFLOW; usato su matrici da 1000+ casi |
| S33 | NASA Cart3D | https://www.nas.nasa.gov/publications/software/docs/cart3d/pages/ | Documentazione NASA | 5 | 2026-05-14 | Automated CFD analysis su geometrie complesse; mesh adaptation; MPI/OpenMP |
| S34 | NASA FUN3D | https://fun3d.larc.nasa.gov/ | Documentazione NASA | 5 | 2026-05-14 | CFD suite NASA per analisi/design; release 14.2 aggiornata a maggio 2026 |

---

## Dati tecnici Airspeeder Mk3

Dalle fonti S11-S15, S35-S36:

- **Dimensioni:** circa 4.1 m di lunghezza riportata da fonti secondarie; verificare prima di usarla per CAD definitivo.
- **Costruzione:** chassis in fibra di carbonio confermato da Alauda.
- **Propulsione:** racing powertrain all-electric.
- **Top speed pubblica:** 100 km/h riportata per EXA/Mk3 da fonti secondarie; non usare come unico dato di progetto senza cross-check.
- **Operazione:** Mk3 remotamente pilotato nelle fonti di gara/test.
- **Test:** 350+ voli di test riportati da fonte tecnica secondaria per il programma Mk3/Mk4.
- **Team:** competenze dichiarate in aerospace, motorsport, aerodinamica, strutture, flight controls, telemetry e compositi.

---

## Note sulla attendibilità delle fonti

| Score | Interpretazione |
|---|---|
| 5 | Certa e aggiornata; usare direttamente |
| 4 | Affidabile ma da cross-checkare se serve un dato numerico preciso |
| 3 | Usare con cautela; utile per triangolare, non come fonte unica |
| 2 | Solo indicazione o troubleshooting |
| 1 | Non citare come supporto tecnico |

### Nota specifica sui case study commerciali

I case study dei vendor (Ansys, Siemens, Cadence, Dassault) sono fonti primarie per sapere **quale stack viene dichiarato**, ma sono anche materiale commerciale. Sono quindi affidabili per mappare workflow industriali e strumenti usati; sono meno neutri per confronti di performance tra vendor.

---

## Impatto dell'aggiornamento Iterazione 02

- La ricerca industriale ora copre più stack proprietari: Fluent, STAR-CCM+, HEEDS, Cadence Fidelity CFD, PowerFLOW.
- Il bias open source è stato ridotto solo per questa valutazione, come richiesto in `improvements/iteration_01_improvements.md`.
- La conclusione aggiornata è che OpenVSP + SU2 resta la baseline replicabile, ma un benchmark commerciale futuro è tecnicamente giustificato.

---

## Impatto dell'aggiornamento Iterazione 03

- Tutti i software dei due nuovi casi studio sono ora presenti come fonti primarie: SOLIDWORKS, NX, Simcenter STAR-CCM+ e Simcenter HEEDS.
- La differenza tra SOLIDWORKS e NX non viene trattata come una preferenza generica: NX ha fonti aerospace/UAV e integrazione nativa nel portfolio Siemens; SOLIDWORKS resta forte come CAD meccanico accessibile e rapido.
- STAR-CCM+ viene documentato non solo come solver CFD, ma come ambiente CAD handling, geometry cleanup, automated meshing, solver, post-processing e design exploration.
- HEEDS viene documentato come orchestratore di workflow e ottimizzatore industriale: modifica parametri, lancia tool esterni, valuta risposte, gestisce HPC/cloud e ricerca famiglie di design tramite SHERPA.

---

## Script di verifica link

```python
# verify_links.py — verifica che i link principali siano raggiungibili
import requests

LINKS = [
    "https://openvsp.org",
    "https://su2code.github.io",
    "https://openfoam.org",
    "https://gmsh.info",
    "https://www.paraview.org",
    "https://optuna.org",
    "https://airspeeder.com",
    "https://www.alauda.aero/",
    "https://www.ansys.com/en-gb/resource-center/case-study/red-bull-racing",
    "https://resources.sw.siemens.com/en-US/case-study-martin-uav/",
    "https://resources.sw.siemens.com/en-US/case-study-tlg-aerospace/",
    "https://resources.sw.siemens.com/en-US/case-study-aotech/",
    "https://www.cadence.com/en_US/home/tools/system-analysis/computational-fluid-dynamics/fidelity.html",
    "https://www.3ds.com/products/simulia/powerflow",
    "https://www.nas.nasa.gov/pubs/ams/2023/03-09-23.html",
    "https://www.nas.nasa.gov/publications/software/docs/cart3d/pages/",
    "https://fun3d.larc.nasa.gov/",
    "https://www.solidworks.com/product/solidworks-design",
    "https://help.solidworks.com/",
    "https://www.siemens.com/en-us/products/designcenter/nx-cad-software/",
    "https://www.siemens.com/en-us/products/designcenter/nx-cad-software/workflows/aerospace-aircraft-design/",
    "https://www.siemens.com/en-gb/products/simcenter/fluids-thermal-simulation/star-ccm/",
    "https://www.siemens.com/en-us/products/simcenter/integration-solutions/heeds/",
    "https://www.siemens.com/en-us/products/simcenter/simulation-test/design-space-exploration-optimization/",
]

for url in LINKS:
    try:
        response = requests.head(url, timeout=10, allow_redirects=True)
        status = "OK" if response.status_code < 400 else "FAIL"
        print(f"{status} {response.status_code} — {url}")
    except Exception as exc:
        print(f"ERROR — {url}: {exc}")
```
