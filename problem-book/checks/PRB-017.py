"""PRB-017 — «alguém com o MEU aniversário» é muito mais raro."""
from fractions import Fraction

def alguem_comigo(n, dias=365):
    return 1 - Fraction(dias - 1, dias) ** n


def dois_quaisquer(n, dias=365):
    p = Fraction(1)
    for k in range(n):
        p *= Fraction(dias - k, dias)
    return 1 - p


for n in (23, 50, 253):
    print("  %3d pessoas: dois quaisquer %.4f · alguém comigo %.4f"
          % (n, float(dois_quaisquer(n)), float(alguem_comigo(n))))
assert float(alguem_comigo(23)) < 0.07
assert float(dois_quaisquer(23)) > 0.50
assert float(alguem_comigo(252)) < 0.5 < float(alguem_comigo(253))
print("são precisas 253 pessoas para passar de 50% no caso comigo")
