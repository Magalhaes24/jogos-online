"""LOG-005 — 8 moedas, uma mais pesada, balança de pratos.
Verifica que 2 pesagens chegam e que 1 não chega."""
from itertools import product

N = 8


def pesa(esq, dir_, pesada):
    e = sum(1 for c in esq if c == pesada)
    d = sum(1 for c in dir_ if c == pesada)
    return "esq" if e > d else ("dir" if d > e else "igual")


# estratégia: 3 vs 3; depois 1 vs 1 dentro do grupo identificado
def resolve(pesada):
    r1 = pesa([0, 1, 2], [3, 4, 5], pesada)
    grupo = {"esq": [0, 1, 2], "dir": [3, 4, 5], "igual": [6, 7]}[r1]
    if len(grupo) == 2:
        return grupo[0] if pesa([grupo[0]], [grupo[1]], pesada) == "esq" else grupo[1]
    r2 = pesa([grupo[0]], [grupo[1]], pesada)
    return {"esq": grupo[0], "dir": grupo[1], "igual": grupo[2]}[r2]


for pesada in range(N):
    assert resolve(pesada) == pesada, pesada
print("estratégia de 2 pesagens: identifica as 8 moedas correctamente")

# limite inferior: uma pesagem tem 3 resultados possíveis < 8 hipóteses
assert 3 ** 1 < N <= 3 ** 2
print("limite: 3^1 =", 3, "< 8 <=", 9, "= 3^2  -> 1 pesagem é impossível, 2 chegam")
