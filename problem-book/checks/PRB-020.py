"""PRB-020 — truque de von Neumann: sorteio justo com moeda viciada."""
import random

rng = random.Random(20)


def justo(p):
    """Lança aos pares; ignora CC e KK; devolve o primeiro do par CK/KC."""
    while True:
        a = rng.random() < p
        b = rng.random() < p
        if a != b:
            return a


for p in (0.5, 0.8, 0.1, 0.99):
    N = 200_000
    caras = sum(justo(p) for _ in range(N)) / N
    print("moeda com p=%.2f -> proporção do truque: %.4f" % (p, caras))
    assert abs(caras - 0.5) < 0.01, (p, caras)

# porquê: P(CK) = p(1-p) = P(KC), sejam quais forem os valores
for p in (0.1, 0.37, 0.8):
    assert abs(p * (1 - p) - (1 - p) * p) < 1e-15
print("-> P(CK) = p(1-p) = P(KC): a simetria não depende de p")
