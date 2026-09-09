"""ENI-029 — os 17 camelos: as fracções não somam 1."""
from fractions import Fraction

partes = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 9)]
soma = sum(partes)
print("1/2 + 1/3 + 1/9 =", soma, "=", float(soma))
assert soma == Fraction(17, 18) < 1

# com 18 camelos as partes são todas inteiras e sobra exactamente um
com18 = [int(18 * p) for p in partes]
print("com 18 camelos: %s -> soma %d, sobra %d" % (com18, sum(com18), 18 - sum(com18)))
assert com18 == [9, 6, 2] and sum(com18) == 17

# com 17 nenhuma parte é inteira
com17 = [Fraction(17) * p for p in partes]
print("com 17 camelos: %s (nenhuma é inteira)" % [str(x) for x in com17])
assert all(x.denominator != 1 for x in com17)

# o testamento distribui MAIS do que 17/18? não: distribui menos
assert sum(com18) == 17 < 18
print("-> o testamento só distribui 17/18 do rebanho: o 18.º camelo é o resto que sobra")
