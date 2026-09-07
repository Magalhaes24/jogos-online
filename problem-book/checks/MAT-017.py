"""MAT-017 — o livro que custa 10 euros mais metade do próprio preço."""
from fractions import Fraction
p = Fraction(10) / (1 - Fraction(1, 2))
print("p = 10 + p/2  ->  p/2 = 10  ->  p =", p)
assert p == 20 and p == 10 + p / 2
assert p != 15, "15 é a resposta intuitiva e falha: 15 != 10 + 7,5"
