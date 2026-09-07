"""MAT-010 — velocidade média de ida e volta: média harmónica, não aritmética."""
from fractions import Fraction

d = Fraction(120)                       # distância só de ida (irrelevante)
t_ida, t_volta = d / 60, d / 40
media = (2 * d) / (t_ida + t_volta)
print("ida a 60: %s h · volta a 40: %s h · total %s h para %s km"
      % (t_ida, t_volta, t_ida + t_volta, 2 * d))
print("velocidade média:", media, "km/h")
assert media == 48, media
assert media != 50, "a média aritmética não se aplica"
# a resposta não depende da distância
for d2 in (1, 7, 1000):
    d2 = Fraction(d2)
    assert (2 * d2) / (d2 / 60 + d2 / 40) == 48
print("independente da distância · média harmónica de 60 e 40 = 48")
