"""MAT-011 — a soma que quase toda a gente erra."""
parcelas = [1000, 40, 1000, 30, 1000, 20, 1000, 10]
total = 0
for x in parcelas:
    total += x
    print("  +%5d -> %5d" % (x, total))
assert total == 4100, total
assert sum(parcelas) == 4100
assert total != 5000, "5000 é a resposta que o cérebro produz sozinho"
print("total:", total, "(e não 5000)")
