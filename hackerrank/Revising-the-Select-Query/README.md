# Revising the Select Query I

## 📖 Descrição

Solução do desafio **Revising the Select Query I** da plataforma HackerRank.

O objetivo é selecionar todas as colunas da tabela `CITY` para as cidades dos Estados Unidos (`USA`) cuja população seja maior que **100000** habitantes.

---

## 🛠️ Conceitos praticados

- `SELECT`
- `FROM`
- `WHERE`
- Operador de comparação (`>`)
- Filtragem de dados
- Consulta em tabelas

---

## 💻 Solução

```sql
SELECT *
FROM CITY
WHERE COUNTRYCODE = 'USA'
  AND POPULATION > 100000;
```

---

## 🧠 O que aprendi

Durante este exercício pratiquei:

- Como selecionar todas as colunas de uma tabela utilizando `SELECT *`.
- Como filtrar registros usando a cláusula `WHERE`.
- Como combinar múltiplas condições com `AND`.
- Que valores do tipo texto devem ser escritos entre aspas simples (`'USA'`).
- Como consultar apenas os dados que atendem aos critérios desejados.

---

## 📚 Plataforma

- HackerRank
- Trilha: SQL
- Dificuldade: Easy