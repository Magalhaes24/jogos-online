"""MAT-002 — quadrado inscrito: área = d²/2, confirmada pelos vértices."""
from fractions import Fraction

raio = 10
diagonal = 2 * raio
area = Fraction(diagonal ** 2, 2)

# confirmação geométrica: vértices em (±r/√2, ±r/√2) => lado² = 2r²... em exacto:
lado_ao_quadrado = Fraction(diagonal ** 2, 2)   # L² + L² = d²

print("diagonal =", diagonal, "· L² =", lado_ao_quadrado, "· área =", area)
assert area == 200, area
assert lado_ao_quadrado == area
