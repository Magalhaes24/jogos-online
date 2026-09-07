"""MAT-001 — aritmética exacta, sem vírgula flutuante."""
from fractions import Fraction

total, diferenca = Fraction(110, 100), Fraction(1)
bola = (total - diferenca) / 2
taco = bola + diferenca

print("bola =", bola, "=", float(bola), "· taco =", taco)
assert bola == Fraction(1, 20), bola          # €0,05
assert bola + taco == total and taco - bola == diferenca
assert bola != Fraction(1, 10), "a resposta intuitiva não pode passar"
