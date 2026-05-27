import streamlit as st
import pandas as pd

from PIL import Image
from pathlib import Path

import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

# =========================
# Configuração
# =========================
st.set_page_config(
    page_title='Fome Zero',
    page_icon='🍽️',
    layout='wide'
)

# =========================
# Caminhos
# =========================
BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR / 'dataset' / 'zomato_clean.csv'
LOGO_PATH = BASE_DIR / 'img' / 'logo.png'

# =========================
# Dados
# =========================
df = pd.read_csv(DATA_PATH)

# =========================
# Função mapa
# =========================
def funcao_mapa(df):
    mapa = folium.Map(location=[20, 0], zoom_start=2)

    marcador = MarkerCluster().add_to(mapa)

    for _, local in df.head(3000).iterrows():
        folium.Marker(
            [local['latitude'], local['longitude']],
            popup=local['restaurant_name'],
            icon=folium.Icon(color='green')
        ).add_to(marcador)

    return mapa

# =========================
# Sidebar
# =========================
with st.sidebar:
    image = Image.open(LOGO_PATH)
    st.image(image, width=120)

    st.markdown('# Fome Zero')
    st.markdown('---')
    st.markdown('### by Alifer Rabelo')

# =========================
# Conteúdo principal
# =========================
st.title('🍽️ Fome Zero Dashboard')

st.markdown(
    '''
### Bem-vindo ao Fome Zero

Aqui você poderá acompanhar:


🌍 **Distribuição global dos restaurantes**

🏙️ **Cidades com maior concentração de estabelecimentos**

⭐ **Avaliações médias por país e por culinária**

🍔 **Principais tipos de culinária cadastrados**

💰 **Comparações de preços entre diferentes regiões**

---

### Mapa global de restaurantes

A visualização abaixo mostra a localização geográfica dos restaurantes
presentes na base de dados. Clique nos marcadores para visualizar cada restaurante
e utilize o zoom para explorar os países.
'''
)

# =========================
# Mapa
# =========================
mapa = funcao_mapa(df)

st_folium(
    mapa,
    width=1200,
    height=600
)