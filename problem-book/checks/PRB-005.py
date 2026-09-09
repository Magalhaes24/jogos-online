"""PRB-005 — pelo menos um 6 em quatro lançamentos: complementar."""
import random
from fractions import Fraction

exacto = 1 - Fraction(5, 6) ** 4
rng = random.Random(5)
N = 2_000_000
sim = sum(1 for _ in range(N)
          if any(rng.randint(1, 6) == 6 for _ in range(4))) / N
print("1 - (5/6)^4 = %s = %.5f · simulado: %.5f" % (exacto, float(exacto), sim))
assert exacto == Fraction(671, 1296)
assert abs(sim - float(exacto)) < 0.005
# a conta errada (4 x 1/6) daria 0,667 e ultrapassa 1 com 7 lançamentos
assert 4 * Fraction(1, 6) > exacto
assert 7 * Fraction(1, 6) > 1
print("4 x 1/6 = %.4f está errado; com 7 lançamentos daria mais de 1" % (4 / 6))
