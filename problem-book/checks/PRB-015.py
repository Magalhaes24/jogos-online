"""PRB-015 — 100 prisioneiros e 100 caixas: a estratégia dos ciclos."""
import random

N, TENTATIVAS = 100, 50
rng = random.Random(15)


def ronda_ciclos():
    caixas = list(range(N))
    rng.shuffle(caixas)                     # caixas[i] = número lá dentro
    for p in range(N):
        atual = p
        for _ in range(TENTATIVAS):
            if caixas[atual] == p:
                break
            atual = caixas[atual]
        else:
            return False
    return True


def ronda_aleatoria():
    caixas = list(range(N))
    rng.shuffle(caixas)
    for p in range(N):
        if p not in [caixas[i] for i in rng.sample(range(N), TENTATIVAS)]:
            return False
    return True


R = 20_000
ciclos = sum(ronda_ciclos() for _ in range(R)) / R
print("estratégia dos ciclos: %.4f de sucesso em %d rondas" % (ciclos, R))
assert 0.29 < ciclos < 0.33, ciclos

aleatoria = sum(ronda_aleatoria() for _ in range(200)) / 200
print("escolha aleatória: %.6f (o valor teórico é 2^-100)" % aleatoria)
assert aleatoria == 0.0
print("-> 31% contra praticamente zero, sem qualquer comunicação")
