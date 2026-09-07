"""MAT-021 — subir 10 degraus com passos de 1 ou 2: Fibonacci."""
from functools import lru_cache


@lru_cache(None)
def formas(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return formas(n - 1) + formas(n - 2)


seq = [formas(n) for n in range(1, 11)]
print("degraus 1..10 ->", seq)
assert formas(10) == 89, formas(10)
assert seq == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# força bruta independente, para n pequeno
from itertools import product
for n in range(1, 13):
    conta = sum(1 for k in range(n + 1)
                for c in product([1, 2], repeat=k) if sum(c) == n)
    assert conta == formas(n), (n, conta, formas(n))
print("confirmado por enumeração exaustiva até n=12")
