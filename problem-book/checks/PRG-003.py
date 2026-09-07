"""PRG-003 — o procedimento de 7 corridas encontra sempre o pódio certo.

Simula com velocidades aleatórias: as corridas só devolvem ordens relativas,
nunca os valores — é a mesma informação que o problema dá ao leitor.
"""
import random

N = 100_000
rng = random.Random(17)
corridas_usadas = set()

for _ in range(N):
    cavalos = list(range(25))
    rng.shuffle(cavalos)
    velocidade = {c: i for i, c in enumerate(sorted(cavalos, reverse=True))}

    def corre(grupo):
        assert len(grupo) <= 5, "a pista só tem 5 raias"
        return sorted(grupo, key=lambda c: velocidade[c])

    n_corridas = 0
    grupos = [corre(cavalos[i * 5:(i + 1) * 5]) for i in range(5)]  # corridas 1–5
    n_corridas += 5

    vencedores = corre([g[0] for g in grupos])                      # corrida 6
    n_corridas += 1
    ordem = {g[0]: i for i, g in enumerate(grupos)}
    a, b, c = (grupos[ordem[v]] for v in vencedores[:3])

    primeiro = a[0]
    candidatos = [a[1], a[2], b[0], b[1], c[0]]                     # 5 candidatos
    podio_2_3 = corre(candidatos)[:2]                               # corrida 7
    n_corridas += 1
    corridas_usadas.add(n_corridas)

    esperado = sorted(cavalos, key=lambda x: velocidade[x])[:3]
    assert [primeiro] + podio_2_3 == esperado, (esperado, [primeiro] + podio_2_3)

print(f"{N} torneios aleatórios · pódio correcto em todos "
      f"· corridas usadas: {sorted(corridas_usadas)}")
assert corridas_usadas == {7}, corridas_usadas
