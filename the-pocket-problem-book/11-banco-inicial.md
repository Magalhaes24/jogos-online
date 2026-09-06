# 11 — Banco inicial: 24 problemas

Três por categoria. Todos escritos no formato final e verificados
(ver [`07`](07-pipeline-de-validacao.md)). Servem para três coisas:

1. testar o EPUB no X4 antes de escrever código de geração;
2. servir de *few-shot examples* ao prompt gerador;
3. fixar o tom.

Legenda dos cabeçalhos: `ID · Título · ★dificuldade · tempo · conceito`

---
---

# 🧠 Lógica

## LOG-001 · As três caixas · ★★★ · 5–10 min · Enumeração de mundos

**Problema**

> Há três caixas: **A**, **B** e **C**. Exactamente uma contém ouro.
>
> Cada caixa tem uma etiqueta:
>
> - **A:** «O ouro está nesta caixa.»
> - **B:** «O ouro não está nesta caixa.»
> - **C:** «O ouro não está na caixa A.»
>
> Sabes que **exactamente uma** das três etiquetas diz a verdade.
>
> Onde está o ouro?

**🤔 Pensa primeiro**

**Dica 1** — Não tentes deduzir a partir das etiquetas. Há só três hipóteses no mundo:
o ouro está em A, em B, ou em C. Testa-as.

**Dica 2** — Para cada hipótese, percorre as três etiquetas e conta quantas ficam
verdadeiras. Procuras a hipótese que dá exactamente uma.

**🛑 STOP**

**✅ Resposta** — O ouro está na caixa **B**.

**Solução**

| Hipótese | A: «está aqui» | B: «não está aqui» | C: «não está em A» | Verdadeiras |
|---|---|---|---|---|
| Ouro em **A** | ✅ V | ✅ V | ❌ F | **2** |
| Ouro em **B** | ❌ F | ❌ F | ✅ V | **1** ✔ |
| Ouro em **C** | ❌ F | ✅ V | ✅ V | **2** |

Só a segunda linha dá exactamente uma etiqueta verdadeira.

**🧠 Porquê**

Quando um enunciado fixa *quantas* afirmações são verdadeiras, ele não está a dar-te
factos — está a dar-te um **filtro**. Não deduzas para a frente a partir das afirmações;
gera todos os mundos possíveis, aplica o filtro, e vê qual sobrevive. Com três, quatro
ou cinco hipóteses, contar é sempre mais rápido e mais seguro do que raciocinar.

**🔄 Variação**

E se soubesses apenas que *pelo menos* uma etiqueta é verdadeira? Quantas respostas
passam a existir?

*Verificação:* `exhaustive` — 3 mundos, 1 solução. ✔

---

## LOG-002 · Os três chapéus · ★★★★ · 10–20 min · Dedução a partir do silêncio

**Problema**

> Três pessoas estão em fila indiana, todas viradas para a frente. A da retaguarda vê
> as duas da frente; a do meio vê só a da frente; a da frente não vê ninguém.
>
> Existem **cinco chapéus: três brancos e dois pretos**. Coloca-se um chapéu na cabeça
> de cada uma, ao acaso; os dois restantes são escondidos. Ninguém vê o seu próprio chapéu.
>
> Perguntam à da **retaguarda** se sabe a cor do seu chapéu. Responde: **«Não.»**
> Perguntam à do **meio**. Responde: **«Não.»**
> Perguntam à da **frente**. Responde: **«Sim.»**
>
> Que cor tem o chapéu da pessoa da frente — e como é que ela sabe?

**🤔 Pensa primeiro**

**Dica 1** — A pessoa da frente não vê nada. Portanto a informação que ela usa não é
visual: é o facto de as outras duas terem dito «não».

**Dica 2** — Só existem dois chapéus pretos. Em que situação é que a pessoa da
retaguarda saberia imediatamente a cor do seu?

**🛑 STOP**

**✅ Resposta** — **Branco.**

**Solução**

1. Se a pessoa da retaguarda visse **dois pretos** à sua frente, saberia que o seu era
   branco (só há dois pretos). Como disse «não», **as duas da frente não são ambas pretas**.
2. A do meio ouve isto e olha para a da frente. Se a da frente tivesse **preto**, então,
   pelo ponto 1, o chapéu da do meio teria de ser branco — e ela saberia. Como disse
   «não», **a da frente não tem preto**.
3. Logo, a da frente tem **branco** — e chega lá exactamente por este raciocínio, sem
   ver nada.

**🧠 Porquê**

*Não saber é informação.* Sempre que alguém com mais dados do que tu declara ignorância,
elimina os cenários em que essa pessoa teria sabido. Uma cadeia de «nãos» é uma cadeia
de eliminações — é o mesmo mecanismo por trás dos problemas dos prisioneiros, dos
olhos azuis e da maioria dos puzzles de conhecimento comum.

**🔄 Variação**

E se a pessoa do meio também tivesse dito «sim»? Que cores seriam possíveis então?

*Verificação:* `exhaustive` — todas as atribuições de {B,B,B,P,P} a 3 posições. ✔

---

## LOG-003 · Três amigos, três pisos · ★★ · 2–5 min · Grelha de dedução

**Problema**

> A Ana, o Bruno e a Clara vivem no mesmo prédio, cada um num piso diferente
> (1, 2 ou 3), e cada um bebe uma bebida diferente: chá, café ou água.
>
> - Quem bebe café vive num piso **acima** do da Ana.
> - O Bruno **não** vive no piso 3.
> - A Clara bebe chá.
>
> Quem bebe água, e em que piso vive cada um?

**🤔 Pensa primeiro**

**Dica 1** — Começa pelas bebidas. Duas das três pistas dizem-te alguma coisa sobre
quem *não* bebe café.

**Dica 2** — Depois de saberes quem bebe café, a primeira pista força um piso mínimo
para essa pessoa. A segunda pista fecha tudo.

**🛑 STOP**

**✅ Resposta** — A **Ana** bebe água, no piso **1**. O Bruno bebe café, no piso **2**.
A Clara bebe chá, no piso **3**.

**Solução**

1. A Clara bebe chá (pista 3).
2. A Ana não bebe café, porque quem bebe café vive acima dela (pista 1) e ninguém vive
   acima de si própria. Logo o café é do **Bruno**, e a **Ana** fica com a água.
3. Pista 1: piso(Bruno) > piso(Ana) ⟹ piso(Bruno) ≥ 2.
4. Pista 2: Bruno ≠ 3 ⟹ **Bruno = 2**, e portanto **Ana = 1** e **Clara = 3**.

**🧠 Porquê**

Numa grelha de dedução, as pistas mais úteis quase nunca são as afirmativas
(«a Clara bebe chá»). São as **comparativas** («acima de»), porque eliminam um extremo:
«X está acima de Y» diz-te de imediato que X não é o piso mais baixo e que Y não é o
mais alto. Ataca primeiro essas.

