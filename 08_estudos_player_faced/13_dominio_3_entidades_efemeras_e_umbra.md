---
type: regra
summary: "Estudo 13 do Sistema Player-Faced: Instanciação completa do Domínio 3 (Entidades Efêmeras e Umbra) nos Níveis 1, 2 e 3, com conversão de espíritos oficiais do M20, matriz dimensional e Princípio da Fluidez."
tags: [srd, design, player-faced, umbra, espiritos, efemera, perdições, banes, pelicula, dimensoes, regras]
---

# Estudo 13: Domínio 3 — Entidades Efêmeras e a Geografia Hostil da Umbra

Este documento estabelece a instanciação prática e o catálogo operacional do **Domínio 3: Entidades Efêmeras e a Geografia da Umbra** sob o **Motor Player-Faced Total** para *Mago: A Ascensão 20 Anos*.

Ameaças umbrais operam através de Corpus, Essência e Encantos (*Charms*). São seres de energia mística imateriais no mundo físico que impõem regras estritas de interação: ataques físicos mundanos causam **Efeito Zero** (imunidade total) sem o uso da Esfera de *Espírito 3*, *Primórdio 2* ou armas e fetiches encantados (`[Ruína Espiritual]`).

---

## 🏛️ 1. O Domínio 3 sob a Ótica Player-Faced

No paradigma *Player-Faced*, entidades efêmeras e barreiras dimensionais operam sob parâmetros calibrados por dimensão:

```
+---------------------------------------------------------------------------------------------------------+
|                               OS 3 NÍVEIS DE ENTIDADES EFÊMERAS E DA UMBRA                              |
|                                                                                                         |
|  [ Nível 1: Desafio Rápido ]   ==> Fator único de OPOSIÇÃO na dimensão relevante (com Meta de Sucessos).|
|  [ Nível 2: Ameaça Ativa ]     ==> Ficha focada na dimensão mística primária (com tabus e brechas).    |
|  [ Nível 3: Alto Impacto ]     ==> Matriz completa das 4 Dimensões + Evento Telegrafado de Crise.       |
+---------------------------------------------------------------------------------------------------------+
```

---

## 🔄 2. O Princípio da Fluidez da Entidade: A Mesma Ameaça nos 3 Níveis

O nível define a escala dramática da interação na cena. Cada entidade umbral de grande porte possui uma matriz dimensional completa e responde em qualquer nível:

### Estudo de Caso: *Jaggling da Tempestade (Elementar de Raios e Ozônio)*

```yaml
---
ameaca: Jaggling da Tempestade (Elementar de Raios)
nivel_padrao: Nível 2 / 3 (Entidade Mística de Alta Potência)

matriz_dimensional:
  dimensao_mistica:      [Oposição: 7] [Ameaça: 6] [Consequência: 4 Agravado (Descarga Efêmera)] [Relógio: 10 Caixas (Limiar 2)]
  dimensao_fisica:       [Efeito Zero sem Espírito/Fetiche] | Se Materializado: [Oposição: 7] [Ameaça: 6] [Consequência: 4 Letal] [Relógio: 7 Caixas (Limiar 2)]
  dimensao_mental:       [Oposição: 6] [Ameaça: 5] [Consequência: -2 Força de Vontade (Sobrecarga Neural)] [Relógio: 5 Caixas]
  dimensao_social:       [Oposição: 7] [Ameaça: 4] [Consequência: Gatilho Fúria Tempestuosa] [Relógio: 4 Caixas (Oferenda de Quintessência)]
---
```

* **Como Nível 1 (Desafio Rápido / Interação Pontual):**
  * *Cenário:* Travessia da Penumbra sem perturbar o elemental ou realização de oferenda rápida de Quintessência.
  * *Parâmetros da Oposição:* **Oposição Social/Ritual: 7** | **Meta: 2 Sucessos**.
* **Como Nível 2 (Ameaça Ativa / Duelo Espiritual):**
  * *Cenário:* Confronto direto na Penumbra com rajadas de relâmpagos efêmeros.
  * *Parâmetros da Oposição (Dimensão Mística):* `[Oposição: 7]` `[Ameaça: 6]` `[Consequência: 4 Agravado]` `[Relógio: 10 Caixas (Limiar 2)]`. Iniciativa: $1d10 + 5$.
