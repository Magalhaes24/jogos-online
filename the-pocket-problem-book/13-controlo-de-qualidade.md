# 13 — Controlo de qualidade

## Estudo de caso: um problema que parece bom e não é

Este é o enunciado que originou o projecto:

> Há três caixas: A, B e C. Uma contém ouro, outra prata e outra está vazia.
>
> - **A** diz: «O ouro está em B.»
> - **B** diz: «Esta caixa está vazia.»
> - **C** diz: «A está a mentir.»
>
> Apenas uma afirmação é verdadeira. Onde está o ouro?

Lê-se bem. Parece rigoroso. Tem uma restrição global elegante ("apenas uma é verdadeira").

**Está partido.** Nove linhas de Python provam-no:

```python
from itertools import permutations

sols = []
for A, B, C in permutations(["ouro", "prata", "vazia"]):
    a = (B == "ouro")     # A: «o ouro está em B»
    b = (B == "vazia")    # B: «esta caixa está vazia»
    c = (not a)           # C: «A está a mentir»
    if [a, b, c].count(True) == 1:
        sols.append({"A": A, "B": B, "C": C})

print(len(sols), sols)
```

Saída:

```
4 [{'A': 'ouro',  'B': 'prata', 'C': 'vazia'},
   {'A': 'prata', 'B': 'ouro',  'C': 'vazia'},
   {'A': 'vazia', 'B': 'ouro',  'C': 'prata'},
   {'A': 'vazia', 'B': 'prata', 'C': 'ouro'}]
```

**Quatro mundos satisfazem o enunciado**, e o ouro pode estar em A, em B **ou** em C.
Não há resposta. Qualquer solução publicada para este problema estaria errada —
incluindo a que parece mais convincente.

### O que correu mal

A afirmação de C (`«A está a mentir»`) é **redundante**: é sempre o oposto exacto da
de A. Logo, das três afirmações, exactamente uma do par (A, C) é verdadeira,
independentemente de tudo o resto. A restrição "apenas uma é verdadeira" fica toda
consumida por esse par, e a afirmação de B passa a ter de ser falsa — que é uma
restrição fraca de mais para fixar três objectos em três caixas.

**Diagnóstico geral:** o enunciado tem menos restrições **efectivas** do que aparenta,
porque duas delas são a mesma restrição. É o modo de falha mais comum em problemas de
lógica gerados por IA — e é invisível a olho nu.

### Como se corrige

A versão publicada como [`LOG-001`](11-banco-inicial.md) reduz o problema a uma única
variável (só ouro, sem prata nem caixa vazia) e substitui a afirmação redundante por
uma independente. Resultado: 3 mundos, 1 solução, verificado.

**A lição:** um problema de lógica não está terminado quando tem uma solução.
Está terminado quando um script provou que **não tem duas**.

---

## Os cinco modos de falha

| # | Falha | Onde aparece | Como se apanha |
|---|---|---|---|
| 1 | **Múltiplas soluções** | LOG, ENI | enumeração exaustiva |
| 2 | **Resposta errada** | MAT, PRB | IA #2 às cegas + simulação |
| 3 | **Pressuposto oculto** | PRB, LAT | IA #3 adversarial |
| 4 | **Dica que resolve** | todas | leitura humana |
| 5 | **Clássico disfarçado** | todas | pesquisa + campo `classic` |

### 1. Múltiplas soluções
Ver o estudo de caso acima. Sintoma típico: restrições redundantes disfarçadas de
independentes.

### 2. Resposta errada
Quase sempre em probabilidade condicional e em contagem. Sintoma típico: a solução usa
`P(A|B)` onde queria `P(B|A)`, ou conta ordenações quando devia contar combinações.
**A simulação apanha isto sempre.**

### 3. Pressuposto oculto
O enunciado não diz que os lançamentos são independentes, que ninguém mente duas vezes,
que o apresentador sabe onde está o carro. A solução usa esse facto. **O leitor não
pode chegar lá.**

Teste: pega na solução e sublinha cada facto usado. Cada um está no enunciado?

### 4. Dica que resolve
`hint_1` que já contém o mecanismo. O leitor perde a oportunidade de descobrir sozinho
com um empurrão pequeno.

