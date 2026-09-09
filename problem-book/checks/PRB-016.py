"""PRB-016 — regressão à média: os melhores do 1.º ano pioram sem causa nenhuma."""
import random
import statistics

rng = random.Random(16)
N = 20_000
# desempenho = talento (fixo) + sorte (nova em cada ano)
talento = [rng.gauss(0, 1) for _ in range(N)]
ano1 = [t + rng.gauss(0, 1) for t in talento]
ano2 = [t + rng.gauss(0, 1) for t in talento]

ordem = sorted(range(N), key=lambda i: ano1[i], reverse=True)
topo = ordem[:N // 100]                  # o 1% melhor do ano 1
fundo = ordem[-N // 100:]

m1_topo = statistics.mean(ano1[i] for i in topo)
m2_topo = statistics.mean(ano2[i] for i in topo)
m1_fundo = statistics.mean(ano1[i] for i in fundo)
m2_fundo = statistics.mean(ano2[i] for i in fundo)

print("melhor 1%%: ano1 %.2f -> ano2 %.2f  (piorou)" % (m1_topo, m2_topo))
print("pior   1%%: ano1 %.2f -> ano2 %.2f  (melhorou)" % (m1_fundo, m2_fundo))
assert m2_topo < m1_topo and m2_fundo > m1_fundo
# e não houve causa nenhuma: o talento não mudou
assert abs(statistics.mean(talento[i] for i in topo)
           - statistics.mean(ano2[i] for i in topo)) < 0.15
print("-> o talento não mudou; só a sorte deixou de estar toda do mesmo lado")
