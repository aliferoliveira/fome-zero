import streamlit as st
import pandas as pd
from pathlib import Path
from PIL import Image

from graficos.culinaria import (
    top_restaurantes,
    top_culinarias,
    piores_culinarias
)

st.set_page_config(page_title='Visão Culinárias', page_icon='🍝', layout='wide')

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / 'dataset' / 'zomato_clean.csv'
LOGO_PATH = BASE_DIR / 'img' / 'logo.png'

df = pd.read_csv(DATA_PATH)

# Sidebar
paises = sorted(df['country_name'].unique())

with st.sidebar:
    image = Image.open(LOGO_PATH)
    st.image(image, width=120)

    st.markdown('# Fome Zero')
    st.markdown('### Visão Culinárias')

    pais_selecionado = st.multiselect(
        'Selecione o país',
        paises,
        default=paises
    )

    df_pais = df[df['country_name'].isin(pais_selecionado)]

    cozinhas = sorted(df_pais['cuisines'].dropna().unique())

    cozinha_selecionada = st.multiselect(
        'Selecione a culinária',
        cozinhas,
        default=cozinhas
    )

    st.markdown('---')
    st.markdown('### by Alifer Rabelo')

# filtro
df_filtrado = df[
    (df['country_name'].isin(pais_selecionado)) &
    (df['cuisines'].isin(cozinha_selecionada))
]

# título
st.title('🍝 Visão das Culinárias')

st.markdown(
    'Nesta página você pode analisar restaurantes e culinárias por país e cidade.'
)

st.markdown('---')

# top restaurantes
st.subheader('Top 10 melhores restaurantes')
top = top_restaurantes(df_filtrado)
st.dataframe(top, use_container_width=True)

st.markdown('---')

# gráficos
col1, col2 = st.columns(2)

with col1:
    st.subheader('Top 10 melhores culinárias')
    fig = top_culinarias(df_filtrado)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader('Top 10 piores culinárias')
    fig = piores_culinarias(df_filtrado)
    st.plotly_chart(fig, use_container_width=True)