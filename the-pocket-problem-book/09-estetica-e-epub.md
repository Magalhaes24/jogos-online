# 09 — Estética e EPUB

## Princípio

> O X4 deve parecer um livro, não uma página web.

Referência visual: livro de puzzles de 1980. Monocromático, tipografia grande,
muito espaço branco, régua horizontal como único ornamento.

---

## O que não usar

| Proibido | Porquê |
|---|---|
| Imagens (excepto diagramas essenciais) | E-ink lento; ficheiro grande; refresh feio |
| Cor | Não existe |
| Cinzentos claros | < 40% de preto desaparece em e-ink |
| Fontes embutidas | O leitor tem as dele; o X4 já rende bem |
| Tabelas com mais de 3 colunas | Não cabem |
| Notas de rodapé | Navegação hostil |
| JavaScript, formulários | Não corre |
| `position`, `float`, colunas | Comportamento imprevisível |

---

## Tipografia

```css
body {
  font-family: serif;
  font-size: 1em;          /* respeita a definição do leitor */
  line-height: 1.5;
  margin: 0;
  text-align: left;        /* nunca justificado: sem hifenização fica horrível */
  hyphens: none;
}
```

Regra geral: **definir o mínimo possível**. Cada propriedade que não defines é uma
propriedade que o leitor pode controlar no dispositivo.

---

## Os blocos

```css
/* Cada bloco de um problema é uma página física */
.page { page-break-after: always; }

/* Cartão de metadados */
.meta {
  text-align: center;
  border-top: 2px solid #000;
  border-bottom: 2px solid #000;
  padding: 1.2em 0;
  margin-bottom: 2em;
}
.meta .id     { font-size: 0.85em; letter-spacing: 0.25em; }
.meta .title  { font-size: 1.5em; text-transform: uppercase; margin: 0.4em 0; }
.meta .stars  { font-size: 1.1em; letter-spacing: 0.15em; }
.meta .time   { font-size: 0.85em; }

/* Barreiras: PENSA PRIMEIRO e STOP */
.barrier {
  text-align: center;
  margin-top: 25%;
  font-size: 1.6em;
  line-height: 2;
  page-break-after: always;
}
.barrier .symbol { font-size: 3em; display: block; margin-bottom: 0.5em; }

/* Dicas */
.hint { margin-top: 2em; }
.hint h2 { font-size: 1.2em; text-transform: uppercase; letter-spacing: 0.1em; }

/* Resposta: sozinha, grande, centrada */
.answer {
  text-align: center;
  margin-top: 20%;
  font-size: 1.5em;
  page-break-after: always;
}

/* Cartão final */
.card {
  border-top: 1px solid #000;
  margin-top: 2em;
  padding-top: 1em;
  font-size: 0.85em;
  font-family: monospace;
}
```

---

## Anatomia em HTML

```html
<!-- [1] problema -->
<section class="page">
  <div class="meta">
    <div class="id">LOG-034</div>
    <div class="title">As três caixas</div>
    <div class="stars">★★★☆☆</div>
    <div class="time">5–10 MIN</div>
  </div>
  <p>Há três caixas: A, B e C. Apenas uma contém ouro…</p>
  <p style="text-align:center;margin-top:3em">PENSA.</p>
</section>

<!-- [2] barreira -->
<section class="barrier">
  <span class="symbol">🤔</span>
  PENSA PRIMEIRO<br>
  <small>Não avances.</small>
</section>

<!-- [3] dica 1 --> …
<!-- [5] barreira STOP -->
<section class="barrier">
  <span class="symbol">🛑</span>
  STOP<br>
  <small>Se ainda não tentaste,<br>não avances.</small>
</section>

<!-- [6] resposta -->
<section class="answer">
  ✅<br>O ouro está em B.
</section>
```

---

## Estrutura do EPUB

```
pocket-problems.epub
├── mimetype
├── META-INF/container.xml
└── OEBPS/
    ├── content.opf
    ├── toc.ncx          ← EPUB 2, o X4 lê melhor
    ├── nav.xhtml        ← EPUB 3
    ├── style.css
    ├── 000-cover.xhtml
    ├── 001-menu.xhtml           ← 🎲 escolhe o teu desafio
    ├── 002-como-usar.xhtml
    ├── 010-jump-5min.xhtml      ← listas de salto
    ├── 011-jump-10min.xhtml
    ├── 012-jump-30min.xhtml
    ├── 020-jump-pensar.xhtml
    ├── …
    ├── 100-LOG-001.xhtml        ← um ficheiro por problema (9 secções)
    ├── 101-LOG-002.xhtml
    ├── …
    ├── 900-daily.xhtml          ← ☀️ tabela dos 365 dias
    ├── 910-index-id.xhtml
    ├── 911-index-difficulty.xhtml
    └── 912-index-concept.xhtml
```

