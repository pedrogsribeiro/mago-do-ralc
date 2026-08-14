---
type: regra
summary: "Estudo 11 do Sistema Player-Faced: Instanciação completa do Domínio 1 (Antagonistas Conscientes) nos Níveis 1, 2 e 3, com conversão 1:1 de perfis de NPCs oficiais, assimetria dimensional e o Princípio da Fluidez."
tags: [srd, design, player-faced, antagonistas, faccoes, tecnocracia, nefandi, conversao-1-1, dimensoes, regras]
---

# Estudo 11: Domínio 1 — Antagonistas Conscientes e Facções

Este documento estabelece a instanciação prática e o catálogo operacional do **Domínio 1: Antagonistas Conscientes** sob o **Motor Player-Faced Total** para *Mago: A Ascensão 20 Anos*.

Antagonistas conscientes são indivíduos e grupos dotados de agência, inteligência, motivações ideológicas e capacidade de agir em múltiplas dimensões (Física, Social, Mental e Mística).

---

## 🏛️ 1. O Domínio 1 sob a Ótica Player-Faced

No paradigma *Player-Faced*, os antagonistas são sintetizados em blocos de parâmetros que expressam sua oposição ao mundo:

```
+---------------------------------------------------------------------------------------------------------+
|                               OS 3 NÍVEIS DE ANTAGONISTAS CONSCIENTES                                   |
|                                                                                                         |
|  [ Nível 1: Desafio Rápido ]   ==> Fator único de OPOSIÇÃO na dimensão relevante (com Meta de Sucessos).|
|  [ Nível 2: Ameaça Ativa ]     ==> Ficha focada na dimensão primária de conflito (com brechas táticas). |
|  [ Nível 3: Alto Impacto ]     ==> Matriz completa das 4 Dimensões + Evento Telegrafado de Crise.       |
+---------------------------------------------------------------------------------------------------------+
```

---

## 🔄 2. O Princípio da Fluidez do NPC: A Mesma Ameaça nos 3 Níveis

O nível define a escala dramática da interação na cena. Cada antagonista de elite possui uma matriz dimensional completa e responde em qualquer nível:

### Estudo de Caso: *Diretor Regional da NOM — Dr. Alistair Vance*

```yaml
---
ameaca: Dr. Alistair Vance (Diretor Regional da NOM)
nivel_padrao: Nível 3 (Antagonista de Elite / Crise)

matriz_dimensional:
  dimensao_social:       [Oposição: 8] [Ameaça: 7] [Consequência: 4 (Dano Social/Status)] [Relógio: 6]
  dimensao_mental:       [Oposição: 8] [Ameaça: 6] [Consequência: 3 (Exposição de Dados)]  [Relógio: 4]
  dimensao_fisica:       [Oposição: 6] [Ameaça: 5] [Consequência: 2 (Pistola Leve)]       [Relógio: 3]
  dimensao_mistica:      [Oposição: 5] [Ameaça: 4] [Consequência: 2 (Dreno Tecnológico)]  [Relógio: 3]
---
```

* **Como Nível 1 (Desafio Rápido / Interação Pontual):**
  * *Cenário:* Infiltração em evento social para clonar credenciais de Vance sem ser notado.
  * *Parâmetros da Oposição:* **Oposição Social: 8** | **Meta: 2 Sucessos**.
* **Como Nível 2 (Ameaça Ativa / Duelo Tático):**
  * *Cenário:* Interrogatório psicológico fechado conduzido diretamente por Vance.
  * *Parâmetros da Oposição (Dimensão Social):* `[Oposição: 8]` `[Ameaça: 7]` `[Consequência: 4]` `[Relógio: 6]`. Iniciativa: $1d10 + 7$.
* **Como Nível 3 (Evento de Alto Impacto / Crise Telegrafada):**
  * *Cenário:* Vance aciona o *Protocolo de Apagão Panóptico*, iniciando a purga de dados e bloqueio de bens em 30 segundos.
  * *Parâmetros da Oposição:* Todas as 4 dimensões ativas na crise, com **Ameaça Social 7** e **Oposição Mental 8** ancorando o Triângulo Tático.

---

## 🎯 3. Nível 1: Desafios Rápidos (Capangas e Atritos Menores)

O obstáculo opera em uma única dimensão com fator de Oposição e Meta de Sucessos:

