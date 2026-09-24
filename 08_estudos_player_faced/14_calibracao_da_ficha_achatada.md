---
type: regra
summary: "Estudo 14: calibração da ficha achatada contra o pipeline original de M20, separando Oposição, Ameaça, Consequência, Integridade e Limiar de Efetividade."
tags: [estudo, player-faced, calibracao, ficha-achatada, oposicao, ameaca, consequencia, limiar, probabilidade]
---

# Estudo 14: Calibração da Ficha Achatada contra M20

Este estudo não cria uma nova arquitetura. Ele testa quantitativamente a arquitetura já desenvolvida:

- **Oposição**
- **Ameaça**
- **Consequência**
- **Integridade / Relógio**
- **Limiar de Efetividade**

distribuídos por dimensão quando pertinente.

A pergunta é:

> **A ficha achatada consegue substituir as operações do Storyteller preservando suficientemente a experiência probabilística e decisória dos jogadores de M20?**

---

## 1. Critério de fidelidade

A validação não pode comparar apenas médias.

Para cada transformação devem ser comparados, quando pertinentes:

- probabilidade de nenhum efeito;
- probabilidade de efeito marginal;
- distribuição completa de dano/Impacto;
- valor esperado;
- variância;
- probabilidade de consequências severas;
- sensibilidade à competência do PJ;
- sensibilidade à competência do NPC;
- duração de conflitos persistentes.

O teste precisa ainda preservar:

- economia de ações;
- recursos usados pelo jogador;
- diferenças entre defesa ativa e ausência de defesa;
- tipos de dano e possibilidade de soak;
- sucessos excedentes;
- propriedades especiais da ficha original.

---

## 2. Quatro calibrações diferentes

### 2.1. Parada defensiva do NPC → Oposição

Caso clássico:

```
PJ age
→ PJ rola
→ NPC rola resistência/defesa
→ sucessos se cancelam
```

Caso player-faced:

```
PJ age
→ PJ rola contra Oposição
→ resultado já incorpora a resistência do NPC
```

Os Estudos 02 e 05 demonstraram que apenas alterar a Dificuldade é insuficiente.

O baseline experimental atual usa **Dificuldade + limiar oculto matemático**.

> Esse limiar oculto pertence somente à transformação probabilística de Oposição e não deve ser confundido com o **Limiar de Efetividade** da ficha.

---

### 2.2. Parada ofensiva do NPC → Ameaça

Caso clássico:

```
NPC age
→ NPC rola ataque/ação
→ PJ pode ou não possuir defesa ativa
```

Caso player-faced:

```
NPC age normalmente na ficção e iniciativa
→ Ameaça representa sua capacidade de impor aquela ação
→ a resolução pertinente fica do lado do jogador
```

Esta calibração precisa testar separadamente duas situações de M20:

1. **PJ declarou defesa ativa**;
2. **PJ não declarou defesa ativa**.

A ficha achatada não pode conceder gratuitamente uma ação defensiva que o jogador não teria no M20 original sem testar o efeito dessa mudança.

---

### 2.3. Parada de dano do NPC → Consequência

Consequência já é um campo necessário da ficha achatada.

A tarefa é converter uma parada de dano variável do NPC em um valor operacional fixo ou quase fixo sem destruir:

- chance de nenhum dano;
- dano médio;
- cauda de dano alto;
- diferenças entre armas e poderes;
- sucessos excedentes do ataque;
- tipos de dano.

A calibração deve ser feita **junto com Ameaça**, porque no M20 sucessos excedentes do ataque alimentam a parada de dano.

---

### 2.4. Soak/resistência do NPC → Limiar de Efetividade

O **Limiar de Efetividade** é a generalização da antiga RD fixa.

No físico:

```
PJ acerta
→ PJ rola dano
→ Limiar reduz o Impacto que atravessa
```

A ação pode ter sido bem-sucedida e ainda causar 0 Impacto, exatamente como um ataque em M20 pode acertar e ter todo o dano absorvido.

O estudo precisa encontrar a conversão:

```
parada de soak original → Limiar de Efetividade
```

comparando a distribuição do dano pós-soak, e não apenas sua média.

Depois, o mesmo conceito pode ser usado em dimensões não físicas quando houver resistência equivalente.

---

## 3. Integridade não deve ser calibrada isoladamente

Integridade / Relógio determina quanto progresso uma Ameaça suporta.

Seu valor só pode ser calibrado **depois** de Oposição e Limiar, porque eles determinam quantos Impactos entram por ação.

A pergunta correta não é:

