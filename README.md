# 📊 Dashboard de Vendas | Python, Streamlit e Plotly

Dashboard interativo desenvolvido com Python, Streamlit, Pandas e Plotly para exploração e análise de dados de vendas.

A aplicação permite visualizar indicadores de desempenho, analisar a distribuição de receita, acompanhar tendências mensais e comparar resultados por estado, categoria de produto e vendedor.

O projeto demonstra a aplicação de técnicas de análise de dados e visualização interativa para transformar dados brutos em informações relevantes para a tomada de decisão. 

## 📸 Visão Geral

<img width="1364" height="629" alt="image" src="https://github.com/user-attachments/assets/89128d4b-29f1-49b8-88b6-9b697ab215ca" />

## 🎯 Objetivo do Projeto

Desenvolver uma aplicação interativa capaz de transformar dados de vendas em visualizações e indicadores que facilitem a compreensão do desempenho comercial.

O dashboard permite explorar diferentes dimensões dos dados, identificar padrões de receita e comparar resultados entre vendedores, categorias de produtos e localidades.

## 🚀 Funcionalidades

- Exploração de Dados: visualização interativa dos registros de vendas em uma tabela.
- Filtros Dinâmicos: seleção de vendedores, categorias de produtos, faixas de preço e períodos de compra.
- Análise de Receita: acompanhamento da receita total e sua distribuição por diferentes dimensões.
- Análise Geográfica: visualização da distribuição de receita por estado.
- Análise Temporal: acompanhamento da evolução mensal da receita e comparação entre anos.
- Análise por Categoria: identificação das categorias de produtos com maior contribuição para a receita.
- Desempenho de Vendedores: comparação entre receita gerada e quantidade de vendas realizadas.
- Exportação de Dados: download dos dados filtrados em formato CSV para análises complementares.

## 🛠️ Tecnologias Utilizadas

| **Tecnologia** | **Aplicação** | 
| -------------- | ------------- | 
| Python         | Desenvolvimento da aplicação       | 
| Streamlit      | Construção da interface interativa       | 
| Pandas         | Manipulação, transformação e análise de dados |
| Plotly         | Criação de visualizações interativas |
| JSON           | Armazenamento dos dados de vendas |
| Git e Github   | Versionamento e documentação do projeto |

## 📈 Análises e Visualizações

**Receita por Estado**
Visualização geográfica da distribuição de receita entre os estados brasileiros. O tamanho dos marcadores representa o valor da receita gerada em cada localidade.

**Evolução Mensal da Receita**
Gráfico de linhas que apresenta a evolução da receita ao longo dos meses, permitindo comparar o desempenho entre diferentes anos e identificar tendências temporais.

**Receita por Categoria de Produto**
Gráfico de barras que compara a receita total de cada categoria de produto, facilitando a identificação das categorias com maior contribuição financeira.

**Desempenho dos Vendedores**
Análise comparativa composta por duas visualizações:
- Receita total gerada por vendedor.
- Quantidade de vendas realizadas por vendedor.

## 📂 Estrutura do Projeto
```
streamlit-dashboard-projeto/
│
├── app.py                  # Aplicação principal Streamlit
├── dataset.py              # Carregamento e preparação dos dados
├── graficos.py             # Construção das visualizações
├── utils.py                # Funções auxiliares e transformações
│
├── dados/
│   └── vendas.json         # Base de dados de vendas
│
├── assets/
│   └── dashboard.png       # Captura de tela do dashboard
│
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação do projeto
```

## ⚙️ Como Executar o Projeto

1. Clone o repositório
```
git clone https://github.com/Georgettig/streamlit-dashboard-projeto.git
```

2. Acesse o diretório
```
cd streamlit-dashboard-projeto
```

3. Crie um ambiente virtual
```
python -m venv .venv
```

Ative o ambiente virtual:

Windows
```
.venv\Scripts\activate
```

Linux ou macOS
```
source .venv/bin/activate
```

4. Instale as dependências
```
pip install -r requirements.txt
```

Caso o arquivo requirements.txt ainda não esteja disponível, instale as principais bibliotecas:

```
pip install streamlit pandas plotly
```

5. Execute a aplicação
```
streamlit run app.py
```

## 🧠 Competências Desenvolvidas

- Manipulação e transformação de dados com Pandas.
- Análise exploratória de dados.
- Desenvolvimento de dashboards interativos.
- Visualização de dados com Plotly.
- Análise temporal e geográfica.
- Construção de indicadores de desempenho comercial.
- Aplicação de filtros e exportação de dados.
- Organização modular de aplicações Python.

## 👨‍💻 Autor

Guilherme Georgetti Albuquerque Galvão

Analista de Dados / Engenheiro de Produção — UNESP

🔗 LinkedIn: www.linkedin.com/in/guilherme-georgetti
