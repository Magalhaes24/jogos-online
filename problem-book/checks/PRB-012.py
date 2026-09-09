"""PRB-012 — os dois envelopes: trocar não ganha nada.
O paradoxo desaparece quando o mecanismo de geração é declarado."""
import random

rng = random.Random(12)
N = 500_000
ganho_trocando = 0
for _ in range(N):
    x = rng.choice([1, 2, 5, 10, 20, 50])       # prior explícito
    envelopes = [x, 2 * x]
    rng.shuffle(envelopes)
    escolhido, outro = envelopes
    ganho_trocando += outro - escolhido

media = ganho_trocando / N
print("ganho médio por trocar, em %d rondas: %.4f" % (N, media))
assert abs(media) < 0.2, media

# o raciocínio falacioso: "tenho A, o outro vale 2A ou A/2, logo 1,25A"
falacia = 0.5 * 2 + 0.5 * 0.5
print("o cálculo falacioso dá 1,25 x o que tenho -> %.2f" % falacia)
assert abs(falacia - 1.25) < 1e-9
print("erro: 'A' significa coisas diferentes nos dois ramos (o par é (A,2A) ou (A/2,A))")
