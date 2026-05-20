---
title: "Tools — Airspeeder Mk3 Aero Workflow"
phase: "Setup"
status: "updated"
last_updated: "2026-05-20"
iteration: 3
---

# Tools

> Tutti gli strumenti usati nel progetto, con versione consigliata, ruolo, link ufficiale e note di installazione.

---

## CAD Parametrico

### OpenVSP
| Campo | Valore |
|---|---|
| **Ruolo** | Modellazione CAD parametrica aeronautica |
| **Versione consigliata** | ≥ 3.40 |
| **Licenza** | Open source (NASA) |
| **OS** | Windows, Linux, macOS |
| **Sito** | https://openvsp.org |
| **Formati input** | `.vsp3` (nativo) |
| **Formati output** | `.stl`, `.stp`, `.obj`, `.degen`, `.vsp3` |
| **Python API** | Sì — `openvsp` package |
| **Note** | Progettato per geometrie aeronautiche; ottimo per parametrizzazione rapida di fusoliere, ali, gondole |

---

### SOLIDWORKS
| Campo | Valore |
|---|---|
| **Ruolo** | CAD parametrico meccanico per parti, assiemi, dettagli produttivi e prototipazione |
| **Versione consigliata** | 2025/2026 o versione allineata alla licenza team |
| **Licenza** | Commerciale; opzioni education/startup/makers |
| **OS** | Windows nativo |
| **Sito** | https://www.solidworks.com/product/solidworks-design |
| **Formati input** | `.sldprt`, `.sldasm`, `.step`, `.iges`, `.x_t`, `.stl` |
| **Formati output** | `.sldprt`, `.sldasm`, `.step`, `.iges`, `.x_t`, `.stl`, `.3mf` |
| **API/Automazione** | Si - API COM/VBA/.NET; design tables, equations, configurations |
| **Note** | Molto rapido per meccanica e assiemi; per CFD esterna serve disciplina su defeaturing, naming superfici ed export Parasolid/STEP |

### Siemens NX
| Campo | Valore |
|---|---|
| **Ruolo** | CAD/CAM/CAE industriale per geometrie complesse, aerospace, superfici, compositi, PLM e digital twin |
| **Versione consigliata** | NX attuale supportato dal pacchetto Siemens Xcelerator del team |
| **Licenza** | Commerciale; licensing modulare/token |
| **OS** | Windows e Linux secondo release/licenza |
| **Sito** | https://www.siemens.com/en-us/products/designcenter/nx-cad-software/ |
| **Formati input** | `.prt`, `.step`, `.iges`, `.jt`, `.x_t`, `.stl`, formati CAD tramite translator |
| **Formati output** | `.prt`, `.step`, `.iges`, `.jt`, `.x_t`, `.stl`, `.obj` |
| **API/Automazione** | Si - NX Open, expressions, journals, Teamcenter integration |
| **Note** | Piu' adatto di SOLIDWORKS se il target e' un workflow drone/eVTOL industriale con STAR-CCM+ e HEEDS |

---

## Meshing

### GMSH
| Campo | Valore |
|---|---|
| **Ruolo** | Generazione mesh non strutturata 2D/3D |
| **Versione consigliata** | ≥ 4.11 |
| **Licenza** | Open source (GPL) |
| **OS** | Windows, Linux, macOS |
| **Sito** | https://gmsh.info |
| **Formati input** | `.stl`, `.stp`, `.iges`, `.brep`, `.geo` |
| **Formati output** | `.msh`, `.su2`, `.vtk`, `.cgns`, `.med` |
| **Python API** | Sì — `gmsh` package |
| **Note** | Altamente configurabile via file `.geo`; supporta raffinamento locale, boundary layers, mesh adattiva |

### STAR-CCM+ Automated Meshing
| Campo | Valore |
|---|---|
| **Ruolo** | Meshing industriale integrato per STAR-CCM+: surface repair/wrapper, trimmer, polyhedral, prism layer, advancing layer, AMR |
| **Licenza** | Commerciale, inclusa nell'ambiente Simcenter STAR-CCM+ secondo bundle/licenza |
| **OS** | Windows/Linux secondo release |
| **Sito** | https://www.siemens.com/en-gb/products/simcenter/fluids-thermal-simulation/star-ccm/ |
| **Formati input** | CAD nativo/importato, STEP/IGES/Parasolid/JT/STL secondo moduli di import |
| **Formati output** | Mesh nativa STAR-CCM+, export verso formati supportati dal tool |
| **Automazione** | Operations pipeline, Design Manager, Java macros, HEEDS orchestration |
| **Note** | Se il solver e' STAR-CCM+, conviene quasi sempre usare questo mesher invece di GMSH per preservare regioni, patch, prism layers e workflow replayable |

