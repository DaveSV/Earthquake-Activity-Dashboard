import pandas as pd
import json
import openai
import markdown

# Configura tu API Key de OpenAI (usa variables de entorno para producción)
openai.api_key = "api_key"
openai.api_base='http://localhost:11434/v1'

def load_earthquake_data(json_path: str):
    """Carga el JSON de USGS y devuelve un DataFrame limpio con coordenadas."""
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    features = data["features"]

    df = pd.DataFrame([{
        "Lugar": f["properties"]["place"],
        "Magnitud": f["properties"]["mag"],
        "Fecha": pd.to_datetime(f["properties"]["time"], unit="ms"),
        "Profundidad_km": f["geometry"]["coordinates"][2],
        "Lat": f["geometry"]["coordinates"][1],
        "Lon": f["geometry"]["coordinates"][0],
        "Tsunami": f["properties"]["tsunami"],
        "URL": f["properties"]["url"]
    } for f in features])

    return df

def generate_ai_report(df: pd.DataFrame):
    """Genera un informe analítico usando OpenAI."""
    significant = df[df["Magnitud"] >= 4.5].sort_values(by="Magnitud", ascending=False)
    summary = significant.head(10).to_dict(orient="records")

    prompt = f"""
Genera un informe técnico de actividad sísmica basado en los datos del USGS.
Analiza magnitud, ubicación y riesgo potencial.

Datos clave:
{summary}

Debes incluir:
- Resumen global de actividad sísmica.
- Zonas más activas y con mayor riesgo.
- Si existe riesgo potencial de tsunami.
- Una conclusión general sobre la estabilidad sísmica global.
    """


    response = openai.ChatCompletion.create(
        model="llama3.2:1b",  # Si tienes GPT-4.1, mejor aún
        messages=[
            {"role": "system", "content": "Eres un experto en geofísica y análisis de datos sísmicos."},
            {"role": "user", "content": prompt}
        ]
    )

    # Obtenemos texto plano desde Ollama
    raw_text = response.choices[0].message["content"]

    # Convertimos Markdown a HTML
    html_report = markdown.markdown(
        raw_text,
        extensions=["fenced_code", "tables", "toc", "sane_lists"]
    )

    return html_report
