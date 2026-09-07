"""ppb — a linha de comandos do livro."""
import argparse
import sys

from . import build as build_mod
from . import db, render, schema, verify


def cmd_check(_args) -> int:
    problems = db.load(only_verified=False)
    errors = schema.integrity(problems)
    print("%d problemas na base de dados" % len(problems))
    if errors:
        print("%d violações de integridade:" % len(errors))
        for e in errors:
            print("  -", e)
        return 1
    print("Integridade: OK (10 regras, doc 06)")
    return 0


def cmd_build(args) -> int:
    path = build_mod.build(ascii_mode=args.ascii)
    size = path.stat().st_size
    print("%s  (%.1f KB)" % (path, size / 1024))
    return 0


def cmd_report(_args) -> int:
    problems = db.load(only_verified=False)
    st = render.Style(False)
    print("BANCO DE PROBLEMAS\n")
    header = "%-22s %8s %6s %7s" % ("Categoria", "VERIFIED", "outros", "alvo")
    print(header)
    print("-" * len(header))
    target = {"logic": 35, "riddles": 30, "math": 30, "probability": 25,
              "lateral": 25, "dilemmas": 20, "what_would_you": 20, "programming": 15}
    tv = to = tt = 0
    for cat in schema.CATEGORIES:
        group = [p for p in problems if p["category"] == cat]
        v = sum(1 for p in group if p["verified"] == "VERIFIED")
        o = len(group) - v
        tv, to, tt = tv + v, to + o, tt + target[cat]
        print("%-22s %8d %6d %7d" % (schema.SYMBOL[cat] + " " + schema.NAME[cat], v, o, target[cat]))
    print("-" * len(header))
    print("%-22s %8d %6d %7d" % ("TOTAL", tv, to, tt))
    print("\nProntos para o Volume I: %d/%d (%.0f%%)" % (tv, tt, 100 * tv / tt))

    verified = [p for p in problems if p["verified"] == "VERIFIED"]
    dist = " · ".join("%s %d" % (st.stars(d), sum(1 for p in verified if p["difficulty"] == d))
                      for d in range(1, 6))
    print("Dificuldade (VERIFIED): " + dist)
    if verified:
        print("Média: ★%.1f" % (sum(p["difficulty"] for p in verified) / len(verified)))
    traps = [p["id"] for p in verified if p.get("trap")]
    print("Armadilhas (trap): %d — %s" % (len(traps), ", ".join(traps)))
    concepts = sorted({p["concept"] for p in verified}, key=str.lower)
    print("Conceitos cobertos: %d" % len(concepts))
    methods: dict[str, int] = {}
    for p in verified:
        m = (p.get("verification") or {}).get("method", "?")
        methods[m] = methods.get(m, 0) + 1
    print("Verificação: " + " · ".join("%s %d" % kv for kv in sorted(methods.items())))
    manual = sum(v for k, v in methods.items() if k in ("manual", "n/a"))
    print("Sem prova automática: %d/%d (%.0f%%)" % (manual, len(verified),
                                                    100 * manual / len(verified)))
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="ppb", description="The Pocket Problem Book")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("check", help="regras de integridade").set_defaults(fn=cmd_check)
    b = sub.add_parser("build", help="gerar o EPUB")
    b.add_argument("--ascii", action="store_true",
                   help="substituir emoji por equivalentes de texto")
    b.set_defaults(fn=cmd_build)
    v = sub.add_parser("verify", help="correr os scripts de verificação")
    v.add_argument("--id", default=None, help="verificar só um problema")
    v.set_defaults(fn=lambda a: verify.run_all(a.id))
    sub.add_parser("report", help="estado do banco").set_defaults(fn=cmd_report)

    args = parser.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
