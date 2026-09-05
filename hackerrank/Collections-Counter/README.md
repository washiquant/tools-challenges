# Collections Counter (HackerRank)

## 📖 Sobre o Exercício

Este desafio do HackerRank simula o controle de estoque de uma loja de calçados.

Raghu possui uma quantidade limitada de sapatos, identificados pelos seus tamanhos. Clientes chegam à loja procurando um determinado tamanho e oferecendo um valor específico pelo produto. Caso o tamanho desejado esteja disponível no estoque, a venda é realizada e o valor é somado ao faturamento da loja. Após a venda, o sapato é removido do estoque e não pode ser vendido novamente.

O objetivo é calcular o faturamento total obtido após atender todos os clientes.

---

## 🎯 Objetivo

Desenvolver uma solução capaz de:

- Ler o estoque inicial da loja;
- Processar cada cliente individualmente;
- Verificar a disponibilidade do tamanho solicitado;
- Atualizar o faturamento da loja;
- Remover o item vendido do estoque;
- Exibir o valor total arrecadado.

---

## 🧠 Conceitos Utilizados

Durante a resolução deste exercício foram praticados diversos conceitos fundamentais da linguagem Python:

- Funções
- Entrada e saída de dados
- Conversão de tipos
- Estruturas condicionais (`if`)
- Estruturas de repetição (`for`)
- Manipulação de listas
- Método `split()`
- Função `map()`
- Operador `in`
- Método `remove()`
- Processamento de dados em tempo real

---

## 📥 Formato da Entrada

A entrada segue a seguinte estrutura:

1. Quantidade de sapatos disponíveis na loja.
2. Lista contendo os tamanhos dos sapatos disponíveis.
3. Quantidade de clientes.
4. Para cada cliente:
   - Tamanho desejado;
   - Valor que o cliente está disposto a pagar.

### Exemplo

```text
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
18 50
```

---

## 📤 Saída

O programa deve exibir apenas o valor total arrecadado pela loja.

### Exemplo

```text
200
```

---

## 🔍 Lógica da Solução

A estratégia utilizada consiste em processar cada cliente no momento em que sua informação é recebida.

Para cada cliente:

1. Ler o tamanho desejado e o valor oferecido.
2. Verificar se o tamanho existe no estoque.
3. Caso exista:
   - Somar o valor ao faturamento.
   - Remover o sapato vendido da lista de estoque.
4. Caso não exista:
   - Ignorar a venda.

Dessa forma, não é necessário armazenar todos os clientes na memória, tornando a solução mais simples e eficiente.

---

## 💻 Implementação

```python
def faturamento_loja():
    lucro = 0

    quantidade_de_sapatos = int(input())

    tamanhos_dos_sapatos = list(map(int, input().split()))

    clientes = int(input())

    for _ in range(clientes):
        size, price = map(int, input().split())

        if size in tamanhos_dos_sapatos:
            lucro += price
            tamanhos_dos_sapatos.remove(size)

    return lucro


print(faturamento_loja())
```

---

## 📊 Complexidade

### Complexidade de Tempo

As operações:

```python
size in tamanhos_dos_sapatos
```

e

```python
tamanhos_dos_sapatos.remove(size)
```

possuem complexidade O(n).

Portanto, a complexidade total da solução é aproximadamente:

```text
O(clientes × estoque)
```

Para os limites propostos pelo HackerRank, essa abordagem é totalmente adequada.

---

## 🚀 Aprendizados

Este exercício foi importante para reforçar conceitos como:

- Processamento de entradas estruturadas;
- Manipulação de listas;
- Controle de estoque utilizando estruturas simples;
- Tomada de decisão baseada em condições;
- Construção de algoritmos orientados a eventos;
- Raciocínio sobre estados mutáveis em Python.

Além disso, o desafio demonstra que nem sempre é necessário armazenar todos os dados antes de processá-los. Em muitos casos, é possível tratar cada informação à medida que ela é recebida, simplificando a implementação e reduzindo o consumo de memória.

---

**Plataforma:** HackerRank  
**Trilha:** Python  
**Categoria:** Collections  
**Desafio:** Collections.Counter()