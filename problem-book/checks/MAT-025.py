"""MAT-025 — 2^100 contra 100!."""
import math

a, b = 2 ** 100, math.factorial(100)
print("2^100  tem %d algarismos" % len(str(a)))
print("100!   tem %d algarismos" % len(str(b)))
print("100! / 2^100 = 10^%.1f" % (math.log10(b) - math.log10(a)))
assert b > a
# porquê: a partir do 3, cada factor de 100! é maior do que 2
assert all(k > 2 for k in range(3, 101))
razao = math.log10(b) - math.log10(a)
assert razao > 100, razao
