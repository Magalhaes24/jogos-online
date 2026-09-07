"""LOG-027 — soma e produto (o «puzzle impossível»): 1 < x < y e x + y <= 100."""
from collections import defaultdict

pares = [(x, y) for x in range(2, 100) for y in range(x + 1, 100) if x + y <= 100]
por_soma, por_prod = defaultdict(list), defaultdict(list)
for x, y in pares:
    por_soma[x + y].append((x, y))
    por_prod[x * y].append((x, y))


def p_sabe(par):
    return len(por_prod[par[0] * par[1]]) == 1


# 1) P: «não sei» ; 2) S: «eu sabia que não sabias»
cands = [p for p in pares if not p_sabe(p)]
somas_ok = {s for s, ps in por_soma.items() if all(not p_sabe(p) for p in ps)}
c1 = [p for p in cands if p[0] + p[1] in somas_ok]

# 3) P: «agora já sei»
prod_count = defaultdict(list)
for p in c1:
    prod_count[p[0] * p[1]].append(p)
c2 = [p for p in c1 if len(prod_count[p[0] * p[1]]) == 1]

# 4) S: «então também sei»
soma_count = defaultdict(list)
for p in c2:
    soma_count[p[0] + p[1]].append(p)
c3 = [p for p in c2 if len(soma_count[p[0] + p[1]]) == 1]

print("pares iniciais:", len(pares), "-> após 1 e 2:", len(c1),
      "-> após 3:", len(c2), "-> após 4:", len(c3))
print("solução:", c3)
assert c3 == [(4, 13)], c3