**Um ficheiro XHTML por problema.** Não um ficheiro por página: os leitores e-ink
tratam mal centenas de ficheiros pequenos, e `page-break-after` já garante a paginação.

### Índice (toc.ncx)

Só duas profundidades:

```
The Pocket Problem Book
├── 🎲 Escolhe o teu desafio
├── Como usar este livro
├── 🧠 Lógica
│   ├── LOG-001 · As três caixas
│   └── …
├── 🕵️ Enigmas
│   └── …
└── Índices
```

**O índice não lista as páginas de solução.** Se listasse, um toque errado no
índice revelaria a resposta.

---

## Emoji

Usados como símbolos de secção (🧠 🕵️ 🔢 🎲 🌀 ⚖️ 🤔 💻 🛑 ✅ 😈 ★).

**Risco:** nem todos os e-readers têm a fonte. Mitigação: o gerador tem um modo
`--ascii` que substitui tudo por equivalentes de texto:

| Emoji | ASCII |
|---|---|
| 🧠 | `[LOG]` |
| 🛑 | `[STOP]` |
| ✅ | `[RESP]` |
| ★★★☆☆ | `***..` |
| 😈 | `!` |

Testar ambas as versões no X4 antes de gerar o Volume I inteiro.

---

## Densidade

Alvo: **um problema = 9 páginas** no X4 com tipo de letra médio.

| Bloco | Páginas |
|---|---|
| Problema | 1 |
| Pensa primeiro | 1 |
| Dica 1 | 1 |
| Dica 2 | 1 |
| STOP | 1 |
| Resposta | 1 |
| Solução | 1–2 |
| Porquê | 1 |
| Variação | 1 (partilha página com "Porquê" se ambos curtos) |

200 problemas × 9 ≈ **1800 páginas**. É um livro grosso — e é isso que se quer:
o modo aleatório (abrir ao calhar) só funciona com volume.

---

## O perfil Xteink X4

Especificações verificadas do aparelho alvo:

| | |
|---|---|
| Ecrã | 4,3", E Ink, 220 PPI (≈ 480×800) |
| Corpo | 114 × 69 × 5,9 mm · 74 g |
| Entrada | **sem táctil** — quatro botões: Back, Confirm, Página Anterior, Página Seguinte |
| Formatos | EPUB e TXT nativos; PDF e MOBI convertidos pela aplicação |
| Navegação | salto de **capítulo** (anterior / actual / seguinte), até **100 capítulos** |
| Menu Confirm | fonte, tamanho, peso, direcção de leitura, marcadores, barra de progresso |

### O que isto obriga a mudar

**1. Os hiperlinks não servem para nada.** Sem táctil e com quatro botões, não há
forma de seguir um link interno. O menu «Escolhe o teu desafio» e as dez listas de
salto — que eram a navegação principal — são inúteis neste aparelho.

Substituição: **cada problema é um capítulo**, e o número do capítulo é impresso no
cabeçalho, a seguir ao ID:

```
   34 · LOG-012
   Os apertos de mão
   ***..
   10-20 MIN
```

Os índices passam a dar endereços (`cap. 34 · LOG-012`) em vez de dependerem de links,
e o desafio do dia diz «vai ao capítulo N». Os links continuam no ficheiro — não fazem
mal a quem tiver um leitor que os suporte — mas o livro funciona inteiro sem eles.

**2. Cabem cerca de 35 caracteres por linha.** Tabelas com mais de 3 colunas não cabem.
O gerador reescreve-as automaticamente como listas empilhadas:

```
Ouro em B
A: «está aqui»: F · B: «não está
aqui»: F · C: «não está em A»: V ·
Verdadeiras: 1
```

**3. O aparelho tem menu próprio de fonte, tamanho e peso.** O CSS do perfil X4 não
fixa nenhum dos três — quem manda é o leitor.

**4. Nada de emoji.** O perfil força os equivalentes de texto (`[ STOP ]`, `***..`).
O firmware é próprio e não há garantia de fonte com emoji.

**5. Menos margem nas barreiras.** `margin-top: 22%` de 800 px empurrava o texto para
fora do ecrã. No perfil X4 são 12%.

**6. O build falha se passar de 100 capítulos.** É um `assert` no gerador, não uma
convenção — o salto de capítulo do X4 não vai além disso.

```bash
./ppb build --profile x4      # -> output/pocket-problems-vol1-x4.epub
```

*Fontes das especificações: [Good e-Reader](https://goodereader.com/blog/electronic-readers/review-of-the-xteink-x4-e-reader),
[Digital Trends](https://www.digitaltrends.com/phones/xteink-x4-review/),
[manual do fabricante](https://manuals.plus/xteink/x4-e-book-reader-manual),
[Xteink](https://www.xteink.com/products/xteink-x4).*
