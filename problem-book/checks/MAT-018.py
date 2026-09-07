"""MAT-018 — comboio a atravessar um túnel: percorre túnel + comprimento."""
comboio, tunel, v = 100, 200, 20      # metros, metros, m/s
distancia = tunel + comboio           # do focinho a entrar até a cauda a sair
print("distância percorrida:", distancia, "m · tempo:", distancia / v, "s")
assert distancia == 300
assert distancia / v == 15
# só o focinho a atravessar daria 10 s: falta o comprimento do próprio comboio
assert tunel / v == 10
