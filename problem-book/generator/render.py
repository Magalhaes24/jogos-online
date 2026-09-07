"""JSON -> XHTML. Um ficheiro por problema, nove secções por ficheiro."""
import random

from . import mdlite, schema

_MD = mdlite.render
_MAX_COLS = [None]          # definido pelo perfil activo no arranque do build


def md(text):
    return _MD(text, _MAX_COLS[0])

# (emoji, equivalente ascii) — o modo --ascii troca todos de uma vez
SYMS = {
    "think": ("🤔", "[ ? ]"), "stop": ("🛑", "[ STOP ]"), "answer": ("✅", "[ RESP ]"),
    "why": ("🧠", "[ PORQUE ]"), "variation": ("🔄", "[ VAR ]"), "trophy": ("🏆", "[ ! ]"),
    "evil": ("😈", "!!!"), "dice": ("🎲", "[ * ]"), "sun": ("☀️", "[ DIA ]"),
    "book": ("📖", "[ IDX ]"), "scales": ("⚖️", "[ ARG ]"), "hint": ("💡", "[ DICA ]"),
    "clock": ("⏱️", "[ TEMPO ]"), "boom": ("🧨", "[ ARMADILHA ]"),
}
CAT_ASCII = {"logic": "[ LOG ]", "riddles": "[ ENI ]", "math": "[ MAT ]",
             "probability": "[ PRB ]", "lateral": "[ LAT ]", "dilemmas": "[ DIL ]",
             "what_would_you": "[ WWY ]", "programming": "[ PRG ]"}

