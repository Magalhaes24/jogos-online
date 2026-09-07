"""LOG-007 — cavaleiros (verdade) e escudeiros (mentira): 4 mundos, 1 solução."""
sols = []
for a_cav in (True, False):
    for b_cav in (True, False):
        # A: «somos os dois escudeiros»  -> afirmação = (not a_cav and not b_cav)
        af_a = (not a_cav) and (not b_cav)
        # B: «exactamente um de nós é cavaleiro»
        af_b = (a_cav != b_cav)
        if af_a == a_cav and af_b == b_cav:
            sols.append(("cavaleiro" if a_cav else "escudeiro",
                         "cavaleiro" if b_cav else "escudeiro"))

print("mundos: 4 · soluções:", sols)
assert len(sols) == 1 and sols[0] == ("escudeiro", "cavaleiro"), sols
