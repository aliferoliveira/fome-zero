import streamlit as st
import pandas as pd
from pathlib import Path
from PIL import Image

from graficos.pais import (
    agrupar_restaurante_pais,
    agrupar_cidade_pais,
    avaliacao_media_pais,
    media_prato_dois
)

# =========================
# Configuração
# =========================

st.set_page_config(
    page_title='Visão Países',
    page_icon='🌍',
    layout='wide'
)

# =========================
# Caminhos
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / 'dataset' / 'zomato_clean.csv'
LOGO_PATH = BASE_DIR / 'img' / 'logo.png'

# =========================
# Leitura dos dados
# =========================

df = pd.read_csv(DATA_PATH)

# =========================
# Filtros
# =========================

paises = sorted(df['country_name'].unique())

# =========================
# Sidebar
# =========================

with st.sidebar:
    image = Image.open(LOGO_PATH)
    st.image(image, width=120)

    st.markdown('# Fome Zero')
    st.markdown('### Visão Países')

    pais_selecionado = st.multiselect(
        'Selecione o país',
        paises,
        default=paises
    )

    st.markdown('---')
    st.markdown('### by Alifer Rabelo')

# =========================
# DataFrame filtrado
# =========================

df_filtrado = df.loc[
    df['country_name'].isin(pais_selecionado),
    :
]

# =========================
# Título
# =========================

st.title('🌍 Visão dos Países')

st.markdown(
    '''
Nesta página você pode acompanhar:
- quantidade de restaurantes
- média de avaliações
- média de preços
- distribuição global
'''
)

st.markdown('---')

# =========================
# KPIs
# =========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        '🌎 Países',
        df_filtrado['country_name'].nunique()
    )

with col2:
    st.metric(
        '🍽️ Restaurantes',
        df_filtrado['restaurant_id'].nunique()
    )

with col3:
    st.metric(
        '⭐ Média Global',
        round(df_filtrado['aggregate_rating'].mean(), 1)
    )

with col4:
    st.metric(
        '🏙️ Cidades',
        df_filtrado['city'].nunique()
    )

st.markdown('---')

# =========================
# Gráficos
# =========================

col1, col2 = st.columns(2)

with col1:
    st.subheader('Restaurantes por país')

    fig = agrupar_restaurante_pais(df_filtrado)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:
    st.subheader('Média de avaliações por país')

    fig = avaliacao_media_pais(df_filtrado)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown('---')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Quantidade de cidades registradas por país')

    fig = agrupar_cidade_pais(df_filtrado)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:
    st.subheader('Média de preço de um prato para duas pessoas por país')

    fig = media_prato_dois(df_filtrado)

    st.plotly_chart(
        fig,
        use_container_width=True
    )