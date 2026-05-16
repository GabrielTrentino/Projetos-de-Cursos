# Introdução à Programação com Python

## Descrição da disciplina

<!-- Preencha com sua visão geral da matéria: objetivos, carga horária, professor(a), turma, links da INFNET/Deepnote, etc. -->

_A descrição desta disciplina será preenchida aqui._

---

## Índice de notebooks

| Notebook | Descrição breve |
|----------|-----------------|
| [Teste de Performance - 1](./Teste%20de%20Performance%20-%201.ipynb) | Primeiro teste de performance: fundamentos de Python — comentários, `print`, variáveis, fluxo IPO, tipos (`int`, `float`, `bool`), operações aritméticas e operadores `//`, `%` e `round` em cenários de logística, finanças e folha de pagamento (16 exercícios). |
| [Teste de Performance - 2](./Teste%20de%20Performance%20-%202.ipynb) | Segundo teste de performance: strings e entrada do usuário — textos multilinha, f-strings, concatenação, repetição de caracteres, métodos de string, `input`, `len`, conversões numéricas e formatação de saída (16 exercícios). |
| [Teste de Performance - 3](./Teste%20de%20Performance%20-%203.ipynb) | Terceiro teste de performance / avaliação integrada: estruturas de decisão e repetição, listas, módulos `math` e `random`, validações e projetos aplicados (16 exercícios — mesmo conteúdo do Assessment). |
| [Assessment](./Assessment.ipynb) | Avaliação final da disciplina: consolida condicionais, laços, listas, simulação Monte Carlo, validação de CPF, juros compostos e mini-jogo em grade no terminal (16 exercícios). |

---

## Resumo geral — funções e conceitos da disciplina

Síntese do que aparece nos notebooks acima, útil como “cola” da disciplina.

### Saída, entrada e tipos

| Recurso | Uso na disciplina |
|---------|-------------------|
| `print()` | Exibir mensagens, variáveis e resultados formatados no terminal. |
| `input()` | Ler texto digitado pelo usuário; costuma ser convertido com `int()` ou `float()`. |
| `type()` | Identificar o tipo de um valor (`int`, `float`, `bool`, `str`, etc.). |
| `int()`, `float()`, `str()` | Converter entre tipos numéricos e texto. |
| `bool` (`True` / `False`) | Representar estados lógicos (ex.: sensor ativo/inativo). |

### Operadores aritméticos e lógicos

| Operador | Significado |
|----------|-------------|
| `+`, `-`, `*`, `/` | Soma, subtração, multiplicação e divisão. |
| `//` | Divisão inteira (ex.: sacas no caminhão, horas completas). |
| `%` | Resto da divisão (ex.: dia no ciclo, minutos excedentes). |
| `in` | Verificar se um caractere ou substring está presente (ex.: `@` na senha). |
| `and`, `or`, `not` | Combinar condições em estruturas de decisão. |

### Funções built-in frequentes

| Função | Uso na disciplina |
|--------|-------------------|
| `len()` | Tamanho de strings e listas (ex.: limite de SMS). |
| `round()` | Arredondar decimais (porcentagens, valores monetários, horas). |
| `sum()` | Somar elementos de uma lista (ex.: transações). |
| `range()` | Gerar sequências para laços `for`. |
| `list()`, `map()` | Criar e transformar listas a partir de entradas. |

### Métodos de `str`

| Método | Uso na disciplina |
|--------|-------------------|
| `.upper()` | Nome completo em maiúsculas (cadastro/RH). |
| `.lower()` | Normalização de texto. |
| `.capitalize()` | Primeira letra maiúscula (nome no crachá). |
| `.swapcase()` | Inverter maiúsculas/minúsculas da mensagem. |
| `.count()` | Contar ocorrências (hashtags, vogais). |
| `.islower()`, `.isupper()` | Verificar composição da senha. |
| `.isdigit()` | Validar se o CPF contém apenas dígitos. |
| `.split()` | Separar tokens de uma linha de entrada. |

### Strings e formatação

- **Literais** com aspas simples/duplas e **strings multilinha** (`'''...'''`) para cabeçalhos de módulo.
- **Concatenação** (`+`) e **repetição** (`caractere * n`) para SKUs, separadores e cartões ASCII.
- **f-strings** (`f"..."`) para mensagens dinâmicas, logs e relatórios de estoque/financeiro.

### Estruturas de controle

| Estrutura | Uso na disciplina |
|-----------|-------------------|
| `if` / `elif` / `else` | Decisões (triagem, validações, regras de jogo). |
| `while` | Repetir até condição (fatorial, pesagem, arrecadação, movimento no mapa). |
| `for` | Percorrer `range`, listas e matrizes lógicas (padrões numéricos, velocidades). |

### Listas e coleções

- **Listas** `[]` para posições, transações, velocidades e mapas.
- `.append()` para ir montando resultados em laços.
- Indexação e fatiamento (`lista[i]`, coordenadas `[x, y]`).

### Módulos importados

| Módulo | Recursos usados |
|--------|-----------------|
| `math` | `sin`, `ceil`, `sqrt` — geometria, simulações e cálculos. |
| `random` | Geração de pontos aleatórios (Monte Carlo). |
| `IPython.display` | `clear_output` — atualizar o mapa do jogo no notebook. |

### Fluxo de programação (conceitos transversais)

1. **Comentários** (`#`) — documentar código e contexto de negócio.
2. **Fluxo IPO** — Entrada (dados/variáveis) → Processamento (cálculos) → Saída (`print`).
3. **Variáveis** — armazenar e reatribuir valores ao longo do programa.
4. **Precedência** — parênteses para ordem correta em expressões (tributos, juros).
5. **Decomposição de problemas** — dividir tarefas em etapas menores.

### Tabela rápida por notebook

| Notebook | Foco principal |
|----------|----------------|
| TP1 | Sintaxe básica, tipos, operadores e aritmética |
| TP2 | Strings, `input` e formatação de texto |
| TP3 / Assessment | Condicionais, laços, listas e bibliotecas |
