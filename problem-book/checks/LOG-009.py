"""LOG-009 — grelha 4x4. Exige solução única e nenhuma pista redundante."""
from itertools import permutations

P = ["Ana", "Bruno", "Carla", "Diogo"]
INSTR = ["piano", "violino", "bateria", "guitarra"]
CIDADE = ["Porto", "Lisboa", "Braga", "Faro"]


def quem(i, instr):
    return next(x for x in P if i[x] == instr)


PISTAS = [
    ("O Bruno vive em Lisboa.",            lambda i, c: c["Bruno"] == "Lisboa"),
    ("A Carla toca violino ou guitarra.",  lambda i, c: i["Carla"] in ("violino", "guitarra")),
    ("Quem toca bateria vive no Porto.",   lambda i, c: c[quem(i, "bateria")] == "Porto"),
    ("A Ana não vive em Faro.",            lambda i, c: c["Ana"] != "Faro"),
    ("A Ana não toca bateria.",            lambda i, c: i["Ana"] != "bateria"),
    ("Quem toca violino vive em Braga.",   lambda i, c: c[quem(i, "violino")] == "Braga"),
]

MUNDOS = [(dict(zip(P, i)), dict(zip(P, c)))
          for i in permutations(INSTR) for c in permutations(CIDADE)]


def resolve(pistas):
    return [m for m in MUNDOS if all(f(*m) for _, f in pistas)]


sols = resolve(PISTAS)
print("combinações: %d · soluções: %d" % (len(MUNDOS), len(sols)))
assert len(sols) == 1, sols

i, c = sols[0]
for x in P:
    print("   %-6s %-9s %s" % (x, i[x], c[x]))
assert i == {"Ana": "violino", "Bruno": "piano", "Carla": "guitarra", "Diogo": "bateria"}
assert c == {"Ana": "Braga", "Bruno": "Lisboa", "Carla": "Faro", "Diogo": "Porto"}

# nenhuma pista pode ser dispensável
for k in range(len(PISTAS)):
    resto = [p for j, p in enumerate(PISTAS) if j != k]
    n = len(resolve(resto))
    assert n > 1, "pista redundante: " + PISTAS[k][0]
print("todas as 6 pistas são necessárias")
