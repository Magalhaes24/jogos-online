# 12 — Plano de execução

Seis fases. Cada uma produz uma coisa utilizável. **Não passes à seguinte sem terminar
a anterior** — o erro clássico neste projecto é começar a gerar em massa antes de saber
rejeitar.

---

## FASE 1 — Especificação ✅

Definir categorias, dificuldades, formato dos problemas, formato das soluções, estilo
visual e sistema de IDs.

**É esta pasta.** Está feito.

**Saída:** os 14 documentos.

---

## FASE 2 — Base inicial e teste no dispositivo

**Objectivo:** descobrir os problemas de formato **antes** de haver 200 problemas para
reformatar.

1. Passar os [24 problemas seed](11-banco-inicial.md) para JSON, à mão.
2. Escrever o `render.py` e o `epub.py` mais simples que funcionem.
3. Gerar um EPUB com 24 problemas.
4. **Ler no X4 durante uma semana**, sem tocar em código.
5. Anotar: a tipografia funciona? As páginas quebram onde deviam? A barreira STOP
   funciona ou vira-se sem pensar? Os emoji aparecem?

**Saída:** um EPUB de 24 problemas que se lê bem no dispositivo real.

**Critério de passagem:** conseguiste resolver 10 problemas no X4 sem uma única vez
teres pensado "isto lê-se mal".

---

## FASE 3 — Verificadores primeiro

**Objectivo:** saber rejeitar antes de saber gerar.

1. `schema.py` + `db.py` + as 10 regras de integridade do doc [`06`](06-esquema-json.md).
2. `verify.py` com os quatro métodos: `exhaustive`, `monte_carlo`, `symbolic`, `execute`.
3. Escrever à mão os verificadores dos 24 seed. **Se algum falhar, o problema seed
   estava errado — corrige-o.** (É exactamente para isto que servem.)
4. `ppb check` a passar a verde.

**Saída:** `ppb verify --all` verde sobre o banco inicial.

**Critério de passagem:** introduz deliberadamente um erro num problema e confirma que
o pipeline o apanha.

---

## FASE 4 — A fábrica

1. `generate.py`, `solve.py`, `attack.py` com os prompts do doc [`08`](08-prompt-mestre.md).
2. `pipeline.py` a encadear os quatro estados.
3. `report.py`.
4. `concepts.yaml` preenchido (ver lista abaixo).
5. Gerar **50 candidatos** e passá-los pelo pipeline completo.
6. Ler os 50 à mão. Sim, os 50. É a única forma de calibrar os prompts.

**Saída:** taxa de aceitação medida, prompts corrigidos.

**Critério de passagem:** taxa de aceitação entre 30% e 50%, e os problemas aceites
são bons quando lidos por um humano. Se a taxa for de 90%, a validação não funciona.
Se for de 5%, os prompts é que estão maus.

---

## FASE 5 — Volume I

Gerar até chegar a 200 `VERIFIED`, com as distribuições alvo.

**Ordem de geração:** por **conceito**, não por categoria. Percorre `concepts.yaml`
de cima a baixo. Isto evita o problema mais comum — dez variações do mesmo puzzle.

**Esperar gerar ~600 candidatos para publicar 200.** É o número normal.

Ao chegar a 200:

- `ppb check` verde
- distribuição de dificuldade dentro de ±3% do alvo
- nenhum conceito repetido mais de 4 vezes
- build EPUB normal + build `--ascii`
- **leitura completa por um humano** — as 1800 páginas, uma vez

**Saída:** `pocket-problems-vol1.epub`

---

## FASE 6 — Iteração

Usar o livro **durante seis a oito semanas**, marcando cada problema resolvido com
uma etiqueta:

