# Matemática para Inteligência Artificial e Ciência de Dados — Álgebra Linear

## Descrição da disciplina

<!-- Preencha com sua visão geral da matéria: objetivos, carga horária, professor(a), turma, links da INFNET/Deepnote, etc. -->

_A descrição desta disciplina será preenchida aqui._

---

## Aulas

| Aula | Conteúdo da aula |
|------|------------------|
| 01 | Definição e cálculo de autovalores e autovetores (equação característica); interpretação geométrica; aplicações (recomendação, reconhecimento facial, compressão/SVD); PCA; PageRank com matriz Google e damping factor; introdução à filtragem colaborativa (SVD). |

---

## Resumo das aulas

### Aula 01

**Retomada:** revisão das duas aulas anteriores sobre transformações de matriz, transformações lineares (visão geométrica e aplicação em dados/computação gráfica) e determinantes.

**Conceitos centrais**

- **Autovalor e autovetor:** dado um operador linear \(T\), busca-se \(\lambda\) e \(\mathbf{v} \neq \mathbf{0}\) tais que \(T\mathbf{v} = \lambda\mathbf{v}\). Geometricamente, a transformação mantém a direção do autovetor (escala, contração, inversão ou identidade conforme \(\lambda\)).
- **Cálculo em duas etapas:** (1) resolver a equação característica \(\det(A - \lambda I) = 0\); (2) substituir cada \(\lambda\) e resolver o sistema linear homogêneo para obter os autovetores associados.
- **Espaços vetoriais:** noção intuitiva (plano cartesiano, \(\mathbb{R}^2\), \(\mathbb{R}^3\), bases canônicas); formalização deixada para depois.

**Aplicações motivacionais**

- **Redes sociais / recomendação:** perfil de comportamento do usuário como autovetor associado ao padrão de uso.
- **Reconhecimento facial:** rosto projetado em uma base de características (distâncias, proporções); comparação por coeficientes/autovetores, não pixel a pixel.
- **Compressão (SVD):** truncamento descartando autovalores/autovetores menores (imagens, MP3); analogia com limites de percepção humana (visão RGB, audição).

**PCA (Análise de Componentes Principais)**

- Redução de dimensionalidade: criar novas colunas como combinações lineares dos dados (ex.: 100 → 2), não apenas escolher colunas existentes.
- Autovetores da **matriz de covariância** = direções de máxima variância; autovalores = quantidade de informação em cada direção.
- Exemplo prático em **NumPy/Matplotlib**: dados simulados, autovalores/autovetores, visualização das direções principais e projeção.
- Desafio de interpretação: componentes são combinações abstratas dos atributos originais.

**PageRank**

- Página importante se páginas importantes apontam para ela; simulação de navegação aleatória converge ao **autovetor principal** (autovalor dominante ≈ 1) da matriz de transição.
- Implementação em Python: matriz de adjacência → matriz estocástica → **matriz Google** com **damping factor** (tipicamente 0,85) para evitar “becos sem saída”.
- Cálculo via `numpy.linalg.eig`; normalização do autovetor (soma = 1, valores positivos); ranking das páginas A, B, C, D.

**Filtragem colaborativa (introdução)**

- Netflix/Spotify usam decomposição em valores singulares (**SVD**), ligada a autovalores/autovetores.
- Matriz usuário × item: autovetores agrupam perfis similares (“perfis psicológicos digitais”) para recomendar conteúdo.
- **Próxima aula:** exemplo prático de filtragem colaborativa com matriz de avaliações.
