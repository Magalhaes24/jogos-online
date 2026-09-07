# 07 — Pipeline de validação

## O problema que isto resolve

Gerar puzzles com IA falha quase sempre da mesma maneira:

> **O enunciado parece correcto. A solução está errada.**

Ou pior, e mais frequente em problemas de lógica:

> **O enunciado admite três respostas, e o autor só encontrou uma.**

Um livro com 200 problemas e 15 soluções erradas não é um livro com 92,5% de qualidade.
É um livro em que o leitor deixa de confiar — e a partir daí, sempre que falha,
a hipótese "o livro está errado" compete com "eu errei". Isso destrói o produto.

**Portanto: nenhum problema entra no livro sem passar os quatro estados.**

---

## Os quatro estados

```
   GENERATED ──→ SOLVED ──→ CHECKED ──→ VERIFIED
       │            │           │           │
    IA #1         IA #2       IA #3      Código
     cria       resolve do   ataca o    prova ou
                  zero        problema  simula
       │            │           │           │
       └────────────┴───────────┴───────────┘
                        ↓
                    REJECTED
              (qualquer falha → rejeitado)
```

### 1. `GENERATED` — IA #1 cria

Recebe: categoria, dificuldade, conceito alvo, e a lista de títulos já existentes
(para evitar duplicados). Devolve o JSON completo, incluindo a sua própria solução.

### 2. `SOLVED` — IA #2 resolve às cegas

Recebe **apenas o campo `problem`**. Não vê a solução, nem as dicas, nem os metadados.
Devolve a sua resposta e o seu raciocínio.

- Respostas coincidem → `SOLVED`
- Não coincidem → **rejeitado ou marcado para revisão humana**

Isto apanha a maioria dos erros aritméticos e de raciocínio.

### 3. `CHECKED` — IA #3 ataca

Recebe o problema **e** a solução, com uma instrução adversarial explícita:

> Encontra uma falha. Procura, por esta ordem:
> (a) outra resposta igualmente válida; (b) ambiguidade no enunciado;
> (c) informação em falta; (d) um pressuposto não declarado;
> (e) uma dica que revela demasiado; (f) um erro de cálculo.
> Se não encontrares nenhuma, di-lo explicitamente.

Isto apanha o erro que o passo 2 não apanha: **ambiguidade**. Duas IAs podem chegar
à mesma resposta e o problema ter, ainda assim, outra resposta válida.

### 4. `VERIFIED` — o código prova

Sempre que a categoria o permitir, um script decide. Ver a tabela seguinte.

---

## Métodos de verificação por categoria

| Categoria | Método | O que o script faz |
|---|---|---|
| 🧠 Lógica | `exhaustive` | Enumera **todos** os mundos possíveis, aplica as restrições, conta as soluções. Aceita **se e só se** houver exactamente uma. |
| 🎲 Probabilidade | `monte_carlo` | Simula ≥ 10⁶ ensaios. Aceita se \|simulado − analítico\| < 0,5%. |
| 🔢 Matemática | `exact` / `brute_force` | `fractions.Fraction` para álgebra e geometria (aritmética exacta, sem vírgula flutuante e sem dependências); força bruta para combinatória e teoria dos números. |
| 💻 Programação | `execute` | Corre o snippet num subprocesso isolado (timeout 5s, sem rede) e compara a saída real com `answer`. |
| 🕵️ Enigmas | `manual` | Revisão humana. Sem prova formal possível. |
| 🌀 Lateral | `manual` | Revisão humana + o teste de inevitabilidade (ver [`13`](13-controlo-de-qualidade.md)). |
| ⚖️ Dilemas | `n/a` | Não há resposta a verificar. Verifica-se equilíbrio dos argumentos. |
| 🤔 O que farias? | `n/a` | Verifica-se que as restrições do cenário são coerentes e que as abordagens as respeitam. |

**Regra:** categorias com método `manual` não podem exceder **27,5% do livro**
(ENI 30 + LAT 25 = 55 de 200). É o limite de confiança aceitável.

---

## O verificador de lógica — o mais importante

A maioria dos problemas de lógica reduz-se a: *variáveis com domínio finito +
restrições*. Isso enumera-se.

```python
from itertools import permutations

# LOG-003 — três amigos, três bebidas, três pisos
pessoas = ["Ana", "Bruno", "Clara"]
solucoes = []

for bebidas in permutations(["cha", "cafe", "agua"]):
    for pisos in permutations([1, 2, 3]):
        b = dict(zip(pessoas, bebidas))
        p = dict(zip(pessoas, pisos))
        quem_cafe = [x for x in pessoas if b[x] == "cafe"][0]

        if not p[quem_cafe] > p["Ana"]:      # pista 1
            continue
        if p["Bruno"] == 3:                  # pista 2
            continue
        if b["Clara"] != "cha":              # pista 3
            continue
        solucoes.append((b, p))

assert len(solucoes) == 1, f"{len(solucoes)} soluções — problema ambíguo!"
print(solucoes[0])
```

O `assert` é a peça central de todo o projecto. **Se falhar, o problema é rejeitado,
independentemente de quão bonito seja.**

---

## O verificador de probabilidade

```python
import random

def simular(n=10_000_000):
    favoraveis = casos = 0
    for _ in range(n):
        viciada = random.random() < 0.5
        p = 0.8 if viciada else 0.5
        if random.random() < p and random.random() < p:   # duas caras
            casos += 1
            favoraveis += viciada
    return favoraveis / casos

analitico = 0.64 / 0.89
simulado  = simular()
assert abs(simulado - analitico) < 0.005, (simulado, analitico)
```

Nota: aqui a simulação também valida a *interpretação* do enunciado, não só a
aritmética. Se a simulação exigir um pressuposto que o enunciado não declara,
o enunciado está incompleto — e isso é um erro tão grave como uma conta errada.

---

## O verificador de programação

```python
import subprocess, sys, textwrap

def executar(codigo: str, timeout=5) -> str:
    r = subprocess.run(
        [sys.executable, "-c", textwrap.dedent(codigo)],
        capture_output=True, text=True, timeout=timeout,
    )
    return (r.stdout + r.stderr).strip()

saida = executar(problema["code"])
assert saida == problema["answer"].strip(), (saida, problema["answer"])
```

Se a resposta esperada for uma excepção, `answer` guarda o nome da excepção
(`"IndexError"`) e a comparação é por `in`.

---

## Revisão humana

Fica sempre um resto. O pipeline marca `NEEDS_REVIEW` quando:

- IA #2 e IA #1 discordam mas nenhuma está obviamente errada;
- IA #3 levanta uma ambiguidade genuína;
- não existe método automático (ENI, LAT, DIL, WWY);
- o script demorou demais ou não terminou.

Estes vão para uma fila. **Um humano decide.** Não há maioria de votos entre IAs —
duas IAs erradas não fazem uma certa.

---

## Métricas a acompanhar

| Métrica | Alvo |
|---|---|
| Taxa de aceitação (gerados → VERIFIED) | 30–50% é normal e saudável |
| Rejeições por ambiguidade | maior em LOG; se > 50%, os prompts estão maus |
| Rejeições por resposta errada | maior em PRB e MAT |
| Duplicados detectados | deve descer à medida que o banco cresce |
| Problemas em `NEEDS_REVIEW` | < 20% do total gerado |

**Gerar 600 problemas para publicar 200 é o resultado esperado.** Se a taxa de
aceitação for de 90%, a validação não está a funcionar.