### Catálogo de Oposições de Nível 1:
1. **Segurança Terceirizado de Portaria:** Oposição Física 6 / Social 5 | Meta: 2 Sucessos. *(NPC Oficial M20)*
2. **Recepcionista de Hospital/Cartório:** Oposição Social 6 / Burocrática 6 | Meta: 2 Sucessos.
3. **Policial Militar em Blitz:** Oposição Social 7 / Percepção 6 | Meta: 2 Sucessos. *(NPC Oficial M20)*
4. **Informante de Beco Assustado:** Oposição Social 5 | Meta: 1 Sucesso. *(NPC Oficial M20)*
5. **Terminal Local da NOM (Criptografia Leve):** Oposição Mental 7 | Meta: 4 Sucessos.

---

## ⚔️ 4. Nível 2: Ameaças Ativas e Conversão 1:1 de NPCs do Livro M20

Antagonistas de Nível 2 operam primariamente em sua dimensão principal de combate, apresentando brechas claras em dimensões secundárias quando houver assimetria.

---

### Tabela de Perfis de NPCs (Origem Oficial M20)

| Arquétipo de NPC | Origem no Livro | Dimensão Primária (Opo / Ame / Cons / Rel) | Dimensão Secundária / Brecha Tática | Bônus Inic. |
| :--- | :--- | :--- | :--- | :---: |
| **Capanga / Mafioso Mortal** | *(NPC Oficial M20)* | **Física:** `[Opo 6]` `[Ame 5]` `[Cons 2]` `[Rel 3]` | **Social:** `[Opo 4]` `[Ame 4]` `[Rel 2]` | $+3$ |
| **Policial / Detetive Civil** | *(NPC Oficial M20)* | **Física:** `[Opo 6]` `[Ame 6]` `[Cons 3]` `[Rel 3]` | **Mental:** `[Opo 6]` `[Ame 5]` `[Rel 3]` | $+4$ |
| **Agente Tático SWAT / BOPE** | *(NPC Oficial M20)* | **Física:** `[Opo 7]` `[Ame 7]` `[Cons 3]` `[Rel 4]` | **Mística:** `[Opo 4]` `[Ame 4]` `[Rel 2]` | $+6$ |
| **Agente de Campo / MIB (NOM)** | *(NPC Oficial M20)* | **Física:** `[Opo 7]` `[Ame 7]` `[Cons 3]` `[Rel 4]` | **Social:** `[Opo 7]` `[Ame 6]` `[Rel 4]` | $+6$ |
| **Soldado Cibernético (Iteração X)**| *(NPC Oficial M20)* | **Física:** `[Opo 8]` `[Ame 8]` `[Cons 4 Agr]` `[Rel 6]`| **Social/Enganação:** `[Opo 4]` `[Ame 4]` `[Rel 2]` | $+8$ |
| **Geneticista (Progenitores)** | *(NPC Oficial M20)* | **Mental/Bio:** `[Opo 8]` `[Ame 7 Toxina]` `[Cons 3 Agr]` `[Rel 3]` | **Física (Corpo a Corpo):** `[Opo 5]` `[Ame 5]` `[Rel 3]` | $+5$ |
| **Liquidatário (Sindicato)** | *(NPC Oficial M20)* | **Social:** `[Opo 8]` `[Ame 7]` `[Cons 3 Social]` `[Rel 4]` | **Física:** `[Opo 5]` `[Ame 5]` `[Rel 3]` | $+7$ |
| **Explorador (Engenheiros do Vazio)**| *(NPC Oficial M20)* | **Física:** `[Opo 7]` `[Ame 7]` `[Cons 3]` `[Rel 4]` | **Mental/Umbral:** `[Opo 7]` `[Ame 6]` `[Rel 4]` | $+6$ |
| **Acólito Nefandi / Cultista** | *(NPC Oficial M20)* | **Mística:** `[Opo 7]` `[Ame 7]` `[Cons 3 Agr]` `[Rel 4]` | **Física:** `[Opo 6]` `[Ame 5]` `[Rel 3]` | $+5$ |
| **Desaurido (Marauder)** | *(NPC Oficial M20)* | **Mística:** `[Opo 7]` `[Ame 7]` `[Cons 4]` `[Rel 5]` | **Mental (Caos):** `[Opo 8]` `[Ame 7]` `[Rel 4]` | $+6$ |
| **Mestre Hermético Antagonista** | *(NPC Oficial M20)* | **Mística:** `[Opo 8]` `[Ame 7]` `[Cons 4 Agr]` `[Rel 5]` | **Física (Desarmado):** `[Opo 5]` `[Ame 5]` `[Rel 3]` | $+7$ |

---

