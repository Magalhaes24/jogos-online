"""PRB-014 — coleccionador de cromos: quantos pacotes para completar 50?"""
import random
from fractions import Fraction

N_CROMOS = 50
esperado = N_CROMOS * sum(Fraction(1, k) for k in range(1, N_CROMOS + 1))
print("valor esperado exacto: %.2f cromos" % float(esperado))
assert abs(float(esperado) - 224.96) < 0.01

rng = random.Random(14)
RONDAS = 20_000
total = 0
for _ in range(RONDAS):
    vistos, n = set(), 0
    while len(vistos) < N_CROMOS:
        vistos.add(rng.randrange(N_CROMOS))
        n += 1
    total += n
sim = total / RONDAS
print("simulado em %d colecções: %.2f cromos" % (RONDAS, sim))
assert abs(sim - float(esperado)) < 3

# o último cromo sozinho custa em média 50 pacotes
print("só o último cromo custa, em média, %d cromos" % N_CROMOS)
assert float(esperado) / N_CROMOS > 4
