"""MAT-009 — inclusão-exclusão: múltiplos de 3 ou de 5 até 1000."""
directo = sum(1 for k in range(1, 1001) if k % 3 == 0 or k % 5 == 0)
tres, cinco, quinze = 1000 // 3, 1000 // 5, 1000 // 15
formula = tres + cinco - quinze
print("múltiplos de 3: %d · de 5: %d · de 15: %d" % (tres, cinco, quinze))
print("contagem directa: %d · 333 + 200 - 66 = %d" % (directo, formula))
assert directo == formula == 467
# sem subtrair a intersecção dava 533 — erro de 66
assert tres + cinco == 533
