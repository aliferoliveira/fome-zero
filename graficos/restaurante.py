import pandas as pd
import plotly.express as px

# Média votos online x offline

def grafico_online_offline(df):

    media_online = df.loc[df['has_online_delivery'] == 1, 'votes'].mean().round(1)
    media_offline = df.loc[df['has_online_delivery'] == 0, 'votes'].mean().round(1)

    grafico = pd.DataFrame({
        'Tipo': ['Online', 'Offline'],
        'Média de Avaliaçoes': [media_online, media_offline]
    })

    fig = px.bar(grafico, x='Tipo', y='Média de Avaliaçoes', text='Média de Avaliaçoes',
                 title=' ',
                 color='Tipo', color_discrete_map={'Online': 'green', 'Offline': 'red'})

    fig.update_layout(title_x=0.5)
    fig.update_traces(textposition='outside')
    fig.update_layout(title_x=0.5, title_font_size=16, margin=dict(t=80)
)

    return fig


# Japonesa x BBQ

def grafico_japao_bbq(df):

    japonesa = df.loc[
        (df['cuisines'] == 'Japanese') &
        (df['country_name'] == 'United States of America'),
        'average_cost_for_two'
    ].mean().round(1)

    bbq = df.loc[
        (df['cuisines'] == 'BBQ') &
        (df['country_name'] == 'United States of America'),
        'average_cost_for_two'
    ].mean().round(1)

    grafico = pd.DataFrame({
        'Tipo': ['Japonesa', 'BBQ'],
        'Valor Medio Prato para Duas Pessoas': [japonesa, bbq]
    })

    fig = px.bar(grafico, x='Tipo', y='Valor Medio Prato para Duas Pessoas',
                 title=' ',
                 color='Tipo', color_discrete_map={'Japonesa': 'red', 'BBQ': 'orange'},
                 text='Valor Medio Prato para Duas Pessoas')

    fig.update_layout(title_x=0.5)
    fig.update_layout(yaxis_title='Valor Médio')
    fig.update_traces(textposition='outside')

    return fig