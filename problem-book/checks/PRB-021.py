"""PRB-021 — São Petersburgo: valor esperado infinito, ganho real pequeno."""
import random
import statistics

rng = random.Random(21)


def jogo():
    premio, n = 2, 1
    while rng.random() < 0.5:
        premio *= 2
        n += 1
    return premio


# valor esperado teórico: soma de (1/2^n) * 2^n = 1 + 1 + 1 + ... = infinito
parcial = sum(1 for _ in range(40))
print("valor esperado truncado em 40 lançamentos:", parcial, "(cresce sem limite)")

for N in (1_000, 100_000, 1_000_000):
    media = statistics.mean(jogo() for _ in range(N))
    print("  média de %7d jogos: %8.2f" % (N, media))

# a média cresce com log(N): não converge, mas na prática é pequena
m1 = statistics.mean(jogo() for _ in range(200_000))
assert m1 < 60, m1
print("-> o valor esperado é infinito, mas quase ninguém pagaria 60 euros")
