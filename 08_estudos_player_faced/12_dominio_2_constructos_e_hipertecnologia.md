---
type: regra
summary: "Estudo 12 do Sistema Player-Faced: Instanciação completa do Domínio 2 (Constructos e Hipertecnologia) nos Níveis 1, 2 e 3, com conversão de perfis oficiais do M20, matriz dimensional e Princípio da Fluidez."
tags: [srd, design, player-faced, constructos, hit-marks, hipertecnologia, automatos, dimensoes, regras]
---

# Estudo 12: Domínio 2 — Constructos, Autômatos e Hipertecnologia

Este documento estabelece a instanciação prática e o catálogo operacional do **Domínio 2: Constructos e Hipertecnologia Autônoma** sob o **Motor Player-Faced Total** para *Mago: A Ascensão 20 Anos*.

Constructos são ameaças artificiais, mecânicas ou biológicas desprovidas de psicologia convencional. Operam por diretrizes lógicas implacáveis, possuem blindagem material densa e são naturalmente imunes a abordagens sociais convencionais (**Efeito Zero** na Dimensão Social, exceto para comandos de voz com credenciais mestras ou reprogramação lógica).

---

## 🏛️ 1. O Domínio 2 sob a Ótica Player-Faced

No paradigma *Player-Faced*, constructos e sistemas de segurança operam sob parâmetros calibrados por dimensão:

```
+---------------------------------------------------------------------------------------------------------+
|                               OS 3 NÍVEIS DE CONSTRUCTOS E HIPERTECNOLOGIA                              |
|                                                                                                         |
|  [ Nível 1: Desafio Rápido ]   ==> Fator único de OPOSIÇÃO na dimensão relevante (com Meta de Sucessos).|
|  [ Nível 2: Ameaça Ativa ]     ==> Ficha focada na dimensão primária de combate (com brechas técnicas). |
|  [ Nível 3: Alto Impacto ]     ==> Matriz completa das 4 Dimensões + Evento Telegrafado de Crise.       |
+---------------------------------------------------------------------------------------------------------+
```

---

## 🔄 2. O Princípio da Fluidez do Constructo: A Mesma Ameaça nos 3 Níveis

O nível define a escala dramática da interação na cena. Cada constructo de elite possui uma matriz dimensional completa e responde em qualquer nível:

### Estudo de Caso: *Hit-Mark Série V (Androide de Extermínio da Iteração X)*

```yaml
---
ameaca: Hit-Mark Série V (Iteração X)
nivel_padrao: Nível 2 / 3 (Constructo Pesado de Combate)

matriz_dimensional:
  dimensao_fisica:       [Oposição: 8] [Ameaça: 8] [Consequência: 4 Letal/Agravado (Plasma)] [Relógio: 6]
  dimensao_mental:       [Oposição: 6] [Ameaça: 6] [Consequência: 2 (Sobrecarga de Sensores)] [Relógio: 3]
  dimensao_mistica:      [Oposição: 6] [Ameaça: 5] [Consequência: 2 (Dreno de Quintessência)] [Relógio: 3]
  dimensao_social:       [Efeito Zero] (Imune a manipulação emocional; Oposição 8 para Protocolo de Voz)
---
```

* **Como Nível 1 (Desafio Rápido / Interação Pontual):**
  * *Cenário:* Hit-Mark em modo de recarga/sentinela; passagem furtiva ou corte de alimentação.
  * *Parâmetros da Oposição:* **Oposição Física: 8** (Sensores Termais) ou **Mental: 6** (Bypass) | **Meta: 2 Sucessos**.
* **Como Nível 2 (Ameaça Ativa / Duelo Tático):**
  * *Cenário:* Combate aberto no pátio com canhão de plasma acionado.
  * *Parâmetros da Oposição (Dimensão Física):* `[Oposição: 8]` `[Ameaça: 8]` `[Consequência: 4 Letal/Agravado]` `[Relógio: 6]`. Iniciativa: $1d10 + 8$.
* **Como Nível 3 (Evento de Alto Impacto / Crise Telegrafada):**
  * *Cenário:* Hit-Mark danificado trava sapatas e inicia a sobrecarga do canhão de antimatéria.
  * *Parâmetros da Oposição:* Sobrecarga telegrafada com **Ameaça Física 8** (Plasma de Área), **Oposição Mental 6** (Sobrecarga de Circuitos) e **Relógio de Crise de 6 Caixas**.

---

## 🎯 3. Nível 1: Desafios Rápidos (Sistemas e Drones Menores)

O obstáculo opera em uma única dimensão com fator de Oposição e Meta de Sucessos:

### Catálogo de Oposições de Nível 1:
1. **Drone de Vigilância Aérea da NOM:** Oposição Física 6 (Sensores) / Mental 5 | Meta: 2 Sucessos. *(Constructo Oficial M20)*
2. **Scanner Biométrico e Quântico de Entrada:** Oposição Mental 7 / Mística 6 | Meta: 3 Sucessos. *(Constructo Oficial M20)*
3. **Cão Cibernético de Patrulha (Iteração X):** Oposição Física 6 / Mental 5 | Meta: 2 Sucessos. *(Constructo Oficial M20)*
4. **Fechadura Rúnica Hermética em Portão de Ferro:** Oposição Mística 6 / Física 7 | Meta: 2 Sucessos.

---

## ⚔️ 4. Nível 2: Ameaças Ativas (Fichas Sintéticas Simétricas)

Constructos de Nível 2 operam com foco em sua dimensão física primária, apresentando brechas técnicas claras em dimensões secundárias.

---

### Tabela de Perfis de Constructos (Origem Oficial M20)

