"""PRB-001 — enumeração exacta + Monte Carlo."""
import random
from fractions import Fraction
from itertools import product

casos = list(product("CK", repeat=3))
favoraveis = [c for c in casos if c.count("C") >= 2]
exacto = Fraction(len(favoraveis), len(casos))

N = 1_000_000
rng = random.Random(7)
sim = sum(1 for _ in range(N)
          if sum(rng.random() < 0.5 for _ in range(3)) >= 2) / N

print("exacto:", exacto, "· simulado:", round(sim, 5), f"({N} ensaios)")
assert exacto == Fraction(1, 2), exacto
assert abs(sim - float(exacto)) < 0.005, sim