DOC = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="pt-PT" lang="pt-PT">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<title>%s</title>
<link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
%s
</body>
</html>
"""


class Style:
    """Decide entre emoji e ascii uma única vez, no arranque do build."""

    def __init__(self, ascii_mode: bool = False, profile: str = "default"):
        self.ascii = ascii_mode
        self.profile = profile
        # o X4 tem 4,3" e ~35 caracteres por linha: mais de 3 colunas não cabe
        _MAX_COLS[0] = 3 if profile == "x4" else None

    def s(self, name: str) -> str:
        return SYMS[name][1 if self.ascii else 0]

    def cat(self, category: str) -> str:
        return CAT_ASCII[category] if self.ascii else schema.SYMBOL[category]

    def stars(self, n: int) -> str:
        return ("*" * n + "." * (5 - n)) if self.ascii else schema.stars(n)

    def evil(self, n: int) -> str:
        return ("!" * n) if self.ascii else ("😈" * n)


def doc(title: str, body: str) -> str:
    return DOC % (mdlite.esc(title), body)


def page(inner: str, cls: str = "", anchor: str = "", last: bool = False) -> str:
    classes = "page" + (" " + cls if cls else "") + (" last" if last else "")
    aid = ' id="%s"' % anchor if anchor else ""
    return '<div class="%s"%s>\n%s\n</div>\n' % (classes, aid, inner)


def meta_card(p: dict, st: Style) -> str:
    ident = p["id"]
    if p.get("_seq"):
        # sem táctil, a navegação é por capítulos: o número é o endereço
        ident = "%d · %s" % (p["_seq"], p["id"])
    return (
        '<div class="meta">'
        '<p class="id">%s</p>'
        '<p class="title">%s</p>'
        '<p class="stars">%s</p>'
        '<p class="time">%s</p>'
        '</div>' % (mdlite.esc(ident), mdlite.esc(p["title"]),
                    st.stars(p["difficulty"]),
                    schema.TIME_LABEL[p["estimated_time"]])
    )


def final_card(p: dict, st: Style) -> str:
    rows = [
        ("Difficulty", "%d/5  (%s)" % (p["difficulty"], schema.LEVEL_NAME[p["difficulty"]])),
        ("Time", schema.TIME_LABEL[p["estimated_time"]].lower()),
        ("Brain", schema.BRAIN[p["category"]] + " / " + p["concept"]),
        ("Frustration", st.evil(p.get("frustration", 0)) or "—"),
        ('"Aha!"', st.stars(p.get("aha_factor", 0))),
    ]
    body = "".join('<p class="row">%-12s %s</p>' % (mdlite.esc(k + ":"), v) for k, v in rows)
    return '<div class="card">%s</div>' % body


def barrier(symbol: str, line: str, small: str = "") -> str:
    sm = "<small>%s</small>" % small if small else ""
    return ('<div class="barrier"><span class="symbol">%s</span>%s%s</div>'
            % (symbol, line, sm))


def block(title: str, body_html: str) -> str:
    return '<h2 class="block">%s</h2>%s' % (title, body_html)


# ── Um problema ────────────────────────────────────────────────────────

def problem_pages(p: dict, st: Style) -> str:
    cat = p["category"]
    if cat == "dilemmas":
        return _dilemma(p, st)
    if cat == "what_would_you":
        return _wwy(p, st)
    return _standard(p, st)


def _standard(p: dict, st: Style) -> str:
    out = []

    # [0] aviso, só para os problemas que enganam a intuição
    if p.get("trap"):
        out.append(page(
            '<div class="warn"><span class="symbol">%s</span>'
            'A tua intuição está<br/>provavelmente errada.</div>' % st.s("evil"),
            anchor=p["id"]))
        anchor = ""
    else:
        anchor = p["id"]

    # [1] problema
    out.append(page(meta_card(p, st) + md(p["problem"])
                    + '<p style="text-align:center;margin-top:2.5em">PENSA.</p>',
                    anchor=anchor))
    # [2] pensa primeiro
    out.append(page(barrier(st.s("think"), "PENSA PRIMEIRO",
                            "Não avances.<br/>Tenta encontrar a resposta<br/>antes de continuar.")))
    # [3] [4] dicas
    out.append(page(block("%s Dica 1" % st.s("hint"), md(p["hint_1"]))))
    out.append(page(block("%s Dica 2" % st.s("hint"), md(p["hint_2"]))))
    # [5] STOP
    out.append(page(barrier(st.s("stop"), "STOP",
                            "Se ainda não tentaste resolver<br/>o problema, não avances."
                            "<br/><br/>%s Achas que acertaste?" % st.s("trophy"))))
    # [6] resposta
    out.append(page('<div class="answer"><span class="symbol">%s</span>%s</div>'
                    % (st.s("answer"), md(p["answer"]))))
    # [7] solução
    out.append(page(block("Solução", md(p["solution"]))))
    # [8] porquê
    out.append(page(block("%s Porquê" % st.s("why"), md(p["why"]))))
    # [9] variação + cartão
    tail = ""
    if p.get("variation"):
        tail += block("%s Variação" % st.s("variation"), md(p["variation"]))
    tail += final_card(p, st)
    out.append(page(tail, last=True))
    return "".join(out)


def _dilemma(p: dict, st: Style) -> str:
    out = [page(meta_card(p, st) + md(p["problem"])
                + '<p style="text-align:center;margin-top:2.5em">DECIDE.</p>',
                anchor=p["id"])]
    out.append(page(barrier(st.s("think"), "DECIDE PRIMEIRO",
                            "Decide antes de virar a página.<br/>"
                            "E escreve mentalmente <em>porquê</em> —<br/>"
                            "a razão importa mais do que a escolha.")))
    out.append(page(block("Reflexão 1", md(p["hint_1"]))))
    out.append(page(block("Reflexão 2", md(p["hint_2"]))))
    out.append(page(barrier(st.s("scales"), "NÃO HÁ<br/>RESPOSTA CERTA",
                            "Há argumentos.<br/>Se acabares com a certeza de que só<br/>"
                            "um lado é defensável, não leste o outro.")))
    out.append(page(block("Argumentos a favor",
                          "<ul>%s</ul>" % "".join("<li>%s</li>" % mdlite.inline(a)
                                                  for a in p["arguments_for"]))))
    contra = block("Argumentos contra",
                   "<ul>%s</ul>" % "".join("<li>%s</li>" % mdlite.inline(a)
                                           for a in p["arguments_against"]))
    if p.get("third_option"):
        contra += block("A terceira opção", md(p["third_option"]))
    out.append(page(contra))
    out.append(page(block("%s Agora as variações" % st.s("variation"),
                          "<p>Responde a cada uma antes de ler a seguinte. "
                          "Se alguma te fizer mudar de resposta, essa é a mais interessante.</p>"
                          "<ol>%s</ol>" % "".join("<li>%s</li>" % mdlite.inline(v)
                                                  for v in p["variations"]))))
    out.append(page(block("%s O que está em jogo" % st.s("why"), md(p["why"]))
                    + final_card(p, st), last=True))
    return "".join(out)


def _wwy(p: dict, st: Style) -> str:
    out = [page(meta_card(p, st) + md(p["problem"])
                + '<p style="text-align:center;margin-top:2.5em">PLANEIA.</p>',
                anchor=p["id"])]
    out.append(page(barrier(st.s("think"), "PLANEIA PRIMEIRO",
                            "Escreve o teu plano antes de avançar.<br/>"
                            "Uma resposta pensada vale dez lidas.")))
    out.append(page(block("Antes de continuares", md(p["hint_1"]))))
    out.append(page(block("Mais uma coisa", md(p["hint_2"]))))
    out.append(page(barrier(st.s("think"), "UMA ABORDAGEM<br/>POSSÍVEL",
                            "Não é a única.<br/>É a que resiste a ser posta em prática.")))
    body = md(p.get("framing", ""))
    for a in p["approaches"]:
        body += '<h2 class="block">%s</h2>%s' % (mdlite.esc(a["name"]), md(a["body"]))
    out.append(page(body))
    out.append(page(block("O erro mais comum", md(p["common_mistake"]))))
    tail = ""
    if p.get("variation"):
        tail += block("%s Restrição adicional" % st.s("variation"), md(p["variation"]))
    tail += final_card(p, st)
    out.append(page(tail, last=True))
    return "".join(out)


def divider(cat: str, count: int, st: Style) -> str:
    return page('<div class="divider"><span class="symbol">%s</span>'
                '<h1>%s</h1><p class="count">%d PROBLEMAS</p></div>'
                % (st.cat(cat), mdlite.esc(schema.NAME[cat]), count),
                anchor="cat-" + cat, last=True)


# ── Navegação ──────────────────────────────────────────────────────────

def cover(total: int, st: Style) -> str:
    return page('<div class="cover">'
                '<h1>The Pocket<br/>Problem Book</h1>'
                '<div class="rule"></div>'
                '<p class="sub">%d problems for when<br/>you have nothing to do.</p>'
                '<p class="vol">VOLUME I</p></div>' % total, last=True)


def how_to(st: Style) -> str:
    body = md("""Este livro não se lê do princípio ao fim.

