"""PRB-004 — soma 7 com dois dados: enumeração + Monte Carlo."""
import random
from fractions import Fraction
from itertools import product

casos = list(product(range(1, 7), repeat=2))
sete = [c for c in casos if sum(c) == 7]
exacto = Fraction(len(sete), len(casos))
print("36 casos ·", len(sete), "dão 7:", sete)
assert exacto == Fraction(1, 6)

rng = random.Random(4)
N = 2_000_000
sim = sum(1 for _ in range(N) if rng.randint(1, 6) + rng.randint(1, 6) == 7) / N
print("exacto: %s = %.5f · simulado: %.5f" % (exacto, float(exacto), sim))
assert abs(sim - float(exacto)) < 0.005
# o 7 é a soma mais provável: nenhuma outra tem 6 maneiras
from collections import Counter
c = Counter(sum(x) for x in casos)
assert max(c.values()) == 6 and c[7] == 6
print("distribuição das somas:", dict(sorted(c.items())))
