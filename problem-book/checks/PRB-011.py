"""PRB-011 — valor esperado de um lançamento de dado e do jogo proposto."""
import random
from fractions import Fraction

esperado_dado = Fraction(sum(range(1, 7)), 6)
print("valor esperado de um dado:", esperado_dado)
assert esperado_dado == Fraction(7, 2)

# jogo: pagas 4 euros e recebes o valor do dado
lucro = esperado_dado - 4
print("jogo a 4 euros -> lucro esperado por jogada:", lucro, "=", float(lucro))
assert lucro == Fraction(-1, 2)

rng = random.Random(11)
N = 2_000_000
sim = sum(rng.randint(1, 6) - 4 for _ in range(N)) / N
print("simulado em %d jogadas: %.5f" % (N, sim))
assert abs(sim - float(lucro)) < 0.01
# preço justo
assert esperado_dado == Fraction(7, 2)
print("preço justo: 3,50 euros")
