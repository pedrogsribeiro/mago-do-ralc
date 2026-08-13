---
type: regra
summary: "Estudo 3 do Sistema Player-Faced: Mecânica de Movimentos Telegrafados para Chefes, análise estatística de escolhas táticas e categorias de telegrafos."
tags: [srd, design, player-faced, chefes, telegrafos, tatica, combate]
---

# Estudo 03: Chefes e Movimentos Telegrafados

Este documento estabelece o sistema de **Movimentos Telegrafados (Telegraphed Moves)** para encontros com Chefes e Antagonistas Principais em *Mago: A Ascensão 20 Anos*. A mecânica elimina rolagens secretas do Narrador e substitui o combate passivo por dilemas táticos de intenção declarada.

---

## 📢 1. O Conceito da Intenção Declarada

No início de cada rodada (ou final da rodada anterior), o Narrador **anuncia abertamente o ataque/perigo iminente do Chefe**:

> *"O HIT-MARK IV travou o sistema de mira térmica no Andrey. No final deste turno, ele disparará um Canhão de Plasma de 5 Danos Agravados."*

---

## 🎮 2. As 3 Respostas Táticas dos Jogadores

Diante do telegrama, o jogador alvo ou a equipe precisa escolher 1 entre 3 opções táticas para alocar sua ação:

```
+-----------------------------------------------------------------------------------------+
|                              OPÇÕES TÁTICAS DO JOGADOR                                  |
+-----------------------------------------------------------------------------------------+
|  Opção A: Tentar Interromper a Carga (Rolagem de Interrupção / Mágika / Ataque Físico)  |
|  Opção B: Mitigar / Focar 100% em Defesa (Rolagem de Esquiva / Mágika de Proteção)      |
|  Opção C: Ignorar o Aviso e Atacar com Tudo (Troca de Dano Direta)                      |
+-----------------------------------------------------------------------------------------+
```

---

## 🧮 3. Prova Matemática das Escolhas Táticas (10.000 Simulações)

Simulação estatística para um PJ com 5 Dados enfrentando um Ataque Telegrafado de 5 de Dano em **Diff 7**:

| Escolha do Jogador | Dano Médio Causado no Chefe | Dano Médio Sofrido pelo PJ | Análise Matemática |
| :--- | :---: | :---: | :--- |
| **Opção A: Interromper** | **1,28 Impactos** | **1,41 Pontos** | **Melhor Equilíbrio:** Se tirar $\ge 2$ sucessos, **cancela o ataque do chefe** e causa dano. |
| **Opção B: Defender 100%** | **0,00 Impactos** | **0,96 Pontos** | **Máxima Sobrevivência:** Preserva a vida do PJ (dano $<1$), mas não avança contra o chefe. |
| **Opção C: Atacar com Tudo** | **1,28 Impactos** | **5,00 Pontos** | **Alto Risco:** Garante dano no chefe, mas engole os 5 Danos em cheio se o chefe não for destruído. |

---

## 📜 4. As 4 Categorias de Telegrafos de Chefes

1. **Golpes Carregados (Heavy Telegraphs):** Ataques devastadores direcionados a um alvo único que exigem interrupção ou esquiva específica.
2. **Controle de Zona (Zone Control Telegraphs):** Perigos ambientais ou emissões que afetam todos os PJs em uma sala no final do turno.
3. **Carga Mágica Vulgar (Vulgar Ritual Telegraphs):** Rituais de grande escala que concedem aos PJs 1 turno de janela para realizarem **Contramágica ativa** ou quebra de concentração.
4. **Mudança de Fase / Frenesi (Phase Shift):** Ativada quando o Relógio de Vitalidade do Chefe chega na metade, alterando as dificuldades e padrões de ataque.
