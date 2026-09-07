"""LOG-026 — pombal com números reais: cabelos numa cidade."""
HABITANTES = 1_000_000
MAX_CABELOS = 150_000          # limite superior conhecido para uma cabeça humana

gavetas = MAX_CABELOS + 1      # 0, 1, ..., 150000
print("habitantes:", HABITANTES, "· valores possíveis de nº de cabelos:", gavetas)
assert HABITANTES > gavetas, "sem excesso de pombos não há garantia"

# quantos partilham garantidamente o mesmo valor, no pior caso
import math
minimo = math.ceil(HABITANTES / gavetas)
print("no pior caso, algum valor é partilhado por pelo menos", minimo, "pessoas")
assert minimo >= 2
# e se a cidade tivesse só 150 000 habitantes, não haveria garantia
assert math.ceil(150_000 / gavetas) == 1
print("com 150 000 habitantes a garantia desapareceria -> o número importa")
