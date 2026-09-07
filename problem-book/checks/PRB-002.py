"""PRB-002 — Bayes exacto + Monte Carlo."""
import random
from fractions import Fraction

meio = Fraction(1, 2)
p_justa, p_viciada = Fraction(1, 2), Fraction(4, 5)
conj_justa = meio * p_justa ** 2
conj_viciada = meio * p_viciada ** 2
exacto = conj_viciada / (conj_justa + conj_viciada)

N = 2_000_000
rng = random.Random(11)
casos = favoraveis = 0
for _ in range(N):
    viciada = rng.random() < 0.5
    p = 0.8 if viciada else 0.5
    if rng.random() < p and rng.random() < p:
        casos += 1
        favoraveis += viciada
sim = favoraveis / casos

print("exacto:", exacto, "=", round(float(exacto), 5),
      "· simulado:", round(sim, 5), f"({casos} casos em {N} ensaios)")
assert exacto == Fraction(64, 89), exacto
assert abs(sim - float(exacto)) < 0.005, (sim, float(exacto))