Teste: dá `problem + hint_1` a uma IA. Se ela resolve com confiança alta, a dica é
demasiado forte.

### 5. Clássico disfarçado
Monty Hall com sacos em vez de portas. Não é errado — é desonesto se não for declarado.
Marca `classic: true`, e usa o clássico na sua forma canónica: é mais reconhecível e
mais bonito.

---

## Checklist editorial

Antes de marcar `VERIFIED`, cada problema passa por isto:

### Enunciado
- [ ] Cabe em 120 palavras
- [ ] É auto-contido (sem referências a outros problemas)
- [ ] Todos os pressupostos usados na solução estão escritos
- [ ] Não exige conhecimento cultural específico
- [ ] Não exige calculadora
- [ ] Uma pessoa que não sabe a resposta consegue perceber a pergunta

### Unicidade
- [ ] Se `has_unique_answer`: existe script que prova **exactamente uma** solução
- [ ] Se não existe script: passou por revisão humana e está dentro do limite de 27,5%
- [ ] IA #2 (às cegas) chegou à mesma resposta
- [ ] IA #3 (adversarial) não encontrou falha fatal

### Dicas
- [ ] `hint_1` reorienta, não resolve
- [ ] `hint_2` dá o mecanismo, não a resposta
- [ ] Nenhuma contém a resposta literal
- [ ] `hint_1 ≠ hint_2`

### Solução
- [ ] Formato de tabela ou lista, não prosa contínua
- [ ] Cada passo é verificável pelo leitor
- [ ] Confirma a resposta contra **todas** as condições do enunciado
- [ ] `why` explica o princípio, não repete a solução
- [ ] `why` tem entre 3 e 5 linhas

### Metadados
- [ ] `title` não revela nada e tem 2–4 palavras
- [ ] `difficulty` e `estimated_time` são consistentes
- [ ] `concept` está em `concepts.yaml`
- [ ] `trap` marcado se engana a intuição
- [ ] `classic` marcado se é conhecido

### Categorias sem resposta (DIL, WWY)
- [ ] Declara explicitamente que não há resposta certa
- [ ] Os argumentos dos dois lados têm força equivalente
- [ ] A variação inverte genuinamente a intuição
- [ ] Sem política partidária
- [ ] (WWY) as abordagens são genuinamente diferentes, não três versões da mesma
- [ ] (WWY) `common_mistake` está preenchido

---

## Testes específicos por categoria

**🌀 Lateral — o teste da inevitabilidade**
Depois de ouvir a resposta, o leitor pensa *"que idiota que eu fui"* ou *"isso é
injusto"*? Se for a segunda, rejeita. Toda a pista do enunciado tem de ser explicada
pela solução — se sobra um detalhe por explicar, ou a solução está errada ou o detalhe
é ruído e deve sair.

**🎲 Probabilidade — o teste da interpretação**
Antes de simular, escreve a simulação a partir **só do enunciado**, sem olhar para a
solução. Se tiveres de tomar uma decisão que o enunciado não especifica, o enunciado
está incompleto. Este teste é mais valioso do que a simulação em si.

**💻 Programação — o teste da execução literal**
A `answer` é o que a consola imprime, carácter a carácter, incluindo espaços e a
formatação de listas do Python. Não é uma descrição do que acontece.

**🧠 Lógica — o teste do script obrigatório**
Sem script, sem `VERIFIED`. Não há excepções nesta categoria.

---

## O que fazer com um problema rejeitado

Não apagar. Marcar `REJECTED` com a razão, e mantê-lo no ficheiro.

Serve para duas coisas:
1. Evita voltar a gerar o mesmo problema partido daqui a três meses.
2. Alimenta o *few-shot* negativo dos prompts: mostrar à IA um problema rejeitado e
   porquê melhora a geração seguinte mais do que mostrar dez bons.

E há uma terceira, ocasional: um problema rejeitado por **ambiguidade** é às vezes um
problema excelente noutra categoria. As três caixas ambíguas deste documento não servem
para 🧠 Lógica — mas «quantas respostas tem este problema?» é um belo problema de lógica
sobre lógica.
