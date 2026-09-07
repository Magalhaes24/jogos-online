"""MAT-028 — três sinos: mínimo múltiplo comum."""
from math import gcd

a, b, c = 6, 8, 12


def mmc(x, y):
    return x * y // gcd(x, y)


m = mmc(mmc(a, b), c)
directo = next(t for t in range(1, 10000) if t % a == t % b == t % c == 0)
print("mmc(6,8,12) =", m, "· primeiro instante comum por procura directa:", directo)
assert m == directo == 24
# quantas vezes tocam juntos num dia
assert (24 * 60) // m == 60
print("num dia de 24 horas tocam juntos", (24 * 60) // m, "vezes")
