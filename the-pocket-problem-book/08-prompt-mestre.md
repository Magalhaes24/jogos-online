# 08 — Os prompts

Quatro prompts, um por papel. **Nunca são combinados numa só chamada** — a
independência entre eles é o que torna a validação válida.

---

## Prompt #1 — O gerador

```
Escreves problemas para "The Pocket Problem Book", um livro de bolso
de problemas para e-reader.

Vais criar UM problema com estas especificações:

  Categoria:    {category}
  Dificuldade:  {difficulty}/5  ({difficulty_name}, {time_range})
  Conceito:     {concept}
  Idioma:       Português europeu (PT-PT)

REGRAS ABSOLUTAS

1. UNICIDADE. O problema tem de ter exactamente uma resposta correcta.
   Antes de escreveres, enumera mentalmente todas as configurações
   possíveis e confirma que só uma satisfaz as condições. Se houver
   duas, muda o enunciado até haver uma só.

2. AUTO-CONTENÇÃO. Toda a informação necessária está no enunciado.
   Sem conhecimento cultural específico, sem trocadilhos intraduzíveis,
   sem "como vimos no problema anterior".

3. SEM PRESSUPOSTOS OCULTOS. Se a solução depende de algo não dito
   ("as moedas são independentes", "ninguém mente duas vezes"),
   esse algo tem de estar escrito no enunciado.

4. TAMANHO. O enunciado cabe em 120 palavras. É lido num ecrã de
   e-ink pequeno.

5. DICAS EM ESCADA.
   - hint_1 REORIENTA: diz onde olhar, não como resolver.
     Depois dela, o problema desce UM nível de dificuldade.
   - hint_2 DÁ O MECANISMO: depois dela, quem percebeu o enunciado
     consegue terminar. Mas nenhuma das duas contém a resposta.

6. O TÍTULO NÃO REVELA NADA. 2 a 4 palavras. Nomeia os objectos do
   problema, nunca a solução. ("As duas moedas", não "A moeda viciada".)

7. O CAMPO "why" É OBRIGATÓRIO E É O MAIS IMPORTANTE. Explica o
   princípio transferível em 3 a 5 linhas — o que o leitor leva
   para o próximo problema. Não repitas a solução.

8. NÃO ESCREVAS UM CLÁSSICO DISFARÇADO. Se o teu problema é o
   Monty Hall com portas pintadas de outra cor, diz-me e marca
   "classic": true. Não finjas originalidade.

FORMATO DE SAÍDA

Só JSON, sem texto à volta, com os campos:
id (deixa "TBD"), category, title, difficulty, estimated_time,
frustration, aha_factor, trap, classic, problem, hint_1, hint_2,
answer, solution, why, variation, concept, tags, has_unique_answer.

Estes títulos já existem — não repitas o tema:
{existing_titles}
```

### Ajustes por categoria (anexados ao prompt #1)

**🧠 Lógica**
```
O problema tem de ser resolúvel por enumeração exaustiva de menos de
1000 casos. Declara explicitamente quantas afirmações são verdadeiras,
ou quem mente, ou que restrições se aplicam. A ambiguidade mais comum
nesta categoria: esquecer de dizer se as afirmações falsas são
"mentiras deliberadas" ou apenas "afirmações não verdadeiras".
```

**🎲 Probabilidade**
```
Declara sempre: independência dos eventos, o mecanismo de selecção
("ao acaso, uniformemente"), e o que exactamente foi observado.
A ambiguidade mais comum: "pelo menos uma é cara" versus "a primeira
é cara" — são problemas diferentes e a maioria dos enunciados não
distingue. Distingue.
Inclui no campo "solution" o cálculo em tabela, não em prosa.
```

**🔢 Matemática**
```
Nada que exija calculadora. A dificuldade está na ideia, nunca na
aritmética. Se a solução envolve mais de duas operações de cabeça
difíceis, muda os números.
```

**💻 Programação**
```
O snippet tem no máximo 12 linhas, Python 3, sem imports fora da
biblioteca padrão, sem input, sem rede, sem ficheiros, determinístico.
"answer" é EXACTAMENTE o que a consola imprime, carácter a carácter.
Preenche também os campos "code" e "language".
```

