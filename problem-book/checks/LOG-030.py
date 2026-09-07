"""LOG-030 — dias da semana: aritmética módulo 7."""
DIAS = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]

# «o dia depois de amanhã é segunda-feira»
for i, hoje in enumerate(DIAS):
    if DIAS[(i + 2) % 7] == "segunda":
        anteontem = DIAS[(i - 2) % 7]
        print("hoje é %s -> anteontem foi %s" % (hoje, anteontem))
        assert hoje == "sábado" and anteontem == "quinta", (hoje, anteontem)
        break
else:
    raise AssertionError("nenhum dia satisfaz o enunciado")
