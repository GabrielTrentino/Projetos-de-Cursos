# Introdução à Visualização de Dados e SQL

## Descrição da disciplina

<!-- Preencha com sua visão geral da matéria: objetivos, carga horária, professor(a), turma, links da INFNET/Deepnote, etc. -->

_A descrição desta disciplina será preenchida aqui._

Disciplina do **Ciclo Base** da INFNET que combina **visualização de dados** (com foco em **Google Looker Studio**) e **consultas SQL** em ambientes práticos (Deepnote e relatórios entregues em PDF).

---

## Materiais na pasta

| Arquivo | Formato | Descrição breve |
|---------|---------|-----------------|
| [Teste de Performance - 1](./Teste%20de%20Performance%20-%201.pdf) | PDF | Primeiro TP: conexão ao Looker Studio e primeiro contato com relatórios (link do dashboard entregue no documento). |
| [Teste de Performance - 2](./Teste%20de%20Performance%20-%202.pdf) | PDF | Segundo TP: tratamento de dados e dashboards interativos no Looker Studio — conexão direta, permissões de acesso (usuário logado vs. anônimo) e relatórios publicados. |
| [Teste de Performance - 3](./Teste%20de%20Performance%20-%203.ipynb) | Notebook | Terceiro TP: SQL no Deepnote sobre o cenário **TechStore** — tabelas `produtos`, `clientes`, `pedidos` e `vendedores`; 16 exercícios de consulta (estoque, clientes, pedidos e equipe comercial). |
| [Assessment](./Assessment.pdf) | PDF | Avaliação: exercícios 1–4 com dashboards no Looker Studio; exercícios 5–16 com SQL sobre catálogo de **filmes**, base de **funcionários** e **produtos de mercado**. |

> **Observação:** no momento, o Assessment e os TPs 1 e 2 estão apenas em PDF; o TP3 é o único notebook `.ipynb` da pasta.

---

## Índice por material

### Teste de Performance 1 (Looker Studio)



### Teste de Performance 2 (Looker Studio)


### Teste de Performance 3 (SQL — TechStore)

O notebook cria e popula quatro tabelas de referência. Os 16 exercícios cobrem:

| Bloco | Tabelas | Foco |
|-------|---------|------|
| Ex. 1–4 | `produtos` | Listagem completa, preços, filtro por categoria (`Periféricos`), estoque e faixas de preço. |
| Ex. 5–8 | `clientes` | Clientes por estado (`SP`, Sul), planos (`Gold`, `Silver`, `Free`) e exclusão de plano `Free`. |
| Ex. 9–12 | `pedidos` | Pedidos por status (`ENTREGUE`, `CANCELADO`, etc.), valor, data e combinações com `AND`/`OR`. |
| Ex. 13–16 | `vendedores` | Meta atingida, região (`Sudeste`, extremos do país), faixas de `vendas_mes` e ordenação. |

### Assessment (Looker Studio + SQL)

| Exercícios | Tema | Descrição breve |
|------------|------|-----------------|
| 1–4 | Looker Studio | Dashboards entregues por link (relatório de visualização). |
| 5–8 | `filmes` | `SELECT`, `WHERE`, `IN`, `ORDER BY`, agregações com `GROUP BY` / `HAVING` (`COUNT`, `AVG`, `MIN`, `MAX`). |
| 9–12 | `funcionarios` | Filtros por status, salário, idade, estado; `OR` e agregações por `ESTADO`. |
| 13–16 | `produtos_mercado` | Catálogo de mercado: disponibilidade, categorias, preço, estoque e resumo por categoria. |

---

## Resumo geral — conceitos da disciplina

Síntese do que aparece nos materiais atuais da pasta.

### Google Looker Studio

| Conceito | Uso na disciplina |
|----------|-------------------|
| Conexão a dados | Vincular planilhas, bases ou conectores ao relatório. |
| Visuais e páginas | Gráficos, tabelas e filtros em dashboards interativos. |
| Compartilhamento | Publicar relatório e controlar quem vê os dados (login vs. acesso anônimo). |
| Tratamento no painel | Preparar campos, métricas e dimensões para exibição correta nos visuais. |

### SQL — estrutura e manipulação de dados

| Comando / cláusula | Uso na disciplina |
|--------------------|-------------------|
| `CREATE TABLE` / `INSERT` | Montar bases de exemplo (`produtos`, `clientes`, `pedidos`, `vendedores`). |
| `SELECT` … `FROM` | Projetar colunas e ler tabelas. |
| `WHERE` | Filtrar por categoria, estado, plano, status, datas e valores. |
| `AND` / `OR` | Combinar critérios (pedidos, funcionários, produtos). |
| `IN` / `NOT IN` | Listas de gêneros, estados, status de venda. |
| `ORDER BY` | Ordenar por nota, idade, preço, estado, etc. |
| `GROUP BY` | Agrupar por gênero, estado, categoria. |
| `HAVING` | Filtrar grupos (ex.: mais de um filme por gênero). |
| Funções de agregação | `COUNT`, `AVG`, `MIN`, `MAX`, `SUM`. |
| `COUNT(DISTINCT …)` | Contar setores ou valores únicos por grupo. |
| Alias (`AS`) | Nomear colunas calculadas nos resultados. |

### Tabela rápida por material

| Material | Foco principal |
|----------|----------------|
| TP1 | Primeiro contato com Looker Studio |
| TP2 | Dashboards interativos |
| TP3 | SQL consultivo no cenário TechStore (Deepnote) |
| Assessment | Looker Studio + SQL integrado (filmes, RH, mercado) |
