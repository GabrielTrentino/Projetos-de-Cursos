![Escola de Data Science](https://github.com/GabrielTrentino/Projetos-de-Cursos/blob/master/00%20-%20Img/04-Escola%20de%20Data%20Science.png?raw=true)

# **Pasta 04 - Escola de Data Science:**

Nessa pasta estão presentes os guias e projetos da aulas da Escola de Data Science juntamente com as suas anotações e informações relevantes sobre a aula. A Escola de Data Science é ministrada pelo professor [Carlos Melo](https://www.linkedin.com/in/carlosfab/) pela plataforma [Escola de Data Science](https://escola.sigmoidal.ai/).

Esse README.md trará informações breve das aulas juntamente com os links de cada Notebook.

## **GUIA 01 - Séries Temporais:**

[LINK DO NOTEBOOK](https://github.com/GabrielTrentino/Projetos-de-Cursos/blob/master/04-EscolaDataScience/Guia001_TimeSeries.ipynb)

Esse guia foi elaborado com o objetivo de resumir e sintetizar o que foi passado nas três aulas da Escola de Data Science (ep. 1, ep.2 e ep.3) cujo o tema foi: Series Temporais. Nesse arquivo é encontrado diversos metodos e testes estatísticos para análises temporais.

**Conceitos iniciais das análises de séries temporais** utilizando dois Datasets:

1. Consumo e Produção de Energia Elétrica ao decorrer dos meses.
2. Utilização das Ferrovias por pessoas ao decorrer das horas de cada dia.

**Séries temporais são observações feitas em intervalos regulares de tempo**. Como existe uma dependência do tempo, técnicas tradicionais não são adequadas para lidar com esse tipo de problema. Essa primeira aula trouxe conceitos de:

Aplicação do Teste Dickey Fuller Aumentado (ADF) e buscamos **transformar uma Série Temporal para Estacionária** aplicando logaritmo, diferenciação e pelo **modelo ARIMA.** **ARIMA** é um dos modelos utilizados na estatística para prever comportamentos de uma Série Temporal.

**Conceitos de Forecasting (Técnicas de Previsão)** que são utilizados em Séries Temporais. Utilizando o Data Set: Consumo e Produção de Energia Elétrica ao decorrer dos meses.

**Forecasting (Previsão) é um processo de estimativa para situações de incertezas**, isto é, podemos buscar um modelo matemático capaz de estimar valores da Bolsa de Ações, mas sempre haverá uma diferença entre o previsto e o real.

* Séries Temporais.
* Componentes de Séries Temporais.
  * Comportamento de Tendência.
  * Comportamento de Sazonalidade.
  * Ruídos.
  * Função `seasonal_decompose` da biblioteca `statsmodels`.
* **Formatação Datetime e Manipulação de Dados com o tempo (`to_datetime` e `dt.year`).**
  * Plots utilizando o `groupby()`.
* Baselines:
  * Naive Approach (Modelo Ingênuo).
    * Segmentação do Dataset por Dia específico.
    * Gráfico com 3 Datasets.
  * Média Móvel.
    * Agrupamento por intervalos específicos `.rolling(n)`.
    * Média Móvel de 7, 14 e 30 dias.
  * Holt's Linear Model.
  * Validação pelo Mean Squared Error (Erro Quadrático Médio).
* Séries Estacionárias.
  * **Teste de Dickey - Fuller.**
  * Hipótese Nula e Alternativa.
  * Teste Dickey Fuller Aumentado.
  * Transformação de uma Série Temporal.
* **Modelo ARIMA**.

## **GUIA 02 - Redes Neurais:**

Em construção

## **PROJETO 01 - Deep Learning:**

Em Construção

## **Aula 011 - Web Scrapping (Scrapy)**

Foi elaborado um Cralwer que obtem as frases e autores da página [Quotes to Scrape](http://quotes.toscrape.com/) e para seu funcionamento devido ele precisa instalar e importar as bibliotecas do seu ambiente virtual. O exercício resolvido está disponível pelo [link](https://github.com/GabrielTrentino/Projetos-de-Cursos/blob/master/04-EscolaDataScience/Aula011-WebScrapping-quotes.rar), em que o arquivo `quotes_spider.py` é responsável pela informação dos dados. Para rodar o programa é necessário acessar a pasta no terminal (para isso clique com o botão direito em `quotes_spider.py` e selecione a opção: `Open in Terminal`) e rodar o seguinte código no terminal:

`scrapy crawl quotes_spider -o quotes.json`

Esse command line savará os resultados em um arquivo `.json`.

## **Dúvidas e Redes Sociais:**
O repositório aumentará o seu tamanho de acordo com as realizações dos cursos. E claro, aceito recomendações de cursos, livros ou vídeos! Qualquer duvida me chame no [LinkedIn](https://www.linkedin.com/in/gabriel-trentino-froes-415558144/).
