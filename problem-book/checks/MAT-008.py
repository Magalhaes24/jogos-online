"""MAT-008 — apertos de mão numa sala de 20 pessoas."""
from itertools import combinations
from math import comb

n = 20
por_forca_bruta = len(list(combinations(range(n), 2)))
formula = n * (n - 1) // 2
print("pares distintos:", por_forca_bruta, "· n(n-1)/2:", formula, "· comb:", comb(n, 2))
assert por_forca_bruta == formula == comb(n, 2) == 190
# o erro comum é 20*19 = 380: conta cada aperto duas vezes
assert n * (n - 1) == 380 == 2 * 190
print("20 x 19 = 380 conta cada aperto duas vezes")
