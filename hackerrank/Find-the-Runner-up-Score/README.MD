# Find the Runner-Up Score

Resolução do desafio **Find the Runner-Up Score**, disponível na plataforma HackerRank.

## 📖 Descrição

Durante um evento esportivo universitário, é fornecida uma lista contendo as pontuações dos participantes.

O objetivo é encontrar a **segunda maior pontuação distinta** (Runner-Up Score).

### Exemplo

Entrada:

```text
5
2 3 6 6 5
```

Saída:

```text
5
```

Explicação:

As pontuações são:

```text
[2, 3, 6, 6, 5]
```

O maior valor é **6**.

Como o desafio pede a **segunda maior pontuação distinta**, ignoramos os valores repetidos e obtemos:

```text
[2, 3, 5, 6]
```

Assim, a resposta correta é:

```text
5
```

---

## 🧠 Conceitos praticados

Este exercício permite praticar diversos conceitos fundamentais da linguagem Python:

- Leitura de entrada (`input()`)
- Conversão de tipos (`int`)
- `map()`
- `split()`
- Estrutura de dados `set`
- Ordenação com `sorted()`
- Indexação de listas
- Manipulação de coleções

---

## 💡 Estratégia utilizada

A solução segue os seguintes passos:

1. Ler a quantidade de elementos da lista.
2. Ler todas as pontuações.
3. Remover valores repetidos utilizando um `set`.
4. Ordenar os valores em ordem decrescente.
5. Retornar o segundo elemento da lista ordenada.

---

## 💻 Código

```python
if __name__ == "__main__":
    n = int(input())
    arr = sorted(set(map(int, input().split())), reverse=True)
    print(arr[1])
```

---

## ⏱ Complexidade

### Tempo

- Conversão para `set`: **O(n)**
- Ordenação: **O(n log n)**

Complexidade total:

```text
O(n log n)
```

### Espaço

O algoritmo utiliza memória adicional para armazenar o conjunto e a lista ordenada.

```text
O(n)
```

---

## 📚 O que aprendi

Durante a resolução deste exercício foi possível reforçar os seguintes conceitos:

- Diferença entre `list` e `set`.
- Como remover elementos duplicados de forma simples.
- Diferença entre o maior elemento e o maior elemento **distinto**.
- Utilização da função `sorted()` com o parâmetro `reverse=True`.
- Importância de interpretar corretamente o enunciado antes de implementar a solução.

---

## 🔗 Plataforma

- HackerRank
- Trilha: **Python → Basic Data Types**
- Exercício: **Find the Runner-Up Score**