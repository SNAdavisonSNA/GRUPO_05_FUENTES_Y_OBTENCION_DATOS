========================================================================
    PROYECTO: ANÁLISIS DEL MERCADO DE VIDEOJUEGOS (DATASET RAWG)
========================================================================
INTEGRANTES:
Sebastián González Varela
David Martinez Luna
Gabriele Massoti
Gabriel Otero
Leandro Rondini


DESCRIPCIÓN:
Este proyecto realiza un análisis integral de datos de la industria de los
videojuegos. Utiliza la API de RAWG para recopilar información sobre miles
de títulos y procesarlos para extraer conclusiones sobre tendencias,
plataformas y comportamiento de los usuarios.

CONTENIDO DEL REPOSITORIO:

1. tfm.ipynb (Jupyter Notebook)
   - Extracción de datos: Script de conexión a la API de RAWG.
   - Limpieza: Procesamiento de nulos y normalización de columnas (géneros, 
     plataformas).
   - EDA: Análisis estadístico profundo, incluyendo estudios de asimetría 
     (skewness) y curtosis en las métricas de rating.
   - Análisis Bivariante: Estudio de la relación entre el abandono de 
     juegos ("Dropped") y la calidad percibida.

2. app.py (Streamlit Dashboard)
   - Aplicación interactiva para visualizar los datos finales.
   - Gráficos de barras para la distribución por plataforma.
   - Boxplots para comparar el rating entre diferentes géneros.

REQUISITOS DEL SISTEMA:
- Python 3.x
- Librerías: pandas, numpy, matplotlib, seaborn, streamlit, requests, scipy.

INSTRUCCIONES DE USO:

Paso 1: Obtención de datos
Abrir 'tfm.ipynb' y ejecutar las celdas de extracción (se requiere una 
API Key de RAWG). Este proceso generará el archivo 'df_final.csv'.

Paso 2: Visualización
Para lanzar el tablero interactivo, ejecute el siguiente comando en la 
consola:
   
   streamlit run app.py

HALLAZGOS RELEVANTES:
- Se identificó que géneros complejos como Estrategia o RPG presentan un 
  alto índice de abandono inicial, pero mantienen ratings muy altos por 
  parte de los usuarios que completan el juego, sugiriendo un "filtro de 
  entrada" por dificultad o extensión.
- El dataset procesado permite filtrar juegos por plataformas específicas 
  y comparar su éxito crítico de forma visual.

------------------------------------------------------------------------
Proyecto desarrollado como Trabajo de Fin de Máster (TFM).
========================================================================