> “quantas caixas equivalem a 7 níveis de Vitalidade?”

e sim:

> “com esta Oposição e este Limiar, qual Integridade reproduz de forma aceitável a duração e a letalidade de uma ficha de M20?”

Para NPCs cuja Vitalidade original já é simples e importante, preservar os 7 níveis pode continuar sendo a melhor resposta.

---

## 4. Dimensões são calibradas separadamente

A ficha achatada não possui um único valor global.

Exemplo:

| Dimensão | Oposição | Ameaça | Consequência | Integridade | Limiar |
| :--- | :---: | :---: | :--- | :---: | :---: |
| Físico | 7 | 7 | 4L | 7 | 2 |
| Social | 5 | 6 | -1 Vontade | 4 | 0 |
| Mental/Técnico | 6 | 7 | Condição | 5 | 1 |
| Mágicko | 0 | 0 | — | — | — |

Os números acima são apenas exemplo estrutural.

**0 não é “baixo”.** É ausência daquela capacidade/resistência relevante.

Cada linha precisa ser derivada das capacidades que realmente existem no conteúdo original.

---

## 5. Pipeline clássico que deve servir de baseline

### PJ ataca NPC com defesa ativa

```
ataque do PJ
→ defesa do NPC
→ sucessos excedentes
→ dano do PJ
→ soak do NPC
→ dano final
```

### NPC ataca PJ com defesa ativa

```
ataque do NPC
→ defesa do PJ
→ sucessos excedentes
→ dano do NPC
→ soak do PJ quando permitido
→ dano final
```

### NPC ataca PJ sem defesa ativa

```
ataque do NPC
→ sucessos excedentes
→ dano do NPC
→ soak do PJ quando permitido
→ dano final
```

O modelo player-faced precisa ser comparado contra os três pipelines, e não apenas contra uma rolagem abstrata de “sucesso/falha”.

---

## 6. Modelos candidatos a testar para Ameaça + Consequência

O estudo não homologa ainda um deles.

### Modelo A — Resposta sempre player-faced
Toda ação do NPC gera uma rolagem de resistência apropriada do PJ contra Ameaça, seguida da aplicação de Consequência conforme o resultado.

Vantagem:
- extremamente uniforme.

Risco:
- pode conceder ao jogador uma defesa que não existia na economia de ações original.

### Modelo B — Economia de ações preservada
Se o PJ declarou defesa, usa sua defesa contra Ameaça.
Se não declarou, não recebe defesa ativa; Consequência incorpora estatisticamente ataque + dano do NPC e o PJ mantém apenas resistências reflexivas que M20 já permitiria.

Vantagem:
- preserva melhor a economia de ações.

Risco:
- Consequência pode precisar carregar mais informação probabilística.

### Modelo C — Resposta reflexiva distinta
Sem defesa ativa, o PJ usa apenas uma resistência reflexiva já existente no sistema, como soak/Vigor quando aplicável, enquanto Ameaça + Consequência comprimem ataque e dano do NPC.

Vantagem:
- mantém a rolagem do jogador em um procedimento que ele já possuía.

Risco:
- não cobre uniformemente ações que não possuem uma resistência reflexiva equivalente.

O script de auditoria deve comparar esses modelos em vez de escolher por intuição.

---

## 7. Saídas exigidas da auditoria

O script deve gerar:

1. melhor conversão de **Oposição** por parada de NPC;
2. melhor **Limiar de Efetividade** por parada de soak;
3. melhores pares **Ameaça + Consequência** por parada ofensiva e dano-base;
4. erro por tamanho de parada do PJ;
5. erro por tipo de defesa;
6. distribuição de dano clássico vs. player-faced;
7. casos extremos que mais se afastam;
8. relatório compacto para decidir o próximo refinamento.

Métricas mínimas:

- distância de variação total (TV);
- erro de probabilidade de efeito;
- erro de dano médio;
- erro de probabilidade de 3+ danos;
- erro máximo por faixa de competência.

---

## 8. Gate do Estudo 14

A ficha achatada só passa para texto final quando:

1. nenhuma conversão relevante depender de “parece razoável”;
2. os erros forem pequenos e sem viés sistemático grave contra PJs fracos ou fortes;
3. a economia de ações não for alterada silenciosamente;
4. tipos de dano e resistências especiais continuarem importando;
5. exemplos reais do capítulo de NPCs produzirem comportamento próximo ao original;
6. playtests confirmarem que diferenças matemáticas residuais não mudam perceptivelmente a experiência.

A etapa atual é **calibração matemática**, seguida por teste em fichas reais e só depois playtest.
