"""MAT-029 — 100 m de rede encostada a um muro: área máxima."""
from fractions import Fraction

REDE = 100
melhor = max(((Fraction(REDE - 2 * x) * x, x) for x in range(1, REDE // 2)),
             key=lambda t: t[0])
area, lado = melhor
print("máximo discreto: x = %d m (os dois lados perpendiculares), área = %s m2"
      % (lado, area))
assert lado == 25 and area == 1250

# sem muro, o mesmo perímetro dá menos área
sem_muro = max(Fraction(x) * (Fraction(REDE, 2) - x) for x in range(1, 50))
print("sem muro, com os mesmos 100 m: área máxima =", sem_muro, "m2 (quadrado 25x25)")
assert sem_muro == 625
assert area == 2 * sem_muro
