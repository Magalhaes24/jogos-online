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
