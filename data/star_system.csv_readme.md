# Solar System & Kepler-90 System CSV Files

This repository contains two CSV files in a **uniform format**, providing basic data about:

1. Our **Solar System** (`solar_system.csv`)
2. The **Kepler-90** exoplanetary system (`kepler_90_system.csv`)

Each file follows the **same column structure** described below.

---

## CSV Format

| Column               | Description                                                                                               
|----------------------|-----------------------------------------------------------------------------------------------------------
| **Name**             | Name of the celestial object (star, planet, dwarf planet, etc.).                                          
| **Type**             | Classification (e.g., “Star”, “Planet”, “Dwarf Planet”).                                                  
| **Mass_kg**          | Approximate mass in kilograms.                                                                            
| **Radius_m**         | Approximate mean radius in meters.                                                                        
| **SemiMajorAxis_m**  | Semi-major axis (orbital distance) in meters, relative to the star (0 for the star itself).               
| **OrbitalPeriod_days** | Orbital period in days (0 for the star).                                                                
| **OrbitalPeriod_s**  | Orbital period in seconds (0 for the star).                                                               
| **Star**             | The name of the star this object orbits. Use “N/A” for the star itself.                                   
| **DiscoveryYear**    | Year of discovery (if known). For anciently known objects or the star, “N/A” or the best approximate date.

---

## Notes

Data are provided “as is” for educational/demo purposes.
Values are derived from public sources (NASA fact sheets, exoplanet archives, etc.) and may be approximate or simplified.

---

## Usage

```
import pandas as pd

solar_df = pd.read_csv("solar_system.csv")
kepler90_df = pd.read_csv("kepler_90_system.csv")

display(solar_df.head())
display(kepler90_df.head())