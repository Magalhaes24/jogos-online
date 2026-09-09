"""ENI-023 — as idades dos dois irmãos."""
from fractions import Fraction

sols = []
for x in range(1, 63):              # a minha idade
    y = 63 - x                      # a tua
    passado = x - y                 # há quantos anos eu tinha a tua idade
    tu_entao = y - passado
    if passado > 0 and tu_entao > 0 and x == 2 * tu_entao:
        sols.append((x, y, tu_entao))

for x, y, t in sols:
    print("eu %d, tu %d · há %d anos eu tinha %d e tu tinhas %d · 2x%d = %d"
          % (x, y, x - y, y, t, t, x))
assert len(sols) == 1, sols
assert sols[0][:2] == (36, 27), sols
