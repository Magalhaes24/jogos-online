# 06 — O esquema JSON

Um problema é um objecto JSON. O livro é uma pasta de ficheiros JSON.
Tudo o resto — EPUB, PDF, web — é derivado.

## Ficheiros

```
problems/
├── logic.json          # array de objectos LOG-*
├── riddles.json        # ENI-*
├── math.json           # MAT-*
├── probability.json    # PRB-*
├── lateral.json        # LAT-*
├── dilemmas.json       # DIL-*
├── what_would_you.json # WWY-*
└── programming.json    # PRG-*
```

Um array por ficheiro, ordenado por ID. Um problema por objecto. Sem aninhamento.

---

## Schema

```jsonc
{
  // ── Identidade ───────────────────────────────────────
  "id":              "PRB-002",           // ^[A-Z]{3}-\d{3}$ · permanente
  "category":        "probability",       // enum, ver abaixo
  "title":           "As duas moedas",    // 2–4 palavras, não revela nada

  // ── Calibração ───────────────────────────────────────
  "difficulty":      4,                   // 1–5
  "estimated_time":  "10-20",             // "<2" | "2-5" | "5-10" | "10-20" | "20+"
  "frustration":     3,                   // 0–5, editorial
  "aha_factor":      5,                   // 0–5, editorial
  "trap":            true,                // engana a intuição? → secção 🧨
  "classic":         false,               // é um clássico conhecido?

  // ── Conteúdo ─────────────────────────────────────────
  "problem":         "Tens duas moedas...",  // markdown, auto-contido
  "hint_1":          "Não perguntes qual...",// reorienta
  "hint_2":          "Escreve as quatro...", // dá o mecanismo
  "answer":          "64/89 ≈ 71,9%",        // uma linha
  "solution":        "| Moeda | P(escolha)...", // raciocínio completo, markdown
  "why":             "Bayes é apenas...",    // o princípio transferível
  "variation":       "E se saíssem três caras?", // opcional, sem solução

  // ── Semântica ────────────────────────────────────────
  "concept":         "Teorema de Bayes",
  "tags":            ["bayes", "condicional", "moedas"],
  "has_unique_answer": true,              // false para DIL e WWY

  // ── Validação ────────────────────────────────────────
  "verified":        "VERIFIED",          // GENERATED|SOLVED|CHECKED|VERIFIED|REJECTED
  "verification": {
    "method":        "monte_carlo",       // ver 07
    "script":        "checks/PRB-002.py", // caminho relativo, opcional
    "result":        "0.7191 vs 0.7191",  // o que o script devolveu
    "checked_at":    "2026-09-06"
  },

  // ── Proveniência ─────────────────────────────────────
  "source":          "generated",         // generated | classic | manual
  "volume":          1
}
```

### Enum `category`

`logic` · `riddles` · `math` · `probability` · `lateral` · `dilemmas` ·
`what_would_you` · `programming`

### Campos por categoria

| Campo | LOG | ENI | MAT | PRB | LAT | DIL | WWY | PRG |
|---|---|---|---|---|---|---|---|---|
| `answer` | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ |
| `solution` | ✅ | ✅ | ✅ | ✅ | ✅ | — | — | ✅ |
| `arguments_for` / `_against` | — | — | — | — | — | ✅ | — | — |
| `approaches` (array) | — | — | — | — | — | — | ✅ | — |
| `common_mistake` | — | — | — | — | — | — | ✅ | — |
| `code` / `language` | — | — | — | — | — | — | — | ✅ |
| `has_unique_answer` | true | true | true | true | true | **false** | **false** | true |

---

## Exemplo completo

```json
{
  "id": "PRB-002",
  "category": "probability",
  "title": "As duas moedas",
  "difficulty": 4,
  "estimated_time": "10-20",
  "frustration": 3,
  "aha_factor": 5,
  "trap": true,
  "classic": true,
  "problem": "Tens duas moedas. Uma é justa. A outra sai cara 80% das vezes.\n\nEscolhes uma ao acaso, sem olhar, e lanças duas vezes. Saem duas caras.\n\nQual é a probabilidade de teres escolhido a moeda viciada?",
  "hint_1": "A resposta não é 80%. Nem 50%. Pergunta-te: de todas as vezes que este cenário acontece, em que fracção delas a moeda era a viciada?",
  "hint_2": "Calcula duas coisas: a probabilidade de sair CC com a moeda justa (0,5 × 0,25) e com a viciada (0,5 × 0,64). A resposta é a segunda a dividir pela soma das duas.",
  "answer": "64/89 ≈ 71,9%",
  "solution": "| Moeda | P(escolher) | P(CC \\| moeda) | Produto |\n|---|---|---|---|\n| Justa | 0,5 | 0,5² = 0,25 | 0,125 |\n| Viciada | 0,5 | 0,8² = 0,64 | 0,320 |\n\nP(CC) = 0,125 + 0,320 = 0,445\n\nP(viciada | CC) = 0,320 / 0,445 = **64/89 ≈ 0,719**",
  "why": "Bayes é apenas isto: entre todos os mundos onde o que observaste acontece, em que fracção deles a tua hipótese é verdadeira. Não penses em fórmulas — desenha a tabela dos mundos e conta.",
  "variation": "E se saíssem três caras seguidas? E se saísse cara-coroa?",
  "concept": "Teorema de Bayes",
  "tags": ["bayes", "condicional", "moedas"],
  "has_unique_answer": true,
  "verified": "VERIFIED",
  "verification": {
    "method": "monte_carlo",
    "script": "checks/PRB-002.py",
    "result": "analítico 0,71910 · simulado 0,71887 (10M ensaios) · Δ 0,03%",
    "checked_at": "2026-09-06"
  },
  "source": "classic",
  "volume": 1
}
```

---

## Regras de integridade (verificadas no build)

O build **falha** se alguma destas for violada:

1. `id` único em toda a base de dados, em todos os volumes.
2. O prefixo do `id` corresponde à `category`.
3. `verified == "VERIFIED"` para todos os problemas incluídos num EPUB.
4. `has_unique_answer == false` ⟺ `category ∈ {dilemmas, what_would_you}`.
5. `answer` existe ⟺ `has_unique_answer == true`.
6. `title` não revela a resposta. Heurística: só contam as palavras de `answer`
   com mais de 3 letras que **não aparecem no enunciado** — vocabulário partilhado
   com o problema («caixa», «moeda») não é spoiler; palavras novas são.
7. `difficulty` e `estimated_time` são consistentes:
   `1→"<2"`, `2→"2-5"`, `3→"5-10"`, `4→"10-20"`, `5→"20+"`.
8. `hint_1 != hint_2` e nenhuma das duas contém `answer` literalmente.
   O bloco `why` é obrigatório em todas as categorias excepto `what_would_you`,
   onde o seu lugar é ocupado por `common_mistake` + `approaches` (doc 04).
   `dilemmas` exige `arguments_for` **e** `arguments_against`.
9. `problem` não referencia outro problema por ID (auto-contenção).
10. `code` é obrigatório sempre que `verification.method == "execute"`.
    A categoria `programming` também admite problemas de algoritmo sem snippet
    (ex.: os 25 cavalos) — esses verificam-se por `brute_force`, não por execução.
