---
type: regra
summary: "Estudo 4 do Sistema Player-Faced: Taxonomia dos 4 Níveis de Carga Narrativa e mecânica detalhada da Oposição Rápida / Menor."
tags: [srd, design, player-faced, taxonomia, oposicao-rapida, oposicao-menor, regras]
---

# Estudo 04: Taxonomia de Carga Narrativa e Oposição Rápida

Este documento estabelece a **Taxonomia Oficial dos 4 Níveis de Carga Narrativa** do sistema *Player-Faced* para *Mago: A Ascensão 20 Anos* e detalha as regras e análises probabilísticas para o **Nível 2: Oposição Rápida (Oposição Menor)**.

---

## 🏛️ 1. Taxonomia dos 4 Níveis de Carga Narrativa

O Narrador (ST) controla a velocidade e o foco da sessão escolhendo o nível de oposição apropriado para cada obstáculo ou NPC:

```
+-----------------------------------------------------------------------------------------+
|                       TAXONOMIA DE CARGA NARRATIVA DO ST                                |
|                                                                                         |
|  Nível 1: OBSTÁCULO PASSIVO     ==> Tarefas ambientais/técnicas (Arrombar, Pular, Hack)   |
|  Nível 2: OPOSIÇÃO RÁPIDA       ==> Interações sociais/furtivas com NPCs menores          |
|             (ou OPOSIÇÃO MENOR)                                                         |
|  Nível 3: AMEAÇA ATIVA          ==> Combates sérios / Hackers ativos (com Relógios)     |
|  Nível 4: AMEAÇA TELEGRAFADA    ==> Chefes climáticos / Rituais (com Intenções Declaradas)|
+-----------------------------------------------------------------------------------------+
```

---

## ⚡ 2. Funcionamento da Oposição Rápida (Nível 2)

Na **Oposição Rápida**, existe um opositor ativo (guarda de portaria, informante hesitante, motorista em perseguição), mas a cena **não justifica a abertura de Relógios de Vitalidade nem combate turno a turno**.

* **Princípio da Transição Suave:** Para que os jogadores sintam zero impacto mecânico ou choque de transição em relação ao Mago M20 clássico, a escala de Dificuldade permanece centrada na **Dificuldade 6 Padrão do M20**, variando de 5 a 8. Os jogadores rolam suas paradas habituais (Atributo + Habilidade) sem notar que o Narrador deixou de rolar dados.
* **Resolução:** Resolvida em **1 Única Rolagem do Jogador**.
* **Competência do NPC:** Traduzida exclusivamente na **Dificuldade do Dado d10 (Diff 5 a 8)**.

### Tabela de Equivalência de Perícia do NPC:

| Nível de Perícia do NPC | Exemplo de NPC | Parada Equivalente no Livro | Dificuldade para o PJ |
| :---: | :---: | :---: | :---: |
| **Inepto / Fraco** | Porteiro distraído, pedestre comum | 2 a 3 Dados | **Diff 5** |
| **Médio / Padronizado** | Segurança corporativo, inspetor civil | 4 a 5 Dados | **Diff 6 (Padrão)** |
| **Treinado / Agente** | Agente da ABIN, Policial veterano | 6 a 7 Dados | **Diff 7** |
| **Perito / Mestre** | Chefe de Segurança, Especialista da NOM | 8 ou + Dados | **Diff 8** |

---

## 📊 3. Análise Probabilística Comparativa

Simulação comparativa entre a **Rolagem Contestada Clássica M20** (ambos rolam) vs **Oposição Rápida Player-Faced** (apenas o PJ rola em Diff 5-8):

| Parada do PJ | Perfil do NPC | Sucesso Total ($\ge 2s$) | Sucesso Parcial (1s com Custo) | Taxa Total de Sucesso ($\ge 1s$) | Falha Simples / Complicação |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **4 Dados** | Inepto (Diff 5) | **$67,2\%$** | $19,3\%$ | **$86,5\%$** | $13,6\%$ |
| **4 Dados** | Médio (Diff 6) | **$55,3\%$** | $24,8\%$ | **$80,1\%$** | $19,9\%$ |
| **4 Dados** | Treinado (Diff 7) | **$41,9\%$** | $29,6\%$ | **$71,5\%$** | $28,5\%$ |
| **4 Dados** | Perito (Diff 8) | **$27,6\%$** | $32,7\%$ | **$60,3\%$** | $39,7\%$ |

### Insight de Agência e Ritmo:
No Storyteller clássico, rolagens contestadas resultam em empates e falhas mútuas em $60\%$ das vezes. Na **Oposição Rápida Player-Faced**, um personagem competente (4 dados) contra um oponente médio (Diff 6) mantém **$80,1\%$ de taxa de sucesso ativo**, onde os $24,8\%$ de acertos parciais criam **custos e ganchos narrativos imediatos** para a cena avançar sem travar.

---

## 🎬 4. Três Cenários de Aplicação Prática

### Cenário A: Infiltração Social (*Manipulação + Manha*)
* *PJ (Hughie - 5 dados) tenta enganar o Porteiro do Data Center.*
* **Porteiro Inepto (Diff 5):** **$75,9\%$** Sucesso Pleno (Libera sem perguntas), **$14,4\%$** Parcial (Libera, mas anota o nome no registro), **$9,7\%$** Falha.

### Cenário B: Nocaute Furtivo Silencioso (*Destreza + Briga*)
* *PJ (Jhonny D. Lee - 8 dados) tenta nocautear silenciosamente um sentinela.*
* **Sentinela Comum (Diff 6):** **$82,2\%$** Sucesso Pleno (Nocaute limpo), **$10,6\%$** Parcial (Nocauteia, mas derruba a lanterna fazendo barulho).

### Cenário C: Perseguição de Carros (*Condução + Percepção*)
* *PJ (Andrey - 5 dados) tenta despistar uma viatura discreta da ABIN.*
* **Motorista Treinado da ABIN (Diff 7):** **$51,0\%$** Sucesso Pleno (Despista limpo), **$25,4\%$** Parcial (Despista, mas raspa a lateral do veículo em um poste), **$23,6\%$** Falha (A ABIN emparelha o carro).
