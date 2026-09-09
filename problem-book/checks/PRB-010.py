"""PRB-010 — falácia do jogador: a moeda não tem memória."""
import random
from fractions import Fraction

rng = random.Random(10)
N, apos_dez, caras_apos = 300_000, 0, 0
seguidas = 0
for _ in range(N):
    x = rng.random() < 0.5
    if seguidas >= 10:
        apos_dez += 1
        caras_apos += x
    seguidas = seguidas + 1 if x else 0

print("lançamentos após 10 caras seguidas: %d · caras: %.4f"
      % (apos_dez, caras_apos / apos_dez if apos_dez else 0))
if apos_dez > 30:
    assert abs(caras_apos / apos_dez - 0.5) < 0.15

# o que É raro é a sequência ANTES de acontecer
antes = Fraction(1, 2) ** 11
print("P(11 caras seguidas de antemão) = %s = %.5f" % (antes, float(antes)))
print("P(a 11.ª ser cara, já com 10 feitas) = 1/2")
assert antes == Fraction(1, 2048)
