"""ENI-025 — sequência 1, 2, 6, 24, 120: factoriais."""
from math import factorial
seq = [factorial(n) for n in range(1, 8)]
print("factoriais 1! a 7!:", seq)
assert seq[:5] == [1, 2, 6, 24, 120]
assert seq[5] == 720, seq[5]

# a regra por multiplicação: cada termo é o anterior vezes a posição
por_multiplicacao = [1]
for n in range(2, 8):
    por_multiplicacao.append(por_multiplicacao[-1] * n)
assert por_multiplicacao == seq
razoes = [b // a for a, b in zip(seq, seq[1:])]
print("razões entre termos consecutivos:", razoes)
assert razoes == [2, 3, 4, 5, 6, 7]
