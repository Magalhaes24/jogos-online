"""PRB-013 — na lotaria, 1-2-3-4-5-6 é tão provável como qualquer outra chave."""
from math import comb
from fractions import Fraction

total = comb(49, 6)
p = Fraction(1, total)
print("chaves possíveis no 6/49: %d · probabilidade de cada uma: %s" % (total, p))
assert total == 13_983_816

# qualquer chave concreta tem a mesma probabilidade
import random
rng = random.Random(13)
for _ in range(5):
    chave = tuple(sorted(rng.sample(range(1, 50), 6)))
    assert Fraction(1, total) == p
print("exemplo de chaves, todas com a mesma probabilidade:",
      [tuple(sorted(rng.sample(range(1, 50), 6))) for _ in range(2)])

# o que MUDA é o prémio: chaves "bonitas" são jogadas por muita gente
consecutivas = 49 - 6 + 1          # 1-6, 2-7, ..., 44-49
print("chaves de 6 números consecutivos: %d em %d = %.7f%%"
      % (consecutivas, total, 100 * consecutivas / total))
assert consecutivas == 44
