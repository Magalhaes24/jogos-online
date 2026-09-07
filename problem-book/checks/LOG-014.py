"""LOG-014 — três idades: produto 36; a soma não chega; «a mais velha»."""
from itertools import combinations_with_replacement

triplos = [t for t in combinations_with_replacement(range(1, 37), 3)
           if t[0] * t[1] * t[2] == 36]
somas = {}
for t in triplos:
    somas.setdefault(sum(t), []).append(t)

# «a soma não chega» => a soma tem de ser ambígua
ambiguas = {s: ts for s, ts in somas.items() if len(ts) > 1}
print("triplos com produto 36:", len(triplos), "· somas ambíguas:", ambiguas)
assert len(ambiguas) == 1, ambiguas
soma, candidatos = next(iter(ambiguas.items()))

# «a mais velha» => existe uma única mais velha (sem empate no topo)
final = [t for t in candidatos if t[2] > t[1]]
print("soma ambígua:", soma, "· candidatos:", candidatos, "· com uma só mais velha:", final)
assert final == [(2, 2, 9)], final
