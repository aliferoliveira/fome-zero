import streamlit as st
import pandas as pd
from pathlib import Path
from PIL import Image

from graficos.cidade import (
    top_cidades_restaurantes,
    top_restaurantes,
    piores_restaurantes,
    top_culinarias
)

# Configuração
st.set_page_config(page_title='Visão Cidades', page_icon='🏙️', layout='wide')

# Caminhos
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / 'dataset' / 'zomato_clean.csv'
LOGO_PATH = BASE_DIR / 'img' / 'logo.png'

# Dados
df = pd.read_csv(DATA_PATH)

# Sidebar
paises = sorted(df['country_name'].unique())

with st.sidebar:
    image = Image.open(LOGO_PATH)
    st.image(image, width=120)

    st.markdown('# Fome Zero')
    st.markdown('### Visão Cidades')

    pais_selecionado = st.multiselect('Selecione o país', paises, default=paises)

    df_pais = df[df['country_name'].isin(pais_selecionado)]
    cidades = sorted(df_pais['city'].unique())

    cidade_selecionada = st.multiselect('Selecione a cidade', cidades, default=cidades)

    st.markdown('---')
    st.markdown('### by Alifer Rabelo')

# Filtro
df_filtrado = df[
    (df['country_name'].isin(pais_selecionado)) &
    (df['city'].isin(cidade_selecionada))
]

# Título
st.title('🏙️ Visão das Cidades')

st.markdown('Nesta página você pode analisar a distribuição dos restaurantes por cidade.')

st.markdown('---')

# Gráfico 1
st.subheader('Top 10 cidades com mais restaurantes')
fig = top_cidades_restaurantes(df_filtrado)
st.plotly_chart(fig, use_container_width=True)

st.markdown('---')

# 2 colunas
col1, col2 = st.columns(2)

with col1:
    st.subheader('Top 7 cidades com restaurantes acima de 4.0')
    fig = top_restaurantes(df_filtrado)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader('Top 7 cidades com restaurantes abaixo de 2.5')
    fig = piores_restaurantes(df_filtrado)
    st.plotly_chart(fig, use_container_width=True)

st.markdown('---')

# Último gráfico
st.subheader('Top 10 cidades com mais culinárias distintas')
fig = top_culinarias(df_filtrado)
st.plotly_chart(fig, use_container_width=True)