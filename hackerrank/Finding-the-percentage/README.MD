# Finding the Percentage

Resolução do desafio **Finding the Percentage**, disponível na plataforma HackerRank.

## 📖 Descrição

Neste desafio, é necessário armazenar as notas de vários alunos utilizando um **dicionário (dictionary)**.

Após cadastrar todos os alunos e suas respectivas notas, o programa recebe o nome de um aluno e deve calcular a **média das suas notas**, exibindo o resultado com exatamente **duas casas decimais**.

### Exemplo

Entrada:

```text
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
```

Saída:

```text
56.00
```

Explicação:

O aluno consultado foi **Malika**, cujas notas são:

```text
[52, 56, 60]
```

A média é:

```text
(52 + 56 + 60) / 3 = 56.00
```

---

## 🧠 Conceitos praticados

Durante a resolução deste exercício foram utilizados diversos conceitos importantes da linguagem Python:

- Dicionários (`dict`)
- Listas (`list`)
- Estruturas de repetição (`for`)
- Desempacotamento de listas (`*line`)
- Conversão de tipos (`float`)
- Função `map()`
- Função `sum()`
- Função `len()`
- Acesso a valores por chave em um dicionário
- Formatação de números com duas casas decimais

---

## 💡 Estratégia utilizada

A solução foi dividida em etapas:

1. Ler a quantidade de alunos.
2. Criar um dicionário para armazenar os alunos e suas notas.
3. Ler o nome e as notas de cada aluno.
4. Converter as notas para `float`.
5. Armazenar os dados no dicionário utilizando o nome como chave.
6. Ler o nome do aluno desejado.
7. Recuperar a lista de notas correspondente.
8. Calcular a média.
9. Exibir o resultado com duas casas decimais.

---

## 💻 Código

```python
n = int(input())
student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()

scores = student_marks[query_name]
average = sum(scores) / len(scores)

print(f"{average:.2f}")
```

---

## ⏱ Complexidade

### Tempo

- Leitura dos dados: **O(n)**
- Busca no dicionário: **O(1)**
- Cálculo da média: **O(m)**

Onde:

- **n** = quantidade de alunos
- **m** = quantidade de notas do aluno consultado

Complexidade total:

```text
O(n + m)
```

---

### Espaço

O dicionário armazena todas as notas dos alunos.

```text
O(n)
```

---

## 📚 O que aprendi

Este exercício reforçou conceitos importantes para o desenvolvimento em Python:

- Como utilizar **dicionários** para relacionar chaves e valores.
- Como armazenar listas dentro de um dicionário.
- Como recuperar dados utilizando uma chave.
- Como utilizar funções nativas como `sum()` e `len()`.
- Como formatar valores numéricos para exibição.
- A importância de interpretar corretamente o enunciado antes de implementar a solução.

---

## 🚀 Tecnologias utilizadas

- Python 3

---

## 🔗 Plataforma

- **HackerRank**
- Trilha: **Python → Basic Data Types**
- Exercício: **Finding the Percentage**