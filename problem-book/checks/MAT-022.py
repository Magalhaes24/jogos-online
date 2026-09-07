"""MAT-022 — soma de todos os dígitos dos números de 1 a 1000."""
directo = sum(sum(int(d) for d in str(k)) for k in range(1, 1001))
# argumento por simetria: 000..999 são 1000 números com 3 dígitos cada,
# cada dígito uniformemente distribuído por 0..9 -> média 4,5 por posição
simetria = 3 * 1000 * 45 // 10 + 1        # +1 do "1" de 1000
print("contagem directa:", directo, "· por simetria:", simetria)
assert directo == simetria == 13501, (directo, simetria)
