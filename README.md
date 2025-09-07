# 🌎 Dashboard de Actividad Sísmica

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/Framework-Plotly%20Dash-00cc96.svg)](https://dash.plotly.com/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange.svg)](https://pandas.pydata.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-Ollama-green.svg)](https://openai.com/)

---

## 📑 Índice
1. [Descripción](#descripción)  
2. [Características](#características)  
3. [Herramientas y Tecnologías](#herramientas-y-tecnologías)  
4. [Despliegue y Uso](#despliegue-y-uso)  
5. [Demo en Vivo](#demo-en-vivo)  
6. [Posibles Mejoras y Futuro](#posibles-mejoras-y-futuro)  

---
<img width="1342" height="761" alt="Captura de pantalla 2025-09-07 171912" src="https://github.com/user-attachments/assets/c475f28e-2c96-4c5f-b466-99770382bd7b" />

## Descripción
Esta aplicación es un prototipo interactivo desarrollado en **Python** que visualiza datos de actividad sísmica reciente.  

Utilizando **Plotly Dash**, el dashboard muestra un mapa de densidad con los sismos más recientes a nivel global y un informe analítico generado por un modelo de Inteligencia Artificial.

El proyecto está diseñado de forma modular, separando la lógica de la interfaz de usuario de la lógica de análisis de datos, lo que facilita su mantenimiento y escalabilidad.

---

## Características
- **Visualización de Datos:** Mapa de densidad interactivo que muestra la ubicación, magnitud y profundidad de los sismos.  
- **Análisis con IA:** Un informe técnico generado por un modelo de lenguaje que resume las zonas de mayor riesgo y la actividad sísmica global.  
- **Componentes reutilizables:** Uso de *Dash Core Components* (`dcc`) y *Dash HTML Components* (`html`).  

---

## Herramientas y Tecnologías
- **Python** (lenguaje principal)  
- **Plotly Dash** (framework para la aplicación web)  
- **Pandas** (procesamiento y análisis de datos)  
- **OpenAI API (Ollama)** con *Llama3.2* (para el informe analítico)  
- **markdown** (para conversión del informe IA de Markdown a HTML)  

---

## Despliegue y Uso

### 1. Requisitos
Asegúrate de tener **Python 3.10** instalado.

### 2. Instalación de Dependencias
Instala todas las bibliotecas necesarias utilizando `pip`:

```bash
pip install dash pandas plotly openai markdown
```

### 3. Configuración de la API
Crea un archivo llamado **`analyzer.py`** y añade tu clave de API de OpenAI.  
Si usas **Ollama**, asegúrate de que el servidor esté en ejecución.

Puedes usar un archivo **`data/earthquakes_raw.json`** para los datos iniciales.

### 4. Estructura de Archivos
Asegúrate de que tus archivos estén organizados de la siguiente manera:

```
/nombre_del_proyecto
|-- app_corrected.py
|-- analyzer.py
|-- data/
|   |-- earthquakes_raw.json
|-- README.md
```

### 5. Ejecución
Para iniciar la aplicación, ejecuta el siguiente comando desde tu terminal en el directorio principal del proyecto:

```bash
python app_corrected.py
```

La aplicación se ejecutará en tu navegador por defecto.  
Abre [http://127.0.0.1:8050/](http://127.0.0.1:8050/) para visualizar el dashboard.

## Posibles Mejoras y Futuro
Este prototipo es la base para una aplicación más robusta. Algunas ideas para futuras implementaciones incluyen:

- **Alertas push:** Añadir una alerta visual o sonora cuando se registre un sismo de magnitud igual o superior a 6.0.  
- **Datos en tiempo real:** Conectarse directamente a la API de **USGS** para actualizar los datos automáticamente sin necesidad de recargar la aplicación manualmente.  
- **Base de datos:** Utilizar una base de datos como **Firestore** para registrar los eventos y evitar alertas duplicadas.  
