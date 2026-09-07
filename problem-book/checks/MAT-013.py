"""MAT-013 — anel circular: a área só depende da corda tangente."""
import math
import random

rng = random.Random(13)
CORDA = 20                                # comprimento da corda tangente

for _ in range(10000):
    r_interno = rng.uniform(0.001, 500)
    # a corda é tangente ao círculo interior: (corda/2)^2 + r_int^2 = r_ext^2
    r_externo = math.hypot(CORDA / 2, r_interno)
    area = math.pi * (r_externo ** 2 - r_interno ** 2)
    assert abs(area - math.pi * (CORDA / 2) ** 2) < 1e-6, (r_interno, area)

print("10 000 raios interiores diferentes · área do anel sempre = pi * 10^2")
print("area = %.6f (= 100 pi)" % (math.pi * 100))
