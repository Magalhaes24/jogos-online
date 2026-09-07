"""MAT-006 — soma de 1 a 100 pelo emparelhamento de Gauss."""
directo = sum(range(1, 101))
gauss = 100 * 101 // 2
pares = 50 * 101                     # 50 pares que somam 101 cada
print("soma directa:", directo, "· n(n+1)/2:", gauss, "· 50 pares de 101:", pares)
assert directo == gauss == pares == 5050
for n in (10, 1000, 12345):
    assert sum(range(1, n + 1)) == n * (n + 1) // 2
print("a fórmula confere para n = 10, 1000 e 12345")
