import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from analyzer import load_earthquake_data, generate_ai_report

# Cargar datos desde el JSON
json_path = "data/earthquakes_raw.json"
df = load_earthquake_data(json_path)

# Crear mapa interactivo
fig = px.density_map(
    df,
    lat="Lat",
    lon="Lon",
    z="Magnitud",
    radius=20,
    center={"lat": 0, "lon": 0},
    zoom=1,
    color_continuous_scale="plasma",
    title="🌎 Mapa de Actividad Sísmica Reciente",
    map_style="open-street-map"
)

# Generar informe con IA
report = generate_ai_report(df)

# Crear aplicación Dash
app = dash.Dash(__name__)
app.title = "Earthquake Dashboard"

app.layout = html.Div([
    html.H1("🌎 Earthquake Activity Dashboard", style={"textAlign": "center"}),
    html.Div([
        html.Div([
            dcc.Graph(figure=fig, style={"height": "600px"})
        ], style={"width": "50%", "display": "inline-block", "padding": "20px"}),

        html.Div(
            # Se ha corregido el error: se cambió de html.Div a dcc.Markdown.
            children=[
                html.H2("📄 Informe de la IA", style={"textAlign": "center", "marginBottom": "10px"}),
                dcc.Markdown(children=report, dangerously_allow_html=True)
            ],
            id="ai-report",
            style={
                "width": "40%",
                "display": "inline-block",
                "backgroundColor": "#fff",
                "padding": "15px",
                "borderRadius": "10px",
                "boxShadow": "0 0 10px rgba(0,0,0,0.1)",
                "fontSize": "15px",
                "lineHeight": "1.6",
                "verticalAlign": "top"
            }
        )
    ])
])

if __name__ == "__main__":
    app.run(debug=True)
