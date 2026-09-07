"""LOG-025 — três habitantes; enumeração dos 8 mundos."""
from itertools import product

sols = []
for a, b, c in product([True, False], repeat=3):     # True = cavaleiro
    af_a = not a and not b and not c          # A: «somos os três escudeiros»
    af_b = [a, b, c].count(True) == 1         # B: «exactamente um de nós é cavaleiro»
    af_c = [a, b, c].count(True) == 2         # C: «exactamente dois são cavaleiros»
    if af_a == a and af_b == b and af_c == c:
        sols.append(tuple("cavaleiro" if x else "escudeiro" for x in (a, b, c)))

print("mundos: 8 · soluções:", sols)
assert len(sols) == 1, sols
assert sols[0] == ("escudeiro", "cavaleiro", "escudeiro"), sols[0]
