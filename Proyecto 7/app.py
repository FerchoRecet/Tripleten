import pandas as pd
import plotly.express as px
import streamlit as st

vehicles = pd.read_csv('../vehicles_us.csv')
st.header('Conjunto de datos de anuncios de venta de autos.')
hist_button = st.button('Si deseas construir un histograma preciona este boton.')
scatter_button = st.button('Si deseas construir un grafico de dispersion presiona este boton.')

if hist_button:
         st.write('El siguiente histograma representa el conjunto de datos de anuncios de ventas de coches.')
         
         fig = px.histogram(vehicles, x="odometer")
     
         st.plotly_chart(fig, use_container_width=True)

if scatter_button:
        st.write('El siguiente grafico de dispersion representa el conjunto de datos de anuncios de ventas de coches.')

        fig_2 = px.scatter(vehicles, x="odometer", y="price")

        st.plotly_chart(fig, use_container_width=True)
     