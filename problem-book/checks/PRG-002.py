"""PRG-002 — executa o snippet e compara linha a linha."""
import json
import pathlib
import subprocess
import sys

BASE = pathlib.Path(__file__).resolve().parent.parent
p = next(x for x in json.loads((BASE / "problems/programming.json").read_text(encoding="utf-8"))
         if x["id"] == "PRG-002")

r = subprocess.run([sys.executable, "-c", p["code"]], capture_output=True,
                   text=True, timeout=5)
saida = [l for l in (r.stdout + r.stderr).strip().split("\n")]
esperado = [l for l in p["answer"].strip().strip("`").strip().split("\n") if l.strip()]

print("saída real:", saida)
print("esperado:  ", esperado)
assert saida == esperado, (saida, esperado)
