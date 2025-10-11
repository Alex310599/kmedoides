import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# --- Definir ruta base ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Cargar modelo ---
model_path = os.path.join(BASE_DIR, "modelo_recomendador.pkl")
with open(model_path, "rb") as f:
    saved = pickle.load(f)

kproto = saved["kproto"]
scaler = saved["scaler"]
cluster_info = saved["cluster_info"]
numerical_cols = saved["numerical_cols"]
categorical_cols = saved["categorical_cols"]

# --- Cargar base original ---
excel_path = os.path.join(BASE_DIR, "bdd", "bdd_limpia", "base_turismo_clean.xlsx")
base_turismo = pd.read_excel(excel_path)

# Convertir categorías a string
for col in categorical_cols:
    base_turismo[col] = base_turismo[col].astype(str)

categorical_idx = [len(numerical_cols) + i for i in range(len(categorical_cols))]

# --- Configurar Streamlit ---
st.set_page_config(page_title="Recomendador Turístico", layout="centered")
st.title("🌴 Recomendador Turístico con K-Prototypes")

# Entradas del usuario
mes_viaje = st.selectbox("Mes de viaje", sorted(base_turismo["mes_viaje"].unique()))
num_noches = st.number_input("Número de noches a viajar", 1, 30, 2)
presupuesto = st.number_input("Presupuesto total (USD)", 10, 10000, 100)


def recomendar_usuario(mes, noches, presupuesto):
    input_df = pd.DataFrame(
        [
            {
                col: 0 if col in numerical_cols else ""
                for col in numerical_cols + categorical_cols
            }
        ]
    )
    input_df.at[0, "mes_viaje"] = mes
    input_df.at[0, "num_noches_durmieron"] = noches

    input_df[numerical_cols] = scaler.transform(input_df[numerical_cols])
    input_array = input_df.to_numpy()

    cluster_pred = kproto.predict(input_array, categorical=categorical_idx)[0]
    info = cluster_info[cluster_pred]
    gasto_estimado = {
        k: round(v * presupuesto, 2) for k, v in info["proporciones_gasto"].items()
    }

    return {
        "cluster_asignado": int(cluster_pred),
        "top_actividades": info["top_actividades"],
        "top_destinos": info["top_destinos"],
        "gasto_estimado": gasto_estimado,
    }


if st.button("Recomendar viaje"):
    resultado = recomendar_usuario(mes_viaje, num_noches, presupuesto)

    st.subheader("🏖️ Top 3 Actividades sugeridas")
    for i, act in enumerate(resultado["top_actividades"], 1):
        st.write(f"{i}. {act}")

    st.subheader("🌍 Top 3 Destinos sugeridos")
    for i, dest in enumerate(resultado["top_destinos"], 1):
        st.write(f"{i}. {dest}")

    st.subheader("💰 Gasto estimado por categoría")
    for k, v in resultado["gasto_estimado"].items():
        st.write(f"{k}: ${v}")
