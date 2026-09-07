"""Corre os scripts de checks/ e confronta-os com o que o JSON declara."""
import pathlib
import subprocess
import sys

from . import db

ROOT = pathlib.Path(__file__).resolve().parent.parent
AUTO = {"exhaustive", "monte_carlo", "brute_force", "execute", "exact", "symbolic"}


def run_all(only: str | None = None) -> int:
    problems = [p for p in db.load(only_verified=False) if not only or p["id"] == only]
    falhas = 0
    for p in problems:
        v = p.get("verification") or {}
        method, script = v.get("method"), v.get("script")

        if method not in AUTO:
            print("  ~  %s  %-12s sem prova automática (revisão humana)" % (p["id"], method))
            continue
        if not script:
            print("  !  %s  método %s sem script declarado" % (p["id"], method))
            falhas += 1
            continue

        path = ROOT / script
        if not path.exists():
            print("  !  %s  script em falta: %s" % (p["id"], script))
            falhas += 1
            continue

        r = subprocess.run([sys.executable, str(path)], capture_output=True,
                           text=True, timeout=300)
        if r.returncode == 0:
            print("  OK %s  %-12s %s" % (p["id"], method, r.stdout.strip().split("\n")[-1]))
        else:
            print("  !  %s  %-12s FALHOU" % (p["id"], method))
            print("     " + r.stderr.strip().replace("\n", "\n     "))
            falhas += 1
    print("\n%d problemas · %d falhas" % (len(problems), falhas))
    return 1 if falhas else 0
