"""LOG-034 — duas cordas de queima irregular, medir 45 minutos.

Simulação verdadeira: cada corda é discretizada em fatias com duração
aleatória (densidade irregular). As frentes de chama avançam fatia a fatia,
com fatias parciais tratadas correctamente. O tempo é medido, não assumido.
"""
import random

rng = random.Random(9)
FATIAS = 500
EPS = 1e-9


def corda_aleatoria(total=60.0):
    d = [rng.random() + 0.01 for _ in range(FATIAS)]
    k = total / sum(d)
    return [x * k for x in d]


def consome_de_uma_ponta(d, tempo):
    """Queima `tempo` minutos a partir da esquerda; devolve o que resta."""
    r = list(d)
    while tempo > EPS and r:
        if r[0] <= tempo + EPS:
            tempo -= r.pop(0)
        else:
            r[0] -= tempo
            tempo = 0.0
    return r


def queima_pelas_duas_pontas(d):
    """Tempo até as duas frentes se encontrarem. Medido, não calculado."""
    r = list(d)
    t = 0.0
    while r:
        if len(r) == 1:
            t += r[0] / 2            # as duas frentes na mesma fatia
            r = []
            break
        passo = min(r[0], r[-1])
        t += passo
        r[0] -= passo
        r[-1] -= passo
        if r[0] <= EPS:
            r.pop(0)
        if r and r[-1] <= EPS:
            r.pop()
    return t


for _ in range(300):
    A, B = corda_aleatoria(), corda_aleatoria()

    t1 = queima_pelas_duas_pontas(A)       # fase 1: A pelas duas pontas
    sobra_B = consome_de_uma_ponta(B, t1)  # B ardeu por uma ponta durante t1
    t2 = queima_pelas_duas_pontas(sobra_B) # fase 2: segunda ponta de B

    assert abs(t1 - 30) < 1e-6, t1
    assert abs(t1 + t2 - 45) < 1e-6, (t1, t2)

print("300 cordas com densidade aleatória (%d fatias cada)" % FATIAS)
print("fase 1 medida: %.9f min · total medido: %.9f min" % (t1, t1 + t2))
assert abs(t1 + t2 - 45) < 1e-6
