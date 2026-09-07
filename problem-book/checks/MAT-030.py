"""MAT-030 — último algarismo de 7^2026."""
ciclo = [pow(7, k, 10) for k in range(1, 9)]
print("últimos algarismos de 7^1..7^8:", ciclo)
assert ciclo[:4] == [7, 9, 3, 1] and ciclo[4:8] == [7, 9, 3, 1]

resto = 2026 % 4
esperado = [1, 7, 9, 3][resto]          # resto 0 -> 7^4 -> 1
print("2026 mod 4 =", resto, "-> último algarismo:", esperado)
assert pow(7, 2026, 10) == esperado == 9
# controlo com o valor completo, para não haver dúvidas
assert int(str(7 ** 2026)[-1]) == 9
print("confirmado calculando 7^2026 por inteiro (%d algarismos)" % len(str(7 ** 2026)))
