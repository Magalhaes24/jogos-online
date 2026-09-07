"""MAT-004 — 20% de desconto seguido de 20% de aumento não volta ao início."""
from fractions import Fraction

p = Fraction(100)
depois = p * Fraction(80, 100) * Fraction(120, 100)
print("100 -> -20%% -> %s -> +20%% -> %s" % (p * Fraction(80, 100), depois))
assert depois == Fraction(96), depois
assert depois != p
# a ordem não importa: a multiplicação é comutativa
assert p * Fraction(120, 100) * Fraction(80, 100) == depois
print("perda: 4% · e é a mesma seja qual for a ordem das operações")
