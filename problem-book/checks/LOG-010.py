"""LOG-010 — tabuleiro 8x8 sem dois cantos opostos: dominós não cobrem.
Prova por emparelhamento máximo (não por argumento verbal)."""
casas = [(r, c) for r in range(8) for c in range(8)
         if (r, c) not in {(0, 0), (7, 7)}]
brancas = [x for x in casas if (x[0] + x[1]) % 2 == 0]
pretas = [x for x in casas if (x[0] + x[1]) % 2 == 1]

adj = {b: [p for p in pretas if abs(b[0] - p[0]) + abs(b[1] - p[1]) == 1]
       for b in brancas}


def emparelhamento_maximo():
    par = {}

    def tenta(b, visto):
        for p in adj[b]:
            if p in visto:
                continue
            visto.add(p)
            if p not in par or tenta(par[p], visto):
                par[p] = b
                return True
        return False

    return sum(1 for b in brancas if tenta(b, set()))


m = emparelhamento_maximo()
print("casas:", len(casas), "· brancas:", len(brancas), "· pretas:", len(pretas))
print("emparelhamento máximo:", m, "dominós · necessários:", len(casas) // 2)
assert len(brancas) != len(pretas), "os cantos opostos têm de ter a mesma cor"
assert m == 30 < 31, m
print("-> impossível: sobram sempre 2 casas da mesma cor")
