"""Orquestra o build: base de dados -> EPUB."""
import pathlib

from . import db, epub, render, schema

ROOT = pathlib.Path(__file__).resolve().parent.parent
CSS = ROOT / "templates" / "style.css"
OUTPUT = ROOT / "output"

TITLE = "The Pocket Problem Book"
CREATOR = "The Pocket Problem Book"
DESC = ("Problemas de lógica, matemática, probabilidade, pensamento lateral e "
        "programação para quando tens cinco a trinta minutos e nada para fazer. "
        "Cada problema traz duas dicas, a resposta separada da explicação, e o "
        "princípio que fica para o problema seguinte.")


def jump_lists(problems: list[dict], st: render.Style):
    """(rótulo do menu, ficheiro, título da página, subtítulo, selecção)."""
    def cat(*names):
        return [p for p in problems if p["category"] in names]

    return [
        ("%s 5 minutos" % st.s("clock"), "jump-5min.xhtml", "Tenho 5 minutos",
         "Aquecimento e fácil. Resolvem-se de cabeça ou quase.",
         [p for p in problems if p["difficulty"] <= 2]),
        ("%s 10 minutos" % st.s("clock"), "jump-10min.xhtml", "Tenho 10 minutos",
         "O miolo do livro.",
         [p for p in problems if p["difficulty"] in (2, 3)]),
        ("%s 30 minutos" % st.s("clock"), "jump-30min.xhtml", "Tenho 30 minutos",
         "Precisam de papel, ou de largar um pressuposto.",
         [p for p in problems if p["difficulty"] >= 4]),
        ("%s Pensar" % st.cat("logic"), "jump-pensar.xhtml", "Quero pensar",
         "Dedução pura. Tens toda a informação de que precisas.", cat("logic")),
        ("%s Fazer contas" % st.cat("math"), "jump-contas.xhtml", "Quero fazer contas",
         "Nada aqui precisa de calculadora.", cat("math", "probability")),
        ("%s Resolver um mistério" % st.cat("riddles"), "jump-misterio.xhtml",
         "Quero resolver um mistério", "Rápidos. Um a cinco minutos.", cat("riddles")),
        ("%s Algo estranho" % st.cat("lateral"), "jump-estranho.xhtml",
         "Quero algo estranho",
         "A solução é sempre óbvia — depois de a ouvires.", cat("lateral")),
        ("%s Programar" % st.cat("programming"), "jump-programar.xhtml",
         "Quero programar", "Sem computador. Só a cabeça.", cat("programming")),
        ("%s Ser enganado" % st.s("evil"), "jump-enganado.xhtml", "Quero ser enganado",
         "Feitos para a intuição falhar. E ela falha.",
         [p for p in problems if p.get("trap")]),
        ("%s Decidir alguma coisa" % st.cat("dilemmas"), "jump-decidir.xhtml",
         "Quero decidir alguma coisa",
         "Sem resposta certa. Só argumentos e consequências.",
         cat("dilemmas", "what_would_you")),
    ]


def build(ascii_mode: bool = False, out: pathlib.Path | None = None,
          profile: str = "default") -> pathlib.Path:
    problems = db.load(only_verified=True)
    errors = schema.integrity(problems)
    if errors:
        raise SystemExit("Integridade falhou:\n  " + "\n  ".join(errors))

    # o X4 não tem táctil: os links não são clicáveis e os emoji são um risco
    if profile == "x4":
        ascii_mode = True

    st = render.Style(ascii_mode, profile)
    # número de capítulo: no X4 é o endereço de cada problema
    for i, prob in enumerate(problems, 1):
        prob["_seq"] = i if profile == "x4" else None
    sufixo = {"x4": " (X4)", "default": " (ascii)" if ascii_mode else ""}[profile]
    book = epub.Book(TITLE + sufixo, CREATOR, DESC)

    # A ordem do spine e a ordem do índice têm de coincidir (EPUB NAV-011).
    book.add("cover.xhtml", render.doc(TITLE, render.cover(len(problems), st)))
    if profile == "x4":
        book.add("how-to.xhtml", render.doc("Como usar este livro",
                                            render.guide_x4(problems, st)))
        book.toc_entry("Como usar este livro", "how-to.xhtml")
        book.add("daily.xhtml", render.doc("Desafio do dia",
                                           render.daily_x4(render.shuffled(problems, 4321), st)))
        book.toc_entry("%s Desafio do dia" % st.s("sun"), "daily.xhtml")
    else:
        lists = jump_lists(problems, st)
        book.add("menu.xhtml", render.doc("Escolhe o teu desafio",
                                          render.menu([(lbl, f) for lbl, f, *_ in lists], st)))
        book.add("how-to.xhtml", render.doc("Como usar este livro", render.how_to(st)))
        book.toc_entry("%s Escolhe o teu desafio" % st.s("dice"), "menu.xhtml")
        book.toc_entry("Como usar este livro", "how-to.xhtml")
        for _, fname, page_title, subtitle, selection in lists:
            book.add(fname, render.doc(page_title,
                                       render.jump_list(page_title, subtitle,
                                                        render.shuffled(selection), st)))
        book.add("daily.xhtml", render.doc("Desafio do dia",
                                           render.daily(render.shuffled(problems, 4321), st)))
        book.toc_entry("%s Desafio do dia" % st.s("sun"), "daily.xhtml")

    # corpo: divisória de categoria + um ficheiro por problema
    for cat, group in db.by_category(problems).items():
        dfile = "cat-%s.xhtml" % cat
        book.add(dfile, render.doc(schema.NAME[cat], render.divider(cat, len(group), st)))
        children = []
        for p in group:
            fname = render.pfile(p)
            book.add(fname, render.doc("%s · %s" % (p["id"], p["title"]),
                                       render.problem_pages(p, st)))
            children.append({"label": "%s · %s" % (p["id"], p["title"]),
                             "href": fname, "children": []})
        if profile == "x4":
            # índice plano: o salto de capítulo do X4 percorre a lista em linha
            book.toc_entry("%s %s" % (st.cat(cat), schema.NAME[cat]), dfile)
            for c in children:
                book.toc_entry(c["label"], c["href"])
        else:
            book.toc_entry("%s %s" % (st.cat(cat), schema.NAME[cat]), dfile, children)

    book.add("idx.xhtml", render.doc("Índices", render.index_home(st)))
    book.add("idx-id.xhtml", render.doc("Índice por número",
                                        render.index_by_id(problems, st)))
    book.add("idx-difficulty.xhtml", render.doc("Índice por dificuldade",
                                                render.index_by_difficulty(problems, st)))
    book.add("idx-concept.xhtml", render.doc("Índice por conceito",
                                             render.index_by_concept(problems, st)))
    book.toc_entry("%s Índices" % st.s("book"), "idx.xhtml", [
        {"label": "Por número", "href": "idx-id.xhtml", "children": []},
        {"label": "Por dificuldade", "href": "idx-difficulty.xhtml", "children": []},
        {"label": "Por conceito", "href": "idx-concept.xhtml", "children": []},
    ])

    nome = {"x4": "pocket-problems-vol1-x4.epub",
            "default": "pocket-problems-vol1%s.epub" % ("-ascii" if ascii_mode else "")}[profile]
    css = (ROOT / "templates" / ("style-x4.css" if profile == "x4" else "style.css"))
    path = out or (OUTPUT / nome)
    caminho = book.write(path, css.read_text(encoding="utf-8"))

    if profile == "x4":
        # o X4 salta no máximo 100 capítulos
        n = len(book.spine)
        assert n <= 100, "%d capítulos: o X4 só salta até 100" % n
    return caminho
