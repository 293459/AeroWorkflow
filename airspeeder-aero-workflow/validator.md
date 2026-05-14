---
title: "Validator — Procedure di Verifica"
phase: "Infrastructure"
status: "ready"
last_updated: "2026-05-13"
depends_on: ["execution_pipeline.md"]
---

# Validator

> Per ogni fase dell'execution pipeline, questo file definisce i criteri di validazione quantitativi, come verificarli e cosa fare in caso di fallimento. È collegato all'execution pipeline — ogni step ha il suo check corrispondente.

---

## Fase 0 — Setup & Struttura Repo

### V0.1 — Struttura directory completa
```bash
# Check automatico
REQUIRED_DIRS=(metrics configs/config_1_openvsp_su2 configs/config_2_openvsp_openfoam 
               configs/config_3_xflr5_preliminary prompts sources examples 
               improvements execution_logs report)
for dir in "${REQUIRED_DIRS[@]}"; do
  [ -d "$dir" ] && echo "✅ $dir" || echo "❌ MISSING: $dir"
done
```
**Criterio pass:** Tutte le directory esistono  
**Se fallisce:** Creare le directory mancanti prima di procedere

### V0.2 — File fondamentali presenti
```bash
REQUIRED_FILES=(README.md brainstorming.md execution_pipeline.md tools.md 
                validator.md cross_references.md assembly_guide.md 
                token_saving_techniques.md metrics/evaluation_metrics.md)
for f in "${REQUIRED_FILES[@]}"; do
  [ -f "$f" ] && echo "✅ $f" || echo "❌ MISSING: $f"
done
```

---

## Fase 1 — CAD Parametrico (OpenVSP)

### V1.1 — Geometria chiusa (watertight)
```python
# check_geometry.py
import trimesh

mesh = trimesh.load("configs/baseline.stl")
print(f"Watertight: {mesh.is_watertight}")
print(f"Volume: {mesh.volume:.4f} m³")
print(f"N facce: {len(mesh.faces)}")

assert mesh.is_watertight, "❌ FAIL: Geometria non chiusa — impossibile procedere con meshing"
assert mesh.volume > 0, "❌ FAIL: Volume negativo — normali invertite"
print("✅ Geometria valida")
```
**Criterio pass:** `is_watertight == True`, `volume > 0`  
**Se fallisce:** In OpenVSP: Tools → Check Geometry. Correggere i gaps prima dell'export.

### V1.2 — Dimensioni geometria plausibili
**Criterio pass:** Bounding box nell'ordine di grandezza corretto per Airspeeder Mk3 (~4.1 m lunghezza)  
**Check:** `mesh.bounding_box.extents` — il valore più grande deve essere ~4.1 m  
**Se fallisce:** Verificare le unità in OpenVSP (mm vs m)

---

## Fase 2 — Meshing (GMSH)

### V2.1 — Qualità mesh (GMSH built-in)
```python
# check_mesh_quality.py
import gmsh
gmsh.initialize()
gmsh.open("mesh/baseline_medium.msh")

# Verifica qualità elementi
gmsh.plugin.setNumber("AnalyseMeshQuality", "JacobianDeterminant", 1)
gmsh.plugin.run("AnalyseMeshQuality")

# Minimo Jacobiano positivo = mesh valida
print("✅ Mesh quality check completato")
gmsh.finalize()
```

### V2.2 — Check con SU2 (se mesh in formato .su2)
```bash
SU2_DEF mesh_deformation.cfg   # verifica lettura mesh
# Oppure:
python -c "
import subprocess
result = subprocess.run(['SU2_CFD', '--dry-run', 'config.cfg'], capture_output=True)
print('✅ Mesh OK' if result.returncode == 0 else '❌ Mesh non valida')
"
```

### V2.3 — Mesh sensitivity study
**Criterio pass:** Variazione Cd < 2% tra mesh medium e fine  
**Procedura:**
1. Run SU2 su mesh coarse → registra `Cd_coarse`
2. Run SU2 su mesh medium → registra `Cd_medium`
3. Run SU2 su mesh fine → registra `Cd_fine`
4. Calcola `|Cd_fine - Cd_medium| / Cd_fine < 0.02`  
**Se fallisce:** Raffinare ulteriormente la mesh fine o verificare i boundary layer

---

## Fase 3 — CFD Simulation (SU2)

### V3.1 — Convergenza residui
```python
# check_convergence.py
import pandas as pd
import numpy as np

hist = pd.read_csv("results/run_001/history.dat", comment="#")
# SU2 history ha colonne: Iter, Res_Flow[0], ..., CL, CD, ...

final_residual = hist["Res_Flow[0]"].iloc[-1]
assert final_residual < 1e-6, f"❌ Residui non convergenti: {final_residual:.2e}"
print(f"✅ Residui finali: {final_residual:.2e} (< 1e-6)")
```

