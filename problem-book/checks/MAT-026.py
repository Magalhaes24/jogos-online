"""MAT-026 — 51 números de 1..100: há sempre um que divide outro.
Prova pela construção das 50 cadeias de parte ímpar."""
import random

def parte_impar(n):
    while n % 2 == 0:
        n //= 2
    return n


cadeias = {}
for n in range(1, 101):
    cadeias.setdefault(parte_impar(n), []).append(n)
print("cadeias (uma por parte ímpar):", len(cadeias))
assert len(cadeias) == 50, len(cadeias)

# dentro de uma cadeia, cada elemento divide o seguinte
for base, membros in cadeias.items():
    membros.sort()
    for a, b in zip(membros, membros[1:]):
        assert b % a == 0, (a, b)

# 51 números -> pelo menos dois na mesma cadeia (pombal)
rng = random.Random(26)
for _ in range(5000):
    esc = rng.sample(range(1, 101), 51)
    assert any(a != b and max(a, b) % min(a, b) == 0
               for i, a in enumerate(esc) for b in esc[i + 1:]), esc
print("5000 escolhas aleatórias de 51 números · há sempre um par que se divide")

# com 50 é possível evitar: os 50 números de 51 a 100
sem_par = list(range(51, 101))
assert not any(a != b and max(a, b) % min(a, b) == 0
               for i, a in enumerate(sem_par) for b in sem_par[i + 1:])
print("com 50 já é possível evitar: {51, 52, ..., 100} não tem nenhum par assim")
