"""PRB-022 — ruína do jogador: simulação e fórmula, para p justo e p=0,49."""
import random

rng = random.Random(22)


def sobrevive(inicio, alvo, p):
    d = inicio
    while 0 < d < alvo:
        d += 1 if rng.random() < p else -1
    return d == alvo


def formula(inicio, alvo, p):
    if p == 0.5:
        return inicio / alvo
    r = (1 - p) / p
    return (1 - r ** inicio) / (1 - r ** alvo)


for p in (0.5, 0.49):
    N = 40_000
    sim = sum(sobrevive(10, 20, p) for _ in range(N)) / N
    teo = formula(10, 20, p)
    print("p=%.2f · 10 -> 20 · simulado %.4f · fórmula %.4f" % (p, sim, teo))
    assert abs(sim - teo) < 0.01, (sim, teo)

assert abs(formula(10, 20, 0.5) - 0.5) < 1e-9
assert abs(formula(10, 20, 0.49) - 0.4013) < 1e-3

# a mesma desvantagem de 1% com apostas maiores é quase fatal
grande = formula(100, 200, 0.49)
print("p=0.49 · 100 -> 200 · fórmula %.4f" % grande)
assert grande < 0.02, grande
print("-> 1% de desvantagem: 40% em 10 jogadas, menos de 2% em 100")
