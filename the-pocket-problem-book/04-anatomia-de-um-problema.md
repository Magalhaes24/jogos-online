# 04 — Anatomia de um problema

Todos os problemas seguem **exactamente** a mesma sequência de páginas. A previsibilidade
é a funcionalidade: o leitor sabe sempre quantos *next page* faltam até à resposta.

```
    [1] PROBLEMA
         ↓
    [2] PENSA PRIMEIRO   ← barreira
         ↓
    [3] DICA 1
         ↓
    [4] DICA 2
         ↓
    [5] STOP 🛑          ← barreira
         ↓
    [6] RESPOSTA
         ↓
    [7] SOLUÇÃO
         ↓
    [8] PORQUÊ
         ↓
    [9] VARIAÇÃO         ← opcional
```

Cada bloco é uma página física no EPUB (`page-break-after: always`).

---

## [1] Problema

```
────────────────────
     LOG-034
   AS TRÊS CAIXAS
     ★★★☆☆
     5–10 MIN
────────────────────

Há três caixas: A, B e C.
Apenas uma contém ouro.

Cada caixa tem uma etiqueta...

────────────────────
        PENSA.
```

O cartão de metadados vem primeiro. O enunciado é auto-contido: nada de "recorda o
problema anterior".

---

## [2] Pensa primeiro

Página deliberadamente quase vazia. Existe para separar fisicamente o enunciado
da primeira dica.

```
        🤔

    PENSA PRIMEIRO

    Não avances.

    Tenta encontrar a resposta
    antes de continuar.
```

---

## [3] Dica 1 — o empurrão

Uma dica que **reorienta**, não que resolve. Aponta para onde olhar.

> Considera primeiro o que aconteceria se a etiqueta de A fosse verdadeira.

**Teste:** depois da dica 1, o problema desce um nível de dificuldade. Não dois.

---

## [4] Dica 2 — a chave

A dica 2 dá o mecanismo. Depois dela, o problema é trabalho e não descoberta.

> Só uma das etiquetas é verdadeira. Testa as três hipóteses e conta quantas
> etiquetas ficam verdadeiras em cada caso.

**Teste:** depois da dica 2, alguém que percebeu o enunciado *consegue* terminar.

---

## [5] STOP

A barreira psicológica. Página inteira, texto grande, quase nada.

```
        🛑

        STOP

    Se ainda não tentaste
    resolver o problema,
    não avances.
```

Também é aqui que o livro pergunta:

```
    🏆 Antes de virares:
       achas que acertaste?
```

Isto prepara o auto-scoring (ver mais abaixo) e aumenta o custo emocional de desistir —
que é exactamente o objectivo.

---

## [6] Resposta

**Só a resposta. Uma linha.**

```
        ✅ RESPOSTA

        O ouro está em B.
```

Existe separada da solução porque muita gente só quer confirmar. Obrigar essa pessoa
a atravessar três parágrafos de explicação é mau design.

---

## [7] Solução

O raciocínio completo, passo a passo. Formato preferido: tabela ou lista numerada,
não prosa contínua — lê-se melhor em e-ink.

---

## [8] Porquê

O princípio transferível, em 3 a 5 linhas.

> **Princípio:** quando um conjunto de afirmações tem um número fixo de verdadeiras,
> não tentes deduzir a partir das afirmações — testa cada mundo possível e conta.
> Enumerar é quase sempre mais rápido do que raciocinar.

Este é o bloco que transforma o livro de entretenimento em treino.

---

## [9] Variação (opcional)

Transforma um problema em vários, sem custo de produção.

> **🔄 E se...** duas etiquetas pudessem ser verdadeiras? Quantas respostas existem então?

A variação **não** tem solução impressa. É deliberado: fica como problema em aberto.
Se a variação for boa o suficiente para merecer solução, torna-se um problema próprio
com ID próprio.

---

## Auto-avaliação

Depois da solução, opcionalmente:

```
    🏆 RESULTADO

    5/5  Génio — sem ajuda
    4/5  Excelente — uma dica
    3/5  Bom — duas dicas
    2/5  Quase — percebeste a ideia
    1/5  O problema ganhou.
```

Não há registo, não há total. É um espelho, não um sistema de pontos.

---

## Blocos alternativos para DIL e WWY

Quando `has_unique_answer` é `false`, os blocos [6]–[8] são substituídos:

| Padrão | `DIL` | `WWY` |
|---|---|---|
| [6] | ⚖️ **NÃO HÁ RESPOSTA CERTA** | 🤔 **UMA ABORDAGEM POSSÍVEL** |
| [7] | Argumentos a favor / contra | 2–4 estratégias distintas |
| [8] | O princípio ético em jogo | O erro mais comum |
| [9] | A variação que inverte a intuição | Restrição adicional |

O gerador **recusa-se** a emitir "✅ RESPOSTA" para estas categorias. É uma regra
de compilação, não uma convenção.
