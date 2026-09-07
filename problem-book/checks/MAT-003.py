"""MAT-003 — expoente de 5 em 100!, por Legendre e por contagem directa."""
def zeros_legendre(n, p=5):
    total, q = 0, p
    while q <= n:
        total += n // q
        q *= p
    return total


def zeros_directo(n):
    """Conta factores 5 multiplicando de facto (lento mas independente)."""
    c, prod = 0, 1
    for k in range(2, n + 1):
        prod *= k
    while prod % 10 == 0:
        prod //= 10
        c += 1
    return c


a, b = zeros_legendre(100), zeros_directo(100)
print("Legendre:", a, "· contagem directa em 100!:", b)
assert a == b == 24, (a, b)