Abre-o quando tiveres cinco a trinta minutos e não souberes o que fazer com eles.

**Cada problema tem sempre a mesma forma.** Do enunciado até à resposta há cinco páginas: pensa primeiro, duas dicas, e uma barreira. Isso é deliberado — nunca vais tropeçar na solução sem querer.

**As estrelas são tempo, não julgamento.** Uma estrela resolve-se de cabeça; cinco precisam de papel e de método.

**Duas secções não têm resposta certa** — Dilemas e O que farias? — e dizem-no na página. Aí o objectivo não é acertar, é perceber porque escolheste o que escolheste.

**Modo aleatório:** abre numa página ao calhar e avança até encontrares um cabeçalho. Nenhum problema ocupa mais de dez páginas, portanto cais sempre perto de um.""")
    return page('<h2 class="block">Como usar este livro</h2>' + body, last=True)


def guide_x4(problems: list[dict], st: Style) -> str:
    body = md("""Este livro foi montado para um leitor **sem ecrã táctil**. Não há nada para tocar, e os links não servem de nada aqui.

A navegação é toda feita com os botões.

**Cada problema é um capítulo.** Salta de problema para problema com o salto de capítulo do teu leitor — no X4, é o menu do botão **Confirm** (Capítulo: anterior / actual / seguinte).

**Cada problema tem um número**, impresso no cabeçalho, a seguir ao código:

```
   34 · LOG-012
   Os apertos de mão
   ***..
   10-20 MIN
```

O **34** é o número do capítulo. É esse o endereço que os índices no fim do livro usam.

**Para escolher pelo tempo que tens**, vai ao índice por dificuldade, no fim. Ele diz-te os números dos capítulos de cada nível.