**🔄 Variação**

Retira a pista 2. Quantas soluções ficam?

*Verificação:* `exhaustive` — 36 combinações, 1 solução. ✔

---
---

# 🕵️ Enigmas

## ENI-001 · O que cresce ao encolher · ★★ · 2–5 min · Redefinição de "maior"

**Problema**

> Quanto mais lhe tiras, maior fica.
>
> O que é?

**🤔 Pensa primeiro**

**Dica 1** — Estás a assumir que "tirar" reduz. Pensa em algo cuja identidade *é* a
ausência de matéria.

**Dica 2** — Está no chão. Provavelmente já caíste num.

**🛑 STOP**

**✅ Resposta** — Um **buraco**.

**Solução**

Um buraco não é feito de material — é definido pelo material que **falta**. Tirar terra
de um buraco é acrescentar buraco. A palavra "tirar" só significa "diminuir" quando o
objecto é positivo; um buraco é um objecto negativo.

**🧠 Porquê**

Muitos enigmas funcionam com uma **assimetria de sinal**: assumes que a operação e o
objecto têm a mesma polaridade. Quando um enunciado parece auto-contraditório, pergunta
se algum dos substantivos é definido por ausência — buraco, dívida, silêncio, sombra,
vazio.

**🔄 Variação**

Quanto mais secas, mais molhada fica. O que é? *(pista: casa de banho)*

*Verificação:* `manual` ✔

---

## ENI-002 · A sequência que se lê · ★★★ · 5–10 min · Sequência auto-descritiva

**Problema**

> Qual é o próximo termo?
>
> ```
> 1
> 11
> 21
> 1211
> 111221
> ?
> ```

**🤔 Pensa primeiro**

**Dica 1** — Não é aritmética. Nenhuma soma, diferença ou produto liga estes números.
Não tentes calcular — tenta **dizer em voz alta**.

**Dica 2** — Cada linha descreve a linha anterior. Lê a linha `21` em voz alta olhando
para a linha `11`.

**🛑 STOP**

**✅ Resposta** — **312211**

**Solução**

Cada termo lê o anterior em voz alta, contando repetições:

| Termo | Lê-se | Gera |
|---|---|---|
| `1` | "um 1" | `11` |
| `11` | "dois 1" | `21` |
| `21` | "um 2, um 1" | `1211` |
| `1211` | "um 1, um 2, dois 1" | `111221` |
| `111221` | "três 1, dois 2, um 1" | **`312211`** |

**🧠 Porquê**

Quando uma sequência resiste a toda a aritmética, o operador provavelmente não é
numérico: é **tipográfico ou linguístico**. A sequência olha para si própria em vez de
para os valores. É a chamada *look-and-say*, e a mesma família inclui sequências
definidas pelo número de letras do nome do número, ou pela forma dos dígitos.

**🔄 Variação**

Se começares em `2` em vez de `1`, a sequência comporta-se de forma diferente?
E existe algum termo que se gere a si próprio?

*Verificação:* `brute_force` — gerador de look-and-say. ✔

---

## ENI-003 · O vidro partido · ★★★ · 5–10 min · Verdades e mentiras

**Problema**

> Alguém partiu a janela da escola. Foi o Rui, a Sara ou o Tomás — e apenas um deles.
>
> - **Rui:** «Não fui eu.»
> - **Sara:** «Foi o Tomás.»
> - **Tomás:** «A Sara está a mentir.»
>
> Sabe-se que **exactamente uma** destas três afirmações é verdadeira.
>
> Quem partiu a janela?

**🤔 Pensa primeiro**

**Dica 1** — Não penses em quem parece mais suspeito. Assume um culpado de cada vez e
vê se o número de afirmações verdadeiras bate certo.

**Dica 2** — Repara que as afirmações da Sara e do Tomás são opostas: uma delas é
sempre verdadeira. Portanto a do Rui tem de ser falsa.

**🛑 STOP**

**✅ Resposta** — Foi o **Rui**.

**Solução**

| Culpado | Rui: «não fui» | Sara: «foi o Tomás» | Tomás: «Sara mente» | Verdadeiras |
|---|---|---|---|---|
| **Rui** | ❌ F | ❌ F | ✅ V | **1** ✔ |
| Sara | ✅ V | ❌ F | ✅ V | **2** |
| Tomás | ✅ V | ✅ V | ❌ F | **2** |

Atalho: Sara e Tomás contradizem-se, logo exactamente uma das duas é verdadeira. Como
só pode haver uma verdadeira no total, a do Rui é falsa — e «não fui eu» falso significa
que foi ele.

**🧠 Porquê**

Procura sempre **pares contraditórios**. Se duas afirmações se negam mutuamente, sabes
que contribuem exactamente uma verdade, sem precisares de saber qual. Isso consome a
quota de verdades e resolve o resto do problema de graça.

**🔄 Variação**

E se fossem exactamente **duas** as afirmações verdadeiras?

*Verificação:* `exhaustive` — 3 mundos, 1 solução. ✔

---
---

# 🔢 Matemática

## MAT-001 · O taco e a bola · ★★ · 2–5 min · Equações lineares · 😈

**Problema**

> Um taco e uma bola custam, juntos, **€1,10**.
>
> O taco custa **€1,00 mais** do que a bola.
>
> Quanto custa a bola?

**🤔 Pensa primeiro**

**Dica 1** — A resposta que te veio à cabeça em dois segundos está provavelmente errada.
Testa-a: se a bola custasse isso, quanto custaria o taco?

**Dica 2** — Chama `b` ao preço da bola. O taco é `b + 1`. Escreve a soma.

**🛑 STOP**

**✅ Resposta** — **€0,05** (5 cêntimos).

**Solução**

```
b + (b + 1,00) = 1,10
2b + 1,00      = 1,10
2b             = 0,10
b              = 0,05
```

Confirmação: bola €0,05, taco €1,05. Soma €1,10 ✔. Diferença €1,00 ✔.

A resposta intuitiva (€0,10) falha o segundo teste: com bola a €0,10 o taco seria
€1,10 e o total €1,20.

**🧠 Porquê**

O erro não é de cálculo — é de **substituição de pergunta**. O cérebro troca "quanto
custa a bola?" por "que número é fácil de separar de 1,10?" e devolve 10 cêntimos.
É o exemplo canónico do sistema rápido a responder por cima do sistema lento. A defesa
é mecânica e barata: **verifica sempre a resposta contra *todas* as condições do
enunciado**, não apenas contra aquela que usaste.

**🔄 Variação**

Um taco e uma bola custam €1,10. O taco custa **dez vezes** mais do que a bola.
Quanto custa a bola?

