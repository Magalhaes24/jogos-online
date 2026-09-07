"""PRG-014 — encontrar o repetido em n+1 números de 1..n, memória O(1),
sem alterar a lista. Ciclo de Floyd sobre a função i -> xs[i]."""
import random

rng = random.Random(14)


def floyd(xs):
    lento = rapido = xs[0]
    while True:
        lento = xs[lento]
        rapido = xs[xs[rapido]]
        if lento == rapido:
            break
    lento = xs[0]
    while lento != rapido:
        lento = xs[lento]
        rapido = xs[rapido]
    return lento


for _ in range(2000):
    n = rng.randrange(2, 60)
    repetido = rng.randrange(1, n + 1)
    xs = list(range(1, n + 1)) + [repetido]
    rng.shuffle(xs)
    copia = list(xs)
    achado = floyd(xs)
    assert achado == repetido, (achado, repetido, xs)
    assert xs == copia, "a lista não pode ser alterada"

print("2000 casos aleatórios · sempre correcto · lista intacta · memória O(1)")
# a soma também resolve, mas transborda com n grande e falha com 2+ repetidos
n, xs = 5, [1, 2, 3, 4, 5, 3]
assert sum(xs) - n * (n + 1) // 2 == 3
print("a alternativa da soma dá o mesmo aqui (3), mas não sobrevive a duas repetições")
