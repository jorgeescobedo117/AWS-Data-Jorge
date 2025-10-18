
# SUPERSTORE DASHBOARD - STREAMLIT + MYSQL + PLOTLY


import streamlit as st
import pandas as pd
import pymysql
import plotly.express as px
import os
from dotenv import load_dotenv

# ==========================================================
# CONFIGURACIÓN INICIAL
# ==========================================================
st.set_page_config(page_title="Superstore Dashboard", layout="wide")

# Carga de variables del entorno (.env)
load_dotenv("Enviorenment.env")

# ==========================================================
# CONEXIÓN A MYSQL
# ==========================================================
@st.cache_data
def get_data(table: str) -> pd.DataFrame:
    """Obtiene los datos de una tabla MySQL como DataFrame."""
    conn = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME")
    )
    df = pd.read_sql(f"SELECT * FROM {table}", conn)
    conn.close()
    return df

# ==========================================================
# TÍTULO PRINCIPAL Y DESCRIPCIÓN
# ==========================================================
st.title("Superstore Dashboard - KPIs y Análisis de Ventas")
# ==========================================================
# SECCIÓN DE KPIs PRINCIPALES
# ==========================================================
try:
    df_kpi = get_data("kpi_summary").iloc[0]

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("Ventas Totales", f"${df_kpi['total_sales']:,.2f}")
    col2.metric("Beneficio Total", f"${df_kpi['total_profit']:,.2f}")
    col3.metric("Margen de Beneficio", f"{df_kpi['profit_margin']:.2f}%")
    col4.metric("Pedidos Únicos", f"{df_kpi['num_orders']:,}")
    col5.metric("Tiempo Prom. Envío", f"{df_kpi['avg_ship_time']:.1f} días")
    col6.metric("Descuento Prom.", f"{df_kpi['avg_discount']:.2f}%")

except Exception as e:
    st.error(f"Error al cargar los KPIs: {e}")

# ==========================================================
# GRÁFICO 1: VENTAS Y BENEFICIO POR CATEGORÍA
# ==========================================================
st.subheader("Ventas y Beneficio por Categoría")
try:
    df_cat = get_data("sales_by_category")

    fig_cat = px.bar(
        df_cat,
        x="category",
        y="total_sales",
        color="total_profit",
        text_auto=".2s",
        color_continuous_scale="Blues"
    )
    fig_cat.update_layout(
        xaxis_title="Categoría",
        yaxis_title="Ventas ($)",
        plot_bgcolor="white",
        paper_bgcolor="white"
    )
    st.plotly_chart(fig_cat, use_container_width=True)
except Exception as e:
    st.warning(f"No se pudo cargar la información de categorías: {e}")

# ==========================================================
# GRÁFICO 2: TENDENCIA MENSUAL DE VENTAS
# ==========================================================
st.subheader("Tendencia Mensual de Ventas Totales")

try:
    df_month = get_data("sales_by_month")

    # Convertir columna 'month' y ordenar cronológicamente
    df_month["month"] = pd.to_datetime(df_month["month"], errors="coerce")
    df_month = df_month.sort_values("month")

    # Crear gráfico de línea con estilo moderno
    fig_trend = px.line(
        df_month,
        x="month",
        y="total_sales",
        markers=True,
        line_shape="spline"
    )

    # Estilo visual del gráfico
    fig_trend.update_traces(
        line=dict(width=4, color="#1f77b4"),
        marker=dict(size=9, color="#ff7f0e", line=dict(width=1.5, color="white")),
        fill='tozeroy',
        fillcolor='rgba(63, 136, 197, 0.1)'
    )

    fig_trend.update_layout(
        xaxis=dict(title="Mes", tickformat="%b %Y", showgrid=True, gridcolor="rgba(200,200,200,0.2)"),
        yaxis=dict(title="Ventas Totales ($)", showgrid=True, gridcolor="rgba(200,200,200,0.2)"),
        plot_bgcolor="white",
        paper_bgcolor="white",
        hovermode="x unified",
        font=dict(size=13, color="#222")
    )

    st.plotly_chart(fig_trend, use_container_width=True)

except Exception as e:
    st.warning(f"No se pudo cargar la tendencia mensual: {e}")

# ==========================================================
# GRÁFICO 3: TOP 10 PRODUCTOS POR VENTAS
# ==========================================================
st.subheader("Top 10 Productos por Ventas")
try:
    df_top = get_data("top_products")

    fig_top = px.bar(
        df_top,
        y="product_name",
        x="total_sales",
        orientation="h",
        text_auto=".2s",
        color="total_sales",
        color_continuous_scale="Viridis"
    )
    fig_top.update_layout(
        yaxis={"categoryorder": "total ascending"},
        plot_bgcolor="white",
        paper_bgcolor="white"
    )
    st.plotly_chart(fig_top, use_container_width=True)
except Exception as e:
    st.warning(f"No se pudo cargar el top de productos: {e}")

# ==========================================================
# GRÁFICO 4: DISTRIBUCIÓN DE VENTAS POR REGIÓN
# ==========================================================
st.subheader("Distribución de Ventas por Región")
try:
    df_region = get_data("sales_by_region")

    fig_pie = px.pie(
        df_region,
        names="region",
        values="total_sales",
        hole=0.45,
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig_pie.update_traces(textinfo="percent+label", pull=[0.05]*len(df_region))
    st.plotly_chart(fig_pie, use_container_width=True)
except Exception as e:
    st.warning(f"No se pudo cargar la distribución por región: {e}")