*Verificação:* `symbolic` — sympy. ✔

---

## MAT-002 · O quadrado no círculo · ★★★ · 5–10 min · Geometria / diagonal

**Problema**

> Um quadrado está inscrito numa circunferência de raio **10**
> (os quatro vértices tocam a circunferência).
>
> Qual é a área do quadrado?

**🤔 Pensa primeiro**

**Dica 1** — Não procures o lado. Procura o que a circunferência te dá directamente:
liga dois vértices opostos do quadrado.

**Dica 2** — A diagonal do quadrado é o diâmetro. E a área de um quadrado pode
escrever-se em função da diagonal, sem passar pelo lado.

**🛑 STOP**

**✅ Resposta** — **200**.

**Solução**

1. A diagonal do quadrado passa pelo centro e liga dois pontos da circunferência:
   é o diâmetro, `d = 2 × 10 = 20`.
2. Num quadrado de lado `L`, `d² = L² + L² = 2L²`, logo `L² = d²/2`.
3. Área = `L² = 20²/2 = 400/2 = **200**`.

(Via lado, se insistires: `L = 20/√2 = 10√2`, e `L² = 200`. Mesmo sítio, mais trabalho.)

**🧠 Porquê**

Guarda esta: **a área de um quadrado é metade do quadrado da diagonal**. Em geometria,
resolver para o lado quando o problema te dá a diagonal é o desvio mais comum e mais
caro. Pergunta sempre: *qual é a grandeza que o enunciado me dá de graça, e existe uma
fórmula que a use directamente?*

**🔄 Variação**

E a área do **hexágono** regular inscrito na mesma circunferência? (Fica maior ou menor
do que 200? Adivinha antes de calcular.)

*Verificação:* `symbolic` ✔

---

## MAT-003 · Os zeros do fim · ★★★★ · 10–20 min · Teoria dos números

**Problema**

> Em quantos zeros termina o número **100!**
>
> (isto é, `100 × 99 × 98 × … × 2 × 1`)

**🤔 Pensa primeiro**

**Dica 1** — Não calcules 100!. Um zero no fim de um número significa um factor 10.
Quantos factores 10 há no produto?

**Dica 2** — 10 = 2 × 5. Há muito mais factores 2 do que 5 no produto, portanto o
número de zeros é o número de factores **5**. Mas atenção: o 25 contribui com dois.

**🛑 STOP**

**✅ Resposta** — **24 zeros**.

**Solução**

Cada zero final vem de um par (2, 5). Os factores 2 são muito mais abundantes,
portanto os 5 são o recurso limitante. Contam-se assim:

| Contribuição | Cálculo | Factores 5 |
|---|---|---|
| Múltiplos de 5 | ⌊100/5⌋ | 20 |
| Múltiplos de 25 (dão um 5 extra) | ⌊100/25⌋ | 4 |
| Múltiplos de 125 | ⌊100/125⌋ | 0 |
| | **Total** | **24** |

**🧠 Porquê**

Esta é a **fórmula de Legendre**: o expoente de um primo `p` em `n!` é
`⌊n/p⌋ + ⌊n/p²⌋ + ⌊n/p³⌋ + …`. Mas o princípio geral vale muito para além dela:
quando um resultado precisa de dois ingredientes, **conta só o escasso**. É o mesmo
raciocínio de um estrangulamento numa linha de produção.

**🔄 Variação**

E em quantos zeros termina 1000!? E qual é o menor `n` tal que `n!` termina em
exactamente 100 zeros — ou não existe nenhum?

*Verificação:* `brute_force` — contagem directa do expoente de 5. ✔

---
---

# 🎲 Probabilidade

## PRB-001 · Três lançamentos · ★★ · 2–5 min · Contagem de casos

**Problema**

> Lança-se uma moeda equilibrada **três vezes**.
>
> Qual é a probabilidade de sair **pelo menos duas caras**?

**🤔 Pensa primeiro**

**Dica 1** — Só há oito resultados possíveis. Escreve-os todos.

**Dica 2** — "Pelo menos duas" significa exactamente duas **ou** três. Conta as duas
famílias em separado.

**🛑 STOP**

**✅ Resposta** — **1/2** (50%).

**Solução**

Os 8 resultados equiprováveis:

```
CCC ✔   CCK ✔   CKC ✔   KCC ✔
CKK     KCK     KKC     KKK
```

Quatro têm duas ou mais caras. `4/8 = 1/2`.

Formalmente: `P = C(3,2)·(1/2)³ + C(3,3)·(1/2)³ = 3/8 + 1/8 = 4/8`.

**🧠 Porquê**

Com 8, 16 ou 36 casos equiprováveis, **enumerar não é um atalho de principiante — é o
método**. Fórmulas são para quando o espaço não cabe numa folha. E há aqui uma simetria
que dá a resposta em três segundos: com um número ímpar de lançamentos, "mais caras do
que coroas" e "mais coroas do que caras" são simétricos e cobrem todos os casos, logo
cada um vale exactamente 1/2.

**🔄 Variação**

E com **quatro** lançamentos, pelo menos duas caras? (Atenção: a simetria acima
deixa de funcionar. Porquê?)

*Verificação:* `monte_carlo` — 10⁷ ensaios → 0,4999. ✔

---

## PRB-002 · As duas moedas · ★★★★ · 10–20 min · Teorema de Bayes · 😈

**Problema**

> Tens duas moedas. Uma é **equilibrada**. A outra sai **cara 80%** das vezes.
>
> Escolhes uma ao acaso, sem olhar, e lanças **duas vezes**. Saem **duas caras**.
>
> Qual é a probabilidade de teres escolhido a moeda viciada?

**🤔 Pensa primeiro**

**Dica 1** — A resposta não é 80%, nem 50%, nem 64%. Reformula a pergunta: de todas as
vezes que este cenário acontece (escolher às cegas e sair CC), em que **fracção** delas
a moeda era a viciada?

**Dica 2** — Calcula duas quantidades: a probabilidade de escolher a justa **e** sair CC
(0,5 × 0,5²), e a de escolher a viciada **e** sair CC (0,5 × 0,8²). A resposta é a
segunda a dividir pela soma.

**🛑 STOP**

**✅ Resposta** — **64/89 ≈ 71,9%**

**Solução**

| Moeda | P(escolher) | P(CC \| moeda) | Produto |
|---|---|---|---|
| Justa | 0,5 | 0,5² = 0,25 | 0,125 |
| Viciada | 0,5 | 0,8² = 0,64 | 0,320 |
| | | **P(CC)** | **0,445** |

```
P(viciada | CC) = 0,320 / 0,445 = 320/445 = 64/89 ≈ 0,7191
```

**🧠 Porquê**

