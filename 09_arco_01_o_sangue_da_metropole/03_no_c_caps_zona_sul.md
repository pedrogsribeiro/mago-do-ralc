---
type: no_investigativo
summary: "Nó C do Arco 01: Hospital CAPS Zona Sul. O surto de viciados em Néctar de Sangue, a enfermeira Ângela e a manifestação de Joana Pipoquinha."
tags: [no_c, caps_zona_sul, angela, joana_pipoquinha, investigacao, cronica, arco_01]
---
# Nó C: Hospital CAPS Zona Sul — Surto & Revelação Efêmera

Este é o **Nó C (Centro de Crise Médica & Contato Efêmero)**. O Centro de Atenção Psicossocial (CAPS) da Zona Sul onde a enfermeira Desperta [Angela](../02_npcs/angela.md) tenta conter um surto maciço de pacientes Adormecidos que sofreram overdoses de Néctar de Sangue.

---

## 🏥 1. A Atmosfera do Hospital

* **A Crise:** Dezenas de pacientes em transe catatônico com veias brilhando em tom azulado de Quintessência residual. Vários sofrem espasmos e alucinações de tempestades de raios.
* **Angela em Ação:** A enfermeira usa Mágika de *Vida 2 / Mente 2* disfarçada de sedativos para impedir que as mentes dos pacientes colapsem sob a raiva mística.

---

## 🔍 2. As 3 Pistas Encontradas no Nó C

### Pista 1C (Conduz ao Nó B: Fábrica Pasta da Nona)
* **Onde encontrar:** Na análise química do sangue das vítimas realizada por Ângela no laboratório clínico.
* **Desafio Player-Faced (Intelectual/Ciência - Diff 6):**
  * *$\ge 2$ Sucessos:* Descobre a presença de um reagente industrial sintético derivado de molho de tomate e farinha de trigo de grau alimentício, isolando o lote específico entregue pela **Fábrica Pasta da Nona** ([Fabrica Pasta da Nona](../03_lugares/fabrica_pasta_da_nona.md)).
  * *1 Sucesso:* Descobre a ligação com a fábrica no Brás, mas se desgasta fisicamente ajudando os pacientes.

### Pista 2C (Conduz ao Nó D: Data Center & ABIN)
* **Onde encontrar:** Nos prontuários dos doadores de sangue e fichas registradas no sistema informatizado.
* **Desafio Player-Faced (Intelectual/Investigação - Diff 6):**
  * *$\ge 2$ Sucessos:* O PJ identifica que todos os doadores infectados haviam sido cadastrados durante uma campanha de vacinação promovida pela Dra. [Elizabeth Barcelos](../02_npcs/elizabeth_barcelos.md), cujos dados foram vazados por [Bernardino](../02_npcs/bernardino.md) para o **Data Center Corporativo** ([Sede Data Center](../03_lugares/sede_data_center.md)).
  * *1 Sucesso:* Rastreia o vazamento até Bernardino e o Data Center, mas alerta os monitores digitais da ABIN.

### Pista 3C (Conduz ao Nó E: Santuário de Lizander — Clímax)
* **Onde encontrar:** Na manifestação mediúnica/espiritual de [Joana Pipoquinha](../02_npcs/joana_pipoquinha.md) (espírito da filha falecida de Lizander).
* **Desafio Player-Faced (Místico/Espírito - Diff 6):**
  * *$\ge 2$ Sucessos:* Joana se manifesta através do espelho da sala de triagem e revela em soluços: *"Meu pai está usando a dor das vacinas e o sangue de vocês para erguer uma torre de raio na antiga usina! Ele quer matar todos os magos da cidade!"*. Ela fornece as coordenadas exatas do **Santuário de Lizander** (`[Vantagem Tática]`).
  * *1 Sucesso:* Joana avisa sobre o pai e a usina, mas o terror efêmero causa surto de pânico na sala.

---

## ⚔️ 3. Oposições Player-Faced do Nó C

### A. Viciados Possuídos por Efêmera de Sangue (Surto Violento)

```yaml
---
ameaca: Pacientes em Overdose de Quintessência (Fúria Efêmera)
nivel: 3 (Ameaça Ativa - Dilema Ético)

aspectos_diegaticos:
  - "[Adormecidos Inocentes em Transe]": Não podem ser mortos sem grave complicação moral/Paradoxo.
  - "[Força Sobre-humana de Primórdio]": Veias azuladas que concedem força violenta.

bloco_mecanico:
  imposicao: Diff 6 (Físico/Contenção Não-Letal) | Diff 5 (Mente/Calmante Psíquico) | Diff 7 (Espírito/Drenagem)
  pressao: Diff 6 (Ataques Frenéticos / Garras Improvisadas)
  impacto: 3 Pontos de Dano Contundente / Estresse Mental
  relogios_de_resolucao:
    relogio_fisico_contencao: 5 Caixas (Imobilização Não-Letal - Diff 6)
    relogio_mental_sedacao: 3 Caixas (Feitiço de Mente/Calmante - Diff 5)
---
```

### B. Joana Pipoquinha (Espírito Guia)

```yaml
---
ameaca: Joana Pipoquinha (Espírito de Criança / Efêmera Triste)
nivel: 2 (Oposição Rápida - Diálogo)

aspectos_diegaticos:
  - "[Ressentimento com Mágika]": Oculta a voz se os magos exibirem mágika vulgar ostensiva.
  - "[Vínculo com Lizander]": Conhece todos os planos de seu pai.

bloco_mecanico:
  dificuldade_resolucao: Diff 5 (Social/Empatia com Crianças) | Diff 6 (Místico/Espírito)
  consequencia_falha: O espírito se dissipa chorando e exige que os PJs voltem depois.
---
```
