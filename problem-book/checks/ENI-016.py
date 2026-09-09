"""ENI-016 — o único número de 1 a 20 cujo nome tem tantas letras quanto o valor."""
NOMES = {1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco", 6: "seis",
         7: "sete", 8: "oito", 9: "nove", 10: "dez", 11: "onze", 12: "doze",
         13: "treze", 14: "catorze", 15: "quinze", 16: "dezasseis",
         17: "dezassete", 18: "dezoito", 19: "dezanove", 20: "vinte"}

coincidem = [n for n, nome in NOMES.items() if len(nome) == n]
for n, nome in NOMES.items():
    marca = "  <--" if len(nome) == n else ""
    print("  %2d  %-10s %2d letras%s" % (n, nome, len(nome), marca))
assert coincidem == [5], coincidem
