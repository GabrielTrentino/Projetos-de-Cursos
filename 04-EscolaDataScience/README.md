![Escola de Data Science](https://github.com/GabrielTrentino/Projetos-de-Cursos/blob/master/00%20-%20Img/04-Escola%20de%20Data%20Science.png?raw=true)

# **Pasta 04 - Escola de Data Science:**

Nessa pasta estarão presentes todas as aulas da Escola de Data Science juntamente com as suas anotações e informações relevantes sobre a aula. A Escola de Data Science é ministrada pelo professor [Carlos Melo](https://www.linkedin.com/in/carlosfab/) pela plataforma [Escola de Data Science](https://escola.sigmoidal.ai/).

Esse README.md trará informações breve das aulas juntamente com os links de cada Notebook.

## **Aula 001 - Séries Temporais - Parte 1: Análise Exploratória:**

[LINK DO NOTEBOOK](https://github.com/GabrielTrentino/Projetos-de-Cursos/blob/master/04-EscolaDataScience/Aula001_S%C3%A9riesTemporais.ipynb) / [LINK DA AULA](https://sigmoidal.memberkit.com.br/2565-escola-de-data-science/137943-aula-001-series-temporais-analise-exploratoria)

Essa aula foi extreada no dia 28 de fevereiro de 2020 às 21h. Nessa primeira aula foi explicado **conceitos iniciais das análises de séries temporais** utilizando dois Datasets:

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

[LINK DO NOTEBOOK](https://github.com/GabrielTrentino/Projetos-de-Cursos/blob/master/04-EscolaDataScience/Aula002_S%C3%A9riesTemporais.ipynb) / [LINK DA AULA](https://sigmoidal.memberkit.com.br/2565-escola-de-data-science/139167-aula-002-series-temporais-tecnicas-de-forecasting)

Essa aula foi extreada no dia 05 de março de 2020 às 21h. Nessa segunda aula foi abordado alguns **conceitos de Forecasting (Técnicas de Previsão)** que são utilizados em Séries Temporais. Aproveitamos o Dataset da aula passada:

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

## **Aula 003 - Séries Temporais - Parte 3: Testes Estatístico e ARIMA.**

[LINK DO NOTEBOOK](https://github.com/GabrielTrentino/Projetos-de-Cursos/blob/master/04-EscolaDataScience/Aula003_S%C3%A9riesTemporais.ipynb) / [LINK DA AULA](https://sigmoidal.memberkit.com.br/2565-escola-de-data-science/143581-aula-003-series-temporais-testes-estatisticos-e-arima)

Essa aula foi extreada no dia 12 de março de 2020 às 21h pelo. Nessa terceira aula revemos a aplicação do Teste Dickey Fuller Aumentado (ADF) e buscamos **transformar uma Série Temporal para Estacionária** aplicando logaritmo, diferenciação e pelo **modelo ARIMA.**

**ARIMA** é um dos modelos utilizados na estatística para prever comportamentos de uma Série Temporal. Nessa aula foi visto:

* Teste Dickey Fuller Aumentado.
* Transformação de uma Série Temporal.
* **Modelo ARIMA**.

## **Aula 004 - Redes Neurais**

[LINK DO NOTEBOOK](https://github.com/GabrielTrentino/Projetos-de-Cursos/blob/master/04-EscolaDataScience/Aula004_RedesNeurais.ipynb) / [LINK DA AULA](https://sigmoidal.memberkit.com.br/2565-escola-de-data-science/144831-aula-004-redes-neurais)

## **Aula 005 - Introdução a Deep Learning** 

[LINK DO NOTEBOOK](https://github.com/GabrielTrentino/Projetos-de-Cursos/blob/master/04-EscolaDataScience/Aula005_Introducao_DeepLearning.ipynb) / [LINK DA AULA](https://sigmoidal.memberkit.com.br/2565-escola-de-data-science/159072-aula-005-introducao-ao-deep-learning)

## **Aula006 - Propragação em Redes Neurais (usando NumPy) **

[LINK DO NOTEBOOK]() / [LINK DA AULA](https://sigmoidal.memberkit.com.br/2565-escola-de-data-science/166571-aula-006-propagacao-em-redes-neurais-usando-numpy)

## **Aula007 - Gradient Descent**

[LINK DO NOTEBOOK]() / [LINK DA AULA](https://sigmoidal.memberkit.com.br/2565-escola-de-data-science/167434-aula-007-gradient-descent)

## **Aula008 - Tensforflow**

[LINK DO NOTEBOOK]() / [LINK DA AULA](https://sigmoidal.memberkit.com.br/2565-escola-de-data-science/171650-aula-008-tensorflow)

## **Aula009 - Classificiação de Roupas usando Deep Learning**

[LINK DO NOTEBOOK]() / [LINK DA AULA](https://sigmoidal.memberkit.com.br/2565-escola-de-data-science/175137-aula-009-projeto-classificacao-de-roupas-usando-deep-learning)

## **Aula010 - Forecasting em Séries Temporais com Prophet**

[LINK DO NOTEBOOK]() / [LINK DA AULA](https://sigmoidal.memberkit.com.br/2565-escola-de-data-science/184332-aula-010-projeto-forecasting-em-series-temporais-com-prophet)
