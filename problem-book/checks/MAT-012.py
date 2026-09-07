"""MAT-012 — a bola que ressalta metade da altura: distância total percorrida."""
from fractions import Fraction

h, r = Fraction(10), Fraction(1, 2)

# soma numérica, sem fórmula
total, altura = Fraction(0), h
for _ in range(200):
    total += altura                 # descida
    altura *= r
    total += altura                 # subida
total_truncado = float(total)

formula = h + 2 * h * r / (1 - r)   # queda inicial + subidas e descidas
print("soma de 200 ressaltos: %.10f m · fórmula: %s m" % (total_truncado, formula))
assert formula == 30, formula
assert abs(total_truncado - 30) < 1e-9
print("a série converge: percorre 30 m em distância, num tempo também finito")
