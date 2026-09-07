"""LOG-022 — as datas da Cheryl: enumeração passo a passo."""
DATAS = [("Maio", 15), ("Maio", 16), ("Maio", 19),
         ("Junho", 17), ("Junho", 18),
         ("Julho", 14), ("Julho", 16),
         ("Agosto", 14), ("Agosto", 15), ("Agosto", 17)]


def dias(cands, mes):
    return [d for m, d in cands if m == mes]


def meses(cands, dia):
    return [m for m, d in cands if d == dia]


c = list(DATAS)
# 1) Albert (sabe o mês): «eu não sei, e sei que o Bernardo também não sabe»
#    => no mês do Albert nenhum dia é único em toda a lista
unicos = {d for m, d in c if len(meses(c, d)) == 1}
c1 = [(m, d) for m, d in c if not any(dd in unicos for mm, dd in c if mm == m)]
print("1) após Albert:", c1)

# 2) Bernardo (sabe o dia): «não sabia, mas agora sei» => o dia é único em c1
c2 = [(m, d) for m, d in c1 if len(meses(c1, d)) == 1]
print("2) após Bernardo:", c2)

# 3) Albert: «agora também sei» => o mês é único em c2
c3 = [(m, d) for m, d in c2 if len(dias(c2, m)) == 1]
print("3) após Albert:", c3)

assert len(c3) == 1 and c3[0] == ("Julho", 16), c3
