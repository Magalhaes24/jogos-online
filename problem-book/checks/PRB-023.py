"""PRB-023 — problema do secretário: rejeitar os primeiros n/e."""
import random

rng = random.Random(23)
N, RONDAS = 100, 40_000


def estrategia(k):
    acertos = 0
    for _ in range(RONDAS):
        cands = list(range(N))
        rng.shuffle(cands)
        melhor_visto = max(cands[:k]) if k else -1
        escolhido = next((c for c in cands[k:] if c > melhor_visto), cands[-1])
        acertos += escolhido == N - 1
    return acertos / RONDAS


resultados = {k: estrategia(k) for k in (0, 10, 25, 37, 50, 75)}
for k, r in resultados.items():
    print("  rejeitar os primeiros %2d -> acerta %.4f" % (k, r))

melhor = max(resultados, key=resultados.get)
print("melhor k testado:", melhor, "· 1/e =", round(1 / 2.718281828, 4))
assert melhor in (25, 37), melhor
assert abs(resultados[37] - 0.37) < 0.03, resultados[37]