**Para abrir ao acaso**, carrega no salto de capítulo umas quantas vezes sem olhar. Nenhum problema ocupa mais de dez páginas, e todos começam com um cabeçalho igual — nunca cais no meio de uma solução sem perceber.

**Entre o enunciado e a resposta há sempre cinco páginas:** pensa primeiro, duas dicas e uma barreira. Carregas em Página Seguinte quando quiseres — mas cada carregada é uma decisão tua.""")
    return page('<h2 class="block">Como usar este livro</h2>' + body, last=True)


def daily_x4(problems: list[dict], st: Style) -> str:
    linhas = "".join(
        "<tr><td>%03d</td><td>cap. %d</td><td>%s</td></tr>"
        % (i + 1, p["_seq"], st.stars(p["difficulty"]))
        for i, p in enumerate(problems))
    intro = md("""Este livro não sabe que dia é hoje. Tu sabes.

Procura o número do dia do ano — 1 de Janeiro é 1 — e vai ao capítulo indicado. Quando passares do fim da tabela, recomeça.

A tabela não mostra títulos, de propósito: aqui não escolhes, aceitas o que sair.""")
    return page('<h2 class="block">%s Desafio do dia</h2>%s'
                '<table><thead><tr><th>Dia</th><th>Vai a</th><th>Nível</th></tr></thead>'
                '<tbody>%s</tbody></table>' % (st.s("sun"), intro, linhas), last=True)


def menu(files: list[tuple[str, str]], st: Style) -> str:
    """files: lista de (rótulo, ficheiro) já agrupada pelas duas famílias."""
    tempo, quero = files[:3], files[3:]

    def group(label, items):
        lis = "".join('<li><a href="%s">%s</a></li>' % (f, mdlite.esc(t)) for t, f in items)
        return '<div class="group"><p class="label">%s</p><ul>%s</ul></div>' % (label, lis)

    extra = ('<div class="group"><p class="label">Ou então</p><ul>'
             '<li><a href="daily.xhtml">%s Desafio do dia</a></li>'
             '<li><a href="idx-id.xhtml">%s Índice completo</a></li>'
             '</ul></div>' % (st.s("sun"), st.s("book")))
    return page('<div class="nav"><h1>%s Escolhe o teu desafio</h1>%s%s%s</div>'
                % (st.s("dice"), group("Tenho…", tempo), group("Quero…", quero), extra),
                last=True)


def jump_list(title: str, subtitle: str, problems: list[dict], st: Style) -> str:
    if not problems:
        items = "<p>Ainda não há problemas nesta lista neste volume.</p>"
    else:
        items = '<ul class="jump">' + "".join(
            '<li><span class="sid">%s</span> · <a href="%s">%s</a> '
            '<span class="st">%s</span></li>'
            % (mdlite.esc(_addr(p)), pfile(p), mdlite.esc(p["title"]),
               st.stars(p["difficulty"]))
            for p in problems) + "</ul>"
    sub = "<p>%s</p>" % mdlite.esc(subtitle) if subtitle else ""
    return page('<h2 class="block">%s</h2>%s%s'
                '%s' % (title, sub, items, voltar(st)), last=True)


def daily(problems: list[dict], st: Style) -> str:
    rows = "".join(
        "<tr><td>%03d</td><td>%s</td><td>%s</td><td><a href=\"%s\">abrir</a></td></tr>"
        % (i + 1, st.stars(p["difficulty"]),
           schema.TIME_LABEL[p["estimated_time"]].lower(), pfile(p))
        for i, p in enumerate(problems))
    intro = md("""Este livro não sabe que dia é hoje. Tu sabes.

Vai ao desafio com o número do dia do ano — 1 de Janeiro é 1, 31 de Dezembro é 365 — e quando passares do fim da tabela, recomeça.

A tabela não mostra títulos, de propósito: aqui não escolhes, aceitas o que sair.""")
    return page('<h2 class="block">%s Desafio do dia</h2>%s'
                '<table><thead><tr><th>N.º</th><th>Dificuldade</th><th>Tempo</th><th></th></tr>'
                '</thead><tbody>%s</tbody></table>'
                '<p style="margin-top:2em"><a href="menu.xhtml">Voltar ao menu</a></p>'
                % (st.s("sun"), intro, rows), last=True)


def index_home(st: Style) -> str:
    body = md("""Três maneiras de encontrar um problema.

