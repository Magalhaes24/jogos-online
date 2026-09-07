"""LOG-004 — princípio do pombal: pior caso ao tirar meias no escuro."""
from itertools import combinations_with_replacement

CORES = {"preta": 10, "azul": 8, "branca": 6}


def existe_par(seleccao):
    return any(seleccao.count(c) >= 2 for c in CORES)


def pior_caso_sem_par():
    """Maior número de meias que se pode ter sem nenhum par."""
    melhor = 0
    for n in range(1, 6):
        for sel in combinations_with_replacement(CORES, n):
            if all(sel.count(c) <= CORES[c] for c in CORES) and not existe_par(list(sel)):
                melhor = max(melhor, n)
    return melhor


sem_par = pior_caso_sem_par()
resposta = sem_par + 1
print("máximo sem par:", sem_par, "(uma de cada cor) · garantia:", resposta)
assert sem_par == 3 and resposta == 4, (sem_par, resposta)
