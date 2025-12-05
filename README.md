# 🇪🇨 Sistema Recomendador de Turismo Interno - Ecuador

> **Trabajo de Titulación:** "Análisis de patrones turísticos de los hogares ecuatorianos mediante técnicas no supervisadas para la construcción de un sistema recomendador de viajes."

## 📋 Descripción del Proyecto

Este repositorio contiene el código fuente, los modelos y la aplicación web desarrollada para identificar patrones de comportamiento turístico en los hogares ecuatorianos y ofrecer recomendaciones personalizadas de viaje.

El proyecto utiliza datos oficiales del año 2021 (INEC - SBI) y aplica técnicas de **Machine Learning No Supervisado** (específicamente el algoritmo **K-Prototypes**) para segmentar a los turistas basándose en variables mixtas (numéricas y categóricas). El resultado final es una aplicación interactiva desplegada en **Streamlit** que sugiere destinos, actividades y estimaciones de presupuesto.

## 🚀 Funcionalidades Principales

* **Segmentación Híbrida:** Agrupamiento de perfiles utilizando K-Prototypes para manejar datos como *Gasto* (numérico) y *Motivación* (categórico) simultáneamente.
* **Perfilamiento de Turistas:** Identificación de 3 clústeres principales:
    * 🌿 *Turista de Naturaleza & Escapada Corta*
    * 🧖 *Turista de Salud & Balnearios (Larga estancia)*
    * 🏖️ *Turista Costero & Social*
* **Interfaz de Recomendación (Cold-Start):** Sistema capaz de sugerir itinerarios a nuevos usuarios solicitando solo 3 parámetros (Mes, Noches, Presupuesto).
* **Estimación de Presupuestos:** Desglose inteligente del gasto predicho por categorías (Alimentación, Transporte, Alojamiento, etc.).

## 🛠️ Tecnologías Utilizadas

El proyecto fue desarrollado íntegramente en **Python 3.x** utilizando las siguientes librerías clave:

* **Streamlit:** Para el desarrollo y despliegue de la interfaz web.
* **KModes:** Implementación del algoritmo K-Prototypes.
* **Scikit-learn:** Preprocesamiento de datos (MinMaxScaler) y pipelines.
* **Pandas & NumPy:** Manipulación y análisis vectorial de datos.
* **Pickle:** Serialización del modelo para inferencia en tiempo real.
* **Plotly/Matplotlib:** Visualización de datos (en la fase exploratoria).

## 📂 Estructura del Repositorio

```text
├── bdd/                   # Base de datos (raw y limpia)
├── notebooks/             # Jupyter Notebooks con el EDA y entrenamiento
├── app.py                 # Script principal de la aplicación Streamlit
├── modelo_recomendador.pkl # Modelo serializado (K-Proto + Scaler + Metadata)
├── requirements.txt       # Lista de dependencias del proyecto
└── README.md              # Documentación del proyecto
```

## 🛠️ Instalación y Uso Local

Si deseas ejecutar este proyecto en tu máquina local, sigue estos pasos:

---

### 📥 1. Clonar el repositorio

```bash
git clone https://github.com/Alex310599/kmedoides.git
cd kmedoides
```
### 📥 2. Crear un entorno virtual (Recomendado):

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En Mac/Linux
python3 -m venv venv
source venv/bin/activate
```
### 📥 3. Instalar dependencias:

```bash
pip install -r requirements.txt
```
### 📥 4. Ejecutar la aplicación:

```bash
streamlit run app.py
```

🌐 Versión en Producción

Si no deseas instalar nada, puedes usar directamente la aplicación desplegada en Streamlit Cloud:

🔗 App en producción:
https://kmedoides-ldndj4gbv8rghpfzkeukcf.streamlit.app/

🔗 Repositorio en GitHub:
https://github.com/Alex310599/kmedoides
