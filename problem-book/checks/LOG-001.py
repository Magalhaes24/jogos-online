"""LOG-001 — enumera os 3 mundos e exige exactamente uma solução."""
sols = []
for ouro in "ABC":
    etiquetas = [ouro == "A",      # A: «o ouro está nesta caixa»
                 ouro != "B",      # B: «o ouro não está nesta caixa»
                 ouro != "A"]      # C: «o ouro não está na caixa A»
    if sum(etiquetas) == 1:
        sols.append(ouro)

print("mundos possíveis: 3 · soluções:", sols)
assert sols == ["B"], sols
