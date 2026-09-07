"""LOG-032 — dez sacos, um só com moedas leves, UMA pesagem numa balança digital."""
NORMAL, LEVE, SACOS = 10.0, 9.0, 10

esperado = sum(range(1, SACOS + 1)) * NORMAL      # se nenhum fosse leve
observado = {}
for falso in range(1, SACOS + 1):
    peso = sum((LEVE if s == falso else NORMAL) * s for s in range(1, SACOS + 1))
    observado[falso] = round(esperado - peso, 6)

for saco, falta in observado.items():
    print("  saco %2d falso -> faltam %4.1f g" % (saco, falta))
assert len(set(observado.values())) == SACOS, "as leituras têm de ser todas distintas"
assert all(abs(observado[s] - s * (NORMAL - LEVE)) < 1e-9 for s in observado)
print("as 10 leituras são distintas -> uma pesagem identifica o saco")
