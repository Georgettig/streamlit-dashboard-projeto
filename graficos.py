import plotly.express as px
from utils import df_receita_estado, df_receita_mensal, df_receita_categoria, df_vendedores

graf_map = px.scatter_geo(
    df_receita_estado,
    lat = 'lat',
    lon = 'lon',
    scope = 'south america',
    size = 'Preço',
    template = 'seaborn',
    hover_name = 'Local da compra',
    hover_data = {'lat': False, 'lon': False},
    title = 'Receita por Estado'
)

graf_line = px.line(
    df_receita_mensal,
    x = 'Mês',
    y = 'Preço',
    markers = True,
    range_y = (0, df_receita_mensal.max()),
    color = 'Ano',
    line_dash = 'Ano',
    title = 'Receita Mensal'
)
graf_line.update_layout(yaxis_title='Receita')

graf_barra = px.bar(
    df_receita_estado.head(5),
    x = 'Local da compra',
    y = 'Preço',
    text_auto = True,
    title = 'Top 5 Receita por Estado'
)

graf_categoria = px.bar(
    df_receita_categoria,
    text_auto = True,
    title = 'Receita por Categoria'
)

graf_rec_vendedores = px.bar(
    df_vendedores[['sum']].sort_values('sum'),
    x = 'sum',
    y = df_vendedores[['sum']].sort_values('sum').index,
    text_auto = True,
    title = 'Receita por Vendedor'
)
graf_rec_vendedores.update_layout(yaxis_title='Vendedor', xaxis_title='Valor')

graf_venda = px.bar(
    df_vendedores[['count']].sort_values('count'),
    x = 'count',
    y = df_vendedores[['count']].sort_values('count').index,
    text_auto = True,
    title = 'Venda Realizada por Vendedor'
)
graf_venda.update_layout(yaxis_title='Vendedor', xaxis_title='Nº de Vendas')