"""PRG-015 — concatenar strings num ciclo: quantos caracteres são copiados."""
def copias_concatenacao(n):
    """Modelo: s = s + x cria uma string nova e copia tudo o que já lá estava."""
    total = comprimento = 0
    for _ in range(n):
        total += comprimento          # copia o que já existe
        comprimento += 1
    return total


def copias_join(n):
    """join percorre a lista uma vez e escreve cada caractere uma só vez."""
    return n


for n in (10, 100, 1000):
    c, j = copias_concatenacao(n), copias_join(n)
    print("n=%5d · concatenação: %9d cópias · join: %5d · rácio %6.1fx"
          % (n, c, j, c / j))
    assert c == n * (n - 1) // 2, c
    assert j == n

# quadrático vs linear: dez vezes mais dados custa cem vezes mais trabalho
assert copias_concatenacao(1000) / copias_concatenacao(100) > 90
print("-> 10x mais dados = ~100x mais cópias: é O(n^2) contra O(n)")
