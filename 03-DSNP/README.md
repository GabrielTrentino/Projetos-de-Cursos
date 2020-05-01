![Data Science na Prática](https://github.com/GabrielTrentino/Projetos-de-Cursos/blob/master/00%20-%20Img/03-DataScienceNaPratica.png?raw=true)

# Pasta 03 - Data Science Na Prática:

Essa pasta é resultado dos estudos realizados do curso [Data Science Na Prática](https://datasciencenapratica.club.hotmart.com). O curso tem como objetivo ensinar os passos essenciais de um projeto de Data Science, envolvendo desde a estatística até o Personal Branding.

Esse README.md trará informações breve das aulas juntamente com os links de cada Notebook.

## Projeto 01 - Análise dos Dados do Airbnb - Rio de Janeiro:

[[LINK DO PROJETO]](https://github.com/GabrielTrentino/Projetos-de-Cursos/blob/master/03-DSNP/01_An%C3%A1lise_Explorat%C3%B3ria_AirBNB_(RIO).ipynb) / [[LINK DO DATASET]](http://insideairbnb.com/get-the-data.html)

Esse primeiro projeto é voltado para o básico da programação e da análise exploratória, pegamos um Dataset do [Inside Airbnb](http://insideairbnb.com/get-the-data.html) do Rio de Janeiro em que mostra os preços das diversas casas e apartamentos disponibilizados pelos anfitriões. Nesse projeto vimos o básico do Pandas e dos plots gráficos.

* Estruturação de um Projeto de Data Sciece.

* Funções básicas do Pandas e Numpy:
  * `.head()` - Visualiza os primeiros 5 termos do Data Frame.
  * `.tail()` - Visualiza os ultimos 5 termos do Data Frame.
  * `.shape` - Retorna a quantidade de linhas e coluna do Data Frame.
  * `.dtype` - Retorna os tipos de variáveis das colunas do Data Frame.
  * `.describe()` - Retorna uma matriz com os valores de mínimo, máximos, quartis e desvio-padrões.
  * `.sort_values()` - Ordenas os valores.
  * `.values_count()` - Conta quantas vezes um valor foi repetido.
  * `.corr()` - Retorna uma matriz de Correlação entre as variáveis.
  
* Gráficos do Pyplot e/ou Seaborn:
  * Boxplot 
  * Heatmap  
  * Histograma 
  * Scatterplot 
* Correção no Data Frame:
  * `.drop()` - Retira uma linha ou coluna, podendo sobre-escrever no DataFrame.

## Projeto 02 - Análise da Violência no Rio de Janeiro:

[[LINK DO PROJETO]](https://github.com/GabrielTrentino/Projetos-de-Cursos/blob/master/03-DSNP/02_Viol%C3%AAncia_Rio.ipynb) / [[LINK DO DATASET]](http://www.ispdados.rj.gov.br/estatistica.html)

Durante o segundo modulo foi apresentado novas funcionalidades do Pandas juntamente com a revisão e aprofudamento de funções apresentados no primeiro projeto. O primeiro modulo foi focado no mercado de Data Science, enquanto que esse segundo Modulo trouxe novas aplicações que podem vir a ser utilizadas.

O Dataset utilizado foi disponibilizado pelo Professor e se refere à **Violência no Rio de Janeiro**.

* Revisão das funcionalidades do primeiro projeto.
* Funções básicas do Pandas e Numpy:
  * `.copy()` - Copia as informações presentes em um Data Frame.
  * `.groupby()` - Agrupa as informações.
  * `.groupby().sum()` - Soma as informações agrupadas.
  * `.dropna()` - Retira valores nulos para linhas ou colunas.
* Criação de novas variáveis.


## Projeto 03 - Análise de Doenças Cardíacas:

[[LINK DO PROJETO]](https://github.com/GabrielTrentino/Projetos-de-Cursos/blob/master/03-DSNP/03_DataVisualization_Doen%C3%A7asCardiacas.ipynb) / [[LINK DO DATASET]](https://archive.ics.uci.edu/ml/datasets/heart+Disease)

O Terceiro Módulo foi focado na Visualização de dados, criando gráficos e buscando a melhor forma visual para criar gráficos. Para isso, utilizamos dois Datasets nesse projeto: um obtido pelo Cleveland Clinic Foundation que continham diversas variáveis que poderiam auxiliar para a identificação de Doenças Cardiovasculares e o segundo Data set foi obtido pela Sociedade Brasileira de Cardiologia (SBC). Nessa aula vimos gráficos do tipo:

* Barplot.
* Scatterpllot.
* Histograma.
* Piechart.
* Heatmap.

## Projeto 04 - Detecção de Fraudes em Cartões de Crédito:

[[LINK DO PROJETO]](https://github.com/GabrielTrentino/Projetos-de-Cursos/blob/master/03-DSNP/04_Fraude_em_Cart%C3%B5es_de_Cr%C3%A9dito.ipynb) / [[LINK DO DATASET]](https://www.kaggle.com/mlg-ulb/creditcardfraud)

Esse quarto modulo vimos técnicas e algoritmos de Machine Learning. E, para prever Fraudes em Cartões de Crédito, utilizamos algumas técnicas, tais como:

* Divisão do Data Frame em X (variável independente) e y (variável dependente, ou o que queremos identificar).
* `train_test_split` - Divisão do Data set em Treino e teste (Técnica Hold out, há outra chamada Cross Validate).
* `.fit()` e `.predict()` - Treina e prevê com o modelo escolhido.
* Random Under Sample.
* Decision Tree Classifier.
* Regressão Logística.
* SVC.
* KNN.
* Matriz de Confusão.
* Coeficiente de determinação.
