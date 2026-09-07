"""MAT-020 — o caracol no poço: simula dia a dia."""
POCO, SOBE, DESCE = 30, 3, 2
altura, dia = 0, 0
while True:
    dia += 1
    altura += SOBE
    if altura >= POCO:
        break
    altura -= DESCE
print("sai no dia", dia, "· altura ao fim do dia anterior:", POCO - SOBE)
assert dia == 28, dia
# a resposta ingénua (30/1 = 30) ignora que o último dia não tem noite
assert POCO // (SOBE - DESCE) == 30
