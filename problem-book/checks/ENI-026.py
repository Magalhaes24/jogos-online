"""ENI-026 — o álibi: quatro pessoas, uma mente. Solução única."""
PESSOAS = ["Aida", "Bento", "Célia", "Dinis"]

# cada um afirma onde estava; só o culpado mente
AFIRMA = {
    "Aida":  lambda c: c != "Aida",           # «estive com o Bento»
    "Bento": lambda c: c == "Célia",          # «foi a Célia»
    "Célia": lambda c: c != "Célia",          # «não fui eu»
    "Dinis": lambda c: c != "Bento",          # «não foi o Bento»
}

sols = []
for culpado in PESSOAS:
    mentiras = [p for p in PESSOAS if not AFIRMA[p](culpado)]
    if mentiras == [culpado]:                 # só o culpado mente
        sols.append(culpado)
    print("  culpado %-6s -> mentem: %s" % (culpado, mentiras or "ninguém"))

print("soluções:", sols)
assert sols == ["Célia"], sols
