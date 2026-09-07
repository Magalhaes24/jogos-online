"""LOG-003 — grelha 3x3: 36 combinações, tem de sobrar uma."""
from itertools import permutations

PESSOAS = ["Ana", "Bruno", "Clara"]
sols = []
for bebidas in permutations(["chá", "café", "água"]):
    for pisos in permutations([1, 2, 3]):
        b = dict(zip(PESSOAS, bebidas))
        p = dict(zip(PESSOAS, pisos))
        quem_cafe = next(x for x in PESSOAS if b[x] == "café")
        if not p[quem_cafe] > p["Ana"]:      # pista 1
            continue
        if p["Bruno"] == 3:                  # pista 2
            continue
        if b["Clara"] != "chá":              # pista 3
            continue
        sols.append((b, p))

print("combinações: 36 · soluções:", len(sols), sols)
assert len(sols) == 1, sols
b, p = sols[0]
assert b["Ana"] == "água" and p == {"Ana": 1, "Bruno": 2, "Clara": 3}, sols
