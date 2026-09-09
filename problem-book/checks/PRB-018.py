"""PRB-018 — paradoxo da inspecção: autocarros de 10 em 10 minutos EM MÉDIA,
mas quem chega ao acaso espera 10 minutos, não 5."""
import random
import statistics

rng = random.Random(18)
MEDIA = 10.0

# chegadas de Poisson: intervalos exponenciais de média 10
intervalos = [rng.expovariate(1 / MEDIA) for _ in range(200_000)]
print("intervalo médio entre autocarros: %.3f min" % statistics.mean(intervalos))
assert abs(statistics.mean(intervalos) - MEDIA) < 0.2

# um passageiro chega num instante ao acaso: cai num intervalo com
# probabilidade proporcional ao COMPRIMENTO desse intervalo
total = sum(intervalos)
esperas = []
for _ in range(200_000):
    alvo = rng.uniform(0, total)
    acumulado = 0.0
    for iv in intervalos:
        if acumulado + iv > alvo:
            esperas.append(acumulado + iv - alvo)
            break
        acumulado += iv
    if len(esperas) >= 20_000:
        break

espera = statistics.mean(esperas)
print("espera média de quem chega ao acaso: %.3f min (em %d chegadas)"
      % (espera, len(esperas)))
assert abs(espera - MEDIA) < 1.5, espera

# o intervalo em que o passageiro cai é, em média, o dobro do intervalo típico
print("-> a espera é ~10 min, não 5: cai-se mais vezes nos intervalos longos")
