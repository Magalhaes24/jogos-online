"""MAT-015 — sobe 25%: quanto tem de descer para voltar ao mesmo?"""
from fractions import Fraction

p = Fraction(100)
subiu = p * Fraction(125, 100)
desconto = 1 - p / subiu
print("100 -> +25%% -> %s · desconto necessário: %s = %s%%"
      % (subiu, desconto, desconto * 100))
assert subiu == 125
assert desconto == Fraction(1, 5), desconto      # 20%, não 25%
assert subiu * (1 - desconto) == p
# tabela geral: subir x% exige descer x/(100+x)
for x in (10, 25, 50, 100):
    d = Fraction(x, 100 + x)
    assert Fraction(100) * (1 + Fraction(x, 100)) * (1 - d) == 100
    print("  subir %3d%% -> descer %s%%" % (x, round(float(d * 100), 2)))