---

## Solver CFD

### Simcenter STAR-CCM+
| Campo | Valore |
|---|---|
| **Ruolo** | Solver CFD/multiphysics industriale con CAD handling, meshing, solving, post-processing e design exploration integrati |
| **Versione consigliata** | Release supportata dalla licenza team; mantenere allineamento con NX/HEEDS |
| **Licenza** | Commerciale Siemens |
| **OS** | Windows e Linux; HPC/cluster secondo licenza |
| **Sito** | https://www.siemens.com/en-gb/products/simcenter/fluids-thermal-simulation/star-ccm/ |
| **Formati input** | CAD diretto/importato, mesh/parti, parametri, Java macro |
| **Formati output** | Scene/plots/reports, solution fields, CSV, immagini, dati per HEEDS |
| **API/Automazione** | Java macros, simulation operations, Design Manager, HEEDS integration |
| **Note** | Forte per geometrie complesse, workflow ripetibili, moving mesh/overset e studi parametrici; costo/licenza sono il principale limite |

### SU2
| Campo | Valore |
|---|---|
| **Ruolo** | Solver CFD RANS per analisi aerodinamica |
| **Versione consigliata** | ≥ 7.5 |
| **Licenza** | Open source (LGPL) |
| **OS** | Windows, Linux, macOS |
| **Sito** | https://su2code.github.io |
| **Formati input** | `.su2` (mesh), `.cfg` (configurazione) |
| **Formati output** | `.vtu`, `.vtk`, `.csv` (forze), `history.dat` |
| **Python API** | Parziale — principalmente via config files + subprocess |
| **Note** | Sviluppato da Stanford; ottimo per ottimizzazione aerodinamica; supporto adjoint method per gradient-based optimization |

### OpenFOAM
| Campo | Valore |
|---|---|
| **Ruolo** | Solver CFD RANS/LES per analisi ad alta fedeltà |
| **Versione consigliata** | ≥ 10 (OpenFOAM.org) o ≥ v2306 (ESI) |
| **Licenza** | Open source (GPL) |
| **OS** | Linux nativo; Windows via WSL2 |
| **Sito** | https://openfoam.org |
| **Formati input** | `polyMesh/` (nativo), `.stl` (per snappyHexMesh) |
| **Formati output** | Formato OpenFOAM nativo, `.vtk`, `.foam` (ParaView) |
| **Python API** | Tramite `PyFOAM` o `fluidfoam` |
| **Note** | Altissima flessibilità; curva di apprendimento elevata; mesh con snappyHexMesh richiede pratica |

### XFLR5
| Campo | Valore |
|---|---|
| **Ruolo** | Analisi a bassa fedeltà (panel method + lifting line) |
| **Versione consigliata** | ≥ 6.60 |
| **Licenza** | Open source (GPL) |
| **OS** | Windows, Linux, macOS |
| **Sito** | http://www.xflr5.tech |
| **Formati input** | `.dat` (profili), coordinate geometria |
| **Formati output** | `.xml`, tabelle polari |
| **Python API** | No — interfaccia GUI |
| **Note** | Ottimo per screening preliminare; non adatto per geometrie 3D complesse come telaio Airspeeder |

---

## Post-Processing

### ParaView
| Campo | Valore |
|---|---|
| **Ruolo** | Visualizzazione e analisi risultati CFD |
| **Versione consigliata** | ≥ 5.11 |
| **Licenza** | Open source (BSD) |
| **OS** | Windows, Linux, macOS |
| **Sito** | https://www.paraview.org |
| **Formati input** | `.vtk`, `.vtu`, `.foam`, `.cgns`, `.ensight` |
| **Formati output** | Immagini, animazioni, CSV dati estratti |
| **Python API** | Sì — `pvpython` / `paraview.simple` |
| **Note** | Standard de facto per visualizzazione CFD open source |

