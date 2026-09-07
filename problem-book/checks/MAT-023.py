"""MAT-023 — invariante: apagar a e b, escrever |a-b|. A paridade não muda."""
import random

rng = random.Random(23)
for _ in range(3000):
    nums = list(range(1, 101))
    paridade_inicial = sum(nums) % 2
    while len(nums) > 1:
        i, j = rng.sample(range(len(nums)), 2)
        a, b = nums[i], nums[j]
        for k in sorted((i, j), reverse=True):
            nums.pop(k)
        nums.append(abs(a - b))
        assert sum(nums) % 2 == paridade_inicial, "a paridade tem de se conservar"
    assert nums[0] % 2 == paridade_inicial

print("3000 sequências aleatórias de operações · soma 1..100 =", sum(range(1, 101)))
print("paridade inicial: par -> o número final é SEMPRE par")
assert sum(range(1, 101)) % 2 == 0
