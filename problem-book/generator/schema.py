"""Esquema de um problema e as regras de integridade do doc 06."""
import re

CATEGORIES = ["logic", "riddles", "math", "probability",
              "lateral", "dilemmas", "what_would_you", "programming"]

PREFIX = {"logic": "LOG", "riddles": "ENI", "math": "MAT", "probability": "PRB",
          "lateral": "LAT", "dilemmas": "DIL", "what_would_you": "WWY",
          "programming": "PRG"}

FILE = {"logic": "logic.json", "riddles": "riddles.json", "math": "math.json",
        "probability": "probability.json", "lateral": "lateral.json",
        "dilemmas": "dilemmas.json", "what_would_you": "what_would_you.json",
        "programming": "programming.json"}

SYMBOL = {"logic": "🧠", "riddles": "🕵️", "math": "🔢", "probability": "🎲",
          "lateral": "🌀", "dilemmas": "⚖️", "what_would_you": "🤔",
          "programming": "💻"}

NAME = {"logic": "Lógica", "riddles": "Enigmas", "math": "Matemática",
        "probability": "Probabilidade", "lateral": "Pensamento lateral",
        "dilemmas": "Dilemas", "what_would_you": "O que farias?",
        "programming": "Programação"}

BRAIN = {"logic": "Lógica", "riddles": "Enigma", "math": "Matemática",
         "probability": "Probabilidade", "lateral": "Lateral",
         "dilemmas": "Ética", "what_would_you": "Estratégia",
         "programming": "Programação"}

TIME_FOR = {1: "<2", 2: "2-5", 3: "5-10", 4: "10-20", 5: "20+"}
TIME_LABEL = {"<2": "MENOS DE 2 MIN", "2-5": "2–5 MIN", "5-10": "5–10 MIN",
              "10-20": "10–20 MIN", "20+": "20+ MIN"}
LEVEL_NAME = {1: "Aquecimento", 2: "Fácil", 3: "Médio", 4: "Difícil", 5: "Monstro"}

NO_ANSWER = {"dilemmas", "what_would_you"}
STATES = ["GENERATED", "SOLVED", "CHECKED", "VERIFIED", "REJECTED", "NEEDS_REVIEW"]

ID_RE = re.compile(r"^[A-Z]{3}-\d{3}$")
# palavras curtas e funcionais que nunca contam como spoiler no título
STOPWORDS = set("""a o as os um uma uns umas de do da dos das em no na nos nas
por para com sem que e ou se ao aos à às é está estão não sim mais menos
esta este isso isto pelo pela nem tem há""".split())


def stars(n: int) -> str:
    return "★" * n + "☆" * (5 - n)


def strip_md(text: str) -> str:
    return re.sub(r"[*`_#>|]", " ", text or "")


def integrity(problems: list[dict]) -> list[str]:
    """As 10 regras do doc 06. Devolve a lista de violações."""
    errors, seen = [], {}

    for p in problems:
        pid = p.get("id", "<sem id>")
        cat = p.get("category")

        # 1. id único
        if pid in seen:
            errors.append(f"{pid}: id duplicado")
        seen[pid] = p

        if not ID_RE.match(pid):
            errors.append(f"{pid}: id malformado")

        # 2. prefixo corresponde à categoria
        if cat not in CATEGORIES:
            errors.append(f"{pid}: categoria desconhecida ({cat})")
            continue
        if not pid.startswith(PREFIX[cat] + "-"):
            errors.append(f"{pid}: prefixo não corresponde a {cat}")

        # 3. estado
        if p.get("verified") not in STATES:
            errors.append(f"{pid}: estado inválido ({p.get('verified')})")

        # 4. has_unique_answer <-> categoria
        unique = p.get("has_unique_answer")
        if unique != (cat not in NO_ANSWER):
            errors.append(f"{pid}: has_unique_answer inconsistente com {cat}")

        # 5. answer existe sse has_unique_answer
        if bool(p.get("answer")) != bool(unique):
            errors.append(f"{pid}: presença de 'answer' inconsistente")

        # 6. o título não revela a resposta.
        #    Só contam as palavras da resposta que NÃO aparecem no enunciado:
        #    vocabulário partilhado com o problema não é spoiler.
        if unique:
            # normaliza plurais: «número» e «números» são a mesma palavra
            def norm(texto):
                out = set()
                for bruto in strip_md(texto).lower().split():
                    w = bruto.strip(".,;:!?()[]«»\u201c\u201d'\"-—–")
                    if not w:
                        continue
                    out.add(w[:-1] if w.endswith("s") and len(w) > 4 else w)
                return out

            title_words = norm(p["title"])
            problem_words = norm(p["problem"])
            answer_words = {w for w in norm(p["answer"])
                            if len(w) > 3 and w not in STOPWORDS}
            leak = (answer_words - problem_words) & title_words
            if leak:
                errors.append(f"{pid}: título revela a resposta ({', '.join(sorted(leak))})")

        # 7. dificuldade e tempo consistentes
        d = p.get("difficulty")
        if d not in TIME_FOR:
            errors.append(f"{pid}: dificuldade fora de 1–5")
        elif TIME_FOR[d] != p.get("estimated_time"):
            errors.append(f"{pid}: tempo {p.get('estimated_time')} inconsistente com ★{d}")

        # 8. dicas distintas e sem a resposta
        if p.get("hint_1") == p.get("hint_2"):
            errors.append(f"{pid}: as duas dicas são iguais")
        if unique:
            ans = strip_md(p["answer"]).lower().strip()
            hints = strip_md(p.get("hint_1", "") + " " + p.get("hint_2", "")).lower()
            if len(ans) > 8 and ans in hints:
                errors.append(f"{pid}: uma dica contém a resposta literal")

        # 9. auto-contenção: o enunciado não cita outro problema
        for other in re.findall(r"[A-Z]{3}-\d{3}", p.get("problem", "")):
            if other != pid:
                errors.append(f"{pid}: o enunciado refere {other}")

        # 10. o código é obrigatório para tudo o que se verifica por execução.
        #     (A categoria programming também admite problemas de algoritmo
        #     sem snippet — esses verificam-se por brute_force, não por execute.)
        method = (p.get("verification") or {}).get("method")
        if method == "execute" and not p.get("code"):
            errors.append(f"{pid}: verificação 'execute' sem campo 'code'")
        if cat == "programming" and not p.get("code") and method == "execute":
            errors.append(f"{pid}: problema de código sem 'code'")

        # extras de forma
        if unique and not p.get("solution"):
            errors.append(f"{pid}: falta 'solution'")
        # o bloco [8] é 'why' em todas as categorias excepto 'o que farias?',
        # onde o seu lugar é ocupado por 'common_mistake' (doc 04)
        if cat == "what_would_you":
            if not p.get("common_mistake"):
                errors.append(f"{pid}: falta 'common_mistake'")
            if not p.get("approaches"):
                errors.append(f"{pid}: falta 'approaches'")
        elif not p.get("why"):
            errors.append(f"{pid}: falta 'why'")
        if cat == "dilemmas" and not (p.get("arguments_for") and p.get("arguments_against")):
            errors.append(f"{pid}: dilema sem argumentos dos dois lados")
        if len(p.get("title", "").split()) > 5:
            errors.append(f"{pid}: título com mais de 5 palavras")

    return errors
