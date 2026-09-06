# 01 — Especificação

## O que é

**The Pocket Problem Book** é um livro de problemas para abrir ao acaso quando tens
5 a 30 minutos livres e não queres olhar para um telemóvel.

Não é um livro para ler do princípio ao fim. É um objecto para **consultar por disposição**:

> Tenho 10 minutos e apetece-me pensar → abro na secção certa → resolvo → fecho.

## Para que dispositivo

Alvo primário: **Xteink X4** (e-ink, ecrã pequeno, navegação por *next page*).

Isto tem consequências de design que não são negociáveis:

- **Páginas curtas.** Um problema tem de caber num ecrã sem scroll mental.
- **Sem imagens complexas.** E-ink lento, contraste limitado. Texto e símbolos.
- **A navegação é linear.** O botão *next page* é a única interacção fiável.
- **Sem interactividade.** Nada de JavaScript, formulários, ou "clica para revelar".
- **A revelação é feita com páginas, não com widgets.** É essa a mecânica central.

## Os cinco princípios

### 1. O livro nunca revela a resposta por acidente
Entre o problema e a solução existem sempre páginas intermédias: *pensa primeiro*,
dica 1, dica 2, barreira STOP. Virar a página é uma decisão, não um deslize.

### 2. Cada problema tem exactamente uma resposta — ou assume-se que não tem nenhuma
Categorias de dedução, matemática, probabilidade e programação exigem **unicidade demonstrada**.
Dilemas e "O que farias?" declaram explicitamente que não têm resposta certa.
Não existe meio-termo: um problema ambíguo apresentado como se tivesse resposta única é um bug.

### 3. A solução explica o princípio, não só o resultado
Depois de "a resposta é 64/89" vem sempre "porquê" — a ideia transferível.
Se o leitor sai sem ter aprendido nada, o problema falhou.

### 4. Metadados antes do conteúdo
Dificuldade e tempo estimado aparecem **antes** do enunciado, para o leitor escolher
com base no tempo que tem.

### 5. O livro é gerado, não escrito
Tudo vive numa base de dados JSON. O EPUB é um artefacto de saída, descartável e
regenerável. Corrigir uma solução significa editar um campo e recompilar.

## A identidade

Não é "livro de puzzles". É:

```
THE POCKET PROBLEM BOOK
200 problems for when you have nothing to do.
```

Estética de livro de puzzles dos anos 80: monocromático, tipografia grande, muito espaço
branco, símbolos em vez de ícones. Ver [`09-estetica-e-epub.md`](09-estetica-e-epub.md).

Cada problema fecha com um cartão de classificação:

```
Difficulty:  4/5
Time:        10 min
Brain:       Logic
Frustration: 😈😈😈
"Aha!":      ★★★★★
```

## O que este projecto não é

- Não é um app. Não há estado, pontuação persistente, ou sincronização.
- Não é um curso. Não há progressão obrigatória nem pré-requisitos.
- Não é uma antologia de clássicos. Clássicos entram (Monty Hall, aniversários), mas
  identificados como tal, e nunca são a maioria.