## 🌪️ 5. Nível 3: Eventos de Alto Impacto e Mestres Antagonistas (4 Dimensões)

Grandes antagonistas e eventos climáticos apresentam a **matriz completa das 4 dimensões**, permitindo interações táticas em qualquer frente durante a crise.

---

### Catálogo de Mestres e Crises de Nível 3

#### 1. Diretor Regional da NOM: "O Apagão Panóptico e a Purga de Identidade" *(NPC Oficial M20)*
* **Matriz Dimensional:**
  * **Dimensão Social (Autoridade Institucional):** `[Oposição: 8]` `[Ameaça: 7]` `[Consequência: 4 (Perda de Identidade/Bens)]` `[Relógio: 6]`
  * **Dimensão Mental (Mainframe e Criptografia):** `[Oposição: 8]` `[Ameaça: 6]` `[Consequência: 3 (Rastreamento Global)]` `[Relógio: 5]`
  * **Dimensão Física (Guarda-Costas Blindados):** `[Oposição: 7]` `[Ameaça: 7]` `[Consequência: 3 Letal]` `[Relógio: 4]`
  * **Dimensão Mística (Contramedidas Estáticas):** `[Oposição: 6]` `[Ameaça: 5]` `[Consequência: 2 Paradoxo]` `[Relógio: 3]`
* **Diegese da Telegrafia:** *"O Diretor digita um código no console mestre. As câmeras de toda a avenida começam a girar em direção ao grupo. No telão do prédio, rostos e nomes civis aparecem classificados como 'Terroristas Biológicos'. Em 30 segundos, a ordem de execução sumária e a deleção de todas as identidades civis será concluída mundialmente."*
* **Mecânica Oculta da Crise:** Relógio de Crise de 6 Caixas (resolvido pelas opções do Triângulo Tático).

#### 2. Mestre Nefandi: "A Inversão do Avatar e Ruptura de Qlippoth" *(NPC Oficial M20)*
* **Matriz Dimensional:**
  * **Dimensão Mística (Feitiçaria Qlippótica):** `[Oposição: 8]` `[Ameaça: 8]` `[Consequência: 5 Agravado (Corrupção de Avatar)]` `[Relógio: 6]`
  * **Dimensão Mental (Guerra Psicológica e Loucura):** `[Oposição: 8]` `[Ameaça: 7]` `[Consequência: 4 (Dano de Vontade/Quiet)]` `[Relógio: 5]`
  * **Dimensão Física (Corpo Flagelado):** `[Oposição: 6]` `[Ameaça: 6]` `[Consequência: 3 Letal]` `[Relógio: 4]`
  * **Dimensão Social (Culto Ocultista Fanático):** `[Oposição: 7]` `[Ameaça: 6]` `[Consequência: 3]` `[Relógio: 5]`
* **Diegese da Telegrafia:** *"O Mestre Nefandi corta as palmas sobre o círculo de espelhos negros. O reflexo de todos sangra pelos olhos e a gravidade se inverte. No fim do turno, uma onda de corrupção entrópica devorará a carne e a essência do Avatar de quem permanecer no círculo."*
* **Mecânica Oculta da Crise:** Relógio de Crise de 6 Caixas (Limiar Mínimo: 2 Sucessos).

#### 3. Desaurido (Marauder): "O Vórtice do Quiet Dinâmico" *(NPC Oficial M20)*
* **Matriz Dimensional:**
  * **Dimensão Mística (Quiet Dinâmico e Caos):** `[Oposição: 8]` `[Ameaça: 8]` `[Consequência: 4 (Paradoxo e Deformação)]` `[Relógio: 6]`
  * **Dimensão Mental (Alucinação Compartilhada):** `[Oposição: 8]` `[Ameaça: 7]` `[Consequência: 3]` `[Relógio: 5]`
  * **Dimensão Física (Anomalia de Gravidade/Matéria):** `[Oposição: 7]` `[Ameaça: 7]` `[Consequência: 4]` `[Relógio: 4]`
  * **Dimensão Social (Delírio Contagioso):** `[Oposição: 7]` `[Ameaça: 6]` `[Consequência: 2]` `[Relógio: 3]`
* **Diegese da Telegrafia:** *"A maga Desaurida gargalha enquanto as paredes de concreto viram vidro líquido e o chão ondula. A bolha de realidade distorcida vai expandir por três quarteirões no próximo turno, apagando a física convencional."*
* **Mecânica Oculta da Crise:** Relógio de Crise de 6 Caixas.
