# 02 — As 8 categorias

Cada problema pertence a **exactamente uma** categoria. O prefixo do ID vem daqui.

| Símbolo | Categoria | Prefixo | Volume I |
|---|---|---|---|
| 🧠 | Lógica | `LOG` | 35 |
| 🕵️ | Enigmas | `ENI` | 30 |
| 🔢 | Matemática | `MAT` | 30 |
| 🎲 | Probabilidade | `PRB` | 25 |
| 🌀 | Pensamento lateral | `LAT` | 25 |
| ⚖️ | Dilemas | `DIL` | 20 |
| 🤔 | O que farias? | `WWY` | 20 |
| 💻 | Programação | `PRG` | 15 |
| | **Total** | | **200** |

---

## 🧠 Lógica — `LOG`

Dedução formal. O leitor tem informação suficiente para chegar à resposta por eliminação.

**Entra:** verdades e mentiras, grelhas de dedução, chapéus e prisioneiros, restrições,
pesagens em balança, atravessar o rio, sequências com regra dedutível.

**Não entra:** nada que dependa de conhecimento externo ou de um truque linguístico
(isso é 🌀 Lateral).

**Requisito duro:** unicidade da solução tem de ser provada por enumeração exaustiva.
Ver [`07-pipeline-de-validacao.md`](07-pipeline-de-validacao.md).

---

## 🕵️ Enigmas — `ENI`

Rápidos e intuitivos. 1 a 5 minutos. O prazer está na velocidade, não na profundidade.

**Entra:** adivinhas, "quem fez isto?", sequências curtas, padrões, jogos de palavras,
mini-mistérios de detective.

**Não entra:** problemas que exigem papel e caneta.

**Nota:** um enigma que precisa de duas dicas está mal calibrado — provavelmente é 🧠 Lógica.

---

## 🔢 Matemática — `MAT`

Sub-dividida por dificuldade, não por tema:

| Nível | Conteúdo |
|---|---|
| ⭐⭐ Fácil | aritmética, percentagens, proporções, sequências |
| ⭐⭐⭐ Médio | álgebra, geometria, optimização simples |
| ⭐⭐⭐⭐–⭐⭐⭐⭐⭐ Difícil | combinatória, teoria dos números, problemas olímpicos |

**Regra:** nada que exija calculadora. Se o cálculo é a dificuldade, o problema é mau.
A dificuldade tem de estar na *ideia*.

---

## 🎲 Probabilidade — `PRB`

A secção com maior taxa de rejeição na validação — e a mais fácil de verificar
(simulação de Monte Carlo).

**Progressão:** contagem de casos → condicional → Bayes → paradoxos que enganam a intuição.

**Requisito duro:** toda a solução tem de bater com uma simulação de ≥ 1.000.000 ensaios,
com tolerância de 0,5%.

---

## 🌀 Pensamento lateral — `LAT`

O objectivo é uma sensação específica:

> "AHHHHH. Como é que não pensei nisso?"

**Entra:** situações aparentemente absurdas com explicação mundana; problemas que só
se resolvem abandonando um pressuposto implícito.

**Não entra:** problemas cuja solução é arbitrária. Se, depois de ouvir a resposta,
o leitor pensar "isso é injusto" em vez de "que idiota que eu fui", o problema não presta.

**Teste:** a solução tem de ser *inevitável em retrospectiva*.

---

## ⚖️ Dilemas — `DIL`

**Não têm resposta certa. Isto é declarado na página.**

Formato: pergunta → o leitor decide → argumentos dos dois lados → uma variação que
inverte a intuição.

**Entra:** ética, trade-offs pessoais, justiça, lealdade.
**Não entra:** política partidária, tópicos escolhidos para provocar em vez de fazer pensar.

O campo `has_unique_answer` é `false` e o gerador recusa-se a imprimir "✅ SOLUÇÃO".
Em vez disso imprime "⚖️ ARGUMENTOS".

---

## 🤔 O que farias? — `WWY`

Problemas de vida real, com restrições concretas. Também sem resposta certa, mas
com uma diferença face aos Dilemas: aqui existe **melhor e pior**, só não existe *único*.

Formato: cenário com restrições explícitas → o leitor planeia → "Uma abordagem possível"
com 2 a 4 estratégias distintas → o que a maioria das pessoas erra.

---

## 💻 Programação — `PRG`

Pequenos desafios **sem computador**.

**Entra:** "o que imprime este código?", pegadilhas de semântica de linguagem,
complexidade algorítmica, algoritmos de papel-e-caneta (25 cavalos, ordenação, hashing).

**Regra:** o snippet cabe em 12 linhas. Python por omissão; outras linguagens só se a
pegadilha for específica delas (e nesse caso a linguagem é nomeada no título).

**Requisito duro:** todo o snippet é executado no pipeline e a saída real é comparada
com a resposta declarada.
