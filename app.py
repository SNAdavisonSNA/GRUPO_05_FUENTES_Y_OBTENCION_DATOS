import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
plt.style.use('default')
import ast

# 1. Configuración de la página
st.set_page_config(page_title="TFM: Análisis de Videojuegos RAWG", layout="wide")

# 2. Carga y limpieza de datos
@st.cache_data
def load_data():
    # Nombre del archivo actualizado a df_final.csv
    df = pd.read_csv('df_final.csv') 
    
    # Manejo de nulos y conversión a string para evitar errores en ast.literal_eval
    df['genres'] = df['genres'].fillna('[]').astype(str)
    df['platform'] = df['platform'].fillna('[]').astype(str)
    
    def parse_list(x):
        try:
            val = ast.literal_eval(x)
            return val if isinstance(val, list) else [x]
        except:
            return []

    df['genres_list'] = df['genres'].apply(parse_list)
    df['platform_list'] = df['platform'].apply(parse_list)
    return df

df_final = load_data()

# --- INTRODUCCIÓN DEL TEMA ---
st.title("🎮 Análisis del Mercado de Videojuegos: Dataset RAWG")
st.markdown("""
### Introducción
Este proyecto de fin de máster (TFM) tiene como objetivo explorar las tendencias de la industria de los videojuegos utilizando datos extraídos de la API de **RAWG**. 

A través de este dashboard, analizaremos cómo se distribuyen los títulos en las diferentes plataformas y si existe una relación directa entre el género de un videojuego y la calificación otorgada por los usuarios. Los datos reflejan información sobre miles de títulos, permitiendo identificar patrones de consumo y éxito crítico.
""")

st.divider()

# --- 1. EDA UNIVARIANTE ---
st.header("1. EDA Univariante: Distribución por Plataforma")
st.write("Este análisis permite observar la cuota de mercado de cada plataforma dentro del dataset, identificando dónde se concentra la mayor producción de videojuegos.")

# Replicamos el 'explode' del Jupyter para contar plataformas individuales
df_exploded = df_final.explode('platform_list').reset_index(drop=True)

fig_uni, ax_uni = plt.subplots(figsize=(10, 8))
sns.countplot(
    data=df_exploded,
    y='platform_list',
    hue='platform_list',
    palette='viridis',
    order=df_exploded['platform_list'].value_counts().index,
    legend=False,
    ax=ax_uni
)
ax_uni.set_title("Cantidad de Juegos por Plataforma")
# Ajustamos etiquetas para fondo claro
ax_uni.tick_params(axis='both', which='major', labelsize=10)
st.pyplot(fig_uni)

st.divider()

# --- 2. ANÁLISIS BIVARIANTE ---
st.header("2. Análisis Bivariante: Rating vs. Género")
st.write("A continuación, se analiza la calidad percibida (Rating) en función del género. El objetivo es determinar qué categorías mantienen estándares de calidad más altos y constantes.")

# Filtrado de juegos con rating (df_vivos) y obtención del género principal
df_vivos = df_final.dropna(subset=['rating']).copy()
df_vivos['genres_clean'] = df_vivos['genres_list'].apply(lambda x: x[0] if len(x) > 0 else "Otros")

fig_bi, ax_bi = plt.subplots(figsize=(12, 7))
sns.boxplot(
    data=df_vivos,
    x='rating',
    y='genres_clean',
    palette='Set3',
    ax=ax_bi
)
ax_bi.set_title("Distribución de Ratings por Género")
st.pyplot(fig_bi)

# --- CIERRE ---
st.sidebar.markdown("### Sobre los datos")
st.sidebar.info(f"Total de juegos cargados: 1000")
st.sidebar.info(f"Juegos Limpiados : {len(df_vivos)}")
