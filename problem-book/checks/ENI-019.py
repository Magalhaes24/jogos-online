"""ENI-019 — sequência 2, 3, 5, 9, 17: cada termo é o dobro do anterior menos 1."""
seq = [2]
for _ in range(6):
    seq.append(seq[-1] * 2 - 1)
print("regra a(n) = 2*a(n-1) - 1 ->", seq)
assert seq[:5] == [2, 3, 5, 9, 17]
assert seq[5] == 33, seq[5]

# a regra equivalente: as diferenças duplicam
difs = [b - a for a, b in zip(seq, seq[1:])]
print("diferenças:", difs)
assert difs[:4] == [1, 2, 4, 8]
assert difs[4] == 16
# forma fechada: a(n) = 2^n + 1
fechada = [2 ** n + 1 for n in range(7)]
assert fechada == seq, (fechada, seq)
print("forma fechada: a(n) = 2^n + 1")
