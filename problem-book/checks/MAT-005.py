"""MAT-005 — 5 máquinas, 5 peças, 5 minutos: e 100 máquinas?"""
from fractions import Fraction

# taxa por máquina, em peças por minuto
taxa = Fraction(5, 5 * 5)
print("cada máquina faz", taxa, "peça por minuto -> 5 minutos por peça")
assert taxa == Fraction(1, 5)

tempo = Fraction(100) / (100 * taxa)     # 100 peças com 100 máquinas
print("100 máquinas, 100 peças ->", tempo, "minutos")
assert tempo == 5, tempo
# controlo: 100 máquinas em 5 minutos fazem exactamente 100 peças
assert 100 * taxa * 5 == 100
