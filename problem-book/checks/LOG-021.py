"""LOG-021 — o silogismo não é válido: procura um contra-modelo."""
from itertools import product

# universo com 3 indivíduos; propriedades: gato, bigodes, preto
contra = None
for atribuicao in product([0, 1], repeat=9):
    gato = atribuicao[0:3]
    bigodes = atribuicao[3:6]
    preto = atribuicao[6:9]
    p1 = all(not gato[i] or bigodes[i] for i in range(3))        # todos os gatos têm bigodes
    p2 = any(bigodes[i] and preto[i] for i in range(3))          # alguns com bigodes são pretos
    conclusao = any(gato[i] and preto[i] for i in range(3))      # alguns gatos são pretos
    if p1 and p2 and not conclusao:
        contra = (gato, bigodes, preto)
        break

print("contra-modelo encontrado:", contra)
assert contra is not None, "sem contra-modelo o silogismo seria válido"
print("-> premissas verdadeiras e conclusão falsa: o argumento é inválido")
