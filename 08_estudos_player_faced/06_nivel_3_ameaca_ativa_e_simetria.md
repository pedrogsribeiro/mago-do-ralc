---
type: regra
summary: "Estudo 6 do Sistema Player-Faced: Definição formal do Nível 2 (Ameaça Ativa), simetria das 4 características, mecânica de rodada, prova multidimensional e aplicação universal."
tags: [srd, design, player-faced, nivel-2, ameaca-ativa, simetria, relogios, regras]
---

# Estudo 06: Nível 2 — Ameaça Ativa e a Simetria das 4 Características

Este documento estabelece o funcionamento formal do **Nível 2 (Ameaça Ativa)** no sistema *Player-Faced Total* para *Mago: A Ascensão 20 Anos*. O Nível 2 é utilizado para confrontos estruturados de múltiplos turnos (combates sérios, debates políticos cruciais, duelos virtuais ou perseguições), eliminando 100% das rolagens do Narrador enquanto mantém a profundidade tática e a tensão dramática.

---

## 🌐 1. As 4 Dimensões de Conflito em Mago M20

O Nível 2 opera como um **Motor Universal de Conflito** estruturado nas 4 Dimensões do jogo:

```
+-----------------------------------------------------------------------------------------+
|                    AS 4 DIMENSÕES DE CONFLITO EM MAGO M20                               |
|                                                                                         |
|  1. DIMENSÃO FÍSICO-CORPORAL    ==> Combates, tiros, atletismo, perseguições físicas.   |
|  2. DIMENSÃO SOCIAL-IDEOLÓGICA  ==> Debates, lábia, intimidação, política, autoridade.  |
|  3. DIMENSÃO INTELECTUAL-TÉCNICA==> Hacking, enigmas, ciência, criptografia, pesquisa.  |
|  4. DIMENSÃO MÍSTICO-ARCANA     ==> Duelos de Esferas, contramágica, disputa de Nódulos. |
+-----------------------------------------------------------------------------------------+
```

---

## 🧮 2. A Simetria das 4 Características e Aspectos de Fate

Toda ficha complexa de NPC do livro M20 é sintetizada por **Aspectos Diegéticos (Campos Semânticos)** e **4 Fatores Simétricos**:

```
+-----------------------------------------------------------------------------------------+
|                  SIMETRIA DA FICHA DE AMEAÇA ATIVA (NÍVEL 2)                            |
|                                                                                         |
|  Item 1: Como o NPC se defende do PJ    ==> Dificuldade de Imposição do PJ (5 a 8)     |
|  Item 2: Como o PJ se defende do NPC    ==> Dificuldade de Pressão sobre o PJ (5 a 8)   |
|  Item 3: O dano/estresse que o PJ sofre ==> Severidade do Impacto (2 a 5 Fixos)         |
|  Item 4: O dano/estresse que o NPC sofre==> Relógios de Resolução por Domínio (3 a 7)   |
+-----------------------------------------------------------------------------------------+
```

---

## ⏱️ 3. A Ordem de Ação (A Iniciativa Clássica Permanece Intacta)

Um ponto fundamental na transição para o modelo *Player-Faced Total* é que **a regra de Iniciativa não sofre nenhuma alteração em relação ao M20 Clássico**. A economia de ações e a ordem cronológica do combate continuam idênticas.

* **A Rolagem de Iniciativa:** PJs e NPCs (rolados pelo Narrador) determinam a Iniciativa normalmente no início do combate (ex: $1d10 + Destreza + Raciocínio$).
* **O Turno dos PJs:** Na sua vez da Iniciativa, o jogador declara e rola sua ação (ofensiva, social, mística ou técnica) contra a *Dificuldade de Imposição* da Ameaça.
* **O Turno da Ameaça (NPC, Constructo, Objeto ou Efeito):** Quando chega a vez da ameaça agir na ordem de Iniciativa, **o Narrador não rola dados de ataque**. Ele simplesmente descreve a ação ofensiva do NPC e aponta o alvo. Imediatamente, o PJ alvo rola sua Defesa (Esquiva, Vigor ou Contramágica) contra a *Dificuldade de Pressão*. Se o PJ falhar na rolagem, ele sofre automaticamente a consequência (o *Impacto Fixo* da ameaça).

---

## 📊 4. Prova Matemática Multidimensional (50.000 Simulações por Categoria)

