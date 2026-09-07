"""ENI-003 — exactamente uma afirmação verdadeira; uma única solução."""
sols = []
for culpado in ("Rui", "Sara", "Tomás"):
    rui = culpado != "Rui"          # «não fui eu»
    sara = culpado == "Tomás"       # «foi o Tomás»
    tomas = not sara                # «a Sara está a mentir»
    if [rui, sara, tomas].count(True) == 1:
        sols.append(culpado)

print("mundos: 3 · soluções:", sols)
assert sols == ["Rui"], sols
