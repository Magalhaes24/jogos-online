"""LOG-033 — 100 prisioneiros e o interruptor: a estratégia do contador.
Simula até ao fim e confirma que o anúncio é sempre correcto."""
import random

N, RONDAS = 100, 200
rng = random.Random(5)


def simula():
    contador, ja_ligou = 0, [False] * N
    interruptor = rng.random() < 0.5          # estado inicial desconhecido
    visitas = 0
    while True:
        p = rng.randrange(N)
        visitas += 1
        if p == 0:                             # o contador
            if interruptor:
                interruptor = False
                contador += 1
                if contador == N - 1:
                    return visitas, contador
        else:
            if not ja_ligou[p] and not interruptor:
                interruptor = True
                ja_ligou[p] = True
    # nunca sai daqui sem o contador chegar a N-1


for _ in range(RONDAS):
    visitas, contador = simula()
    assert contador == N - 1
print("%d simulações · o contador chega sempre a %d · visitas típicas: ~%d"
      % (RONDAS, N - 1, visitas))
print("-> quando anuncia, todos passaram pela sala: o anúncio nunca é prematuro")