### V3.2 — Convergenza forze (Cd)
```python
# check_force_convergence.py
hist = pd.read_csv("results/run_001/history.dat", comment="#")
cd_last_100 = hist["CD"].iloc[-100:]
cd_variation = (cd_last_100.max() - cd_last_100.min()) / cd_last_100.mean()

assert cd_variation < 0.01, f"❌ Cd non convergente: variazione {cd_variation*100:.1f}%"
print(f"✅ Cd convergente: variazione {cd_variation*100:.2f}%")
```

### V3.3 — Valori fisicamente plausibili
```python
# Airspeeder Mk3: quadricottero a ~100 km/h, Cd atteso in range [0.3, 1.5]
cd = float(...)  # valore finale da history.dat
cl = float(...)

assert 0.1 < cd < 3.0, f"❌ Cd fuori range fisico: {cd}"
print(f"✅ Cd = {cd:.4f} (range atteso 0.3–1.5)")
```

### V3.4 — No NaN nei risultati
```bash
grep -i "nan\|inf" results/run_001/history.dat && echo "❌ NaN/Inf trovati" || echo "✅ No NaN"
```

---

## Fase 4 — Post-Processing

### V4.1 — File output presenti
```python
import os
EXPECTED = ["results/run_001/metrics.csv", 
            "results/run_001/plots/pressure_surface.png",
            "results/run_001/plots/cd_history.png"]
for f in EXPECTED:
    status = "✅" if os.path.exists(f) else "❌"
    print(f"{status} {f}")
```

### V4.2 — Metriche aggregate correttamente
```python
df = pd.read_csv("results/run_001/metrics.csv")
required_cols = ["run_id", "Cd", "Cl", "mesh_level", "timestamp"]
for col in required_cols:
    assert col in df.columns, f"❌ Colonna mancante: {col}"
print("✅ Struttura metrics.csv corretta")
```

---

## Fase 5 — Ottimizzazione

### V5.1 — Funzione obiettivo decresce
```python
opt_history = pd.read_csv("optimization/history.csv")
initial_cd = opt_history["Cd"].iloc[0]
best_cd = opt_history["Cd"].min()
improvement = (initial_cd - best_cd) / initial_cd * 100
print(f"✅ Miglioramento Cd: {improvement:.1f}%")
assert improvement > 0, "❌ Ottimizzazione non migliorata rispetto al baseline"
```

### V5.2 — Parametri nei bounds
```python
# Verificare che i parametri geometrici restino fisicamente sensati
params = opt_history[["chord", "sweep", "radius"]].iloc[-1]
assert 0.1 < params["chord"] < 2.0, "❌ Chord fuori bounds"
```

---

## Fase 6 — Report LaTeX

### V6.1 — Compilazione senza errori
```bash
cd report/
pdflatex -interaction=nonstopmode report.tex
# Check
[ $? -eq 0 ] && echo "✅ LaTeX compilato OK" || echo "❌ Errori di compilazione"
```

### V6.2 — Tutte le figure presenti
```bash
# Verifica che le figure referenziate in LaTeX esistano
grep -o "includegraphics{[^}]*}" report/report.tex | while read fig; do
    fname=$(echo $fig | sed 's/includegraphics{//;s/}//')
    [ -f "report/figures/$fname" ] && echo "✅ $fname" || echo "❌ MISSING: $fname"
done
```

---

## Fase 7 — Improvements & Log

### V7.1 — Log di esecuzione compilato
```python
import os
from datetime import datetime

log_dir = "execution_logs/"
logs = sorted(os.listdir(log_dir))
assert len(logs) > 0, "❌ Nessun log trovato"
latest = logs[-1]
print(f"✅ Ultimo log: {latest}")

# Verifica che il log contenga le sezioni richieste
with open(os.path.join(log_dir, latest)) as f:
    content = f.read()
required_sections = ["## Cosa ho fatto", "## Risultati", "## Problemi"]
for s in required_sections:
    assert s in content, f"❌ Sezione mancante nel log: {s}"
```

---

## Validator — Fonti esterne (sources.md)

### V_SRC.1 — Link raggiungibili
```python
# Vedi sources/sources.md per lo script verify_links.py
```

### V_SRC.2 — Reliability score assegnato
**Check manuale:** Ogni fonte in `sources/sources.md` ha un reliability score nella colonna dedicata.

---

## Riepilogo checks per fase

| Fase | Check | Automatizzabile? | Critico? |
|---|---|---|---|
| 0 — Setup | Struttura repo completa | ✅ Sì (bash) | ✅ Sì |
| 1 — CAD | Watertight + dimensioni | ✅ Sì (trimesh) | ✅ Sì |
| 2 — Mesh | Qualità + sensitivity | ✅ Parzialmente | ✅ Sì |
| 3 — CFD | Convergenza + plausibilità | ✅ Sì (Python) | ✅ Sì |
| 4 — Post | File presenti + struttura | ✅ Sì | ⚠️ Medio |
| 5 — Opt | Cd decresce + bounds | ✅ Sì | ✅ Sì |
| 6 — Report | LaTeX compila + figure | ✅ Sì (bash) | ⚠️ Medio |
| 7 — Log | Log compilato + sezioni | ✅ Sì | ⚠️ Medio |
