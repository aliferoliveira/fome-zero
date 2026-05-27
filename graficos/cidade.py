from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVO = BASE_DIR / 'dataset' / 'zomato_clean.csv'

df = pd.read_csv(ARQUIVO)
import plotly.express as px

# Top 10 cidades com mais restaurantes

def top_cidades_restaurantes(df):
    cidade_mais_restaurantes = (df.groupby('city')
                                .agg(
                                    quantidade_restaurantes=('restaurant_id', 'nunique'),
                                    menor_id=('restaurant_id', 'min')
                                ).sort_values(by=['quantidade_restaurantes', 'menor_id'], ascending=[False, True]).reset_index().head(10))
    fig = px.bar(cidade_mais_restaurantes, x='city', y='quantidade_restaurantes', text='quantidade_restaurantes', labels={'city': 'Cidades'})
    
    fig.update_layout(xaxis_title = 'Cidades', showlegend=False)
    fig.update_traces(textposition='auto')
    
    return fig

top_cidades_restaurantes(df)

# Top 7 cidades com restaurantes com media acima de 4

def top_restaurantes(df):
    restaurante_nota_alta = df.loc[df['aggregate_rating'] > 4 , ['city' , 'restaurant_id']].groupby('city')['restaurant_id'].count().sort_values(ascending=False).reset_index(name='Quantidade de Restaurantes').head(7)
    fig = px.bar(restaurante_nota_alta, x='city', y='Quantidade de Restaurantes', text='Quantidade de Restaurantes', color='city', labels={'city': 'Cidades'})
    
    fig.update_layout(xaxis_title = 'Cidades', showlegend=False)
    fig.update_traces(textposition='auto')
    
    return fig

top_restaurantes(df)

# Top 7 cidades com restaurantes com media abaixo de 2.5

def piores_restaurantes(df):
    restaurante_nota_baixa = df.loc[df['aggregate_rating'] < 2.5 , ['city' , 'restaurant_id']].groupby('city')['restaurant_id'].count().sort_values(ascending=False).reset_index(name='Quantidade de Restaurantes').head(7)
    fig = px.bar(restaurante_nota_baixa, x='city', y='Quantidade de Restaurantes', text='Quantidade de Restaurantes', color='city', labels={'city': 'Cidades'})
    
    fig.update_layout(xaxis_title = 'Cidades', showlegend=False)
    fig.update_traces(textposition='auto')
    
    


    return fig

piores_restaurantes(df)

# Top 10 cidades com restaurantes com mais tipos de culinarias distitnas

def top_culinarias(df):
    cidade_culinaria_distinta = df.loc[: , ['city', 'cuisines']].groupby('city')['cuisines'].nunique().sort_values(ascending=False).reset_index(name='Tipos de Culinarias Distintas').head(10)
    fig = px.bar(cidade_culinaria_distinta, x='city', y='Tipos de Culinarias Distintas', text='Tipos de Culinarias Distintas',   labels={'city': 'Cidades'})

    fig.update_layout(xaxis_title = 'Cidades', showlegend=False)
    fig.update_traces(textposition='auto')

    return fig

top_culinarias(df)