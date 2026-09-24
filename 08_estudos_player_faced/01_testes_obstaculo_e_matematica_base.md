---
type: regra
summary: "Estudo 1 do Sistema Player-Faced: Regras para rolagens de obstáculo/ambiente e análise probabilística trinomial para Mago M20."
tags: [srd, design, player-faced, probabilidade, d10, regras, obstaculos]
---

# Estudo 01: Rolagens de Obstáculo e Matemática Base (Player-Faced M20)

Este documento estabelece a base mecânica e probabilística para o modelo **100% Player-Faced** aplicado a *Mago: A Ascensão 20 Anos*. Neste sistema, **apenas os jogadores rolam dados**; o Narrador (Storyteller) gerencia a ficção, os perigos e as consequências.

---

## 🎲 1. O Princípio da Resolução em 4 Faixas

Toda ação de superar um obstáculo estático, perigo ambiental, intrusão digital ou teste de atributo é resolvida em uma única rolagem do jogador com a seguinte interpretação de resultados:

* **$\ge 2$ Sucessos Líquidos:** **Sucesso Pleno / Sólido** — O objetivo é cumprido com segurança e qualidade compatíveis com os graus de sucesso de M20.
* **1 Sucesso Líquido:** **Sucesso Marginal que Move a Ficção** — O objetivo é alcançado no nível mínimo suficiente para a história continuar. O Storyteller pode qualificar o resultado conforme a situação — efeito reduzido, exposição, atraso, posição pior, informação incompleta ou outro custo ficcional — mas a complicação **não é obrigatória nem constitui uma nova faixa mecânica importada de PbtA**. O ponto central é preservar a regra de M20 de que 1 sucesso continua sendo sucesso.
* **0 Sucessos Líquidos (sem 1s desacompanhados):** **Falha Simples** — O objetivo não é alcançado; o Storyteller descreve a consequência apropriada segundo a ficção.
* **$< 0$ Sucessos Líquidos (com 1s):** **Falha Crítica (Botch)** — Desastre, dano severo, revelação imediata ou acúmulo de Paradoxo, conforme as regras e a situação em M20.

---

## 📊 2. Análise Probabilística Exata (Dificuldade Padrão 6)

Simulação trinomial exata considerando a regra clássica de Storyteller (dados de valor $1$ anulam sucessos):

| Parada de Dados ($N$) | Perfil do Personagem | Falha Crítica (Botch) | Falha Simples | Sucesso Marginal (1 Sucesso) | Sucesso Total ($\ge 2$ Sucessos) | Taxa Total de Sucesso ($\ge 1$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **2 Dados** | Inexperiente / Penalizado | $9,0\%$ | $26,1\%$ | **$40,0\%$** | $24,9\%$ | $64,9\%$ |
| **3 Dados** | Mediano / Treinado | $6,1\%$ | $20,0\%$ | **$31,6\%$** | $42,4\%$ | $73,9\%$ |
| **4 Dados** | Profissional Competente | $3,7\%$ | $16,3\%$ | **$24,8\%$** | **$55,3\%$** | $80,1\%$ |
| **5 Dados** | Especialista | $2,1\%$ | $13,5\%$ | **$19,7\%$** | **$64,8\%$** | $84,5\%$ |
| **6 Dados** | Mestre / Referência | $1,2\%$ | $11,1\%$ | **$15,7\%$** | **$72,0\%$** | $87,8\%$ |

---

## 📈 3. Efeito dos Modificadores de Dificuldade ($D$)

Para uma parada típica de 4 Dados (Atributo 3 + Habilidade 1):

| Dificuldade ($D$) | Conceito | Falha Crítica | Falha Simples | Sucesso Marginal (1s) | Sucesso Total ($\ge 2s$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Diff 5** | Favorável / Fácil | $1,7\%$ | $11,8\%$ | $19,5\%$ | **$67,0\%$** |
| **Diff 6** | Padrão | $3,7\%$ | $16,3\%$ | $24,8\%$ | **$55,3\%$** |
| **Diff 7** | Exigente / Adverso | $6,7\%$ | $21,8\%$ | **$29,6\%$** | $41,9\%$ |
| **Diff 8** | Extremamente Difícil | $12,5\%$ | $28,0\%$ | **$31,2\%$** | $28,3\%$ |

* **Insight de Design:** Aumentar a dificuldade de 6 para 7 reduz a frequência de resultados sólidos e aumenta a proporção de resultados marginais. Como **1 sucesso continua sendo sucesso em M20**, essa faixa é especialmente importante para manter a ficção em movimento: o personagem consegue o mínimo necessário, e o Storyteller interpreta a qualidade concreta desse êxito segundo a situação.

---

## 🎯 4. A Separação Fundamental: Escala do Objetivo vs. Condições Ambientais

Para manter a arbitragem Player-Faced rápida e consistente, o Narrador divide qualquer teste de obstáculo em **duas variáveis independentes**:

1. **Quantidade de Sucessos Requeridos (Limiar / Relógio):** Define a **COMPLEXIDADE E ESCALA DO OBJETIVO**.
   - **2 Sucessos (Padrão):** Superar um obstáculo rotineiro ou invadir um sistema individual (ex: PC comum de escritório).
   - **4 a 6 Sucessos Acumulados (Relógio de Progresso):** Superar uma infraestrutura militar ou invadir a rede central da NOM / Apple.

2. **Dificuldade do Dado d10 (Diff 4 a 9):** Define as **CONDIÇÕES E ESTRESSE DO AMBIENTE**.
   - **Dificuldade 6 (Padrão):** Ambiente controlado, ferramentas adequadas.
   - **Dificuldade 8 (+2 Diff / Péssimas Condições):** Tentativa realizada no meio de um tiroteio, com um celular de tela quebrada sob fuga de carro.
   - **Dificuldade 4 (-2 Diff / Excelentes Condições):** Tentativa realizada dentro de um Santuário/Nódulo místico, com terminal dedicado e auxílio de *Correspondência 2*.