Bayes não é uma fórmula a decorar — é uma **tabela de mundos**. Escreve todas as
maneiras de o que observaste acontecer, pesa cada uma pela sua probabilidade, e vê que
fracção do total corresponde à tua hipótese. Repara também que a resposta (71,9%) fica
*abaixo* de 80%: duas caras são evidência a favor da moeda viciada, mas evidência
fraca — a moeda justa também as produz uma vez em quatro. **A força da evidência é a
razão entre as verosimilhanças (0,64 / 0,25 ≈ 2,6), não o valor absoluto de nenhuma delas.**

**🔄 Variação**

E se saíssem **três** caras? E se saísse cara-coroa — ficarias com que probabilidade?

*Verificação:* `monte_carlo` — analítico 0,71910 · simulado 0,71887 (10⁷). ✔

---

## PRB-003 · As três portas · ★★★ · 5–10 min · Probabilidade condicional · 😈 · clássico

**Problema**

> Num concurso há **três portas**. Atrás de uma está um carro; atrás das outras duas,
> cabras. Escolhes a porta 1.
>
> O apresentador, que **sabe** onde está o carro, abre sempre uma porta que não
> escolheste e que tem uma cabra. Abre a porta 3: cabra.
>
> Oferece-te trocar para a porta 2.
>
> Trocar aumenta as tuas hipóteses?

**🤔 Pensa primeiro**

**Dica 1** — A informação decisiva não é a porta que se abriu. É que o apresentador
**sabia** onde estava o carro, e por isso nunca poderia ter aberto a porta do carro.

**Dica 2** — Qual era a probabilidade de teres acertado à primeira? Essa probabilidade
mudou depois de o apresentador abrir uma porta que ele *tinha* de conseguir abrir de
qualquer maneira?

**🛑 STOP**

**✅ Resposta** — **Sim. Trocar dá 2/3; ficar dá 1/3.**

**Solução**

A tua escolha inicial acerta com probabilidade 1/3. Nada do que o apresentador faz
altera isso, porque ele consegue sempre abrir uma porta com cabra, aconteça o que
acontecer. Logo:

| | Prob. inicial | Se ficares | Se trocares |
|---|---|---|---|
| Escolheste o carro | 1/3 | ✅ ganhas | ❌ perdes |
| Escolheste uma cabra | 2/3 | ❌ perdes | ✅ **ganhas** |

Nos 2/3 dos casos em que começaste numa cabra, o apresentador é **obrigado** a abrir a
outra cabra — e trocar leva-te ao carro. Trocar ganha em 2 de 3 jogos.

**🧠 Porquê**

O erro é tratar a acção do apresentador como um sorteio. Não é: é uma escolha
**condicionada** ao que ele sabe. Sempre que alguém informado filtra as opções que te
mostra, essa filtragem transporta informação — e a informação vai toda para a porta
que ele **não** abriu.

Teste decisivo: imagina **100 portas**. Escolhes uma (1% de hipóteses). O apresentador
abre 98 com cabras. Trocas para a única que sobra? Agora é evidente.

**🔄 Variação**

E se o apresentador **não** soubesse onde está o carro e tivesse aberto a porta 3 por
sorte, calhando ser uma cabra? Trocar continua a valer a pena? *(A resposta muda —
e é por isso que este problema causa tanta discussão.)*

*Verificação:* `monte_carlo` — 10⁷ ensaios → 0,6667 / 0,3333. ✔

---
---

# 🌀 Pensamento lateral

## LAT-001 · O copo de água · ★★★ · 5–10 min · Pressuposto sobre a intenção

**Problema**

> Um homem entra num restaurante e pede um copo de água.
>
> O empregado aponta-lhe uma arma.
>
> O homem diz «obrigado» e vai-se embora.
>
> Porquê?

**🤔 Pensa primeiro**

**Dica 1** — Ninguém neste cenário é violento e ninguém está em perigo. O homem sai
satisfeito, e o empregado ajudou-o. Pergunta o que ele **realmente** queria.

**Dica 2** — A água era um meio, não um fim. Havia outra forma de resolver o problema
dele — e o empregado encontrou-a.

**🛑 STOP**

**✅ Resposta** — O homem tinha **soluços**.

**Solução**

Ele pediu água para tentar parar os soluços. O empregado percebeu e resolveu o problema
de forma mais eficaz: um **susto**. Os soluços passaram, e o homem agradeceu — já não
precisava da água.

**🧠 Porquê**

O enunciado convida-te a interpretar a arma como ameaça, porque associaste "arma" a
"assalto" antes de teres qualquer prova. Mas o pressuposto verdadeiramente escondido é
outro, e é mais interessante: **assumiste que o pedido dito era o pedido real**. As
pessoas raramente pedem o que querem — pedem o que julgam ser o caminho para o que
querem. Este é o mesmo erro que se comete a receber requisitos de um cliente.

**🔄 Variação**

Mesma cena, mas desta vez o empregado serve-lhe a água e o homem sai **furioso**. Porquê?

*Verificação:* `manual` — teste de inevitabilidade: passa. ✔

---

## LAT-002 · O sétimo andar · ★★★ · 5–10 min · Pressuposto sobre a capacidade

**Problema**

> Um homem vive no 10.º andar de um prédio.
>
> Todas as manhãs entra no elevador, carrega no botão do rés-do-chão e vai trabalhar.
>
> Ao regressar, entra no elevador, carrega no botão do **7.º andar** e sobe os últimos
> três andares a pé.
>
> Excepto quando chove — nesses dias vai directo ao 10.º.
>
> Porquê?

**🤔 Pensa primeiro**

**Dica 1** — Ele não escolhe parar no 7.º. Não consegue fazer melhor. O que é preciso
para carregar no botão do 10.º que não é preciso para carregar no do 7.º?

**Dica 2** — Nos dias de chuva ele leva consigo uma coisa que não leva nos outros dias.

**🛑 STOP**

**✅ Resposta** — Ele é **baixo** e não alcança o botão do 10.º. O 7.º é o mais alto a
que chega. Nos dias de chuva leva um **guarda-chuva**, e usa-o para carregar no botão.

**Solução**

Todos os elementos apontam para a mesma explicação e nenhum sobra: o botão mais alto
alcançável, o esforço voluntário de subir três andares, e a excepção exacta dos dias
de chuva — que é a única pista que identifica o guarda-chuva.

**🧠 Porquê**

Num problema lateral bem construído, a **excepção é a chave**. A parte da história que
parece um detalhe decorativo (a chuva) é o que distingue a solução verdadeira de dez
soluções plausíveis. Regra operacional: quando estiveres encravado, pergunta *"que
detalhe do enunciado é que a minha teoria ainda não explica?"* — e resolve esse.

**🔄 Variação**

E se ele subisse a pé **todos** os dias, chuva ou sol, mas apenas às terças-feiras
fosse directo ao 10.º?

