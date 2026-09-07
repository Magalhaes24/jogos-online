"""MAT-014 — estimativa de Fermi: bolas de ténis num autocarro.
Verifica que a estimativa cai na ordem de grandeza certa, com margens largas."""
import math

# volume interior do autocarro: intervalos plausíveis, não valores exactos
comp = (10, 13)      # metros
larg = (2.3, 2.6)
alt = (1.9, 2.3)
DIAM = 0.067         # bola de ténis, norma ITF: 6,54 a 6,86 cm
EMPACOTAMENTO = (0.55, 0.70)   # aleatório denso a cúbico de faces centradas

v_bola = (4 / 3) * math.pi * (DIAM / 2) ** 3
baixo = comp[0] * larg[0] * alt[0] * EMPACOTAMENTO[0] / v_bola
alto = comp[1] * larg[1] * alt[1] * EMPACOTAMENTO[1] / v_bola

print("volume de uma bola: %.2e m3" % v_bola)
print("estimativa: entre %.0f e %.0f bolas" % (baixo, alto))
print("ordem de grandeza: 10^%d a 10^%d" % (math.floor(math.log10(baixo)),
                                            math.floor(math.log10(alto))))
assert math.floor(math.log10(baixo)) == math.floor(math.log10(alto)) == 5
print("-> centenas de milhares: 10^5, robusto a todas as escolhas plausíveis")
