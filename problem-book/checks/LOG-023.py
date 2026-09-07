"""LOG-023 — 100 moedas às escuras, 10 com a cara para cima.
Separar 10 e virá-las iguala sempre o número de caras."""
TOTAL, CARAS, PILHA = 100, 10, 10

for k in range(0, min(CARAS, PILHA) + 1):        # caras que calharam na pilha de 10
    pilha_apos_virar = PILHA - k                  # as coroas viradas passam a caras
    resto = CARAS - k
    assert pilha_apos_virar == resto, (k, pilha_apos_virar, resto)
    print("  k=%2d caras na pilha -> depois de virar: %2d vs %2d no resto  OK"
          % (k, pilha_apos_virar, resto))

print("funciona para todos os %d casos possíveis, sem saber qual é qual"
      % (min(CARAS, PILHA) + 1))