*Verificação:* `manual` ✔

---

## LAT-003 · O hotel · ★★★★ · 10–20 min · Pressuposto sobre o contexto

**Problema**

> Uma mulher empurra o seu carro até um hotel.
>
> Quando lá chega, percebe que está falida.
>
> O que aconteceu?

**🤔 Pensa primeiro**

**Dica 1** — Não há avaria, não há gasolina em falta, e não há dívidas. Repara que ela
*empurra* o carro com a mão — não o conduz.

**Dica 2** — O carro é pequeno o suficiente para caber na palma da mão. E o hotel
pertence a outra pessoa.

**🛑 STOP**

**✅ Resposta** — Ela está a jogar **Monopólio**.

**Solução**

A peça em forma de carro avança as casas que os dados mandaram e cai numa propriedade
com hotel construído. A renda é superior ao dinheiro que ela tem: falência.

**🧠 Porquê**

Aqui não é uma palavra que engana — é a **escala**. "Carro", "hotel" e "falida" são
todas literais; só o tamanho e o contexto é que não são o que assumiste. Quando um
cenário parece impossível no mundo real, verifica se é possível num **mundo mais
pequeno**: um jogo, um sonho, um ecrã, uma maquete, uma história dentro da história.

**🔄 Variação**

Um homem vira um objecto ao contrário e uma pessoa morre. Não lhe tocou. O que era o
objecto? *(pista: areia)*

*Verificação:* `manual` ✔

---
---

# ⚖️ Dilemas

> **Esta secção não tem respostas.** Tem argumentos. Se acabares um destes problemas
> com a certeza de que só um dos lados é defensável, provavelmente não leste bem o outro.

## DIL-001 · A alavanca · ★★★ · 5–10 min · Consequencialismo vs. deontologia

**Problema**

> Um comboio desgovernado vai atropelar **cinco pessoas**.
>
> Podes accionar uma alavanca e desviá-lo para outra linha, onde está **uma pessoa**,
> que morrerá.
>
> Ninguém te vê. Não há terceira opção. Não há tempo para avisar ninguém.
>
> Accionas a alavanca?

**🤔 Decide primeiro**

Decide **antes** de virar a página. E escreve mentalmente *porquê* — a razão importa
mais do que a escolha.

**Reflexão 1** — Se disseste sim: a tua razão é o número, ou o facto de não conheceres
nenhum deles?

**Reflexão 2** — Se disseste não: a tua razão é não querer matar, ou não querer ser
responsável? São coisas diferentes.

**⚖️ Não há resposta certa**

**Argumentos para accionar**

- Cinco vidas valem mais do que uma. Se as vidas valem todas o mesmo, a aritmética é
  trivial e recusar é escolher o pior resultado por conforto pessoal.
- Não agir também é uma escolha, com consequências. A inacção não te devolve as mãos
  limpas — devolve-te cinco mortos.
- Se todos nesta situação accionassem a alavanca, morreriam menos pessoas no mundo.

**Argumentos para não accionar**

- Há uma diferença moral entre **deixar morrer** e **matar**. Ao puxar a alavanca,
  tornas-te a causa da morte de alguém que não estava em perigo.
- A pessoa da segunda linha não consentiu em ser um recurso. Usá-la como meio para
  salvar outros trata-a como objecto.
- Um mundo em que estranhos calculam o teu valor e agem sobre ti é pior do que um mundo
  em que ninguém decide quem morre — mesmo que morra mais gente.

**⚖️ Agora as variações**

Responde a cada uma antes de ler a seguinte. Se alguma te fizer mudar de resposta,
essa é a mais interessante.

1. Em vez da alavanca, tens de **empurrar** um homem grande de uma ponte para travar o
   comboio. Mesmos números. Fazes?
   *(A maioria das pessoas puxa a alavanca e não empurra. Se és uma delas: qual é a
   diferença moral, se o resultado é idêntico?)*
2. E se a pessoa sozinha for **alguém que conheces**?
3. E se as cinco pessoas estivessem na linha por terem ignorado um aviso, e a pessoa
   sozinha estivesse a trabalhar legalmente na via?
4. E se fosses **tu** a estar na segunda linha, e outra pessoa tivesse a alavanca —
   o que é que querias que ela fizesse?

**🧠 O que está em jogo**

Duas famílias éticas em colisão frontal. O **consequencialismo** avalia actos pelos
resultados: cinco > um, fim. A **deontologia** avalia actos pelo tipo de acto: matar é
proibido, mesmo com bons resultados. Nenhuma das duas sobrevive intacta a todas as
variações — e é por isso que o problema tem cinquenta anos e continua a ser discutido.

O teste mais útil não é qual escolheste, mas se a tua resposta se mantém **coerente**
da alavanca até à ponte.

---

## DIL-002 · A carteira · ★★ · 2–5 min · Honestidade vs. necessidade

**Problema**

> Encontras uma carteira na rua com **€500** em dinheiro e um cartão com morada,
> mas sem telefone nem email.
>
> Pelo cartão percebes que o dono é claramente rico. Tu estás com o mês apertado —
> €500 resolviam-te um problema real.
>
> Ninguém te viu.
>
> O que fazes?

**🤔 Decide primeiro**

**Reflexão** — Antes de virares: mudarias de resposta se a morada fosse de um bairro
pobre? Se sim, o que é que isso diz sobre o critério que estás a usar?

**⚖️ Não há resposta certa**

**Argumentos para devolver**

- O dinheiro não é teu. A situação financeira do dono não altera a propriedade.
- "Ele não precisa" é um critério que não aguenta ser generalizado: quem decide quanto
  é preciso?
- O custo de te tornares uma pessoa que fica com carteiras alheias é pago por ti,
  todos os dias, e é maior do que €500.

**Argumentos para ficar (ou para hesitar)**

- A utilidade marginal de €500 é enormemente maior para ti do que para ele. O mundo
  fica melhor, em soma, se ficares.
- Devolver tem um custo real: tempo, deslocação, e nenhuma garantia de reciprocidade.
- Grande parte do impulso de devolver é medo de ser apanhado disfarçado de moral —
  e o enunciado retirou esse medo de propósito.

**⚖️ Variações**

1. E se fossem **€20**? E se fossem **€50.000**?
2. E se, ao ires devolver, percebesses que o dono é uma pessoa que te fez mal no passado?
3. E se em vez de dinheiro fossem documentos sem valor para ti mas essenciais para ele?
4. E se **te vissem** a encontrar a carteira?
   *(Se esta última muda a tua resposta, a questão nunca foi moral.)*

**🧠 O que está em jogo**

A diferença entre **moral** e **reputação**. Muitas pessoas descobrem, ao responder à
variação 4, que estavam a modelar o custo social e não o acto. Isso não faz de ninguém
má pessoa — mas é bom saber qual dos dois motores está a conduzir.

