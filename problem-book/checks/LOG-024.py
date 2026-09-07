"""LOG-024 — três interruptores, uma lâmpada noutro andar.
Modela a observação (aceso, quente) e exige que os 3 casos sejam distintos."""
# estratégia: liga o 1 e espera; desliga o 1 e liga o 2; sobe.
def observa(verdadeiro):
    aceso = (verdadeiro == 2)                 # só o 2 fica ligado
    quente = (verdadeiro == 1)                # o 1 esteve ligado muito tempo
    return (aceso, quente)


obs = {s: observa(s) for s in (1, 2, 3)}
for s, o in obs.items():
    print("  interruptor %d -> aceso=%-5s quente=%-5s" % (s, *o))
assert len(set(obs.values())) == 3, obs
print("as três observações são distintas -> uma subida chega")

# controlo: sem a informação do calor, dois casos ficam iguais
so_luz = {s: observa(s)[0] for s in (1, 2, 3)}
assert len(set(so_luz.values())) == 2, so_luz
print("só com a luz: %s -> 2 observações para 3 casos, impossível" % sorted(set(so_luz.values())))
