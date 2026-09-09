"""PRB-019 — dois filhos, ambos rapazes, sem nenhuma informação extra."""
import random
from fractions import Fraction
from itertools import product

familias = list(product("RM", repeat=2))
p = Fraction(sum(1 for f in familias if f == ("R", "R")), len(familias))
print("as quatro famílias igualmente prováveis:", familias)
assert p == Fraction(1, 4)

rng = random.Random(19)
N = 1_000_000
sim = sum(1 for _ in range(N)
          if rng.choice("RM") == "R" and rng.choice("RM") == "R") / N
print("exacto 1/4 = 0.25 · simulado %.5f" % sim)
assert abs(sim - 0.25) < 0.005