---

## DIL-003 · O que sabes · ★★★★ · 10–20 min · Lealdade vs. verdade

**Problema**

> Descobres, por acaso e com certeza, que o teu melhor amigo está a trair a mulher.
>
> Ela também é tua amiga, há tantos anos como ele.
>
> Nenhum dos dois sabe que tu sabes.
>
> Contas?

**🤔 Decide primeiro**

**Reflexão 1** — A tua resposta seria a mesma se soubesses que ela **suspeita** e te
perguntasse directamente?

**Reflexão 2** — Existe uma terceira opção que não é nem contar nem calar. Consegues
nomeá-la antes de virar a página?

**⚖️ Não há resposta certa**

**Argumentos para contar**

- Ela está a tomar decisões de vida com informação falsa. Guardar silêncio é participar
  no engano.
- A amizade dela contigo é tão antiga como a dele. Escolher o silêncio já é escolher
  um lado — apenas de forma confortável para ti.
- Riscos concretos (saúde, dinheiro, futuro) não são teus para decidir esconder.

**Argumentos para não contar**

- Não é a tua vida, e não sabes o que existe entre eles. Casamentos têm acordos que
  não te foram explicados.
- A tua intervenção destrói uma relação com base num acto teu, não dela — e vais ser
  para sempre a pessoa que trouxe a notícia.
- Podes estar errado sobre o significado do que viste, mesmo estando certo sobre o facto.

**A terceira opção**

Confrontar **o teu amigo** primeiro: dizer-lhe o que sabes e dar-lhe um prazo para
contar ele próprio. Preserva a agência dele, mas não te torna cúmplice indefinido.
Tem um custo: podes perder a amizade sem resolver nada, e ele pode simplesmente mentir.

**⚖️ Variações**

1. E se ela estivesse **grávida**?
2. E se fosse **ela** a trair, e ele o teu melhor amigo? Mudou alguma coisa? *Porquê?*
3. E se te tivessem contado em confidência, em vez de teres visto?
4. E se ela te perguntasse a ti, directamente, a olhar-te nos olhos?

**🧠 O que está em jogo**

Dois deveres genuínos em conflito — lealdade e honestidade — sem hierarquia óbvia entre
eles. Repara que a variação 4 muda o problema por completo: **calar** e **mentir** não
são a mesma coisa, e muita gente que aceita o primeiro recusa o segundo. Encontrar
exactamente onde é que essa linha passa em ti é o objectivo deste problema.

---
---

# 🤔 O que farias?

> Também não há resposta certa aqui. Mas, ao contrário dos Dilemas, **há melhor e pior**.
> As abordagens apresentadas não são as únicas — são as que resistem a ser postas em
> prática.

## WWY-001 · Mil euros e três meses · ★★★★ · 10–20 min · Restrições e alavancagem

**Problema**

> Tens **€1.000** e **três meses**.
>
> - Não podes pedir dinheiro emprestado nem levantar investimento.
> - Sabes programar, mas não tens audiência nenhuma.
> - Ao fim dos três meses, o negócio tem de dar dinheiro — não "potencial".
>
> O que farias?

**🤔 Planeia primeiro**

Escreve o teu plano em cinco linhas antes de virar a página: o que vendes, a quem, e
como é que a primeira pessoa te encontra.

**Antes de continuares** — se o teu plano contém a palavra "lançar", pergunta-te quando
é que o primeiro cliente paga. Se a resposta for "depois de estar pronto", tens um
problema de calendário, não de produto.

**🤔 Uma abordagem possível**

**A restrição verdadeira não é o dinheiro. É a audiência.** €1.000 chegam para servidores,
domínio e ferramentas durante três meses com folga. O que não tens é distribuição — e
é isso que o plano tem de resolver primeiro.

**Estratégia A — Serviços primeiro, produto depois**
Vender trabalho de programação a um nicho estreito (ex.: automações para clínicas
dentárias). Receita na semana 2, e cada cliente é uma entrevista paga sobre os problemas
do sector. Ao fim de três meses, tens dinheiro e sabes qual é o produto.
*Custo:* troca-se tempo por dinheiro; não escala. *É o caminho com maior probabilidade
de terminar com receita.*

**Estratégia B — Parasitar uma plataforma existente**
Construir onde já existe procura com intenção de compra: uma extensão, um plugin, um
add-on de marketplace. A audiência é da plataforma; tu só precisas de resolver uma dor
concreta e ficar bem posicionado na pesquisa interna.
*Custo:* dependes de regras que não controlas. *É o caminho com melhor rácio
esforço/alcance.*

**Estratégia C — Vender antes de construir**
Escolher um problema, escrever a página de vendas, e tentar cobrar **na primeira semana**,
antes de existir produto. Zero vendas em duas semanas = muda de problema, com €1.000
ainda intactos.
*Custo:* desconfortável. *É o caminho que maximiza o que aprendes por euro gasto.*

**Estratégia D — Arbitragem de trabalho aborrecido**
Encontrar uma tarefa manual, repetitiva e cara que alguém já paga a humanos, e vender
o resultado — não o software. Cobras pelo output, não por licenças.
*Custo:* muito trabalho manual no início. *É o caminho que valida a disponibilidade
para pagar mais depressa.*

**❌ O erro mais comum**

Gastar os três meses a construir e o dia 89 a descobrir se alguém quer. Com três meses
de prazo, a única sequência que faz sentido é **vender → construir → entregar**, e não
o contrário. O segundo erro mais comum é gastar os €1.000: neste cenário, dinheiro
gasto é quase sempre dinheiro que substituiu uma conversa com um cliente.

**🔄 Restrição adicional**

Mesmo problema, mas **não podes escrever uma única linha de código**. Muda a resposta?
*(Se muda muito, o teu plano dependia mais das tuas ferramentas do que do mercado.)*

---

## WWY-002 · A casa da aldeia · ★★★ · 5–10 min · Custos afundados

**Problema**

> Herdaste uma casa numa aldeia a **3 horas** de onde vives.
>
> - Precisa de **€30.000** de obras.
> - Vale **€25.000** no estado actual, e ninguém a compra há dois anos.
> - Custa-te **€1.200/ano** em impostos e manutenção mínima.
> - Era a casa da tua avó. Passaste lá todos os Verões.
>
> O que farias?

**🤔 Planeia primeiro**

**Antes de continuares** — separa as duas perguntas que estás a misturar: *quanto vale
esta casa?* e *quanto vale o que sinto por ela?* Nenhuma das duas se responde com a outra.

**🤔 Uma abordagem possível**

**A conta fria:** €1.200/ano é o preço da opção de adiar. Não é catastrófico, mas é
uma subscrição vitalícia a uma decisão não tomada.