| Constructo Oficial | Origem no Livro | Dimensão Primária (Opo / Ame / Cons / Rel) | Dimensão Secundária / Brecha Tática | Bônus Inic. |
| :--- | :--- | :--- | :--- | :---: |
| **Hit-Mark Série V** | *(Oficial M20)* | **Física:** `[Opo 8]` `[Ame 8]` `[Cons 4 Agr]` `[Rel 6]` | **Mental/Entrópica:** `[Opo 6]` `[Ame 6]` `[Rel 3]` | $+8$ |
| **Golem de Pedra Hermético** | *(Oficial M20)* | **Física:** `[Opo 8]` `[Ame 6]` `[Cons 4]` `[Rel 7]` | **Mística (Padrão/Selo):** `[Opo 6]` `[Ame 5]` `[Rel 3]` | $+6$ |
| **Aberração Quimérica** | *(Oficial M20)* | **Física:** `[Opo 7]` `[Ame 8]` `[Cons 3 Agr]` `[Rel 5]` | **Fisiológica/Fogo:** `[Opo 5]` `[Ame 5]` `[Rel 3]` | $+7$ |
| **Torreta Panóptica Fixa** | *(Oficial M20)* | **Física:** `[Opo 7]` `[Ame 8]` `[Cons 4 Letal]` `[Rel 4]`| **Digital/Furtiva:** `[Opo 5]` `[Ame 5]` `[Rel 2]` | $+7$ |

---

## 🌪️ 5. Nível 3: Eventos de Alto Impacto e Hipertecnologia (4 Dimensões)

Constructos e instalações de Nível 3 possuem a **matriz completa das 4 dimensões** para gerenciar crises multifacetadas.

---

### Catálogo de Constructos e Crises de Nível 3

#### 1. Hit-Mark Série X: "Protocolo de Varredura e Canhão de Antimatéria" *(Oficial M20)*
* **Matriz Dimensional:**
  * **Dimensão Física (Chassi Pesado e Canhão Antimatéria):** `[Oposição: 8]` `[Ameaça: 8]` `[Consequência: 6 Agravado (Desintegração)]` `[Relógio: 7]`
  * **Dimensão Mental (IA Tática e Firewalls):** `[Oposição: 8]` `[Ameaça: 7]` `[Consequência: 3 (Bloqueio de Dados)]` `[Relógio: 5]`
  * **Dimensão Mística (Campos de Força Tecnocráticos):** `[Oposição: 7]` `[Ameaça: 6]` `[Consequência: 3 Paradoxo]` `[Relógio: 4]`
  * **Dimensão Social (Protocolo de Autorização de Nível Alfa):** `[Oposição: 8]` `[Ameaça: 4]` `[Relógio: 3]` *(Exige código mestre)*
* **Diegese da Telegrafia:** *"O Hit-Mark racha a blindagem do peito expondo o reator de fusão a hélio líquido. O ar distorce em azul brilhante e as travas magnéticas se cravam no piso. Em segundos, uma rajada de antimatéria e plasma pesado vaporizará uma linha reta de 50 metros."*
* **Mecânica Oculta da Crise:** Relógio de Crise de 7 Caixas (Limiar Mínimo: 2 Sucessos).

#### 2. Titã Bioquímico: "Ruptura Celular e Nuvem Necrosante" *(Oficial M20)*
* **Matriz Dimensional:**
  * **Dimensão Física (Massa Muscular e Bílis Ácida):** `[Oposição: 7]` `[Ameaça: 8]` `[Consequência: 5 Agravado (Ácido)]` `[Relógio: 6]`
  * **Dimensão Mística (Corrupção de Padrão Biológico):** `[Oposição: 7]` `[Ameaça: 7]` `[Consequência: 4 Agravado]` `[Relógio: 5]`
  * **Dimensão Mental (Instinto Primitivo):** `[Oposição: 5]` `[Ameaça: 4]` `[Consequência: 1]` `[Relógio: 3]`
  * **Dimensão Social:** Imune (Efeito Zero).
* **Diegese da Telegrafia:** *"A carcaça da monstruosidade incha com veias roxas fluorescentes e vapor corrosivo derretendo o piso. O coração mutante entra em taquicardia terminal. No final do turno, o monstro explodirá em uma névoa viral que dissolve tecidos celulares."*
* **Mecânica Oculta da Crise:** Relógio de Crise de 6 Caixas.

#### 3. Lockdown Panóptico: "Purga Molecular da Instalação" *(Oficial M20)*
* **Matriz Dimensional:**
  * **Dimensão Mental (Mainframe de Contenção e IA Central):** `[Oposição: 8]` `[Ameaça: 7]` `[Consequência: 4 (Bloqueio Total)]` `[Relógio: 6]`
  * **Dimensão Física (Comportas de Chumbo e Gás Ionizado):** `[Oposição: 8]` `[Ameaça: 7]` `[Consequência: 4 Agravado (Calor)]` `[Relógio: 6]`
  * **Dimensão Mística (Barreira de Estática Tecnocrática):** `[Oposição: 7]` `[Ameaça: 6]` `[Consequência: 3 Paradoxo]` `[Relógio: 5]`
  * **Dimensão Social (Comandos de Voz da Diretoria):** `[Oposição: 8]` `[Ameaça: 5]` `[Relógio: 3]`
* **Diegese da Telegrafia:** *"Paredes de chumbo descem selando as saídas e bicos no teto liberam gás ionizado. A contagem regressiva nos monitores marca 10 segundos para a despressurização e purgação termal total da instalação."*
* **Mecânica Oculta da Crise:** Relógio de Crise de 6 Caixas.
