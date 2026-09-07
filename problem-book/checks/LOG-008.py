"""LOG-008 — jarros de 5 e 3 litros: BFS para medir exactamente 4."""
from collections import deque

CAP = (5, 3)
inicio = (0, 0)
fila, dist = deque([inicio]), {inicio: 0}
alvo = None
while fila:
    e = fila.popleft()
    if 4 in e:
        alvo = (e, dist[e])
        break
    a, b = e
    seguintes = [(CAP[0], b), (a, CAP[1]), (0, b), (a, 0)]
    t = min(a, CAP[1] - b); seguintes.append((a - t, b + t))   # A -> B
    t = min(b, CAP[0] - a); seguintes.append((a + t, b - t))   # B -> A
    for s in seguintes:
        if s not in dist:
            dist[s] = dist[e] + 1
            fila.append(s)

print("estado alvo:", alvo[0], "· operações mínimas:", alvo[1],
      "· estados alcançáveis:", len(dist))
assert alvo[1] == 6, alvo
