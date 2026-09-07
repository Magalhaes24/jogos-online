"""Carregamento e consulta do banco de problemas."""
import json
import pathlib

from . import schema

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROBLEMS_DIR = ROOT / "problems"
ORDER = schema.CATEGORIES


def load(only_verified: bool = True) -> list[dict]:
    """Devolve todos os problemas, por ordem de categoria e depois de id."""
    out = []
    for cat in ORDER:
        path = PROBLEMS_DIR / schema.FILE[cat]
        if not path.exists():
            continue
        items = json.loads(path.read_text(encoding="utf-8"))
        for p in items:
            if only_verified and p.get("verified") != "VERIFIED":
                continue
            out.append(p)
    out.sort(key=lambda p: (ORDER.index(p["category"]), p["id"]))
    return out


def by_category(problems: list[dict]) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = {c: [] for c in ORDER}
    for p in problems:
        groups[p["category"]].append(p)
    return {c: v for c, v in groups.items() if v}