| Marca | Significado | Consequência no Volume II |
|---|---|---|
| `fácil demais` | resolvido em menos de metade do tempo estimado | recalibrar `difficulty` |
| `difícil demais` | desistiu | recalibrar, ou melhorar as dicas |
| `solução confusa` | acertou mas não percebeu a explicação | reescrever `solution` e `why` |
| `excelente` | resolveu e ficou contente | **gerar mais deste conceito** |
| `aborrecido` | resolveu sem prazer nenhum | despriorizar o conceito |
| `mais deste tipo` | quer mais | entra no topo do `concepts.yaml` |

A marca `excelente` é o sinal mais valioso do projecto inteiro: é o que orienta a
geração do Volume II para o que realmente funciona **para ti**, e não para o que a
IA acha que é um bom puzzle.

---

## `concepts.yaml` — a lista de conceitos alvo

Gerar por conceito, não por categoria. Percorrer esta lista é o que garante variedade.

```yaml
logic:
  - enumeração de mundos
  - verdades e mentiras
  - dedução a partir do silêncio
  - conhecimento comum
  - princípio do pombal
  - paridade
  - invariantes
  - pesagens em balança
  - grelhas de dedução
  - travessias com restrições
  - auto-referência

math:
  - proporções e taxas
  - sequências e recorrências
  - geometria sem trigonometria
  - princípio da inclusão-exclusão
  - teoria dos números elementar
  - combinatória
  - médias e desigualdades
  - estimativa (problemas de Fermi)
  - optimização discreta

probability:
  - contagem de casos
  - probabilidade condicional
  - teorema de Bayes
  - valor esperado
  - o paradoxo dos aniversários
  - paradoxo de Simpson
  - problema dos prisioneiros
  - regressão à média
  - viés de selecção
  - passeio aleatório

programming:
  - avaliação de defaults
  - mutabilidade e aliasing
  - closures e captura de variáveis
  - iteração sobre estruturas mutáveis
  - coerção e comparação de tipos
  - vírgula flutuante
  - curto-circuito e ordem de avaliação
  - complexidade algorítmica
  - torneios e limites inferiores
  - hashing e colisões

lateral:
  - pressuposto sobre a intenção
  - pressuposto sobre a escala
  - pressuposto sobre o contexto
  - pressuposto sobre a identidade
  - pressuposto temporal
  - pressuposto sobre a capacidade

riddles:
  - definição por ausência
  - sequências auto-descritivas
  - jogos de palavras
  - padrões visuais
  - mini-mistérios

dilemmas:
  - consequencialismo vs. deontologia
  - lealdade vs. verdade
  - justiça vs. misericórdia
  - liberdade vs. segurança
  - presente vs. futuro

what_would_you:
  - restrições e alavancagem
  - custos afundados
  - risco e sequenciação
  - negociação
  - alocação de tempo
```

---

## Depois do Volume I

| Edição | Conteúdo | Nº |
|---|---|---|
| **Volume II** | 200 novos, guiados pelas marcas da Fase 6 | 200 |
| **Travel Edition** | só ⭐ e ⭐⭐, 1–5 min | 150 |
| **Math Edition** | matemática + probabilidade | 200 |
| **Programmer Edition** | programação + algoritmos | 150 |
| **Special Edition** | só ⭐⭐⭐⭐ e ⭐⭐⭐⭐⭐ | 100 |
| **Evil Edition 😈** | só `trap: true` — feitos para enganar a intuição | 100 |

Todas saem da mesma base de dados. Uma edição nova é um **filtro** sobre `problems/`,
não conteúdo novo — excepto o Volume II.

---

## 🧨 A secção que dá identidade ao livro

Dentro do Volume I, uma secção transversal: **Problemas que te enganam**
(todos os `trap: true`).

Antes de cada um, uma página com uma única frase:

```
    😈

  A tua intuição está
  provavelmente errada.
```

Candidatos: Monty Hall, aniversários, paradoxo de Simpson, o problema dos dois
envelopes, taxa de falsos positivos em testes médicos, o taco e a bola, a falácia do
jogador, o paradoxo da inspecção, regressão à média.

É a secção que as pessoas vão querer mostrar a outras pessoas — e por isso é a que
define o livro.
