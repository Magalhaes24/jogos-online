"""LOG-012 — apertos de mão: 3 casais, respostas 0..4 todas diferentes.
Enumera todos os grafos possíveis (2^12) e exige solução única."""
from itertools import combinations

PESSOAS = list(range(6))          # 0 = eu, 1 = a minha mulher, (2,3) e (4,5) casais
CASAIS = {(0, 1), (2, 3), (4, 5)}


def conjuges(a, b):
    return (min(a, b), max(a, b)) in CASAIS


ARESTAS = [e for e in combinations(PESSOAS, 2) if not conjuges(*e)]
assert len(ARESTAS) == 12

sols = []
for mask in range(1 << len(ARESTAS)):
    grau = [0] * 6
    for k, (a, b) in enumerate(ARESTAS):
        if mask >> k & 1:
            grau[a] += 1
            grau[b] += 1
    # as 5 respostas dos outros (todos menos eu) são 0,1,2,3,4 todas diferentes
    if sorted(grau[1:]) == [0, 1, 2, 3, 4]:
        sols.append(grau[1])

print("grafos testados: %d · valores possíveis para a minha mulher: %s"
      % (1 << len(ARESTAS), sorted(set(sols))))
assert set(sols) == {2}, sorted(set(sols))
