# Swap Case

## 📖 Descrição

Este desafio faz parte da trilha de **Python** do HackerRank.

O objetivo é receber uma string e inverter o formato de cada letra:

- Letras minúsculas devem ser convertidas para maiúsculas.
- Letras maiúsculas devem ser convertidas para minúsculas.
- Caracteres que não são letras (espaços, números, pontuação, etc.) devem permanecer inalterados.

---

## 📝 Enunciado

Dada uma string, altere o caso de todos os caracteres alfabéticos.

Exemplos:

- `a` → `A`
- `A` → `a`

A função deve retornar uma nova string contendo todas as letras com o caso invertido.

---

## 💡 Exemplo

### Entrada

```text
HackerRank.com presents "Pythonist 2".
```

### Saída

```text
hACKERrANK.COM PRESENTS "pYTHONIST 2".
```

---

## 🛠️ Conceitos praticados

Durante a resolução deste exercício foram praticados os seguintes conceitos:

- Criação de funções
- Iteração sobre strings com `for`
- Estruturas condicionais (`if` e `elif`)
- Métodos de strings:
  - `lower()`
  - `upper()`
  - `join()`
- Manipulação de listas
- Construção de uma nova string

---

## 🚀 Estratégia utilizada

Como strings são imutáveis em Python, a solução consiste em criar uma nova lista para armazenar cada caractere convertido.

Para cada caractere da string:

1. Verificar se ele está em letra minúscula.
2. Caso esteja, convertê-lo para maiúscula.
3. Caso contrário, convertê-lo para minúscula.
4. Adicionar o caractere convertido em uma nova lista.
5. Ao final, utilizar o método `join()` para unir todos os caracteres em uma única string.

---

## 📈 Complexidade

- **Complexidade de tempo:** `O(n)`
- **Complexidade de espaço:** `O(n)`

Onde **n** representa a quantidade de caracteres da string.

---

## 📚 Plataforma

- Plataforma: HackerRank
- Linguagem: Python 3
- Categoria: Strings
- Desafio: Swap Case

---

## 🎯 Aprendizados

Durante a resolução deste desafio aprendi:

- Como identificar se um caractere está em maiúsculo ou minúsculo utilizando `lower()` e `upper()`.
- Que strings em Python são imutáveis, sendo necessário criar uma nova estrutura para armazenar o resultado.
- Como utilizar o método `join()` para transformar uma lista de caracteres em uma única string.
- A importância de desenvolver a lógica da solução antes de pesquisar métodos específicos da linguagem.