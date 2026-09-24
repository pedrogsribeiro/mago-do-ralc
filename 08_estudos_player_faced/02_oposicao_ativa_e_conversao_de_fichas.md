---
type: regra
summary: "Estudo 2 do Sistema Player-Faced: oposição ativa, agência de NPCs e hipótese de compressão matemática de fichas M20 para resolução centrada no jogador."
tags: [srd, design, player-faced, conversao, npcs, ameaca, relogios]
---

# Estudo 02: Oposição Ativa e Matriz de Conversão de Fichas

Este documento investiga como manter **NPCs plenamente agentes na ficção e na iniciativa** sem exigir que o Storyteller role suas paradas em cena. A hipótese é comprimir a contribuição mecânica da ficha do NPC em poucos parâmetros de oposição usados na resolução dos jogadores.

A pesquisa posterior mostrou que converter a parada do NPC **somente em Dificuldade** não reproduz adequadamente uma rolagem resistida de M20. O refinamento corrente usa **Dificuldade + Limiar oculto** como aproximação experimental. A conversão ainda não é considerada matematicamente encerrada.

---

## ⚙️ 1. O Princípio da Agência e da Resolução Player-Faced

O NPC **não se torna passivo** por ter a ficha comprimida. Ele continua possuindo intenção, ações próprias, posição na iniciativa e capacidade de atacar, fugir, esconder-se, perseguir, manipular, conjurar ou executar qualquer outra ação apropriada à ficção.

A mudança ocorre apenas na fonte de aleatoriedade:

* **Quando a ação envolve diretamente a agência de um jogador**, a incerteza é resolvida por uma rolagem do próprio jogador. Se um agente tenta se esconder de um PJ, por exemplo, o agente é quem age na ficção, mas o PJ rola para determinar se percebe ou não a ocultação.
* **Quando não existe agência relevante de jogador**, o Storyteller não precisa simular o mundo rolando contra si mesmo. Ele decide se a ação do NPC acontece de acordo com a ficção, as capacidades estabelecidas e as necessidades da história.
* **NPCs continuam agindo em seus turnos.** A ausência de rolagem do ST não elimina ações, iniciativa ou causalidade ficcional.

### A. Ação Proativa do PJ

O jogador usa sua parada normal de M20 contra a oposição comprimida pertinente.

* **$\ge 2$ sucessos líquidos:** resultado sólido, com qualidade compatível com os graus de sucesso de M20.
* **1 sucesso líquido:** **sucesso marginal**. A ação funciona no mínimo necessário e move a ficção adiante. O Storyteller qualifica seu alcance, precisão ou efeito conforme a situação; custo ou complicação não são automáticos.
* **0 sucessos:** falha simples; a situação evolui segundo a ficção e as ações já declaradas.
* **Botch:** segue a lógica de falha crítica de M20.

### B. Ação Proativa do NPC

O NPC declara e executa sua ação normalmente em sua posição na iniciativa. Quando o resultado da ação ameaça ou disputa diretamente algo sob agência de um PJ, a resolução é ancorada na rolagem adequada do jogador contra a oposição do NPC. O objetivo da compressão é substituir **a rolagem do NPC**, não substituir **a ação do NPC**.

---

## 🧮 2. Hipótese de Conversão Matemática da Oposição

A primeira versão deste estudo tentou representar a competência do NPC **exclusivamente pela Dificuldade do dado do PJ**. Auditoria exata posterior mostrou que essa transformação é insuficiente: alterar a dificuldade muda a chance de sucesso de cada dado, enquanto uma disputa resistida de M20 subtrai uma quantidade **variável** de sucessos produzidos por outra rolagem.

O refinamento atual testa dois parâmetros ocultos do Storyteller:

1. **Dificuldade ajustada:** corrige a taxa de produção de sucessos do PJ.
2. **Limiar oculto:** subtrai uma quantidade fixa de sucessos para aproximar a pressão que a rolagem do NPC exerceria.

### Melhor ajuste global encontrado até aqui

Calibração exata para PJs de 2 a 10 dados, contra NPCs de 2 a 12 dados, considerando ambos em Dificuldade 6 no baseline resistido:

| Parada do NPC | Dificuldade do PJ | Limiar oculto |
| :---: | :---: | :---: |
| **2d** | **6** | **1** |
| **3d** | **6** | **1** |
| **4d** | **7** | **1** |
| **5d** | **6** | **2** |
| **6d** | **6** | **2** |
| **7d** | **7** | **2** |
| **8d** | **7** | **2** |
| **9d** | **6** | **3** |
| **10d** | **7** | **3** |
| **11d** | **7** | **3** |
| **12d** | **7** | **3** |

Essa tabela é **experimental, não normativa**. Ela reduz drasticamente o erro da hipótese “somente dificuldade”, mas ainda não reproduz perfeitamente a variância de uma segunda rolagem independente. O estudo matemático posterior deve continuar refinando essa equivalência.


---

## 🏷️ 3. Exemplos Práticos de Conversão

### A. Cientista Extraordinário (Não Iluminado)
* **Oposição experimental:** uma parada relevante de **5–6 dados** converte provisoriamente para **Diff 6 + Limiar 2**; uma competência física menor deve usar a parada efetiva correspondente antes da conversão.
* **Persistência de cena:** relógios e dano fixo continuam hipóteses separadas de compressão e não são validados automaticamente pela tabela probabilística acima.

### B. HIT-MARK X (Ciborgue de Extermínio Tecnocrático)
* **Oposição experimental:** capacidades na faixa de **9–12 dados** usam provisoriamente combinações entre **Diff 6–7 + Limiar 3**, conforme a parada efetiva convertida.
* **Relógio de Vitalidade e Dano Fixo:** permanecem objetos de estudo próprios; não devem ser considerados equivalentes a M20 apenas porque a oposição foi calibrada.
* **Gatilhos Dramáticos:**
  * *Aura de Pânico:* Ao se aproximar, o PJ rola *Força de Vontade (Diff 6)* ou sofre +1 de dificuldade.
  * *Autodestruição:* Ao chegar a 0 Impactos, detona em 1 turno (PJs rolam *Atletismo/Esquiva Diff 7* para evitar 4 Danos Letais).