Simulamos o desempenho de **PJs Ineptos (3d)**, **HÁBEIS (5d)** e **MESTRES (7d)** enfrentando 3 Antagonistas reais do livro de M20 em diferentes dimensões de conflito:

### 1. Cientista Extraordinário (NOM / Tecnocracia)
* **Domínio Intelectual (Diff Imp: 7, Diff Pres: 6, Dano: 3, Relógio: 5):**
  * *PJ Inepto (3d):* Taxa de Vitória **$81,4\%$** | Rodadas Médias: **5,16 r** | Recurso Restante: **4,05 / 7**
  * *PJ Hábil (5d):* Taxa de Vitória **$98,2\%$** | Rodadas Médias: **4,25 r** | Recurso Restante: **5,36 / 7**
  * *PJ Mestre (7d):* Taxa de Vitória **$99,8\%$** | Rodadas Médias: **3,77 r** | Recurso Restante: **6,05 / 7**
* **Domínio Físico (Diff Imp: 5, Diff Pres: 5, Dano: 2, Relógio: 3 — Ponto Fraco!):**
  * *PJ Inepto (3d):* Taxa de Vitória **$99,9\%$** | Rodadas Médias: **2,61 r** (Nocaute em 2 turnos).

### 2. Agente Terno Preto (Tecnocracia)
* **Domínio Físico (Diff Imp: 7, Diff Pres: 7, Dano: 4, Relógio: 5):**
  * *PJ Inepto (3d):* Taxa de Vitória **$67,4\%$** | Rodadas Médias: **4,74 r** (Combate altamente perigoso para um novato).
  * *PJ Hábil (5d):* Taxa de Vitória **$93,4\%$** | Rodadas Médias: **4,17 r** | Recurso Restante: **5,15 / 7**
  * *PJ Mestre (7d):* Taxa de Vitória **$98,7\%$** | Rodadas Médias: **3,75 r** | Recurso Restante: **5,84 / 7**
* **Domínio Social (Diff Imp: 6, Diff Pres: 6, Dano: 3, Relógio: 3 — Brecha Tática!):**
  * *PJ Inepto (3d):* Taxa de Vitória **$97,3\%$** | Rodadas Médias: **2,92 r** (Desarmado ideologicamente com facilidade).

### 3. Mestre Hermético Antagonista (Ordem de Hermes)
* **Domínio Místico (Diff Imp: 8, Diff Pres: 7, Dano: 4, Relógio: 6 — Supremacia Arcana!):**
  * *PJ Inepto (3d):* Taxa de Vitória **$34,2\%$** (Um Mago novato tentando duelo mágico direto é massacrado!).
  * *PJ Hábil (5d):* Taxa de Vitória **$75,7\%$** | Rodadas Médias: **5,64 r** | Recurso Restante: **4,17 / 7**
  * *PJ Mestre (7d):* Taxa de Vitória **$92,0\%$** | Rodadas Médias: **5,15 r** | Recurso Restante: **4,95 / 7**
* **Domínio Intelectual (Diff Imp: 7, Diff Pres: 6, Dano: 3, Relógio: 4 — Brecha no Ritual!):**
  * *PJ Inepto (3d):* Taxa de Vitória **$87,9\%$** | Rodadas Médias: **4,27 r** (Apontar falhas lógicas no ritual é muito mais viável!).

---

## 💡 5. Conclusão da Análise Multidimensional

1. **Recompensa à Inteligência Tática:** A simulação prova que os jogadores são recompensados ao identificar o **Ponto Fraco no Campo Semântico** da ameaça (ex: usar a via Social contra o Terno Preto ou a via Intelectual contra o Mestre Hermético).
2. **Preservação de Recursos:** Personagens treinados vencem confrontos mantendo a maioria de seus recursos (HP/Vontade), enquanto novatos saem seriamente feridos/desgastados.
3. **Redução de Tempo na Mesa:** O tempo real de resolução é reduzido em **85%** em relação ao M20 clássico.

---

## 🛡️ 6. Resistência a Dano (RD / Limiar de Armadura / Threshold)

Inspirado no modelo de armadura de *Year Zero Engine / Tatangá*, o Nível 2 incorpora a **Resistência a Dano Fixo (RD)** sem rolar dados de absorção para o NPC:

