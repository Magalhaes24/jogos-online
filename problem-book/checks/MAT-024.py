"""MAT-024 — regra dos 72: a que taxa é que o dinheiro duplica em 10 anos?"""
import math

exacta = (2 ** (1 / 10) - 1) * 100
regra72 = 72 / 10
print("taxa exacta: %.4f%% · regra dos 72: %.1f%% · erro: %.2f pontos"
      % (exacta, regra72, abs(exacta - regra72)))
assert abs(exacta - 7.177) < 0.001
assert abs(exacta - regra72) < 0.05, "a regra tem de estar a menos de 0,05 pontos"

# a regra é boa para taxas entre 4% e 12%
for taxa in (4, 6, 8, 10, 12):
    anos_exacto = math.log(2) / math.log(1 + taxa / 100)
    anos_regra = 72 / taxa
    erro = abs(anos_exacto - anos_regra) / anos_exacto
    print("  %2d%% -> exacto %.2f anos · regra %.2f · erro %.1f%%"
          % (taxa, anos_exacto, anos_regra, erro * 100))
    assert erro < 0.035
