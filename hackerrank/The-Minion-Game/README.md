# The Minion Game - HackerRank

## Descrição

Solução do desafio **The Minion Game** do HackerRank utilizando Python.

O desafio apresenta dois jogadores:

- Kevin → pontua com substrings iniciadas por vogais.
- Stuart → pontua com substrings iniciadas por consoantes.

Dada uma palavra, é necessário calcular a pontuação total de cada jogador e determinar o vencedor.

---

## O que tornou esse exercício difícil

A dificuldade principal não está na sintaxe do Python.

O desafio foi entender a regra matemática escondida por trás do problema.

Minha primeira interpretação foi que seria necessário gerar todas as substrings possíveis e depois contar quantas vezes cada uma aparecia.

Após estudar o problema com mais calma, percebi que a pontuação pode ser calculada sem gerar as substrings.

---

## Insight principal

Para qualquer posição da palavra:

```python
pontos = len(string) - indice
```

Essa expressão representa quantas substrings podem ser criadas começando naquela posição.

Exemplo:

```text
BANANA
```

Tamanho da palavra:

```text
6
```

### Stuart (Consoantes)

```text
B -> índice 0 -> 6 - 0 = 6
N -> índice 2 -> 6 - 2 = 4
N -> índice 4 -> 6 - 4 = 2

Total = 12
```

### Kevin (Vogais)

```text
A -> índice 1 -> 6 - 1 = 5
A -> índice 3 -> 6 - 3 = 3
A -> índice 5 -> 6 - 5 = 1

Total = 9
```

Resultado:

```text
Stuart 12
```

---

## Conceitos praticados

- Loops (`for`)
- `enumerate()`
- Strings
- Condicionais (`if/else`)
- Acumulação de valores
- Estruturas de dados
- Raciocínio matemático aplicado a algoritmos
- Leitura e interpretação de problemas

---

## Maior aprendizado

Esse exercício me mostrou que muitos problemas não são resolvidos pela força bruta.

A solução aparece quando encontramos uma forma de generalizar o padrão matemático do problema.

Ao invés de gerar todas as substrings possíveis, basta calcular quantas substrings cada posição consegue produzir.

Foi um dos primeiros exercícios em que precisei procurar a regra por trás do problema, e não apenas escrever código.

---

## Tecnologias

- Python 3
- HackerRank