**Estratégia A — Vender ao preço que o mercado dá**
Aceitar €20–25.000, guardar dois ou três objectos da casa e fotografar tudo antes.
Elimina a subscrição e liberta capital.
*Quando faz sentido:* se ao fim de dois anos ainda não a usaste, a resposta empírica
já foi dada.

**Estratégia B — Rendimento mínimo viável**
Fazer só as obras que a tornam habitável (não as que a tornam bonita) e arrendar por
temporadas. Objectivo: cobrir os €1.200 e parar a hemorragia, sem investir €30.000.
*Quando faz sentido:* se a aldeia tiver alguma procura sazonal.

**Estratégia C — Prazo explícito**
Dar-te **24 meses**: usa-la pelo menos seis vezes nesse período. Se não acontecer,
vendes sem discussão. Transforma uma indecisão permanente numa experiência com fim.
*Quando faz sentido:* quando não consegues distinguir se queres a casa ou a memória.

**Estratégia D — Partilhar o custo**
Trazer primos ou irmãos para co-proprietários com quota de despesas e calendário de uso.
*Quando faz sentido:* se a ligação afectiva for familiar e não só tua. *Risco:* uma
casa com quatro donos e nenhum responsável degrada-se mais depressa.

**❌ O erro mais comum**

Raciocinar a partir dos €30.000 de obras como se fossem obrigatórios. Não são: são o
custo de a pôr como estava na tua memória. A pergunta certa é *qual é o menor
investimento que resolve o problema real* — e o problema real, quase sempre, é o
€1.200/ano e a culpa, não as paredes.

O segundo erro é o **custo afundado**: "já paguei impostos dois anos, agora não vou
vender". Esse dinheiro foi-se de qualquer maneira e não deve entrar na decisão.

**🔄 Restrição adicional**

E se um vizinho te oferecesse **€40.000** — 60% acima do valor de mercado — com a
condição de assinares na próxima semana?

---

## WWY-003 · Seis meses de folga · ★★★★ · 10–20 min · Risco e sequenciação

**Problema**

> Tens **seis meses** de despesas poupadas.
>
> Odeias o teu emprego, mas paga bem. Não tens outro à vista, nem uma ideia clara
> do que queres fazer a seguir. Não tens dependentes.
>
> O que farias?

**🤔 Planeia primeiro**

**Antes de continuares** — nomeia exactamente o que odeias: o trabalho, o chefe, o
sector, ou a ausência de progresso? As quatro respostas dão planos completamente
diferentes, e três delas não exigem despedires-te.

**🤔 Uma abordagem possível**

**Estratégia A — Sair já**
Seis meses são um prazo real. Força clareza e elimina a fadiga que te impede de pensar.
*Custo:* procurar emprego sem emprego enfraquece a tua posição negocial, e a ansiedade
do mês 4 costuma levar a aceitar exactamente o tipo de trabalho de que fugiste.

**Estratégia B — Ficar e comprar tempo**
Manter o salário e comprometer 8 horas por semana com uma alternativa concreta
(projecto, portefólio, entrevistas), com data de revisão marcada ao fim de 90 dias.
*Custo:* o esforço a seguir a um dia mau é pequeno, e é fácil enganar-se a si próprio
sobre quanto se avançou. *É a opção com melhor rácio risco/aprendizagem, se a data for
mesmo cumprida.*

**Estratégia C — Sair, mas com destino**
Ficar até teres uma oferta assinada, e usar os seis meses de poupança apenas como rede.
*Custo:* mais lento, e mantém-te no ambiente que odeias. *É a opção que a maioria das
pessoas deve escolher e não escolhe, porque não é dramática.*

**Estratégia D — Mudar o emprego em vez do trabalho**
Pedir mudança de equipa, de função ou de horário antes de sair. É a intervenção mais
barata e a menos tentada.
*Custo:* pode não resultar — mas descobrir isso custa uma conversa e duas semanas.

**❌ O erro mais comum**

Tratar isto como uma escolha binária entre "ficar infeliz" e "saltar no vazio". Quase
sempre existe uma sequência que reduz o risco: **testar antes de saltar**. E há um erro
de contabilidade frequente: seis meses de despesas não são seis meses de pista — são
quatro, porque ninguém quer chegar ao último euro, e as decisões tomadas com um mês de
poupança são todas más.

**🔄 Restrição adicional**

Mesmo cenário, mas com **um filho de dois anos**. Quais das quatro estratégias
sobrevivem?

---
---

# 💻 Programação

## PRG-001 · A lista que cresce · ★★★ · 5–10 min · Iteração sobre estrutura mutável

**Problema**

> O que imprime este código?
>
> ```python
> x = [1, 2, 3]
> for i in x:
>     x.append(i + 3)
>     if len(x) > 6:
>         break
> print(x)
> ```

**🤔 Pensa primeiro**

**Dica 1** — O `for` em Python não trabalha sobre uma cópia da lista. Trabalha sobre um
índice interno que avança na lista **real**, tal como ela está em cada momento.

**Dica 2** — Faz a tabela: em cada iteração escreve o índice actual, o valor de `i`, a
lista depois do `append`, e o comprimento. Pára quando o comprimento passar de 6.

**🛑 STOP**

**✅ Resposta**

```
[1, 2, 3, 4, 5, 6, 7]
```

**Solução**

| Iteração | Índice | `i` | `x` depois do append | `len` | `> 6`? |
|---|---|---|---|---|---|
| 1 | 0 | 1 | `[1,2,3,4]` | 4 | não |
| 2 | 1 | 2 | `[1,2,3,4,5]` | 5 | não |
| 3 | 2 | 3 | `[1,2,3,4,5,6]` | 6 | não (6 não é > 6) |
| 4 | 3 | 4 | `[1,2,3,4,5,6,7]` | 7 | **sim → break** |

Repara na quarta iteração: `i` vale **4**, um elemento que não existia quando o ciclo
começou. Sem o `break`, o ciclo nunca terminaria.

**🧠 Porquê**

Iterar sobre uma coleção que estás a modificar é um dos erros mais antigos da
programação. Em Python, o iterador de lista guarda um índice, não um instantâneo:
acrescentar durante o ciclo empurra o fim para longe, e remover faz o ciclo **saltar**
elementos silenciosamente — que é o caso pior, porque não rebenta.

Regra: itera sobre uma cópia (`for i in x[:]`) ou constrói uma lista nova. Nunca
modifiques aquilo sobre que estás a iterar.

**🔄 Variação**

E se em vez de `x.append(...)` fosse `x.remove(i)`? O que imprime `x` no fim — e quantas
iterações acontecem?

*Verificação:* `execute` — saída real confere. ✔

---

## PRG-002 · O argumento por omissão · ★★★★ · 10–20 min · Avaliação de defaults

**Problema**

