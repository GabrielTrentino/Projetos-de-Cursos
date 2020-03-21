![Escola de Data Science](https://github.com/GabrielTrentino/Projetos-de-Cursos/blob/master/00%20-%20Img/04-Escola%20de%20Data%20Science.png?raw=true)

# **Pasta 04 - Escola de Data Science:**

Nessa pasta estarão presentes todas as aulas da Escola de Data Science juntamente com as suas anotações e informações relevantes sobre a aula. A Escola de Data Science é ministrada pelo professor [Carlos Melo](https://www.linkedin.com/in/carlosfab/) pela plataforma [Escola de Data Science](https://escola.sigmoidal.ai/).

Esse README.md trará informações breve das aulas juntamente com os links de cada Notebook.

## **Aula 001 - Séries Temporais - Parte 1: Análise Exploratória:**

[LINK DO NOTEBOOK](https://github.com/GabrielTrentino/Projetos-de-Cursos/blob/master/04-EscolaDataScience/Aula001_S%C3%A9riesTemporais.ipynb)

Essa aula foi extreada no dia 28 de fevereiro de 2020 às 21h pelo [link](https://sigmoidal.memberkit.com.br/2565-escola-de-data-science/137943-aula-001-series-temporais-analise-exploratoria). Nessa primeira aula foi explicado **conceitos iniciais das análises de séries temporais** utilizando dois Datasets:

1. Consumo e Produção de Energia Elétrica ao decorrer dos meses.
2. Utilização das Ferrovias por pessoas ao decorrer das horas de cada dia.

**Séries temporais são observações feitas em intervalos regulares de tempo**. Como existe uma dependência do tempo, técnicas tradicionais não são adequadas para lidar com esse tipo de problema. Essa primeira aula trouxe conceitos de:

* Séries Temporais.
* Componentes de Séries Temporais.
  * Comportamento de Tendência.
  * Comportamento de Sazonalidade.
  * Ruídos.
* Função `seasonal_decompose` da biblioteca `statsmodels`.
* **Formatação Datetime e Manipulação de Dados com o tempo (`to_datetime` e `dt.year`).**
* Plots utilizando o `groupby()`.

## **Aula 002 - Séries Temporais - Parte 2: Técnicas de Forecasting:**

[LINK DO NOTEBOOK](https://github.com/GabrielTrentino/Projetos-de-Cursos/blob/master/04-EscolaDataScience/Aula002_S%C3%A9riesTemporais.ipynb)

Essa aula foi extreada no dia 05 de março de 2020 às 21h pelo [link](https://sigmoidal.memberkit.com.br/2565-escola-de-data-science/139167-aula-002-series-temporais-tecnicas-de-forecasting). Nessa segunda aula foi abordado alguns **conceitos de Forecasting (Técnicas de Previsão)** que são utilizados em Séries Temporais. Aproveitamos o Dataset da aula passada:

1. Consumo e Produção de Energia Elétrica ao decorrer dos meses.

**Forecasting (Previsão) é um processo de estimativa para situações de incertezas**, isto é, podemos buscar um modelo matemático capaz de estimar valores da Bolsa de Ações, mas sempre haverá uma diferença entre o previsto e o real. Nessa aula foi visto:

* Naive Approach (Modelo Ingênuo).
  * Segmentação do Dataset por Dia específico.
  * Gráfico com 3 Datasets.
* Média Móvel.
  * Agrupamento por intervalos específicos `.rolling(n)`.
  * Média Móvel de 7, 14 e 30 dias.
* Holt's Linear Model.
* Mean Squared Error (Erro Quadrático Médio).
* Séries Estacionárias.
  * **Teste de Dickey - Fuller.**
  * Hipótese Nula e Alternativa.
