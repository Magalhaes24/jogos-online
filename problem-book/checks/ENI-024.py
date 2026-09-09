"""ENI-024 — quantos quadrados cabem num tabuleiro 8x8 (de todos os tamanhos)."""
total = 0
for lado in range(1, 9):
    posicoes = (9 - lado) ** 2
    total += posicoes
    print("  quadrados %dx%d: %2d posições" % (lado, lado, posicoes))
print("total:", total)
assert total == 204

# contagem independente, por força bruta sobre cantos
bruto = sum(1 for lado in range(1, 9)
            for r in range(9 - lado) for c in range(9 - lado))
assert bruto == total == 204
# fórmula fechada: soma dos quadrados de 1 a 8
assert sum(k * k for k in range(1, 9)) == 204
