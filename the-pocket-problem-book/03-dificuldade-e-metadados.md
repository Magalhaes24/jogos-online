# 03 — Dificuldade e metadados

## Os 5 níveis

| Nível | Nome | Tempo | Significado operacional |
|---|---|---|---|
| ⭐ | Aquecimento | < 2 min | Resolve-se de cabeça, sem escrever nada |
| ⭐⭐ | Fácil | 2–5 min | Uma ideia só; a maioria das pessoas chega lá |
| ⭐⭐⭐ | Médio | 5–10 min | Duas ideias, ou uma ideia + trabalho |
| ⭐⭐⭐⭐ | Difícil | 10–20 min | Precisa de papel, ou de abandonar um pressuposto |
| ⭐⭐⭐⭐⭐ | Monstro | 20+ min | Precisa de método, não de inspiração |

**Como calibrar (regra prática):** o nível é o tempo que uma pessoa *que já resolveu
problemas deste tipo* demora, multiplicado por 2. Não é o tempo de um especialista.

**Distribuição alvo no Volume I:**

| Nível | % | Nº aprox. |
|---|---|---|
| ⭐ | 10% | 20 |
| ⭐⭐ | 25% | 50 |
| ⭐⭐⭐ | 35% | 70 |
| ⭐⭐⭐⭐ | 20% | 40 |
| ⭐⭐⭐⭐⭐ | 10% | 20 |

Um livro com demasiados ⭐⭐⭐⭐ deixa de ser de bolso — passa a ser trabalho.

---

## Sistema de IDs

```
LOG-034
│   │
│   └── número sequencial dentro da categoria, 3 dígitos, nunca reutilizado
└────── prefixo da categoria (LOG ENI MAT PRB LAT DIL WWY PRG)
```

Regras:

- O ID é **permanente**. Se um problema for retirado, o número morre com ele.
- O ID é independente da posição no livro. O EPUB pode reordenar; o ID não muda.
- Volumes futuros continuam a mesma numeração (não há `LOG-034-v2`).

---

## O cartão de metadados

Aparece **antes** do enunciado, para o leitor escolher pelo tempo disponível:

```
────────────────────
     LOG-034
   AS TRÊS CAIXAS
     ★★★☆☆
     5–10 MIN
────────────────────
```

E, **depois** da solução, o cartão completo:

```
Difficulty:   3/5
Time:         5–10 min
Brain:        Lógica / Dedução
Frustration:  😈😈
"Aha!":       ★★★★☆
```

### Frustration (😈, 0 a 5)
Quão desagradável é falhar. Alto = o problema faz-te sentir estúpido.
Monty Hall tem 😈😈😈😈. Uma sequência numérica tem 😈.

### "Aha!" factor (★, 0 a 5)
Quão boa é a sensação de perceber. Alto = a solução é simultaneamente surpreendente
e óbvia em retrospectiva.

**Estes dois campos são editoriais, não calculados.** São a única parte subjectiva
do sistema — e são também o principal sinal para escolher o que gerar mais no Volume II.

---

## Campos obrigatórios (resumo)

| Campo | Tipo | Nota |
|---|---|---|
| `id` | string | `^[A-Z]{3}-\d{3}$` |
| `category` | enum | uma das 8 |
| `difficulty` | 1–5 | inteiro |
| `estimated_time` | string | `"<2"`, `"2-5"`, `"5-10"`, `"10-20"`, `"20+"` |
| `title` | string | 2 a 4 palavras, sem revelar a solução |
| `problem` | markdown | o enunciado |
| `hint_1`, `hint_2` | markdown | ver [`04`](04-anatomia-de-um-problema.md) |
| `answer` | markdown | curto — uma frase ou um número |
| `solution` | markdown | o raciocínio completo |
| `concept` | string | o princípio (ex.: `"Bayes"`, `"princípio do pombal"`) |
| `has_unique_answer` | bool | `false` para `DIL` e `WWY` |
| `verified` | enum | `GENERATED` → `SOLVED` → `CHECKED` → `VERIFIED` |

Schema completo: [`06-esquema-json.md`](06-esquema-json.md).

---

## Duas regras sobre títulos

1. **O título nunca revela a resposta.** "A moeda viciada" é mau se a resposta for
   "escolheste a viciada". Usa-se "As duas moedas".
2. **O título é neutro quanto à dificuldade.** Nada de "O impossível". A dificuldade
   já está nas estrelas, e prometer dificuldade estraga a experiência de quem falha.
