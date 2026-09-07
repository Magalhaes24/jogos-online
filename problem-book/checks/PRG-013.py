"""PRG-013 — máximo e mínimo em simultâneo.
Conta as comparações de facto e confronta-as com o limite 3n/2 - 2."""
import math
import random

rng = random.Random(13)


class Contador:
    def __init__(self):
        self.n = 0

    def maior(self, a, b):
        self.n += 1
        return a > b


def ingenuo(xs, c):
    mx = mn = xs[0]
    for x in xs[1:]:
        if c.maior(x, mx):
            mx = x
        if c.maior(mn, x):
            mn = x
    return mx, mn


def aos_pares(xs, c):
    """Compara os elementos dois a dois ANTES de os confrontar com os extremos.
    A paridade é tratada no arranque, não no fim."""
    n = len(xs)
    if n % 2 == 0:
        mx, mn = (xs[0], xs[1]) if c.maior(xs[0], xs[1]) else (xs[1], xs[0])
        i = 2
    else:
        mx = mn = xs[0]
        i = 1
    while i < n:
        a, b = xs[i], xs[i + 1]
        if c.maior(a, b):            # 1: garante a <= b
            a, b = b, a
        if not c.maior(a, mn):       # 2: só o menor do par disputa o mínimo
            mn = a
        if c.maior(b, mx):           # 3: só o maior do par disputa o máximo
            mx = b
        i += 2
    return mx, mn


for n in (2, 3, 8, 9, 100, 101, 1000):
    xs = [rng.randrange(10 ** 6) for _ in range(n)]
    c1, c2 = Contador(), Contador()
    r1, r2 = ingenuo(xs, c1), aos_pares(xs, c2)
    assert r1 == r2 == (max(xs), min(xs)), (n, r1, r2)
    limite = math.ceil(3 * n / 2) - 2
    print("n=%4d · ingénuo: %4d · aos pares: %4d · limite 3n/2-2 = %d"
          % (n, c1.n, c2.n, limite))
    assert c1.n == 2 * (n - 1), c1.n
    assert c2.n == limite, (c2.n, limite)

print("-> o método aos pares atinge exactamente o limite teórico")
