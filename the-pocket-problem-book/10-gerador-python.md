# 10 — O gerador

## Estrutura do projecto

```
problem-book/
│
├── problems/                  # a base de dados — a única coisa que importa
│   ├── logic.json
│   ├── riddles.json
│   ├── math.json
│   ├── probability.json
│   ├── lateral.json
│   ├── dilemmas.json
│   ├── what_would_you.json
│   └── programming.json
│
├── checks/                    # verificadores, um por problema quando aplicável
│   ├── LOG-001.py
│   ├── PRB-002.py
│   └── …
│
├── generator/
│   ├── __init__.py
│   ├── schema.py              # dataclasses + validação de integridade
│   ├── db.py                  # carregar / gravar / consultar problems/
│   ├── generate.py            # prompt #1 → GENERATED
│   ├── solve.py               # prompt #2 → SOLVED
│   ├── attack.py              # prompt #3 → CHECKED
│   ├── verify.py              # prompt #4 + execução → VERIFIED
│   ├── pipeline.py            # orquestra os quatro
│   ├── render.py              # JSON → XHTML por bloco
│   ├── epub.py                # XHTML → EPUB
│   ├── pdf.py                 # opcional
│   └── report.py              # estatísticas do banco
│
├── templates/
│   ├── problem.html.j2        # os 9 blocos
│   ├── dilemma.html.j2        # variante sem "resposta"
│   ├── wwy.html.j2
│   ├── menu.html.j2
│   ├── jump_list.html.j2
│   ├── daily.html.j2
│   ├── index.html.j2
│   └── style.css
│
├── concepts.yaml              # a lista de conceitos alvo (ver 12)
├── tests/
│   ├── test_schema.py
│   ├── test_integrity.py      # as 10 regras do doc 06
│   └── test_render.py
└── output/
    ├── pocket-problems.epub
    ├── pocket-problems-ascii.epub
    └── report.md
```

---

## CLI

```bash
# gerar 20 candidatos de lógica, dificuldade 3, percorrendo concepts.yaml
ppb generate --category logic --difficulty 3 --count 20

# correr o pipeline sobre tudo o que ainda não está VERIFIED
ppb pipeline --all

# correr só um passo
ppb solve  --id LOG-034
ppb attack --id LOG-034
ppb verify --id LOG-034

# integridade (as 10 regras do doc 06)
ppb check

# construir
ppb build --volume 1 --format epub
ppb build --volume 1 --format epub --ascii
ppb build --volume 1 --format pdf

# estado do banco
ppb report
```

### `ppb report` — exemplo de saída

```
BANCO DE PROBLEMAS — 2026-09-06

Categoria         VERIFIED  CHECKED  SOLVED  GENERATED  REJECTED   alvo
─────────────────────────────────────────────────────────────────────────
🧠 logic                12        3       5         21        44     35
🕵️ riddles              18        0       2          6        11     30
🔢 math                  9        4       1         14        27     30
🎲 probability           7        2       3          9        31     25
🌀 lateral              14        1       0          4         6     25
⚖️ dilemmas              11        0       0          3         2     20
🤔 what_would_you         8        0       0          5         1     20
💻 programming           6        1       2          7         9     15
─────────────────────────────────────────────────────────────────────────
TOTAL                   85       11      13         69       131    200

Taxa de aceitação: 39%
Prontos para o Volume I: 85/200 (42%)
Em NEEDS_REVIEW: 14

Dificuldade (VERIFIED):  ★ 9 · ★★ 22 · ★★★ 31 · ★★★★ 17 · ★★★★★ 6
Distribuição alvo:       ★ 10% · ★★ 25% · ★★★ 35% · ★★★★ 20% · ★★★★★ 10%
Desvio: falta ★★★★★ (-4), excesso ★★★ (+1)

Conceitos sem cobertura: princípio do pombal, paridade, invariantes,
  paradoxo de Simpson, teoria dos jogos
```

O relatório é o painel de controlo do projecto. Diz sempre a próxima coisa a gerar.

---

## `schema.py` — esqueleto

```python
from dataclasses import dataclass, field
from typing import Literal

Category = Literal["logic", "riddles", "math", "probability",
                   "lateral", "dilemmas", "what_would_you", "programming"]
State = Literal["GENERATED", "SOLVED", "CHECKED", "VERIFIED",
                "REJECTED", "NEEDS_REVIEW"]

PREFIX = {"logic": "LOG", "riddles": "ENI", "math": "MAT",
          "probability": "PRB", "lateral": "LAT", "dilemmas": "DIL",
          "what_would_you": "WWY", "programming": "PRG"}

TIME_FOR = {1: "<2", 2: "2-5", 3: "5-10", 4: "10-20", 5: "20+"}
NO_ANSWER = {"dilemmas", "what_would_you"}


@dataclass
class Problem:
    id: str
    category: Category
    title: str
    difficulty: int
    estimated_time: str
    problem: str
    hint_1: str
    hint_2: str
    why: str
    concept: str
    has_unique_answer: bool
    verified: State
    answer: str | None = None
    solution: str | None = None
    variation: str | None = None
    frustration: int = 0
    aha_factor: int = 0
    trap: bool = False
    classic: bool = False
    tags: list[str] = field(default_factory=list)
    code: str | None = None
    language: str | None = None
    volume: int = 1

    def validate(self) -> list[str]:
        """As 10 regras de integridade do doc 06."""
        errs = []
        if not self.id.startswith(PREFIX[self.category]):
            errs.append(f"{self.id}: prefixo não corresponde a {self.category}")
        if TIME_FOR[self.difficulty] != self.estimated_time:
            errs.append(f"{self.id}: tempo inconsistente com dificuldade")
        if (self.category in NO_ANSWER) != (not self.has_unique_answer):
            errs.append(f"{self.id}: has_unique_answer inconsistente")
        if self.has_unique_answer and not self.answer:
            errs.append(f"{self.id}: falta answer")
        if self.answer and self.answer.lower() in self.title.lower():
            errs.append(f"{self.id}: título revela a resposta")
        if self.hint_1 == self.hint_2:
            errs.append(f"{self.id}: dicas iguais")
        if self.answer and self.answer.lower() in (self.hint_1 + self.hint_2).lower():
            errs.append(f"{self.id}: dica revela a resposta")
        if self.category == "programming" and not self.code:
            errs.append(f"{self.id}: falta code")
        return errs
```

---

## Ordem de construção

Constrói por esta ordem. Cada passo é útil sozinho.

1. **`schema.py` + `db.py` + `test_integrity.py`** — sem base de dados sólida,
   o resto é areia.
2. **`render.py` + `epub.py`** — com 5 problemas escritos à mão. Testa no X4 **antes**
   de escrever qualquer código de IA. É aqui que se descobre que a tipografia está mal.
3. **`verify.py`** — o verificador vem antes do gerador. Só se automatiza a geração
   quando já se sabe rejeitar.
4. **`generate.py` / `solve.py` / `attack.py`** — por esta ordem.
5. **`pipeline.py` + `report.py`** — a fábrica.

**Erro clássico:** começar pelo gerador. Acaba-se com 400 problemas não verificáveis
e um EPUB que não se lê bem no dispositivo.

---

## Dependências

Mínimas, deliberadamente:

```
jinja2        # templates
ebooklib      # EPUB (ou construir o zip à mão — o formato é simples)
sympy         # verificação simbólica
pyyaml        # concepts.yaml
anthropic     # ou o cliente do modelo escolhido
```

Sem base de dados, sem framework, sem front-end. Ficheiros JSON e um script.
