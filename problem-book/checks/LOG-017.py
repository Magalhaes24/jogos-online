"""LOG-017 — ponte e lanterna: BFS sobre estados, tempo mínimo."""
import heapq

TEMPOS = {"A": 1, "B": 2, "C": 5, "D": 10}
TODOS = frozenset(TEMPOS)

inicio = (TODOS, "esq")
fim = (frozenset(), "dir")
dist = {inicio: 0}
fila = [(0, TODOS, "esq")]
melhor = None
while fila:
    t, esq, lanterna = heapq.heappop(fila)
    estado = (esq, lanterna)
    if estado == fim:
        melhor = t
        break
    if t > dist.get(estado, 1e9):
        continue
    if lanterna == "esq":                       # atravessam 1 ou 2 da esquerda
        cands = [frozenset(c) for n in (1, 2)
                 for c in __import__("itertools").combinations(esq, n)]
        for grupo in cands:
            nt = t + max(TEMPOS[p] for p in grupo)
            novo = (esq - grupo, "dir")
            if nt < dist.get(novo, 1e9):
                dist[novo] = nt
                heapq.heappush(fila, (nt, novo[0], "dir"))
    else:                                        # volta 1 ou 2 da direita
        direita = TODOS - esq
        cands = [frozenset(c) for n in (1, 2)
                 for c in __import__("itertools").combinations(direita, n)]
        for grupo in cands:
            nt = t + max(TEMPOS[p] for p in grupo)
            novo = (esq | grupo, "esq")
            if nt < dist.get(novo, 1e9):
                dist[novo] = nt
                heapq.heappush(fila, (nt, novo[0], "esq"))

print("tempo mínimo:", melhor, "minutos · estados:", len(dist))
assert melhor == 17, melhor
# o plano ingénuo (o mais rápido acompanha sempre) dá 19
ingenuo = 2 + 1 + 10 + 1 + 5    # A+B, A volta, A+D, A volta, A+C
assert ingenuo == 19
print("plano ingénuo (o mais rápido acompanha sempre):", ingenuo, "minutos")
