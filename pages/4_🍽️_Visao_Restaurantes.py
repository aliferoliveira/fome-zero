import streamlit as st
import pandas as pd

from pathlib import Path
from PIL import Image

from graficos.restaurante import (
    grafico_online_offline,
    grafico_japao_bbq
)

st.set_page_config(
    page_title='Visão Restaurantes',
    page_icon='🍽️',
    layout='wide'
)

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / 'dataset' / 'zomato_clean.csv'
LOGO_PATH = BASE_DIR / 'img' / 'logo.png'

df = pd.read_csv(DATA_PATH)

# filtros
paises = sorted(df['country_name'].unique())

with st.sidebar:
    image = Image.open(LOGO_PATH)
    st.image(image, width=120)

    st.markdown('# Fome Zero')
    st.markdown('### Visão Restaurantes')

    pais_selecionado = st.multiselect(
        'Selecione o país',
        paises,
        default=paises
    )

    st.markdown('---')
    st.markdown('### by Alifer Rabelo')

df_filtrado = df[
    df['country_name'].isin(pais_selecionado)
]

# título
st.title('🍽️ Visão dos Restaurantes')

st.markdown(
    '''
Nesta página você acompanha indicadores e comparações dos restaurantes.
'''
)

st.markdown('---')

# kpis
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        '🍽️ Restaurantes',
        df_filtrado['restaurant_id'].nunique()
    )

with col2:
    st.metric(
        '⭐ Média',
        round(df_filtrado['aggregate_rating'].mean(), 1)
    )

with col3:
    st.metric(
        '🗳️ Votos',
        int(df_filtrado['votes'].sum())
    )

with col4:
    st.metric(
        '💰 Ticket médio',
        round(df_filtrado['average_cost_for_two'].mean(), 1)
    )

st.markdown('---')


st.subheader('Média de Votos: Online x Offline')
fig = grafico_online_offline(df_filtrado)
st.plotly_chart(fig, use_container_width=True)




