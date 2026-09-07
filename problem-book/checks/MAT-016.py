"""MAT-016 — badaladas: contam-se os INTERVALOS, não as badaladas."""
from fractions import Fraction

intervalos_6 = 6 - 1
intervalo = Fraction(5, intervalos_6)
tempo_12 = intervalo * (12 - 1)
print("6 badaladas = %d intervalos de %s s · 12 badaladas = %d intervalos = %s s"
      % (intervalos_6, intervalo, 11, tempo_12))
assert intervalo == 1 and tempo_12 == 11, (intervalo, tempo_12)
assert tempo_12 != 10, "10 seria a resposta se as badaladas durassem tempo"
