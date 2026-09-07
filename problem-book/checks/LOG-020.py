"""LOG-020 — cinco piratas e 100 moedas: indução para trás.
Regra: a proposta passa com pelo menos metade dos votos (o proponente vota).
Um pirata só vota a favor se ganhar ESTRITAMENTE mais do que ganharia depois."""
MOEDAS = 100


def resultado(n):
    """Distribuição quando restam n piratas; índice 0 = o mais graduado."""
    if n == 1:
        return [MOEDAS]
    seguinte = resultado(n - 1)          # o que cada um dos outros teria sem ele
    futuro = [0] + seguinte              # alinhado com os índices actuais
    precisa = (n + 1) // 2 - 1           # votos além do próprio
    # compra os mais baratos: os que ficariam com menos
    candidatos = sorted(range(1, n), key=lambda i: (futuro[i], -i))
    dist = [0] * n
    gasto = 0
    for i in candidatos[:precisa]:
        dist[i] = futuro[i] + 1
        gasto += dist[i]
    dist[0] = MOEDAS - gasto
    return dist


for n in range(1, 6):
    print("  %d piratas -> %s" % (n, resultado(n)))
final = resultado(5)
assert final == [98, 0, 1, 0, 1], final
assert sum(final) == MOEDAS
