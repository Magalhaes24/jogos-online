"""ENI-002 — gerador look-and-say."""
def ler(t):
    out, i = "", 0
    while i < len(t):
        j = i
        while j < len(t) and t[j] == t[i]:
            j += 1
        out += str(j - i) + t[i]
        i = j
    return out


seq, t = ["1"], "1"
for _ in range(5):
    t = ler(t)
    seq.append(t)

print(" -> ".join(seq))
assert seq[:5] == ["1", "11", "21", "1211", "111221"], seq
assert seq[5] == "312211", seq[5]
