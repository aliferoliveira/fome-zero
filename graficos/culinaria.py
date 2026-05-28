from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVO = BASE_DIR / 'dataset' / 'zomato_clean.csv'

df = pd.read_csv(ARQUIVO)
import plotly.express as px

# Top 10 melhores restaurantes

def top_restaurantes(df):
    cols = ['restaurant_id','restaurant_name','country_name','city','cuisines','average_cost_for_two','aggregate_rating','votes']

    top = (df.loc[:, cols].groupby('restaurant_name')
           .agg({'restaurant_id':'min','country_name':'first','city':'first','cuisines':'first',
                 'average_cost_for_two':'first','aggregate_rating':'mean','votes':'sum'})
           .reset_index()
           .sort_values(by=['aggregate_rating','votes','restaurant_id'],
                        ascending=[False, False, True])
           .head(10))

    return top

top_restaurantes(df)

# Top 10 melhores culinarias
def top_culinarias(df):
    culinaria_nota_media = (df.loc[ : , ['cuisines', 'aggregate_rating', 'restaurant_id', 'country_name']].groupby('cuisines')
                            .agg(
                                maior_nota = ('aggregate_rating', 'max'),
                                menor_id = ('restaurant_id', 'min'),
                                country_name=('country_name', 'first')
                            ).sort_values(by=['maior_nota', 'menor_id'] , ascending=[False, True]).reset_index().head(10))
    
    fig = px.bar(culinaria_nota_media, x='cuisines', y='maior_nota', text='maior_nota', color='country_name', labels={'country_name': 'Países'} )
    fig.update_layout(
                      xaxis_title='Culinária',
                      yaxis_title='Média Nota'
                      )
    
    fig.update_traces(textposition='auto')

    return fig

top_culinarias(df)


# Top 10 piores culinarias

def piores_culinarias(df):
    culinaria_nota_media = (df.loc[ : , ['cuisines', 'aggregate_rating', 'restaurant_id', 'country_name']].groupby('cuisines')
                            .agg(
                                menor_nota = ('aggregate_rating', 'min'),
                                menor_id = ('restaurant_id', 'min'),
                                country_name=('country_name', 'first')
                            ).sort_values(by=['menor_nota', 'menor_id'] , ascending=[False, True]).reset_index().head(10))
    
    fig = px.bar(culinaria_nota_media, x='cuisines', y='menor_nota',  text='menor_nota', color='country_name', labels={'country_name': 'Países'} )
    fig.update_layout(
                      xaxis_title='Culinária',
                      yaxis_title='Média Nota'
                      )
    
    fig.update_traces(textposition='outside')

    return fig

top_culinarias(df)

