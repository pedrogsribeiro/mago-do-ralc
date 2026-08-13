---
type: no_investigativo
summary: "Nó E do Arco 01: O Santuário de Lizander. O Clímax da crônica utilizando o modelo de Nível 4 (Ameaça Telegrafada / Chefe Climático)."
tags: [no_e, santuario_lizander, lizander, climax, nivel_4, telegrafado, chefe, cronica, arco_01]
---
# Nó E: Santuário de Lizander — O Clímax do Arco 01

Este é o **Nó E (O Clímax do Arco 01)**. A antiga usina hidrelétrica abandonada na periferia de São Paulo, transformada por [Lizander Filho do Raio](../02_npcs/lizander_filho_do_raio.md) em um santuário místico de *Forças 4 / Primórdio 3*. Aqui, ele canaliza a Quintessência colhida do sangue contaminado para alimentar um grande ritual de extermínio de magos.

---

## ⚡ 1. O Cenário do Clímax

* **A Usina Abandonada:** O salão das turbinas está iluminado por arcos elétricos azuis de 10.000 volts que crepitam no teto. No centro, uma torre metálica acumula o plasma refinado do Néctar de Sangue.
* **O Motor do Ritual:** Lizander está suspenso no ar em um transe de Fúria Mística, usando a dor da pandemia como catalisador arcano.

---

## 🎭 2. Mecânica do Nível 4: Ameaça Telegrafada & Intenções Declaradas

Diferente do Nível 3, um confrontamento de **Nível 4 (Chefe Climático)** opera via **Movimentos Telegrafados Declarados no início de cada rodada**:

```
+---------------------------------------------------------------------------------------------------+
|                   FLUXO DA RODADA TELEGRAFADA DE CHEFE (NÍVEL 4)                                  |
|                                                                                                   |
|  1. DECLARAÇÃO DE INTENÇÃO ==> O Narrador declara a ação devastadora do Chefe para a próxima turna.|
|  2. DECISÃO TÁTICA DOS PJS ==> Cada jogador escolhe 1 de 3 opções:                                 |
|                                - Opção A: Interromper a Carga (Diff 7 / Ganha 2 Impactos se passar)|
|                                - Opção B: Focar 100% em Defesa (Diff 6 / Evita todo o dano)        |
|                                - Opção C: Atacar com Tudo (Toma o Dano em cheio, mas acerta fácil)  |
|  3. RESOLUÇÃO DOS DADOS  ==> Os jogadores rolam os dados e aplicam as consequências.              |
+---------------------------------------------------------------------------------------------------+
```

---

## 🌩️ 3. As 2 Fases do Confronto contra Lizander

### FASE 1: O Escudo de Tempestade & Carga de Raios
Lizander está protegido por uma barreira de eletricidade estática (RD 2).

* **Movimento Telegrafado (Rodada 1):** *“Lizander ergue os braços e canaliza 50.000 volts na turbina principal. No próximo turno, uma descarga de Raios em Cadeia atingirá todos no salão (5 de Dano Agravado)!”*
* **Decisões dos PJs:**
  * *Interromper (Opção A - Diff 7):* Rola *Mágika de Forças/Espírito/Matéria* ou tiroteio no painel. Se passar ($\ge 2s$), cancela o raio e causa 2 Impactos no relógio de Lizander!
  * *Defender (Opção B - Diff 6):* Rola *Esquiva/Vigor/Avatar*. Se passar ($\ge 2s$), desvia perfeitamente atrás das colunas blindadas.
  * *Atacar com Tudo (Opção C - Diff 5):* Rola o ataque mais poderoso da ficha. Toma os 5 de Dano Agravado em cheio, mas marca 2 Impactos garantidos no relógio de Lizander.

### FASE 2: A Aparição de Joana Pipoquinha & O Dilema Moral
Quando o Relógio de Lizander chega a **3 Caixas**, o espírito de sua filha [Joana Pipoquinha](../02_npcs/joana_pipoquinha.md) se manifesta chorando entre os arcos elétricos.

* **O Dilema Tático da Fase 2:**
  * **Via de Destruição Físico/Mística ($Diff 8$):** Continuar atacando Lizander com força bruta para zerar suas últimas 3 Caixas.
  * **Via de Redenção Social/Mística ($Diff 6$):** Usar *Empatia / Mente 3 / Espírito 2* para ajudar Joana a comover o pai. Se os PJs obtiverem $\ge 2s$, Lizander entra em colapso emocional, cancela o ritual e cai ajoelhado chorando pela filha, encerrando o confronto sem mais mortes!

---

## ⚔️ 4. Ficha de Chefe Nível 4: Lizander Filho do Raio

```yaml
---
ameaca: Lizander Filho do Raio (Mestre de Forças Fanático)
nivel: 4 (Ameaça Telegrafada / Chefe Climático)

aspectos_diegaticos:
  - "[Mestre da Eletricidade e Primórdio]": Domina arcos elétricos, plasma e tempestades efêmeras.
  - "[Luto Devastador por Joana]": Sua fraqueza emocional oculta é o espírito de sua falecida filha.
  - "[Aura de Relâmpagos Permanentes]": Proteção elétrica passiva de Forças 4 (RD 2 Físico).

bloco_mecanico:
  imposicao_fase1: Diff 7 (Físico) | Diff 8 (Místico) | Diff 6 (Social se invocar Joana)
  pressao_telegrafada: Diff 7 (Resistir a Descargas de Raios em Cadeia)
  impacto_telegrafado: 5 Pontos de Dano Agravado
  relogio_chefe: 7 Caixas de Integridade Arcana
  resistencia_dano: RD 2 (Anula 1 Impacto de TODOS os acertos em Fase 1)
  limiar_efetividade: Limiar Mínimo = 2 (Ações fracas de 1s sofrem Efeito Zero no relógio)

movimentos_telegrafados:
  - "Raios em Cadeia": Dano 5 Agravado em área se não for interrompido.
  - "Sobrecarga de Nódulo": Drena 2 de Quintessência dos magos no recinto.
---
```

---

## 📜 5. Epílogo e Consequências do Arco 01

Com o encerramento do conflito no Santuário de Lizander:
* **Se Lizander for derrotado/redimido:** A distribuição da droga Néctar de Sangue é interrompida, salvando os pacientes do CAPS de Ângela.
* **Se os PJs resgatarem Joana:** O espírito de Joana encontra paz e concede um **Fetiche Espiritual** aos PJs (`[Cristal de Raio Pacificado]`).
* **Conexão com o Próximo Arco:** Os servidores apreendidos e as revelações de Elizabeth Barcelos expõem a conspiração maior da Tecnocracia e da ABIN para o **Arco 02**!
