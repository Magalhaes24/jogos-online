"""LOG-002 — 3 brancos + 2 pretos, três posições; a cadeia de «nãos» tem de
deixar exactamente uma cor possível para quem está à frente."""
from collections import Counter
from itertools import product

POS = ("retaguarda", "meio", "frente")


def valido(w):
    c = Counter(w)
    return c["B"] <= 3 and c["P"] <= 2


mundos = [w for w in product("BP", repeat=3) if valido(w)]

# a retaguarda diz «não» => não vê dois pretos à frente
apos_1 = [w for w in mundos if not (w[1] == "P" and w[2] == "P")]


def meio_saberia(w):
    """O meio vê só a frente; deduz a partir do «não» da retaguarda."""
    possiveis = {c for c in "BP"
                 if valido((w[0], c, w[2])) and not (c == "P" and w[2] == "P")}
    return len(possiveis) == 1


apos_2 = [w for w in apos_1 if not meio_saberia(w)]
cores = sorted({w[2] for w in apos_2})

print("mundos:", len(mundos), "· após 1.º não:", len(apos_1),
      "· após 2.º não:", len(apos_2), "· cores possíveis à frente:", cores)
assert cores == ["B"], cores
