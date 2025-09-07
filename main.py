import requests
import pandas as pd
import plotly.express as px
import json

# URL del feed de terremotos recientes (magnitud > 2.5)
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
response = requests.get(url)
data = response.json()["features"]

# Guardar el JSON original completo
with open("data/earthquakes_raw.json", "w", encoding="utf-8") as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)

# Extraer datos relevantes para el DataFrame
quakes = [{
    "Place": q["properties"]["place"],
    "Mag": q["properties"]["mag"],
    "Time": pd.to_datetime(q["properties"]["time"], unit="ms"),
    "Lat": q["geometry"]["coordinates"][1],
    "Lon": q["geometry"]["coordinates"][0]
} for q in data]

# Crear DataFrame
df = pd.DataFrame(quakes)

# Guardar CSV para Plotly Studio
df.to_csv("earthquakes.csv", index=False, encoding="utf-8")

print("✅ Datos guardados correctamente.")
print(f"🔹 Total de registros: {len(df)}")

# Crear heatmap usando la nueva API de Plotly (MapLibre)
fig = px.density_map(
    df,
    lat="Lat",
    lon="Lon",
    z="Mag",
    radius=20,
    center={"lat": 0, "lon": 0},
    zoom=1,
    color_continuous_scale="plasma",
    title="🌎 Heatmap de Terremotos Recientes (M>2.5)",
    map_style="open-street-map"  # No necesita token
)

fig.show()

