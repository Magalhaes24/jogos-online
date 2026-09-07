"""LOG-016 — quatro afirmações auto-referentes: só uma atribuição é consistente."""
from itertools import product

sols = []
for v in product([True, False], repeat=4):
    falsas = v.count(False)
    afirma = [falsas == 1, falsas == 2, falsas == 3, falsas == 4]
    if list(v) == afirma:
        sols.append(v)

print("atribuições testadas: 16 · consistentes:", sols)
assert len(sols) == 1, sols
v = sols[0]
assert v == (False, False, True, False), v
print("verdadeira: apenas a afirmação 3")
