"""LOG-006 — lobo, cabra e couve: BFS no espaço de estados."""
from collections import deque

ITENS = ("lobo", "cabra", "couve")


def seguro(margem_sem_barqueiro):
    if "lobo" in margem_sem_barqueiro and "cabra" in margem_sem_barqueiro:
        return False
    if "cabra" in margem_sem_barqueiro and "couve" in margem_sem_barqueiro:
        return False
    return True


inicio = (frozenset(ITENS), frozenset(), "esq")
objectivo = (frozenset(), frozenset(ITENS), "dir")

fila, visto = deque([(inicio, 0)]), {inicio}
solucao = None
while fila:
    (esq, dir_, barco), n = fila.popleft()
    if (esq, dir_, barco) == objectivo:
        solucao = n
        break
    origem, destino = (esq, dir_) if barco == "esq" else (dir_, esq)
    for carga in [None] + list(origem):
        novo_origem = origem - {carga} if carga else origem
        novo_destino = destino | ({carga} if carga else set())
        if not seguro(novo_origem):
            continue
        estado = ((novo_origem, novo_destino, "dir") if barco == "esq"
                  else (novo_destino, novo_origem, "esq"))
        if estado not in visto:
            visto.add(estado)
            fila.append((estado, n + 1))

print("travessias mínimas:", solucao, "· estados alcançáveis:", len(visto))
assert solucao == 7, solucao
