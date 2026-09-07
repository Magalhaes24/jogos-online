"""LOG-028 — grelha 3x3: três amigos, três desportos, três cores."""
from itertools import permutations

P = ["Rita", "Simão", "Tiago"]
DESP = ["natação", "ténis", "corrida"]
COR = ["azul", "verde", "vermelho"]

PISTAS = [
    ("O Simão não faz natação.",    lambda d, c: d["Simão"] != "natação"),
    ("Quem corre veste vermelho.",  lambda d, c: c[next(x for x in P if d[x] == "corrida")] == "vermelho"),
    ("O Tiago joga ténis.",         lambda d, c: d["Tiago"] == "ténis"),
    ("O Tiago não veste azul.",     lambda d, c: c["Tiago"] != "azul"),
]
MUNDOS = [(dict(zip(P, d)), dict(zip(P, c)))
          for d in permutations(DESP) for c in permutations(COR)]


def resolve(pistas):
    return [m for m in MUNDOS if all(f(*m) for _, f in pistas)]


sols = resolve(PISTAS)
print("combinações: %d · soluções: %d" % (len(MUNDOS), len(sols)))
for d, c in sols:
    for x in P:
        print("   %-6s %-9s %s" % (x, d[x], c[x]))
assert len(sols) == 1, sols
d, c = sols[0]
assert d == {"Rita": "natação", "Simão": "corrida", "Tiago": "ténis"}
assert c == {"Rita": "azul", "Simão": "vermelho", "Tiago": "verde"}
for k in range(len(PISTAS)):
    assert len(resolve([p for j, p in enumerate(PISTAS) if j != k])) > 1, PISTAS[k][0]
print("as 4 pistas são todas necessárias")
