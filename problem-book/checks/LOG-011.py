"""LOG-011 — três lógicos ao balcão: cada «não sei» elimina mundos."""
from itertools import product

mundos = list(product([True, False], repeat=3))   # quer cerveja?

# 1.º: sabe responder «todos querem?» só se ELE não quiser (aí a resposta é não)
apos1 = [w for w in mundos if w[0]]
# 2.º: idem, sabendo já que o 1.º quer
apos2 = [w for w in apos1 if w[1]]
# 3.º diz «sim» => sabe que todos querem => ele próprio quer
apos3 = [w for w in apos2 if w[2]]

print("mundos:", len(mundos), "-> após 1.º «não sei»:", len(apos1),
      "-> após 2.º:", len(apos2), "-> após «sim»:", len(apos3), apos3)
assert apos3 == [(True, True, True)], apos3
