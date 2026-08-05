# Tuples - HackerRank

## 📌 Objetivo

Neste exercício, o objetivo era ler uma sequência de números inteiros, criar uma **tupla** com esses valores e imprimir o resultado da função `hash()` aplicada sobre ela.

---

## 🧠 Conceitos praticados

- Entrada de dados com `input()`
- Conversão de tipos utilizando `map()`
- Separação de strings com `split()`
- Criação de tuplas com `tuple()`
- Utilização da função nativa `hash()`

---

## 💻 Lógica utilizada

1. Ler a quantidade de elementos da entrada.
2. Ler a sequência de números separados por espaço.
3. Converter todos os valores para inteiros.
4. Transformar a sequência em uma tupla.
5. Aplicar a função `hash()` sobre a tupla.
6. Imprimir o resultado.

---

## 📚 O que aprendi

Durante este exercício compreendi melhor a diferença entre **listas** e **tuplas**.

Aprendi que:

- Tuplas são estruturas **imutáveis**.
- Objetos imutáveis podem ser utilizados com a função `hash()`.
- A função `map()` retorna um iterador, que pode ser convertido em uma tupla utilizando `tuple()`.
- Nem sempre é necessário utilizar estruturas de repetição (`for` ou `while`), pois muitas funções nativas do Python já realizam esse trabalho de forma eficiente.

Também compreendi melhor o fluxo dos dados:

```
input()
      ↓
string
      ↓
split()
      ↓
sequência de strings
      ↓
map(int)
      ↓
inteiros
      ↓
tuple()
      ↓
hash()
      ↓
print()
```

---

## ⚠️ Dificuldades encontradas

A maior dificuldade foi entender o propósito da função `hash()`, já que o exercício não explica seu funcionamento.

Durante a resolução também encontrei diferenças entre versões do Python (Python 2, Python 3 e PyPy), o que gerou resultados diferentes para o mesmo teste no ambiente do HackerRank.

Isso me mostrou que nem sempre um erro está relacionado à lógica do código; às vezes o ambiente de execução também precisa ser investigado.

---

## 🚀 Resultado

Exercício utilizado para praticar manipulação de tuplas, funções nativas do Python e reforçar o entendimento sobre estruturas de dados imutáveis.