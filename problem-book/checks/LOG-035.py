"""LOG-035 — tarefa de selecção de Wason: que cartas é preciso virar."""
from itertools import product

VOGAIS, PARES = set("AEIOU"), {0, 2, 4, 6, 8}
CARTAS = [("A", None), ("K", None), (None, 4), (None, 7)]   # face visível


def pode_violar(carta):
    """Existe um verso que torne a regra falsa?
    Regra: se tem vogal de um lado, tem número par do outro."""
    letra, numero = carta
    if letra is not None:
        if letra not in VOGAIS:
            return False                      # consoante: a regra não diz nada
        return True                           # pode ter número ímpar do outro lado
    if numero in PARES:
        return False                          # par: com vogal ou consoante, cumpre
    return True                               # ímpar: se tiver vogal do outro lado, viola


precisa = [c for c in CARTAS if pode_violar(c)]
nomes = {("A", None): "A", ("K", None): "K", (None, 4): "4", (None, 7): "7"}
for c in CARTAS:
    print("  carta %-2s -> %s" % (nomes[c], "VIRAR" if pode_violar(c) else "irrelevante"))
assert [nomes[c] for c in precisa] == ["A", "7"], precisa
print("-> só A e 7. Virar o 4 não pode revelar nenhuma violação.")
