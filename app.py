import streamlit as st
from dataset import df
from utils import format, convert_csv, mensagem
from graficos import graf_map, graf_line, graf_barra, graf_categoria, graf_rec_vendedores, graf_venda

st.set_page_config(layout="wide")
st.title("Dashboard de Vendas")

st.sidebar.title("Fitlro de Vendedores")

filtro_vendedor = st.sidebar.multiselect('Vendedores', sorted(df['Vendedor'].unique()))
if filtro_vendedor:
    df = df[df['Vendedor'].isin(filtro_vendedor)]

with st.expander('Colunas'):
    colunas = st.multiselect(
        'Selecione as Colunas',
        list(df.columns),
        list(df.columns)
        )

st.sidebar.title("Filtro de Categoria")
with st.sidebar.expander('Categoria do Produto'):
    categorias = st.multiselect(
        'Selecione as Categorias',
        df['Categoria do Produto'].unique(),
        df['Categoria do Produto'].unique()
        )

st.sidebar.title("Filtro de Preços")
with st.sidebar.expander('Preço do Produto'):
    preco = st.slider(
        'Selecione o Preço',
        0, 5000,
        (0, 5000)
    )

st.sidebar.title("Filtro de Data da Compra")
with st.sidebar.expander('Data da Compra'):
    data = st.date_input(
        'Selecione a Data',
        (df['Data da Compra'].min(),
        df['Data da Compra'].max())
    )

query = '''
    `Categoria do Produto` in @categorias and \
    @preco[0] <= Preço <= @preco[1] and \
    @data[0] <= `Data da Compra` <= @data[1]
'''

filtro_dados = df.query(query)
filtro_dados = filtro_dados[colunas]

st.markdown(f'A tabela possui :red[{filtro_dados.shape[0]}] linhas e :red[{filtro_dados.shape[1]}] colunas')

aba1, aba2, aba3 = st.tabs(['Dataset','Receita','Vendedores'])

with aba1:
    st.dataframe(filtro_dados)
    st.markdown('Escreva o nome do arquivo:')

    col1, col2 = st.columns(2)
    with col1:
        nome_arquivo = st.text_input(
            '',
            label_visibility='collapsed'
        )
        nome_arquivo += '.csv'

    with col2:
        st.download_button(
            'Baixar arquivo',
            data=convert_csv(filtro_dados),
            file_name=nome_arquivo,
            mime='text/csv',
            on_click=mensagem
        )

with aba2:
    col1, col2 = st.columns(2)

    with col1:
        st.metric('Receita Total', format(df['Preço'].sum(), 'R$'))
        st.plotly_chart(graf_map, use_container_width=True)
        st.plotly_chart(graf_barra, use_container_width=True)
    with col2:
        st.metric('Total de Vendas', format(df.shape[0]))
        st.plotly_chart(graf_line, use_container_width=True)
        st.plotly_chart(graf_categoria, use_container_width=True)

with aba3:
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(graf_rec_vendedores, use_container_width=True)

    with col2:
        st.plotly_chart(graf_venda, use_container_width=True)