"""PRB-025 — duas bolas da mesma cor, sem reposição."""
import random
from fractions import Fraction

B, P_ = 3, 2
p = Fraction(B, B + P_) * Fraction(B - 1, B + P_ - 1) + \
    Fraction(P_, B + P_) * Fraction(P_ - 1, B + P_ - 1)
print("brancas: %s · pretas: %s · total: %s"
      % (Fraction(3, 5) * Fraction(2, 4), Fraction(2, 5) * Fraction(1, 4), p))
assert p == Fraction(2, 5)

rng = random.Random(25)
saco = ["b"] * B + ["p"] * P_
N = 1_000_000
sim = sum(1 for _ in range(N) if len(set(rng.sample(saco, 2))) == 1) / N
print("exacto %s = %.4f · simulado %.5f" % (p, float(p), sim))
assert abs(sim - float(p)) < 0.005
