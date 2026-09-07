"""MAT-019 — 1 - 2 + 3 - 4 + ... + 99 - 100."""
total = sum(k if k % 2 else -k for k in range(1, 101))
pares = sum(1 - 2 for _ in range(50))     # 50 pares, cada um vale -1
print("soma alternada:", total, "· 50 pares de (-1):", pares)
assert total == pares == -50
# generalização: até 2n dá -n
for n in (3, 10, 500):
    assert sum(k if k % 2 else -k for k in range(1, 2 * n + 1)) == -n
print("até 2n a soma é sempre -n")
