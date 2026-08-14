---
type: no_investigativo
summary: "Nó B do Arco 01: Fábrica Pasta da Nona. A refinaria mística de Carlito Heizenberg e a frota de entregas dos Pastafarianos."
tags: [no_b, fabrica_pasta, carlito_heizenberg, refinaria, investigacao, cronica, arco_01]
---
# Nó B: Fábrica Pasta da Nona — Refinaria de Sangue

Este é o **Nó B (Centro Logístico & Laboratório Alquímico)**. Antiga instalação industrial no Brás reutilizada pela seita dos [Pastafarianos](../05_faccoes/pastafarianos.md) para operar a frota do *Appetito Delivery* e abrigar o laboratório místico de [Carlito Heizenberg](../02_npcs/carlito_heizenberg.md).

---

## 🏭 1. O Cenário da Refinaria Clandestina

* **Fachada:** Empresa de massas italianas artesanais com dezenas de motoboys de vermelho entrando e saindo com bags térmicas.
* **Interior:** Tanques industriais inox de macarrão convertidos em centrifugadoras de sangue. O cheiro de molho de tomate oculta o odor de plasma e reagentes de Quintessência.
* **O Laboratório Secreto:** No subsolo, Carlito destila o **Néctar de Sangue** utilizando tubos de vidro místico e caldeiras de *Matéria 3 / Primórdio 2*.

---

## 🔍 2. As 3 Pistas Encontradas no Nó B

### Pista 1B (Conduz ao Nó C: Hospital CAPS Zona Sul)
* **Onde encontrar:** Nas notas fiscais de transporte e guias de recolhimento de bolsas de sangue no escritório de Carlito.
* **Desafio Player-Faced (Intelectual - Diff 6):**
  * *$\ge 2$ Sucessos:* Descobre o contrato secreto de extração de sangue mantido com a equipe noturna do **CAPS Zona Sul**, revelando que a enfermeira [Angela](../02_npcs/angela.md) está tentando bloquear o esquema por dentro (`[Vantagem Tática]`).
  * *1 Sucesso:* Descobre a ligação com o CAPS Zona Sul, mas dispara um alarme de invasão na rede interna.

### Pista 2B (Conduz ao Nó D: Data Center & ABIN)
* **Onde encontrar:** Nos servidores de rede locais que gerenciam o aplicativo *Appetito Delivery*.
* **Desafio Player-Faced (Intelectual/Computação - Diff 7):**
  * *$\ge 2$ Sucessos:* O PJ hackeia os servidores e encontra transações financeiras em criptomoedas ligando a distribuidora ao influenciador [Bernardino](../02_npcs/bernardino.md) e ao **Data Center Corporativo** ([Sede Data Center](../03_lugares/sede_data_center.md)).
  * *1 Sucesso:* Rastreia o sinal até o Data Center, mas sofre uma retaliação do ICE Firewall.

### Pista 3B (Conduz ao Nó E: Santuário de Lizander — Clímax)
* **Onde encontrar:** No altaz místico de Primórdio no fundo do laboratório de Carlito.
* **Desafio Player-Faced (Místico/Ocultismo - Diff 7):**
  * *$\ge 2$ Sucessos:* Identifica que 30% de toda a Quintessência refinada no sangue está sendo canalizada à distância para o nódulo de [Lizander Filho do Raio](../02_npcs/lizander_filho_do_raio.md), obtendo a frequência exata de ressonância do Santuário.
  * *1 Sucesso:* Descobre a ligação com Lizander, mas sofre 1 ponto de estresse místico de Paradoxo.

---

## ⚔️ 3. Oposições Player-Faced do Nó B

### A. Carlito Heizenberg (Alquimista do Sangue)

```yaml
---
ameaca: Carlito Heizenberg (Alquimista Renegado de Sangue)
nivel: 2 (Ameaça Ativa)

aspectos_diegaticos:
  - "[Mestre em Destilação Alquímica de Primórdio]": Usa frascos de Quintessência corrosiva como projéteis.
  - "[Aura de Sangue Contaminado]": Provoca náusea mística nos magos ao redor.
  - "[Escudo de Matéria 3/Vigor Alquímico]": Pele endurecida quimicamente (RD 1 Físico).

bloco_mecanico:
  imposicao: Diff 7 (Físico/Tático) | Diff 6 (Social/Chantagem) | Diff 7 (Místico)
  pressao: Diff 7 (Arremesso de Frascos de Sangue Ácido / Descargas de Primórdio)
  impacto: 4 Pontos de Dano Letal / Corrosão de 1 Ponto de Quintessência
  relogio_vitalidade: 6 Caixas de Vitalidade
  resistencia_dano: RD 1 (Acerto Parcial de 1s causa Efeito Zero no Relógio)
  limiar_efetividade: Limiar Mínimo = 2 (Exige ataques potentes para romper a armadura química)
---
```

### B. Capangas Pastafarianos (Oposição Menor)

```yaml
---
ameaca: Cultistas Pastafarianos (Membros da Frota de Entregas)
nivel: 1 (Desafio Rápido)

aspectos_diegaticos:
  - "[Fanatismo do Molho Sagrado]": Atacam com porretes e cortadores de pizza pesados.

bloco_mecanico:
  dificuldade_resolucao: Diff 6 (Físico/Briga)
  consequencia_falha: 2 Pontos de Dano Contundente
---
```