O terceiro é o mais útil dos três: procura a **técnica** de que precisas, não o problema de que te lembras.""")
    links = ('<ul class="jump">'
             '<li><a href="idx-id.xhtml">Por número</a></li>'
             '<li><a href="idx-difficulty.xhtml">Por dificuldade</a></li>'
             '<li><a href="idx-concept.xhtml">Por conceito</a></li>'
             '</ul>')
    return page('<h2 class="block">%s Índices</h2>%s%s%s'
                % (st.s("book"), body, links, voltar(st)), last=True)


def index_by_id(problems: list[dict], st: Style) -> str:
    body = ""
    for cat, group in _grouped(problems).items():
        body += '<h2 class="block">%s %s</h2><ul class="jump">' % (
            st.cat(cat), mdlite.esc(schema.NAME[cat]))
        body += "".join('<li><span class="sid">%s</span> · <a href="%s">%s</a> '
                        '<span class="st">%s</span></li>'
                        % (_addr(p), pfile(p), mdlite.esc(p["title"]),
                           st.stars(p["difficulty"]))
                        for p in group)
        body += "</ul>"
    return page('<h2 class="block">%s Índice por número</h2>%s'
                '%s' % (st.s("book"), body, voltar(st)), last=True)


def index_by_difficulty(problems: list[dict], st: Style) -> str:
    body = ""
    for d in range(1, 6):
        group = [p for p in problems if p["difficulty"] == d]
        if not group:
            continue
        body += '<h2 class="block">%s %s · %s</h2><ul class="jump">' % (
            st.stars(d), mdlite.esc(schema.LEVEL_NAME[d]),
            schema.TIME_LABEL[schema.TIME_FOR[d]].lower())
        body += "".join('<li><span class="sid">%s</span> · <a href="%s">%s</a></li>'
                        % (_addr(p), pfile(p), mdlite.esc(p["title"])) for p in group)
        body += "</ul>"
    return page('<h2 class="block">Índice por dificuldade</h2>%s'
                '%s' % (body, voltar(st)), last=True)


def index_by_concept(problems: list[dict], st: Style) -> str:
    concepts: dict[str, list[dict]] = {}
    for p in problems:
        concepts.setdefault(p["concept"], []).append(p)
    rows = ""
    for concept in sorted(concepts, key=str.lower):
        links = ", ".join('<a href="%s">%s</a>' % (pfile(p), _addr(p))
                          for p in concepts[concept])
        rows += "<tr><td>%s</td><td>%s</td></tr>" % (mdlite.esc(concept), links)
    intro = md("O índice mais útil do livro: procura a **técnica**, não o problema.")
    return page('<h2 class="block">Índice por conceito</h2>%s'
                '<table><thead><tr><th>Conceito</th><th>Problemas</th></tr></thead>'
                '<tbody>%s</tbody></table>'
                '%s' % (intro, rows, voltar(st)), last=True)


# ── Auxiliares ─────────────────────────────────────────────────────────

def voltar(st: Style) -> str:
    """No X4 não há menu nem links clicáveis: o rodapé desaparece."""
    if st.profile == "x4":
        return ""
    return '<p style="margin-top:2em"><a href="menu.xhtml">Voltar ao menu</a></p>'


def _addr(p: dict) -> str:
    """Endereço do problema: número de capítulo quando existe, senão o id."""
    return "cap. %d · %s" % (p["_seq"], p["id"]) if p.get("_seq") else p["id"]


def pfile(p: dict) -> str:
    return "p-%s.xhtml" % p["id"]


def _grouped(problems: list[dict]) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    for p in problems:
        out.setdefault(p["category"], []).append(p)
    return out


def shuffled(problems: list[dict], seed: int = 20260907) -> list[dict]:
    """Baralhado, mas fixo: o mesmo build dá sempre a mesma ordem."""
    out = list(problems)
    random.Random(seed).shuffle(out)
    return out
