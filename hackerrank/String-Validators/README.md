# String Validators - HackerRank

## 📖 Sobre o Projeto

Solução do desafio **String Validators** da plataforma HackerRank utilizando Python.

O objetivo do exercício é analisar uma string informada pelo usuário e verificar se ela contém:

- Caracteres alfanuméricos
- Caracteres alfabéticos
- Dígitos
- Letras minúsculas
- Letras maiúsculas

Para cada validação, o programa deve imprimir `True` ou `False`.

---

## 🎯 Conceitos Praticados

Durante a resolução deste desafio foram utilizados conceitos fundamentais de Python:

- Manipulação de Strings
- Laços de Repetição (`for`)
- Funções Built-in
- Generator Expressions
- Métodos de String
- Lógica de Programação
- Interpretação de Requisitos

---

## 🛠️ Tecnologias Utilizadas

- Python 3

---

## 📚 Métodos Utilizados

| Método | Descrição |
|----------|------------|
| `isalnum()` | Verifica se o caractere é alfanumérico |
| `isalpha()` | Verifica se o caractere é uma letra |
| `isdigit()` | Verifica se o caractere é um número |
| `islower()` | Verifica se o caractere está em minúsculo |
| `isupper()` | Verifica se o caractere está em maiúsculo |
| `any()` | Retorna `True` se pelo menos um elemento for verdadeiro |

---

## 💻 Solução

```python
s = input()

print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))
```

---

## 🔍 Aprendizado Obtido

O principal aprendizado deste desafio foi compreender a diferença entre:

- Validar a string inteira;
- Validar cada caractere individualmente.

Inicialmente a tentativa foi aplicar métodos como `isalnum()` diretamente sobre a string completa. Porém, o desafio exigia verificar se existia **ao menos um caractere** que atendesse cada condição.

A solução correta foi percorrer cada caractere da string utilizando uma *generator expression* em conjunto com a função `any()`.

Exemplo:

```python
any(c.isdigit() for c in s)
```

Isso significa:

> "Existe pelo menos um caractere em `s` que seja um dígito?"

---

## 🚀 Autor

**Washington Moreira**

- Estudante de Análise e Desenvolvimento de Sistemas
- Focado em Back-end com Python
- Desenvolvendo projetos e resolvendo desafios para fortalecer fundamentos de programação

GitHub: https://github.com/washiquant