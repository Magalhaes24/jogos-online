# 05 — Navegação e modo aleatório

O EPUB não corre código. Toda a "interactividade" é feita com **hiperligações internas**,
que o X4 suporta nativamente. É suficiente.

---

## O menu de entrada

Primeira página depois da capa:

```
────────────────────
  🎲 ESCOLHE O TEU
     DESAFIO
────────────────────

  TENHO...

  → 5 MINUTOS
  → 10 MINUTOS
  → 30 MINUTOS

  QUERO...

  → 🧠 Pensar
  → 🔢 Fazer contas
  → 🕵️ Resolver um mistério
  → 🌀 Algo estranho
  → 💻 Programar
  → 😈 Ser enganado

  → 📖 Índice completo
  → ☀️ Desafio do dia
────────────────────
```

### Mapeamento tempo → problemas

| Escolha | Dificuldades | Categorias favorecidas |
|---|---|---|
| 5 minutos | ⭐, ⭐⭐ | ENI, LAT, PRG |
| 10 minutos | ⭐⭐, ⭐⭐⭐ | todas |
| 30 minutos | ⭐⭐⭐⭐, ⭐⭐⭐⭐⭐ | LOG, MAT, PRB, WWY |

### Mapeamento disposição → categorias

| Escolha | Categorias |
|---|---|
| 🧠 Pensar | LOG |
| 🔢 Fazer contas | MAT, PRB |
| 🕵️ Resolver um mistério | ENI |
| 🌀 Algo estranho | LAT |
| 💻 Programar | PRG |
| 😈 Ser enganado | tudo com `trap: true` |
| (sem símbolo) | DIL, WWY — acessíveis pelo índice |

---

## As listas de salto

Cada opção do menu leva a uma página com 15 a 25 ligações, **em ordem baralhada
mas fixa** (a semente é guardada no build, para o mesmo EPUB dar sempre a mesma ordem):

```
  ⏱️ 5 MINUTOS

  ENI-003 · O vidro partido        ★★
  LAT-011 · O elevador             ★★★
  PRG-002 · A lista que cresce     ★★
  ...
```

O leitor escolhe pelo título e pelas estrelas. O título nunca revela nada
(ver [`03`](03-dificuldade-e-metadados.md)).

---

## O modo verdadeiramente aleatório

O EPUB não tem gerador de números aleatórios. A solução é física:

> **Abre o livro numa página ao acaso e avança até encontrares um cabeçalho de problema.**

Para tornar isto fiável, o gerador garante que **nenhum problema ocupa mais de 9 páginas**
e que todos os cabeçalhos são visualmente idênticos. Abrir ao calhar cai sempre a menos
de 9 páginas de um problema novo.

Alternativa determinística — a **tabela dos dados**:

```
  🎲 LANÇA DOIS DADOS

   2 → LOG-007      8 → PRB-012
   3 → ENI-019      9 → LAT-004
   4 → MAT-022     10 → DIL-006
   ...
```

Uma tabela por secção do livro. Custa nada e funciona bem.

---

## ☀️ Desafio do dia

O EPUB não sabe que dia é. Portanto não se finge que sabe.

**Modelo adoptado:** uma sequência numerada de 1 a 200, independente do índice temático.

```
  ☀️ DESAFIO DO DIA

  Não sei que dia é hoje.
  Tu sabes.

  Vai ao desafio número N,
  onde N é o dia do ano.

  (1 de Janeiro = 1,
   31 de Dezembro = 365)

  → Tabela de desafios
```

A tabela mapeia 1–365 para os 200 problemas (com repetição controlada: os 165 dias
extra reutilizam os problemas com `aha_factor >= 4`, que aguentam ser revisitados).

Cada entrada mostra só o número, a dificuldade e o tempo — **nunca o título**, para
não haver escolha:

```
  247   ★★★★   10 min   → p. 412
```

---

## Índice completo

Três índices no fim do livro:

1. **Por ID** — `LOG-001` … `PRG-015`
2. **Por dificuldade** — cinco listas
3. **Por conceito** — `Bayes`, `princípio do pombal`, `invariantes`, `paridade`, …

O terceiro é o mais valioso e o mais barato de gerar: sai directamente do campo
`concept` do JSON, e transforma o livro numa referência de técnicas.
