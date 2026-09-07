"""LOG-018 — 10 prisioneiros, chapéus a duas cores: a estratégia da paridade
salva sempre pelo menos 9. Testa as 1024 configurações."""
from itertools import product

N = 10
piores = N


def simula(chapeus):
    """Índice 0 = o de trás (vê todos os outros). Cor: 0 ou 1."""
    salvos = 0
    # o de trás anuncia a paridade do que vê e arrisca a própria vida
    paridade = sum(chapeus[1:]) % 2
    salvos += paridade == chapeus[0]
    conhecido = paridade
    for i in range(1, N):
        a_frente = sum(chapeus[i + 1:]) % 2
        palpite = (conhecido - a_frente) % 2      # deduz a própria cor
        salvos += palpite == chapeus[i]
        conhecido = (conhecido - chapeus[i]) % 2  # actualiza com o que ouviu
    return salvos


for chapeus in product([0, 1], repeat=N):
    s = simula(chapeus)
    assert s >= N - 1, (chapeus, s)
    piores = min(piores, s)

print("configurações testadas: %d · pior caso: %d salvos de %d" % (2 ** N, piores, N))
assert piores == N - 1
