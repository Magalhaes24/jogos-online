"""MAT-007 — o lírio que duplica todos os dias."""
area = 1
dia = 0
while area < 2 ** 48:
    area *= 2
    dia += 1
assert dia == 48
metade = 2 ** 48 / 2
print("no dia 48 o lago está cheio (%d unidades)" % 2 ** 48)
print("metade =", int(metade), "= área do dia", 47)
assert 2 ** 47 == metade
# a resposta intuitiva (24) está errada por um factor enorme
assert 2 ** 24 / 2 ** 48 < 1e-7
print("no dia 24 o lírio cobre %.9f%% do lago" % (100 * 2 ** 24 / 2 ** 48))
