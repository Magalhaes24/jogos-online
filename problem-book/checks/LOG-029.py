"""LOG-029 — quatro suspeitos, cada um diz uma verdade e uma mentira."""
from itertools import product

P = ["Rui", "Sara", "Tomás", "Vera"]
# afirmações: (índice do suspeito) -> duas funções sobre o culpado
AFIRMACOES = {
    "Rui":   [lambda c: c != "Rui",    lambda c: c == "Vera"],
    "Sara":  [lambda c: c != "Vera",   lambda c: c == "Tomás"],
    "Tomás": [lambda c: c != "Tomás",  lambda c: c == "Rui"],
    "Vera":  [lambda c: c != "Sara",   lambda c: c == "Sara"],
}

sols = []
for culpado in P:
    ok = all(sum(f(culpado) for f in fs) == 1 for fs in AFIRMACOES.values())
    if ok:
        sols.append(culpado)

print("mundos: 4 · soluções:", sols)
for culpado in P:
    detalhe = {p: [f(culpado) for f in fs] for p, fs in AFIRMACOES.items()}
    print("  se o culpado fosse %-6s ->" % culpado,
          {k: ("V" if v[0] else "F") + ("V" if v[1] else "F") for k, v in detalhe.items()})
assert sols == ["Sara"], sols
