"""PRB-003 — Monty Hall: simula as duas estratégias."""
import random

N = 1_000_000
rng = random.Random(3)
ganha_trocando = ganha_ficando = 0
for _ in range(N):
    carro = rng.randrange(3)
    escolha = rng.randrange(3)
    # o apresentador sabe onde está o carro e abre uma porta com cabra
    aberta = rng.choice([d for d in range(3) if d != escolha and d != carro])
    troca = next(d for d in range(3) if d not in (escolha, aberta))
    ganha_ficando += escolha == carro
    ganha_trocando += troca == carro

pt, pf = ganha_trocando / N, ganha_ficando / N
print("trocar:", round(pt, 4), "· ficar:", round(pf, 4), f"({N} jogos)")
assert abs(pt - 2 / 3) < 0.005, pt
assert abs(pf - 1 / 3) < 0.005, pf
assert pt > pf
