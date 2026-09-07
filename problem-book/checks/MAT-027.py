"""MAT-027 — divisibilidade por 9 pela soma dos algarismos."""
n = 123456789
soma = sum(int(d) for d in str(n))
print("%d -> soma dos algarismos = %d" % (n, soma))
assert soma == 45 and soma % 9 == 0
assert n % 9 == 0
# a regra funciona porque 10 = 9 + 1, logo 10^k deixa resto 1 na divisão por 9
for k in range(1, 12):
    assert 10 ** k % 9 == 1
# controlo em números ao acaso
import random
rng = random.Random(27)
for _ in range(20000):
    m = rng.randrange(1, 10 ** 9)
    assert (m % 9 == 0) == (sum(int(d) for d in str(m)) % 9 == 0)
print("regra confirmada em 20 000 números aleatórios")