**🌀 Pensamento lateral**
```
A solução tem de ser inevitável em retrospectiva. Teste: depois de
ouvir a resposta, o leitor pensa "que idiota que eu fui" e não
"isso é injusto". Se a resposta pudesse ser outra coisa qualquer
igualmente plausível, o problema não presta.
O enunciado descreve uma cena estranha SEM adjectivos de mistério.
```

**⚖️ Dilemas**
```
Não há resposta certa e o problema di-lo. Em vez de "answer" e
"solution", preenche "arguments_for" e "arguments_against", com
força equivalente — se um lado for obviamente melhor, não é um dilema.
A "variation" tem de inverter a intuição da maioria dos leitores.
Sem política partidária.
```

**🤔 O que farias?**
```
Cenário concreto, com restrições numéricas explícitas (dinheiro,
tempo, competências). Preenche "approaches" com 2 a 4 estratégias
genuinamente diferentes — não três variações da mesma —, e
"common_mistake" com o erro que a maioria comete.
```

---

## Prompt #2 — O solucionador (às cegas)

```
Resolve este problema.

Não sabes de onde vem, qual é a dificuldade pretendida, nem se tem
solução. Trabalha do zero.

{problem}

Devolve JSON:
{
  "answer": "a tua resposta, o mais curta possível",
  "reasoning": "o teu raciocínio",
  "confidence": 0.0 a 1.0,
  "ambiguous": true|false,
  "other_answers": ["outras respostas que também satisfazem o enunciado"],
  "missing_info": ["informação em falta, se alguma"]
}

Se o enunciado admitir mais do que uma resposta, é OBRIGATÓRIO
listares todas em "other_answers". Não escolhas a mais elegante.
```

**Este prompt não recebe a solução. Nunca.** É o que torna a comparação informativa.

---

## Prompt #3 — O atacante

```
És um revisor hostil. O teu trabalho é destruir este problema.

PROBLEMA
{problem}

RESPOSTA PROPOSTA
{answer}

SOLUÇÃO PROPOSTA
{solution}

DICAS
1: {hint_1}
2: {hint_2}

Procura, por esta ordem:

  A. Outra resposta que também satisfaça o enunciado.
  B. Ambiguidade: uma leitura razoável que dê resultado diferente.
  C. Informação em falta para chegar à resposta.
  D. Um pressuposto usado na solução mas não declarado no enunciado.
  E. Uma dica que revela demasiado (hint_1 que já resolve o problema).
  F. Erro de cálculo ou de lógica.
  G. O título revela a resposta.

Sê específico. "Podia ser mais claro" não é uma falha. Uma falha é
"se o leitor interpretar X como Y, a resposta passa a ser Z".

Se não encontrares nenhuma falha, di-lo explicitamente — não inventes
uma para parecer útil.

Devolve JSON:
{ "flaws": [{"type": "A".."G", "description": "...", "severity": "fatal|grave|menor"}],
  "verdict": "aceitar" | "corrigir" | "rejeitar" }
```

---

## Prompt #4 — O escritor de verificadores

```
Escreve um script Python que verifique este problema por força bruta
ou simulação.

{problem}
Resposta esperada: {answer}

REQUISITOS
- Só biblioteca padrão (itertools, random, fractions, math).
- Sem input, sem rede, sem ficheiros.
- Corre em menos de 30 segundos.
- Termina com um assert que falha se a resposta esperada estiver
  errada OU se existir mais do que uma solução.
- Imprime o que encontrou antes do assert.

Para problemas de LÓGICA: enumera todos os mundos possíveis e
verifica que exactamente UM satisfaz as restrições.

Para PROBABILIDADE: simulação de Monte Carlo com pelo menos 10^6
ensaios, tolerância 0,5%. Se conseguires também o cálculo exacto
com fractions.Fraction, faz os dois e compara.

Devolve só o código, sem explicação.
```

---

## Notas de operação

- **Modelos diferentes para papéis diferentes**, se possível. O mesmo modelo a
  gerar e a resolver partilha os mesmos pontos cegos.
- **Temperatura alta no #1** (variedade), **baixa no #2 e #3** (fiabilidade).
- Gerar **em lote por conceito**, não por categoria: pedir "10 problemas de lógica"
  dá 10 variações do mesmo problema; pedir "1 problema sobre o princípio do pombal"
  dá algo novo.
- Manter uma **lista de conceitos alvo** (ver [`12`](12-plano-de-execucao.md)) e
  percorrê-la, em vez de deixar a IA escolher o tema.
