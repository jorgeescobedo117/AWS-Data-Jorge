
                                                            # Usando Streamlit + pandas + Plotly + API FreeToGame


# Importamos las librerías necesarias 
import requests       # Para hacer solicitudes HTTP a la API
import pandas as pd   # Para manipular los datos en formato tabla
import streamlit as st  # Para crear la interfaz web interactiva
import plotly.express as px  # Para generar gráficos dinámicos y bonitos


# Titulo que aparece en la pestaña del navegador y define el ancho de la app
st.set_page_config(page_title="Videojuegos Gratuitos Dashboard", layout="wide")

# ------------------------------
# Esta es la funcion para cargar los datos de la API
# ------------------------------
@st.cache_data  # Esta etiqueta guarda los datos en caché 
def load_data():
    # URL de la API pública FreeToGame
    url = "https://www.freetogame.com/api/games"
    
    # Hacemos la petición GET a la API
    resp = requests.get(url)
    
    
    # Convertimos la respuesta JSON a un diccionario de Python
    data = resp.json()
    
    # Lo convertimos a un DataFrame de pandas para analizarlo fácilmente
    df = pd.DataFrame(data)
    
    return df  # Retornamos el DataFrame

# Llamamos la función y guardamos el resultado
df = load_data()


#  TÍTULO PRINCIPAL

st.title("Dashboard de Videojuegos Gratuitos")


#  SIDEBAR:


# Obtenemos las listas únicas de plataformas, géneros y años de lanzamiento
platforms = sorted(df['platform'].unique())  #  PC, Browser
genres = sorted(df['genre'].unique())        # Shooter, MMORPG
release_years = sorted(df['release_date'].str[:4].unique())  # Extraemos los 4 primeros caracteres del año

# Creamos los filtros en la barra lateral
plat_filter = st.sidebar.multiselect("Plataforma", options=platforms, default=platforms)
genre_filter = st.sidebar.multiselect("Género", options=genres, default=genres)
year_filter = st.sidebar.multiselect("Año de lanzamiento", options=release_years, default=release_years)


#  AQUI FILTRAREMOS LOS DATOS :DD


# Extraemos el año (como texto) de la fecha de lanzamiento
df['release_year'] = df['release_date'].str[:4]

# Filtramos el DataFrame según las selecciones del usuario
filtered = df[
    (df['platform'].isin(plat_filter)) &
    (df['genre'].isin(genre_filter)) &
    (df['release_year'].isin(year_filter))
]


#  MÉTRICAS PRINCIPALES 


# Calculamos algunos indicadores
total_games = len(df)                      # Total de juegos en la API
unique_genres = df['genre'].nunique()      # Número de géneros distintos
avg_release_year = df['release_year'].astype(int).mean()  # Promedio del año de lanzamiento

# Mostramos los indicadores en tres columnas
col1, col2, col3 = st.columns(3)
col1.metric("Total de juegos gratis", total_games)
col2.metric("Géneros únicos", unique_genres)
col3.metric("Año promedio de lanzamiento", f"{avg_release_year:.0f}")

# Graficas


col1, col2 = st.columns(2)  # Dividimos el espacio en dos columnas para mostrar dos gráficos lado a lado

with col1:
    # Conteo de juegos por plataforma
    plat_counts = filtered['platform'].value_counts().reset_index()
    plat_counts.columns = ['platform', 'count']  # Renombramos columnas para claridad
    
    # Gráfica de barras
    fig1 = px.bar(
        plat_counts,
        x='platform',
        y='count',
        title="Juegos por plataforma"
    )
    
    # Mostramos el gráfico en Streamlit
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    # Conteo de juegos por género
    genre_counts = filtered['genre'].value_counts().reset_index()
    genre_counts.columns = ['genre', 'count']
    
    # Gráfico de pastel (pie chart)
    fig2 = px.pie(
        genre_counts,
        names='genre',
        values='count',
        title="Distribución por género"
    )
    
    st.plotly_chart(fig2, use_container_width=True)


# TABLA DE DATOS

st.subheader("Algunos registros")

# Mostramos los primeros 30 juegos filtrados
st.dataframe(filtered.head(30), use_container_width=True)


