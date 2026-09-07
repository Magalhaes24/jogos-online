# problem-book

O gerador de **The Pocket Problem Book**. Especificação completa em
[`../the-pocket-problem-book/`](../the-pocket-problem-book/).

```
problems/     a base de dados — 24 problemas em JSON, a única coisa que importa
checks/       um script por problema verificável; o assert é a peça central
generator/    schema, db, mdlite, render, epub, build, verify, cli
templates/    style.css
output/       os EPUB gerados
ppb           a linha de comandos
```

## Usar

```bash
./ppb check            # as 10 regras de integridade do doc 06
./ppb verify           # corre todos os scripts de checks/
./ppb build            # -> output/pocket-problems-vol1.epub
./ppb build --ascii    # variante sem emoji, para leitores sem a fonte
./ppb report           # estado do banco
```

**Zero dependências.** Só a biblioteca padrão do Python 3.9+. O markdown, o
XHTML e o EPUB são construídos à mão — nenhum deles é complicado o suficiente
para justificar uma dependência que se parte daqui a dois anos.

## Estado

| | |
|---|---|
| Problemas `VERIFIED` | 24 de 200 |
| Integridade | 0 violações |
| Verificação automática | 14 de 24 (as outras 10 são `manual` ou `n/a` por natureza) |
| epubcheck 5.1.0 | 0 erros, 0 avisos |

## O que ainda não existe

A fábrica (Fase 4 do [plano](../the-pocket-problem-book/12-plano-de-execucao.md)):
`generate.py`, `solve.py`, `attack.py`, `pipeline.py`. Os prompts estão escritos
no [doc 08](../the-pocket-problem-book/08-prompt-mestre.md); falta o código que os
chama. A ordem é deliberada: os verificadores vieram primeiro.
