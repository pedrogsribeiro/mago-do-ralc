---
type: regra
summary: "Estudo 2 do Sistema Player-Faced: Matriz de conversão direta de fichas clássicas de M20 para Fatores de Ameaça e Relógios de Cena."
tags: [srd, design, player-faced, conversao, npcs, ameaca, relogios]
---

# Estudo 02: Oposição Ativa e Matriz de Conversão de Fichas

Este documento estabelece a fórmula de conversão direta de qualquer ficha de NPC do livro básico de *Mago 20 Anos* para o formato **Fator de Ameaça Player-Faced**, eliminando a necessidade de o ST gerenciar fichas secundárias de personagens ou rolar dados em cena.

---

## ⚙️ 1. O Princípio da Ação e Reação Única (Single Roll Resolution)

Em vez de 4 rolagens por troca de combate (*Ataque $\rightarrow$ Esquiva $\rightarrow$ Dano $\rightarrow$ Absorção*), a troca é resolvida na rolagem do jogador:

### A. Ação Proativa do PJ (O PJ ataca ou hackeia)
* **$\ge 2$ Sucessos:** Causa dano pleno / avanço pleno sem sofrer dano.
* **1 Sucesso:** Causa dano / avança o objetivo, **MAS o opositor contra-ataca** (dano leve ou complicação).
* **0 Sucessos:** Erra o alvo e o opositor ganha a iniciativa (Ação de Ameaça).

### B. Reação do PJ (O Opositor ataca o PJ)
* O jogador rola **Esquiva / Vigor / Mente**:
* **$\ge 2$ Sucessos:** Desvia/bloqueia perfeitamente (0 dano).
* **1 Sucesso:** Sofre **1 Ponto de Dano de raspão** ou complicação de posição.
* **0 Sucessos:** Toma o **Dano Fixo da Ameaça** em cheio.

---

## 🧮 2. Matriz de Conversão Direta (Ficha Clássica M20 $\rightarrow$ Fator de Ameaça)

| Parada do NPC no Livro (Atrib + Hab) | Nível da Ameaça | Oposição (Diff PJ Agir) | Ameaça (Diff PJ Defender) | Relógio de Caixas | Limiar de Sucessos |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **3 a 4 dados** | Amador / Capanga / Suporte | **Diff 5** | **Diff 5** | **3 Caixas** | **Padrão** (1s marca 1 caixa) |
| **5 a 6 dados** | Treinado / Agente Padronizado | **Diff 6** | **Diff 6** | **4 Caixas** | **Padrão** (1s marca 1 caixa) |
| **7 a 8 dados** | Elite / Terno Preto / Especialista | **Diff 7** | **Diff 7** | **5 Caixas** | **Limiar 2** (1s = Efeito Zero no Relógio) |
| **9 ou + dados** | Lendário / Hit-Mark X / Mestre | **Diff 8** | **Diff 8** | **6 a 7 Caixas** | **Limiar 2 ou 3** (Super-Blindagem) |


---

## 🏷️ 3. Exemplos Práticos de Conversão

### A. Cientista Extraordinário (Não Iluminado)
* **Dificuldade Alvo:** **Diff 6** (Ciência/Computação) | **Diff 5** (Combate Físico).
* **Relógio de Vitalidade:** **3 Impactos** (1 Sucesso Pleno do PJ o incapacita).
* **Dano Fixo:** **2 Pontos** (Pistola leve) ou **Bloqueio de Terminal** (se o PJ tirar 0 sucessos).

### B. HIT-MARK X (Ciborgue de Extermínio Tecnocrático)
* **Dificuldade Alvo:** **Diff 7** (Para Danificar) | **Diff 7** (Para Esquivar dos Canhões).
* **Relógio de Vitalidade:** **7 Impactos** (*Armadura de Primium:* Reduz em 1 Impacto todo dano de acertos parciais).
* **Dano Fixo de Ameaça:** **4 Pontos de Dano Agravado**.
* **Gatilhos Dramáticos:**
  * *Aura de Pânico:* Ao se aproximar, o PJ rola *Força de Vontade (Diff 6)* ou sofre +1 de dificuldade.
  * *Autodestruição:* Ao chegar a 0 Impactos, detona em 1 turno (PJs rolam *Atletismo/Esquiva Diff 7* para evitar 4 Danos Letais).
