"""LOG-019 — três caixas, todas as etiquetas erradas.
Verifica que um só fruto resolve, e SÓ se for tirado da caixa «mistura»."""
from itertools import permutations

ETIQUETAS = ("maçãs", "laranjas", "mistura")

ARRANJOS = [c for c in permutations(ETIQUETAS)
            if all(x != e for x, e in zip(c, ETIQUETAS))]
print("arranjos com todas as etiquetas erradas:", len(ARRANJOS))
for a in ARRANJOS:
    print("   ", dict(zip(ETIQUETAS, a)))
assert len(ARRANJOS) == 2, ARRANJOS


def frutos_possiveis(conteudo):
    return {"maçãs": {"maçã"}, "laranjas": {"laranja"},
            "mistura": {"maçã", "laranja"}}[conteudo]


def resolve(caixa):
    """Tirar um fruto desta caixa identifica sempre o arranjo?"""
    for fruto in ("maçã", "laranja"):
        compativeis = [a for a in ARRANJOS if fruto in frutos_possiveis(a[caixa])]
        if len(compativeis) > 1:
            return False, fruto
    return True, None


for j, etiqueta in enumerate(ETIQUETAS):
    ok, culpado = resolve(j)
    print("  tirar da caixa «%-9s» -> %s" % (
        etiqueta, "resolve sempre" if ok else "ambíguo se sair %s" % culpado))

assert resolve(ETIQUETAS.index("mistura"))[0], "a caixa MISTURA tem de resolver"
assert not resolve(ETIQUETAS.index("maçãs"))[0]
assert not resolve(ETIQUETAS.index("laranjas"))[0]
print("-> só a caixa etiquetada MISTURA funciona")
