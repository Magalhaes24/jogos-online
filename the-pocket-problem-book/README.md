# 📖 The Pocket Problem Book

> *200 problems for when you have nothing to do.*

Especificação completa de um livro-jogo de bolso para e-readers (optimizado para o **Xteink X4**),
e da pequena fábrica de problemas que o produz.

Isto **não é** uma colectânea de puzzles escrita à mão. É um sistema:

```
banco de problemas (JSON)  →  gerador  →  validação  →  EPUB / PDF / web
```

---

## Como ler esta pasta

Lê por ordem se estás a começar. Salta directamente se já sabes o que procuras.

| # | Ficheiro | O que contém |
|---|---|---|
| 01 | [`01-especificacao.md`](01-especificacao.md) | Conceito, princípios, identidade do produto |
| 02 | [`02-categorias.md`](02-categorias.md) | As 8 categorias, o que entra e o que não entra |
| 03 | [`03-dificuldade-e-metadados.md`](03-dificuldade-e-metadados.md) | Níveis, tempos, IDs, ratings (Frustration, Aha) |
| 04 | [`04-anatomia-de-um-problema.md`](04-anatomia-de-um-problema.md) | A sequência de páginas problema → dica → solução |
| 05 | [`05-navegacao-e-modo-aleatorio.md`](05-navegacao-e-modo-aleatorio.md) | "Tenho 5 minutos", desafio do dia, índices |
| 06 | [`06-esquema-json.md`](06-esquema-json.md) | O schema canónico de um problema |
| 07 | [`07-pipeline-de-validacao.md`](07-pipeline-de-validacao.md) | Como garantir que a solução está certa |
| 08 | [`08-prompt-mestre.md`](08-prompt-mestre.md) | Os prompts de geração, resolução e ataque |
| 09 | [`09-estetica-e-epub.md`](09-estetica-e-epub.md) | Tipografia, CSS, estrutura do EPUB para o X4 |
| 10 | [`10-gerador-python.md`](10-gerador-python.md) | Estrutura do projecto e CLI |
| 11 | [`11-banco-inicial.md`](11-banco-inicial.md) | 24 problemas seed, completos e verificados |
| 12 | [`12-plano-de-execucao.md`](12-plano-de-execucao.md) | As 6 fases, Volume I, edições futuras |
| 13 | [`13-controlo-de-qualidade.md`](13-controlo-de-qualidade.md) | Checklist editorial e armadilhas conhecidas |

---

## A regra que governa tudo

Um problema só entra no livro se **três coisas independentes** concordarem na resposta:
quem o criou, quem o resolveu do zero, e — sempre que possível — um script que o verifica
por força bruta ou simulação.

Ver [`07-pipeline-de-validacao.md`](07-pipeline-de-validacao.md).

## Estado

Especificação. Nenhum código escrito ainda — o [plano de execução](12-plano-de-execucao.md)
diz por que ordem construir.