### Python (scipy + matplotlib + pandas)
| Campo | Valore |
|---|---|
| **Ruolo** | Post-processing numerico, plotting, ottimizzazione |
| **Versione consigliata** | Python ≥ 3.9 |
| **Pacchetti chiave** | `numpy`, `scipy`, `matplotlib`, `pandas`, `optuna`, `openvsp` |
| **Note** | Collante tra tutti gli strumenti; automazione workflow, aggregazione risultati |

---

## Ottimizzazione

### Optuna
| Campo | Valore |
|---|---|
| **Ruolo** | Bayesian optimization per esplorazione spazio parametrico |
| **Licenza** | Open source (MIT) |
| **Sito** | https://optuna.org |
| **Note** | TPE (Tree-structured Parzen Estimator); ideale per ottimizzazione black-box dove ogni valutazione è costosa |

### Simcenter HEEDS
| Campo | Valore |
|---|---|
| **Ruolo** | Design space exploration, MDAO e orchestrazione workflow CAD/CAE |
| **Licenza** | Commerciale Siemens |
| **Sito** | https://www.siemens.com/en-us/products/simcenter/integration-solutions/heeds/ |
| **Input** | Variabili continue/discrete, bounds, constraints, workflow software, template file, response extractors |
| **Output** | Design table, Pareto front, sensitivity, trade-off plots, best design families |
| **Algoritmi** | SHERPA hybrid adaptive search, DOE, multi-objective exploration, AI Simulation Predictor |
| **Note** | Adatto quando ogni run CFD costa minuti/ore e serve esplorare centinaia di varianti senza intervento manuale |

### SciPy SLSQP
| Campo | Valore |
|---|---|
| **Ruolo** | Ottimizzazione gradient-based locale |
| **Note** | Da usare dopo Optuna per raffinamento locale; richiede che la funzione obiettivo sia liscia |

---

## Versionamento & Collaborazione

### Git / GitHub
| Campo | Valore |
|---|---|
| **Ruolo** | Versionamento codice e file progetto |
| **Note** | Tutta la repo è versionata; usare branch per iterazioni di ottimizzazione; `.gitignore` per file mesh grandi |

### Git LFS
| Campo | Valore |
|---|---|
| **Ruolo** | Storage file grandi (mesh, risultati CFD) |
| **Note** | Necessario per file `.su2`, `.stl`, `.vtu` di grandi dimensioni |

---

## Documentazione

### LaTeX
| Campo | Valore |
|---|---|
| **Ruolo** | Report tecnico finale |
| **Distribuzione consigliata** | TeX Live (Linux) / MiKTeX (Windows) |
| **Note** | Compilare con `pdflatex` o `lualatex` |

### Mermaid
| Campo | Valore |
|---|---|
| **Ruolo** | Diagrammi workflow nei file markdown |
| **Note** | Renderizzato automaticamente su GitHub; usare nei file `.md` con blocchi ` ```mermaid ` |

---

## Stack consigliato per questo progetto

```mermaid
graph LR
    A[OpenVSP\nCAD Parametrico] -->|.stl export| B[GMSH\nMeshing]
    B -->|.su2 mesh| C[SU2\nCFD Solver]
    C -->|.vtu results| D[ParaView\nVisualizzazione]
    C -->|forces.csv| E[Python\nPost-processing]
    E -->|metriche Cd/Cl| F[Optuna\nOttimizzazione]
    F -->|nuovi parametri| A
    
    style A fill:#4a90d9,color:#fff
    style B fill:#20b2aa,color:#fff
    style C fill:#ff6b6b,color:#fff
    style D fill:#ffa500,color:#fff
    style E fill:#7b68ee,color:#fff
    style F fill:#2e8b57,color:#fff
```

## Stack proprietario consigliato come benchmark

```mermaid
graph LR
    A[NX\nCAD parametrico + superfici] -->|NX/Parasolid/STEP| B[STAR-CCM+\nCAD prep + mesh]
    B -->|mesh nativa| C[STAR-CCM+\nCFD + reports]
    C -->|Cd/Cl/Cm + constraints| D[HEEDS\nSHERPA optimization]
    D -->|nuove expressions/parametri| A
```

SOLIDWORKS puo' sostituire NX se il team e' gia' SOLIDWORKS-first, ma per droni/eVTOL complessi il benchmark proprietario raccomandato resta NX + STAR-CCM+ + HEEDS.
