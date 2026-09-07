"""Mini-markdown -> XHTML.

Suporta apenas o subconjunto usado pelos problemas: parágrafos, listas
ordenadas e não ordenadas, tabelas, blocos de código com cerca, e os
estilos inline **negrito**, *itálico* e `código`.

Deliberadamente sem dependências: o livro tem de compilar em qualquer
máquina com Python 3.9+ e mais nada instalado.
"""
import re

_CODE_SPAN = re.compile(r"`([^`]+)`")
_BOLD = re.compile(r"\*\*(.+?)\*\*", re.S)
_ITALIC = re.compile(r"(?<!\*)\*(?!\s)([^*]+?)(?<!\s)\*(?!\*)")


def esc(text: str) -> str:
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;"))


def inline(text: str) -> str:
    """Escapa e aplica estilos inline, protegendo o que está em `crases`."""
    out, last = [], 0
    for m in _CODE_SPAN.finditer(text):
        out.append(_styles(esc(text[last:m.start()])))
        out.append("<code>%s</code>" % esc(m.group(1)))
        last = m.end()
    out.append(_styles(esc(text[last:])))
    return "".join(out)


def _styles(chunk: str) -> str:
    chunk = _BOLD.sub(r"<strong>\1</strong>", chunk)
    chunk = _ITALIC.sub(r"<em>\1</em>", chunk)
    return chunk


def _stacked(head: list[str], body: list[list[str]]) -> str:
    """Tabela larga -> lista empilhada, para ecrãs estreitos."""
    itens = []
    for row in body:
        rotulo = inline(row[0]) if row else ""
        resto = " · ".join("%s: %s" % (inline(h), inline(c))
                           for h, c in zip(head[1:], row[1:]) if c.strip())
        itens.append("<li><strong>%s</strong><br/>%s</li>" % (rotulo, resto))
    return '<ul class="stacked">%s</ul>' % "".join(itens)


def _table(lines: list[str], max_cols: int | None = None) -> str:
    def cells(row: str) -> list[str]:
        row = row.strip()
        if row.startswith("|"):
            row = row[1:]
        if row.endswith("|"):
            row = row[:-1]
        return [c.strip() for c in row.split("|")]

    head, body = cells(lines[0]), [cells(r) for r in lines[2:]]
    if max_cols is not None and len(head) > max_cols:
        return _stacked(head, body)
    out = ['<table>', '<thead><tr>']
    out += ["<th>%s</th>" % inline(c) for c in head]
    out += ['</tr></thead>', '<tbody>']
    for row in body:
        out.append("<tr>" + "".join("<td>%s</td>" % inline(c) for c in row) + "</tr>")
    out += ['</tbody>', '</table>']
    return "".join(out)


def render(text: str | None, max_cols: int | None = None) -> str:
    """Converte um bloco de markdown-lite em XHTML.

    `max_cols` limita a largura das tabelas: acima desse número de colunas,
    a tabela é reescrita como lista empilhada (ecrãs estreitos)."""
    if not text:
        return ""
    lines = text.replace("\r\n", "\n").split("\n")
    html, i = [], 0

    while i < len(lines):
        line = lines[i]

        # bloco de código com cerca
        if line.lstrip().startswith("```"):
            i += 1
            buf = []
            while i < len(lines) and not lines[i].lstrip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            html.append("<pre><code>%s</code></pre>" % esc("\n".join(buf)))
            continue

        # tabela: cabeçalho + linha separadora
        if (line.strip().startswith("|") and i + 1 < len(lines)
                and set(lines[i + 1].strip()) <= set("|-: ")
                and "-" in lines[i + 1]):
            buf = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                buf.append(lines[i])
                i += 1
            html.append(_table(buf, max_cols))
            continue

        # lista não ordenada
        if re.match(r"^\s*[-*]\s+", line):
            items = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                items.append(re.sub(r"^\s*[-*]\s+", "", lines[i]))
                i += 1
            html.append("<ul>%s</ul>" % "".join("<li>%s</li>" % inline(x) for x in items))
            continue

        # lista ordenada
        if re.match(r"^\s*\d+\.\s+", line):
            items = []
            while i < len(lines) and re.match(r"^\s*\d+\.\s+", lines[i]):
                items.append(re.sub(r"^\s*\d+\.\s+", "", lines[i]))
                i += 1
            html.append("<ol>%s</ol>" % "".join("<li>%s</li>" % inline(x) for x in items))
            continue

        # linha em branco
        if not line.strip():
            i += 1
            continue

        # parágrafo: junta até à próxima linha em branco ou início de outro bloco
        buf = []
        while i < len(lines) and lines[i].strip():
            nxt = lines[i]
            if (nxt.lstrip().startswith("```") or nxt.strip().startswith("|")
                    or re.match(r"^\s*[-*]\s+", nxt) or re.match(r"^\s*\d+\.\s+", nxt)):
                break
            buf.append(nxt.strip())
            i += 1
        if buf:
            html.append("<p>%s</p>" % inline(" ".join(buf)))

    return "".join(html)
