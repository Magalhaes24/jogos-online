"""PRB-009 — paradoxo de Simpson com números concretos (cálculos renais)."""
from fractions import Fraction

# (sucessos, total) por tratamento e por gravidade
dados = {
    "A": {"pedras pequenas": (81, 87), "pedras grandes": (192, 263)},
    "B": {"pedras pequenas": (234, 270), "pedras grandes": (55, 80)},
}

for grupo in ("pedras pequenas", "pedras grandes"):
    a, b = dados["A"][grupo], dados["B"][grupo]
    ta, tb = Fraction(*a), Fraction(*b)
    print("%-16s A: %3d/%3d = %.1f%%   B: %3d/%3d = %.1f%%"
          % (grupo, *a, float(ta) * 100, *b, float(tb) * 100))
    assert ta > tb, grupo          # A ganha nos DOIS subgrupos

globais = {}
for t in "AB":
    s = sum(x[0] for x in dados[t].values())
    n = sum(x[1] for x in dados[t].values())
    globais[t] = Fraction(s, n)
    print("total %s: %3d/%3d = %.1f%%" % (t, s, n, float(globais[t]) * 100))

assert globais["B"] > globais["A"], "no total, B tem de ganhar"
print("-> A ganha nos dois subgrupos e perde no total: paradoxo de Simpson")
# a causa: A recebeu sobretudo os casos difíceis
assert dados["A"]["pedras grandes"][1] > dados["A"]["pedras pequenas"][1]
assert dados["B"]["pedras pequenas"][1] > dados["B"]["pedras grandes"][1]
