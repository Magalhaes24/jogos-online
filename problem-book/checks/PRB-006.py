"""PRB-006 — paradoxo dos aniversários: quantas pessoas para passar de 50%?"""
import random
from fractions import Fraction

def prob_coincidencia(n, dias=365):
    p = Fraction(1)
    for k in range(n):
        p *= Fraction(dias - k, dias)
    return 1 - p


for n in (10, 20, 22, 23, 30, 50, 70):
    print("  %2d pessoas -> %.4f" % (n, float(prob_coincidencia(n))))
assert prob_coincidencia(22) < Fraction(1, 2) < prob_coincidencia(23)
assert abs(float(prob_coincidencia(23)) - 0.5073) < 1e-4

rng = random.Random(6)
N = 200_000
sim = sum(1 for _ in range(N)
          if len(set(rng.randrange(365) for _ in range(23))) < 23) / N
print("23 pessoas -> exacto %.4f · simulado %.4f"
      % (float(prob_coincidencia(23)), sim))
assert abs(sim - float(prob_coincidencia(23))) < 0.005