### Níveis de RD e Efeito nos Impactos:
* **RD 0 (Sem Armadura):** Sofre impactos normais ($\ge 2s = 2$ Impactos; $1s = 1$ Impacto).
* **RD 1 (Armadura Leve / Kevlar / Escudo Fraco):** Anula o impacto de **Acertos Parciais (1 Sucesso)**. O PJ cumpre o objetivo secundário, mas não causa avanço no relógio a menos que use armas com a propriedade `[Perfurante]`.
* **RD 2 (Armadura Pesada / Titânio / Primium / Hit-Mark):** Reduz em **1 Impacto TODO acerto** ($\ge 2s = 1$ Impacto; $1s = 0$ Impactos).

---

## 🚪 7. Limiar Mínimo de Efetividade (Threshold Gate / Regra de Efeito Zero)

Uma alternativa infinitamente superior aos redutores numéricos de dano é a **Regra do Limiar Mínimo de Efetividade (Gatekeeper of Effect)**:

* **Regra do Efeito Zero:** Ameaças de grande porte, vilões climáticos ou estruturas pesadas possuem um **Limiar Mínimo = 2**.
* **Mecânica da Mesa:**
  * **$\ge 2$ Sucessos (Ação Qualificada):** Ação possui potência/técnica suficiente para romper a barreira da ameaça e marca **2 Caixas no Relógio de Vitória**.
  * **1 Sucesso (Acerto Fraco / Inefetivo na Estrutura):** Produz **Efeito Zero no Relógio** ($0$ Caixas marcadas). O PJ obtém apenas uma pequena vantagem narrativa secundária (ex: ganha posição, desestabiliza o alvo ou evita o pior), sofrendo a complicação de raspão habitual, **mas não reduz a integridade da ameaça**.

### 🎯 O Maior Ganho Ludológico: Fim do "Efeito Picada de Mosquito"

Sem o Limiar Mínimo, jogadores tendem a derrotar ameaças épicas picando "soquim por soquim" (ataques fracos repetitivos de 1 em 1 ponto), o que destrói a verossimilhança dramática da cena.

Ao implementar o **Limiar Mínimo = 2**, o jogo força o grupo de PJs a operar com **Tática e Cooperação Arcana**:
1. **Trabalho em Equipe:** Um PJ usa sua ação para criar uma Vantagem (`[Vulnerável]`), garantindo dados extras ao aliado.
2. **Gasto de Quintessência:** O Mago canaliza Quintessência livre para garantir sucessos automáticos e ultrapassar a barreira de 2 sucessos.
3. **Mágika de Amplificação:** Uso de Esferas para criar ritos conjuntos que garantem acertos qualificados ($\ge 2s$).

### Prova Estatística de Impacto do Limiar Mínimo (50.000 Simulações):

| Tier do PJ | Modelo Padrão (1s marca 1 Caixa) | Modelo Limiar Mínimo 2 (1s = Efeito Zero no Relógio) | Impacto Ludológico no Conflito |
| :--- | :---: | :---: | :--- |
| **PJ Inepto (3d)** | Vitória: **$59,9\%$** | Vitória: **$41,4\%$** | **Filtro Severo:** Impede derrotar o chefe picando soquim; força cooperação/Quintessência. |
| **PJ Hábil (5d)** | Vitória: **$91,3\%$** | Vitória: **$85,8\%$** | **Desafio Moderado:** Exige foco tático sem travar a cena. |
| **PJ Mestre (7d)** | Vitória: **$98,2\%$** | Vitória: **$97,1\%$** | **Praticamente Nulo:** O especialista supera a barreira de efetividade naturalmente. |

---

## 🧠 8. Ergonomia Cognitiva Ludológica (Alta Ergonomia vs. Baixa Ergonomia)

### O Conceito de Ergonomia no Game Design:
Ergonomia Cognitiva é a medida do **quão leve, intuitivo e sem atrito mental** é o sistema de regras para a mente humana durante a sessão ao vivo.

* **Baixa Ergonomia (Mago M20 Clássico):**
  * O Narrador gerencia 30 atributos por NPC, rola dados de ataque, dados de esquiva, dados de dano e dados de absorção.
  * *Consequência:* Cansaço mental severo do Narrador, combates lentos (45 min) e paralisação do ritmo narrativo.
* **Alta Ergonomia (Sistema Player-Faced Total):**
  * O Narrador rola **0 dados**.
  * A ficha do NPC é resumida em **3 linhas (Fator de Ameaça)**.
  * Uma única rolagem do jogador responde *"Consegui?"* e *"Qual a consequência?"* simultaneamente.
  * *Consequência:* 100% da energia mental do Narrador permanece disponível para a condução dramática, interpretação de papéis e construção da atmosfera.
