# HackerRank — Lists em Python

Este projeto contém a resolução do exercício **Lists**, da trilha **Python > Basic Data Types** do HackerRank.

O objetivo do desafio é criar uma lista vazia e executar uma sequência de comandos recebidos pela entrada padrão.

## Objetivo

O programa começa com uma lista vazia:

```python
lista = []
```

A primeira linha da entrada informa a quantidade de comandos que serão executados. Em seguida, cada nova linha contém um comando e, quando necessário, seus argumentos.

## Comandos disponíveis

| Comando | Descrição |
|---|---|
| `insert i e` | Insere o inteiro `e` na posição `i`. |
| `print` | Exibe a lista atual. |
| `remove e` | Remove a primeira ocorrência do inteiro `e`. |
| `append e` | Adiciona o inteiro `e` ao final da lista. |
| `sort` | Ordena a lista em ordem crescente. |
| `pop` | Remove o último elemento da lista. |
| `reverse` | Inverte a ordem dos elementos da lista. |

## Exemplo

### Entrada

```text
4
append 1
append 2
insert 1 3
print
```

### Processamento

1. `append 1` → `[1]`
2. `append 2` → `[1, 2]`
3. `insert 1 3` → `[1, 3, 2]`
4. `print` → exibe a lista

### Saída

```text
[1, 3, 2]
```

## Lógica utilizada

A solução segue este fluxo:

1. Ler a quantidade de comandos com `input()`.
2. Converter essa quantidade para inteiro.
3. Repetir a leitura de comandos usando um laço `for`.
4. Separar cada comando e seus argumentos com `split()`.
5. Identificar a ação pelo primeiro elemento da linha.
6. Converter apenas os argumentos numéricos para `int`.
7. Executar o método correspondente na lista.

## Conceitos praticados

- Entrada de dados com `input()`
- Conversão de tipos com `int()`
- Estruturas de repetição com `for` e `range()`
- Condicionais com `if`
- Separação de strings com `split()`
- Acesso a elementos por índice
- Manipulação de listas em Python
- Interpretação de comandos recebidos pela entrada padrão

## Como executar

No terminal, execute:

```bash
python main.py
```

Depois, informe a quantidade de comandos e cada comando em uma linha diferente.

## Aprendizado principal

A primeira chamada de `input()` lê somente a quantidade de comandos. As chamadas seguintes, realizadas dentro do laço, leem um comando por vez.

Cada linha deve ser analisada nesta ordem:

```text
Ler a linha → separar as partes → identificar a ação → converter os argumentos → executar
```

Essa organização evita tentar converter comandos sem argumentos, como `print`, `sort`, `pop` e `reverse`.

## Plataforma

Exercício disponível no HackerRank:

**Python Lists — Basic Data Types**