* **Como Nível 3 (Evento de Alto Impacto / Crise Telegrafada):**
  * *Cenário:* O Jaggling se ancora ao transformador central e inicia a *Sobrecarga de Tempestade Penumbral*.
  * *Parâmetros da Oposição:* Crise telegrafada com **Ameaça Mística 6** (Descargas em Área), **Oposição Mística 7** (Dissipar Vórtice) e **Relógio de Crise de 10 Caixas (Limiar 2)**.

---

## 🎯 3. Nível 1: Desafios Rápidos (Gafflings e Travessia da Película)

O obstáculo opera em uma única dimensão com fator de Oposição e Meta de Sucessos:

### Catálogo de Oposições de Nível 1:
1. **Gaffling de Poeira / Sentinela Espiritual:** Oposição Mística 5 / Furtividade 5 | Meta: 1 Sucesso. *(Espírito Oficial M20)*
2. **Romper a Película Urbana (Gauntlet 7):** Oposição Mística 7 | Meta: 2 Sucessos. *(Regra Oficial M20)*
3. **Rastrear Trilha de Ressonância na Penumbra:** Oposição Mística 6 / Percepção 6 | Meta: 2 Sucessos.
4. **Pequena Perdição de Ódio (Bane Menor):** Oposição Mística 6 / Social 6 | Meta: 2 Sucessos. *(Espírito Oficial M20)*
5. **Romper a Película em Laboratório Tecnocrata Rígido (Gauntlet 8):** Oposição Mística 8 | Meta: 3 Sucessos. *(Regra Oficial M20)*

---

## ⚔️ 4. Nível 2: Ameaças Ativas (Fichas Sintéticas Simétricas)

Entidades de Nível 2 operam com foco em sua dimensão mística primária, apresentando tabus e brechas claras em dimensões secundárias.

---

### Tabela de Perfis de Espíritos (Origem Oficial M20)

| Espírito Oficial | Origem no Livro | Dimensão Primária (Opo / Ame / Cons / Rel) | Dimensão Secundária / Brecha Tática | Bônus Inic. |
| :--- | :--- | :--- | :--- | :---: |
| **Gaffling de Combate** | *(Espírito Oficial M20)* | **Mística:** `[Opo 5]` `[Ame 5]` `[Cons 2]` `[Rel 3]` | **Social (Domar):** `[Opo 4]` `[Ame 3]` `[Rel 2]` | $+2$ |
| **Jaggling da Tempestade** | *(Espírito Oficial M20)* | **Mística:** `[Opo 7]` `[Ame 6]` `[Cons 4 Agr]` `[Rel 5]` | **Física/Aterramento de Cobre:** `[Opo 5]` `[Rel 3]` | $+5$ |
| **Perdição de Sangue (Bane)** | *(Espírito Oficial M20)* | **Mística:** `[Opo 7]` `[Ame 7]` `[Cons 3 Agr]` `[Rel 5]` | **Fogo/Purificação:** Dano Dobrado no Relógio | $+6$ |
| **Aranha da Teia Digital** | *(Espírito Oficial M20)* | **Mental/Digital:** `[Opo 7]` `[Ame 6]` `[Cons 3 Dreno]` `[Rel 4]` | **PEM / Corte de Fibra:** `[Ame 4]` `[Rel 2]` | $+5$ |
| **Espírito de Concreto** | *(Espírito Oficial M20)* | **Mística/Física:** `[Opo 8]` `[Ame 6]` `[Cons 4]` `[Rel 6]` | **Entropia/Matéria:** Ignora blindagem | $+6$ |
| **A Própria Película Ativa** | *(Mecânica Oficial M20)* | **Mística:** `[Opo 8]` `[Ame 6]` `[Cons 2 Paradoxo]` `[Rel 4]` | **Ponto Focal / Nodo:** `[Opo 6]` `[Rel 2]` | $+6$ |

---

## 🌪️ 5. Nível 3: Eventos de Alto Impacto e Lordes Umbrais (4 Dimensões)

