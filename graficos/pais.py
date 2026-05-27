from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVO = BASE_DIR / 'dataset' / 'zomato_clean.csv'

df = pd.read_csv(ARQUIVO)
import plotly.express as px

# agrupar restaurante por pais

def agrupar_restaurante_pais(df):
  df_restaurantes = df.groupby('country_name')['restaurant_id'].nunique().sort_values(ascending=False).reset_index(name='Quantidade de Restaurantes')
  fig = px.bar(df_restaurantes, x='country_name', y='Quantidade de Restaurantes', text='Quantidade de Restaurantes', labels={'country_name': 'País'})

  fig.update_layout(xaxis_title='Países', showlegend=False)
  
  return fig

agrupar_restaurante_pais(df)

# Quantidade de cidades registradas por país

def agrupar_cidade_pais(df):
  df_cidade_pais = df.groupby('country_name')['city'].nunique().sort_values(ascending=False).reset_index(name='Quantidade de Cidades')
  fig = px.bar(df_cidade_pais, x='country_name', y='Quantidade de Cidades', text='Quantidade de Cidades', labels={'country_name': 'País'})
  
  fig.update_layout(xaxis_title='Países', showlegend=False)

  return fig

agrupar_cidade_pais(df)

# Média de avaliações por pais

def avaliacao_media_pais(df):
  df_media_pais = df.groupby('country_name')['votes'].mean().sort_values(ascending=False).reset_index(name='Media de Avaliacoes').round(2)
  fig = px.bar(df_media_pais, x='country_name', y='Media de Avaliacoes', text='Media de Avaliacoes',  labels={'country_name': 'País'})
  
  fig.update_layout(xaxis_title='Países', showlegend=False)

  return fig

avaliacao_media_pais(df)

# Média de preço de um prato pra duas pessoas por país

def media_prato_dois(df):
  df_media_prato_dois = df.groupby('country_name')['average_cost_for_two'].mean().sort_values(ascending=False).reset_index(name='Media Prato para Dois').round(2)
  fig = px.bar(df_media_prato_dois, x='country_name', y='Media Prato para Dois', text='Media Prato para Dois')

  fig.update_layout(xaxis_title='Países')
  

  return fig

media_prato_dois(df)
