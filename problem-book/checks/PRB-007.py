"""PRB-007 — teste médico: P(doente | positivo) com base rara."""
import random
from fractions import Fraction

PREV = Fraction(1, 1000)
SENS = Fraction(99, 100)      # detecta os doentes
ESPEC = Fraction(99, 100)     # não acusa os saudáveis

vp = PREV * SENS
fp = (1 - PREV) * (1 - ESPEC)
posterior = vp / (vp + fp)
print("verdadeiros positivos: %s · falsos positivos: %s" % (vp, fp))
print("P(doente | positivo) = %s = %.4f" % (posterior, float(posterior)))
assert abs(float(posterior) - 0.0902) < 1e-4

rng = random.Random(7)
N = 4_000_000
pos = doentes_pos = 0
for _ in range(N):
    doente = rng.random() < 1 / 1000
    positivo = rng.random() < (0.99 if doente else 0.01)
    if positivo:
        pos += 1
        doentes_pos += doente
sim = doentes_pos / pos
print("simulado: %.4f (%d positivos em %d)" % (sim, pos, N))
assert abs(sim - float(posterior)) < 0.005
print("-> num teste 99% fiável, 9 em cada 10 positivos são falsos alarmes")
