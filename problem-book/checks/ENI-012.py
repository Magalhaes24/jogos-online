"""ENI-012 — a sequência é feita das iniciais dos números por extenso."""
NUMEROS = ["um", "dois", "três", "quatro", "cinco", "seis",
           "sete", "oito", "nove", "dez", "onze", "doze"]
iniciais = [n[0].upper() for n in NUMEROS]
print("números:", NUMEROS[:10])
print("iniciais:", iniciais[:10])
assert iniciais[:9] == ["U", "D", "T", "Q", "C", "S", "S", "O", "N"]
assert iniciais[9] == "D", iniciais[9]
print("o 10.º termo é '%s' (de '%s')" % (iniciais[9], NUMEROS[9]))
# os dois S seguidos e os dois D confirmam que a regra é a inicial, não o valor
assert iniciais[5] == iniciais[6] == "S"
assert iniciais[1] == iniciais[9] == "D"
