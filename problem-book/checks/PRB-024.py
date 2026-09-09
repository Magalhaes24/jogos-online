"""PRB-024 — duas cartas seguidas do mesmo naipe."""
import random
from fractions import Fraction

p = Fraction(12, 51)
print("a primeira carta define o naipe; restam 12 do mesmo naipe em 51 cartas")
print("P =", p, "=", float(p))
assert p == Fraction(4, 17)

baralho = [(v, n) for n in "COPE" for v in range(1, 14)]
assert len(baralho) == 52
rng = random.Random(24)
N = 1_000_000
sim = sum(1 for _ in range(N)
          if (lambda c: c[0][1] == c[1][1])(rng.sample(baralho, 2))) / N
print("simulado: %.5f" % sim)
assert abs(sim - float(p)) < 0.005
