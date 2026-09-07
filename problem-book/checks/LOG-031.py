"""LOG-031 — 21 fósforos, tirar 1 a 3, quem tira o último ganha.
Resolve o jogo por programação dinâmica."""
N, MAX = 21, 3
vence = [False] * (N + 1)          # vence[k] = quem joga com k fósforos ganha?
for k in range(1, N + 1):
    vence[k] = any(not vence[k - t] for t in range(1, MAX + 1) if t <= k)

perdedores = [k for k in range(N + 1) if not vence[k]]
print("posições perdedoras (para quem joga):", perdedores)
assert perdedores == [0, 4, 8, 12, 16, 20], perdedores
assert vence[N], "com 21 o primeiro jogador ganha"

jogada = next(t for t in range(1, MAX + 1) if not vence[N - t])
print("com 21 fósforos o 1.º jogador ganha tirando", jogada, "-> deixa", N - jogada)
assert jogada == 1 and (N - jogada) % 4 == 0
