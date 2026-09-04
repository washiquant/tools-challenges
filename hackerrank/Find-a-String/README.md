# Find a String

## Descrição

Este desafio consiste em contar quantas vezes uma substring aparece dentro de uma string.

Diferentemente de uma busca simples, ocorrências sobrepostas também devem ser consideradas.

**Plataforma:** HackerRank  
**Dificuldade:** Fácil  
**Categoria:** Strings

---

## Problema

Dada uma string e uma substring, determine quantas vezes a substring aparece na string principal.

### Exemplo

**Entrada**

```text
ABCDCDC
CDC
```

**Saída**

```text
2
```

### Explicação

A substring `CDC` aparece duas vezes na string:

```text
ABCDCDC
  ^^^

ABCDCDC
    ^^^
```

---

## Estratégia Utilizada

A solução utiliza o conceito de **janela deslizante (Sliding Window)**.

A ideia é percorrer a string principal e, para cada posição possível, extrair um trecho com o mesmo tamanho da substring.

Em seguida:

1. Recorta uma parte da string utilizando fatiamento (*slicing*).
2. Compara o trecho extraído com a substring.
3. Caso sejam iguais, registra uma ocorrência.
4. Ao final, retorna a quantidade total de ocorrências encontradas.

---

## Implementação

```python
def count_substring(string, sub_string):
    count = 0

    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1

    return count
```

---

## Conceitos Praticados

- Estruturas de repetição (`for`)
- Função `range()`
- Manipulação de strings
- Fatiamento de strings (*string slicing*)
- Comparação de strings
- Janela deslizante (*Sliding Window*)
- Contagem de ocorrências

---

## Complexidade

### Complexidade de Tempo

```text
O(n × m)
```

Onde:

- `n` representa o tamanho da string principal.
- `m` representa o tamanho da substring.

Cada comparação pode analisar até `m` caracteres.

### Complexidade de Espaço

```text
O(1)
```

A solução utiliza apenas uma variável contadora.

---

## Aprendizados

Durante a resolução deste desafio foram praticados os seguintes conceitos:

- Percorrer strings utilizando índices.
- Utilizar fatiamento para extrair partes de uma string.
- Compreender o funcionamento da função `range()`.
- Aplicar o padrão de janela deslizante para busca de padrões.
- Identificar e contar ocorrências sobrepostas em uma string.

---

## Autor

**Washington Willian Roncador Moreira**

- GitHub: https://github.com/washiquant
- LinkedIn: https://www.linkedin.com/in/washington-willian-roncador-moreira-04a0662b9/