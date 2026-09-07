"""LOG-013 — 100 cacifos, 100 passagens: ficam abertos os quadrados perfeitos."""
cacifos = [False] * 101
for passagem in range(1, 101):
    for c in range(passagem, 101, passagem):
        cacifos[c] = not cacifos[c]

abertos = [c for c in range(1, 101) if cacifos[c]]
print("abertos:", abertos, "· total:", len(abertos))
assert abertos == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
assert len(abertos) == 10
# porquê: o número de divisores só é ímpar nos quadrados perfeitos
for c in range(1, 101):
    div = sum(1 for d in range(1, c + 1) if c % d == 0)
    assert (div % 2 == 1) == (c in abertos), c