Grandes entidades, Incarnas e fenômenos cósmicos da Umbra possuem a **matriz completa das 4 dimensões** para representar seu impacto em todas as esferas da realidade.

---

### Catálogo de Entidades e Crises de Nível 3

#### 1. Lorde de Paradoxo: "O Julgamento da Teia de Paradoxo" *(Oficial M20)*
* **Matriz Dimensional:**
  * **Dimensão Mística (Agulhas Temporais e Fios de Paradoxo):** `[Oposição: 8]` `[Ameaça: 8]` `[Consequência: 5 Agravado (Banimento para Reino de Paradoxo)]` `[Relógio: 7]`
  * **Dimensão Mental (Imposição de Estase Lógica):** `[Oposição: 8]` `[Ameaça: 7]` `[Consequência: 3 (Paralisia Mental)]` `[Relógio: 5]`
  * **Dimensão Física (Corpo Incorpóreo Imaterial):** Imune a ataques mundanos (Efeito Zero).
  * **Dimensão Social (Pacto de Absolvição / Redenção Arcana):** `[Oposição: 8]` `[Ameaça: 6]` `[Relógio: 4 (Oferenda de Quintessência/Vontade)]`
* **Diegese da Telegrafia:** *"A Penumbra racha e uma figura imensa de fios prateados e agulhas de relógio desce. As agulhas giram no sentido anti-horário e o tempo congela. Em 10 segundos, as agulhas perfurarão o peito do alvo, banindo corpo e alma para um Reino de Paradoxo isolado."*
* **Mecânica Oculta da Crise:** Relógio de Crise de 7 Caixas (Limiar Mínimo: 2 Sucessos).

#### 2. Grande Perdição Tóxica: "A Erupção de Miasma Penumbral" *(Oficial M20)*
* **Matriz Dimensional:**
  * **Dimensão Mística (Miasma Corruptor de Essência):** `[Oposição: 7]` `[Ameaça: 8]` `[Consequência: 5 Agravado (Corrupção de Padrão)]` `[Relógio: 6]`
  * **Dimensão Física (Lodo Ácido Materializado):** `[Oposição: 7]` `[Ameaça: 7]` `[Consequência: 4 Agravado]` `[Relógio: 6]`
  * **Dimensão Mental (Aura de Terror e Loucura):** `[Oposição: 7]` `[Ameaça: 6]` `[Consequência: 3 (Estresse/Fobia)]` `[Relógio: 4]`
  * **Dimensão Social:** Imune (Efeito Zero para diplomacia; apenas exorcismo puro).
* **Diegese da Telegrafia:** *"O chão do esgoto borbulha em lodo negro e um tumor de carne pútrida e olhos múltiplos emerge. Bolsas de gás sulfúrico inflam no dorso. No fim do turno, o monstro vomitará uma torrente de lodo ácido espiritual que dissolverá padrões biológicos e espirituais em 30 metros."*
* **Mecânica Oculta da Crise:** Relógio de Crise de 6 Caixas.

#### 3. Tempestade de Avatar: "O Rompimento e Estilhaços de Essência" *(Oficial M20)*
* **Matriz Dimensional:**
  * **Dimensão Mística (Cacos Cósmicos de Avatar):** `[Oposição: 8]` `[Ameaça: 8]` `[Consequência: 4 Agravado (Cicatriz no Avatar / Perda de Quintessência)]` `[Relógio: 6]`
  * **Dimensão Física (Turbulência Gravitacional):** `[Oposição: 7]` `[Ameaça: 7]` `[Consequência: 3 Letal]` `[Relógio: 5]`
  * **Dimensão Mental (Eco de Gritos de Almas Rompidas):** `[Oposição: 7]` `[Ameaça: 6]` `[Consequência: 2 (Trauma)]` `[Relógio: 4]`
  * **Dimensão Social:** Não aplicável (Fenômeno Cósmico).
* **Diegese da Telegrafia:** *"Um trovão sem som estala na Película danificada. Uma tempestade de cacos brilhantes de vidro místico e fragmentos de Avatares começa a girar em um tornado violento. No próximo instante, a ventania cortará os laços da alma de quem estiver na travessia."*
* **Mecânica Oculta da Crise:** Relógio de Crise de 6 Caixas.
