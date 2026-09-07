"""LOG-015 — dois guardas, uma pergunta. Testa a pergunta em todos os mundos."""
import itertools

sucesso = 0
mundos = list(itertools.product(["A", "B"], [0, 1], [0, 1]))
# (guarda a quem pergunto, qual guarda é o mentiroso 0=A, porta da liberdade 0/1)
for perguntado, mentiroso_e_A, liberdade in mundos:
    mentiroso = "A" if mentiroso_e_A else "B"
    outro = "B" if perguntado == "A" else "A"

    # «Que porta é que o OUTRO guarda me diria que dá para a liberdade?»
    # o outro apontaria: verdade -> liberdade ; mentira -> a outra porta
    resposta_do_outro = liberdade if outro != mentiroso else 1 - liberdade
    # quem eu perguntei relata isso: verdade -> tal e qual ; mentira -> troca
    resposta = resposta_do_outro if perguntado != mentiroso else 1 - resposta_do_outro

    escolha = 1 - resposta          # a estratégia: escolher a porta OPOSTA
    sucesso += escolha == liberdade

print("mundos testados:", len(mundos), "· acertos:", sucesso)
assert sucesso == len(mundos), sucesso