> O que imprime este código?
>
> ```python
> def adicionar(item, lista=[]):
>     lista.append(item)
>     return lista
>
> print(adicionar(1))
> print(adicionar(2))
> print(adicionar(3, []))
> print(adicionar(4))
> ```

**🤔 Pensa primeiro**

**Dica 1** — Pergunta-te *quando* é que a lista `[]` do cabeçalho é criada: em cada
chamada, ou uma só vez?

**Dica 2** — O valor por omissão é avaliado **uma vez**, quando a função é definida, e
fica guardado no próprio objecto função. As chamadas que não passam o argumento
partilham todas essa mesma lista.

**🛑 STOP**

**✅ Resposta**

```
[1]
[1, 2]
[3]
[1, 2, 4]
```

**Solução**

| Chamada | Usa que lista? | Estado depois | Imprime |
|---|---|---|---|
| `adicionar(1)` | a partilhada | `[1]` | `[1]` |
| `adicionar(2)` | a partilhada | `[1, 2]` | `[1, 2]` |
| `adicionar(3, [])` | uma lista nova | a partilhada não muda | `[3]` |
| `adicionar(4)` | a partilhada | `[1, 2, 4]` | `[1, 2, 4]` |

Podes ver o objecto directamente: `adicionar.__defaults__` devolve `([1, 2, 4],)`.

**🧠 Porquê**

O valor por omissão é avaliado **na definição**, não na chamada. Com valores imutáveis
(`0`, `None`, `"x"`) isso não se nota. Com uma lista, um dicionário ou um conjunto,
crias estado global escondido dentro da função — e o bug aparece semanas depois, em
produção, com dados que se acumulam entre pedidos.

A forma correcta:

```python
def adicionar(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista
```

**🔄 Variação**

E se o valor por omissão fosse `lista=[]` mas a função fizesse `lista = lista + [item]`
em vez de `lista.append(item)`? O que muda, e porquê?

*Verificação:* `execute` — saída real confere. ✔

---

## PRG-003 · Vinte e cinco cavalos · ★★★★★ · 20+ min · Torneios e limites inferiores

**Problema**

> Tens **25 cavalos** e uma pista com **5 raias**.
>
> Cada corrida põe 5 cavalos a correr e diz-te apenas a **ordem de chegada** entre eles
> — não há cronómetro, não há tempos.
>
> Cada cavalo corre sempre à mesma velocidade e não há empates.
>
> Qual é o **número mínimo de corridas** para determinares os **3 mais rápidos**, por ordem?

**🤔 Pensa primeiro**

**Dica 1** — Começa pelas 5 corridas óbvias (todos os cavalos uma vez) e uma sexta com
os 5 vencedores. Depois pergunta: dos 25, quantos ainda podem estar no pódio?

**Dica 2** — Depois da corrida dos vencedores, o 1.º lugar está decidido. Restam
exactamente **5 candidatos** aos 2.º e 3.º lugares. Uma corrida chega para os separar.

**🛑 STOP**

**✅ Resposta** — **7 corridas.**

**Solução**

**Corridas 1–5:** divide os 25 em 5 grupos e corre cada grupo. Chama aos grupos
A, B, C, D, E, e aos cavalos `A1 > A2 > A3 …` pela ordem de chegada.
Os 4.º e 5.º de cada grupo estão eliminados (têm 3 cavalos à frente): sobram 15.

**Corrida 6:** os cinco vencedores `A1, B1, C1, D1, E1`. Digamos que dá
`A1 > B1 > C1 > D1 > E1`.

- **`A1` é o mais rápido dos 25** — ganhou ao seu grupo e a todos os outros vencedores.
- `D1` e `E1` têm pelo menos 3 cavalos à frente (`A1, B1, C1`): eliminados, e com eles
  os grupos D e E inteiros.
- `C2` e `C3` têm pelo menos 3 à frente (`A1, B1, C1`): eliminados.
- `B3` tem pelo menos 3 à frente (`A1, B1, B2`): eliminado.

Sobram exactamente **5 candidatos** aos 2.º e 3.º lugares:
`A2, A3, B1, B2, C1`.

**Corrida 7:** corre esses cinco. Os dois primeiros são o 2.º e o 3.º cavalos mais
rápidos do conjunto. **Total: 7.**

*Porque não 6:* com 6 corridas vês no máximo 30 posições, mas mais importante — depois
das 6 primeiras existem sempre 5 candidatos genuínos aos lugares 2 e 3, e nenhuma
comparação anterior os ordena entre si. É preciso pelo menos mais uma corrida.

**🧠 Porquê**

Duas ideias, e ambas se transferem para código:

1. **Eliminação por transitividade.** Não precisas de comparar tudo com tudo. Se
   `x < y` e `y < z`, a comparação `x` vs `z` é desperdício. É exactamente o que um
   torneio faz, e é por isso que encontrar o máximo custa `n−1` comparações e não `n²`.
2. **Encontrar os `k` maiores é muito mais barato do que ordenar.** Ordenar 25 cavalos
   exigiria dezenas de corridas; encontrar os 3 primeiros exige 7. É a diferença entre
   `sorted(xs)[:k]` e `heapq.nlargest(k, xs)` — e a razão pela qual bases de dados têm
   uma optimização dedicada a `ORDER BY ... LIMIT k`.

**🔄 Variação**

E para encontrar os **4** mais rápidos? *(Cuidado: a resposta não é 8.)*
E se quisesses o **último** classificado — quantas corridas?

*Verificação:* `brute_force` — simulação sobre permutações aleatórias, confirmando que
o procedimento de 7 corridas identifica sempre o pódio correcto. ✔

---
---

## Resumo do banco inicial

| Categoria | IDs | ★ médio | Verificação |
|---|---|---|---|
| 🧠 Lógica | LOG-001…003 | 3,0 | `exhaustive` |
| 🕵️ Enigmas | ENI-001…003 | 2,7 | `manual` / `brute_force` |
| 🔢 Matemática | MAT-001…003 | 3,0 | `symbolic` / `brute_force` |
| 🎲 Probabilidade | PRB-001…003 | 3,0 | `monte_carlo` |
| 🌀 Lateral | LAT-001…003 | 3,3 | `manual` |
| ⚖️ Dilemas | DIL-001…003 | 3,0 | `n/a` |
| 🤔 O que farias? | WWY-001…003 | 3,7 | `n/a` |
| 💻 Programação | PRG-001…003 | 4,0 | `execute` |

**Média global: ★3,2** — acima do alvo de ★2,9 do Volume I. Faltam problemas ⭐ e ⭐⭐
no banco inicial; é a primeira coisa a gerar.

**Todos os problemas com resposta única foram verificados por código** (ver
[`07`](07-pipeline-de-validacao.md)), incluindo a unicidade — não apenas a correcção
da resposta.
