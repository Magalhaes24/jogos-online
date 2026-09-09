"""PRB-008 — dois filhos, pelo menos um rapaz. O mecanismo é declarado:
escolhe-se ao acaso uma família com dois filhos DE ENTRE as que têm rapaz."""
import random
from fractions import Fraction
from itertools import product

familias = list(product("RM", repeat=2))          # R = rapaz, M = rapariga
com_rapaz = [f for f in familias if "R" in f]
dois_rapazes = [f for f in com_rapaz if f == ("R", "R")]
exacto = Fraction(len(dois_rapazes), len(com_rapaz))
print("famílias:", familias)
print("com pelo menos um rapaz:", com_rapaz, "-> dois rapazes:", dois_rapazes)
assert exacto == Fraction(1, 3)

rng = random.Random(8)
N, casos, favoraveis = 2_000_000, 0, 0
for _ in range(N):
    f = (rng.choice("RM"), rng.choice("RM"))
    if "R" in f:
        casos += 1
        favoraveis += f == ("R", "R")
sim = favoraveis / casos
print("exacto 1/3 = %.5f · simulado %.5f" % (1 / 3, sim))
assert abs(sim - 1 / 3) < 0.005

# variante com outro mecanismo: "o mais velho é rapaz" dá 1/2
mais_velho = [f for f in familias if f[0] == "R"]
assert Fraction(sum(1 for f in mais_velho if f == ("R", "R")), len(mais_velho)) == Fraction(1, 2)
print("com «o mais velho é rapaz» a resposta seria 1/2: o mecanismo importa")
