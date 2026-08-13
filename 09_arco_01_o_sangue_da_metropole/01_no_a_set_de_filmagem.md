---
type: no_investigativo
summary: "Nó A do Arco 01: O Set de Filmagem. Incidente inicial com a explosão do delivery de sangue e revelação das 3 pistas primárias."
tags: [no_a, set_de_filmagem, inicio, investigacao, cronica, arco_01]
---
# Nó A: O Set de Filmagem — O Sangue da Metrópole

Este é o **Nó de Entrada (Incidente Inicial)** do Arco 01. Ele conecta a Situação Compartilhada dos 4 PJs com o estopim da trama: o acidente do entregador do *Appetito Delivery* carregando a droga sintética de sangue.

---

## 🎬 1. Posicionamento dos Jogadores no Local

* [Jhonny D. Lee](../07_pjs/jhonny_d_lee.md): No centro do set, gravando uma cena de combate marcial para um comercial de TV sob os holofotes.
* [Andrey Golubenko](../07_pjs/andrey_golubenko.md): Nos bastidores urbanos, rastreando uma distorção mística/digital no sinal de celular.
* [Hughie](../07_pjs/hughie.md): Na multidão de curiosos Adormecidos do lado de fora das grades, observando a gravação.
* [Niki](../07_pjs/niki.md): Seguindo a moto do entregador do *Appetito Delivery* que apresentava comportamento errático.

---

## 💥 2. O Incidente Inicial (Minuto 01)

A moto do entregador atravessa o bloqueio do set desgovernada e se chocará contra o **gerador principal de energia**.

* **O Impacto:** O gerador explode em uma onda de chamas azuis e faíscas eletrostáticas. A explosão espalha cacos de frascos plásticos contendo o **Néctar de Sangue** ([Sangue](../06_itens/sangue.md)), liberando um vapor de Quintessência espessa.
* **O Efeito na Penumbra:** A névoa mística rompe a Película local, atraindo [Espíritos da Fuligem Urbana](../05_faccoes/espiritos_das_cidades.md) na Penumbra Média.

---

## 🔍 3. As 3 Pistas Encontradas no Nó A

Seguindo a **Regra das 3 Pistas de The Alexandrian**, a investigação deste local fornece 3 caminhos independentes:

### Pista 1A (Conduz ao Nó B: Fábrica Pasta da Nona)
* **Onde encontrar:** No smartphone trincado no bolso do entregador acidentado.
* **Desafio Player-Faced (Intelectual - Diff 6):**
  * *$\ge 2$ Sucessos:* O PJ descriptografa o GPS completo, revelando a rota de saída da **Fábrica Pasta da Nona** ([Fabrica Pasta da Nona](../03_lugares/fabrica_pasta_da_nona.md)) + a chave de acesso do portão dos fundos (`[Vantagem Tática]`).
  * *1 Sucesso:* Obtém o endereço da Fábrica Pasta da Nona, mas o celular ativa um alarme de autodestruição que alerta Carlito Heizenberg.

### Pista 2A (Conduz ao Nó C: Hospital CAPS Zona Sul)
* **Onde encontrar:** Nos cacos de frascos plásticos da droga espalhados pelo chão.
* **Desafio Player-Faced (Intelectual/Percepção - Diff 5):**
  * *$\ge 2$ Sucessos:* O PJ analisa os frascos e identifica o carimbo médico de triagem de doadores de sangue do **CAPS da Zona Sul**, notando que o sangue pertencia a vítimas de um surto recente.
  * *1 Sucesso:* Descobre a etiqueta do CAPS Zona Sul, mas se contamina levemente com o odor da droga (*sofrendo 1 de Estresse de Vontade*).

### Pista 3A (Conduz ao Nó D: Data Center & ABIN)
* **Onde encontrar:** Na van preta sem placas que encosta segundos após a explosão para recolher o material.
* **Desafio Player-Faced (Físico/Furtividade - Diff 7):**
  * *$\ge 2$ Sucessos:* O PJ observa os agentes federais da [ABIN](../05_faccoes/abin.md) operando um scanner militar de radiofrequência vinculado ao **Data Center Corporativo** ([Sede Data Center](../03_lugares/sede_data_center.md)), descobrindo que a ABIN está acobertando a live de [Bernardino](../02_npcs/bernardino.md).
  * *1 Sucesso:* Descobre a conexão com o Data Center, mas atrai a atenção dos agentes da ABIN para uma perseguição.

---

## ⚔️ 4. Oposições Player-Faced do Nó A

### A. Agente de Campo da ABIN (Oposição de Elite)

```yaml
---
ameaca: Agente de Campo da ABIN (Operativo Federal)
nivel: 3 (Ameaça Ativa)

aspectos_diegaticos:
  - "[Colete Tático Nível IIIA]": Proteção contra tiros leves (RD 1 Físico).
  - "[Equipamento de Varredura da ABIN]": Scanner de radiofrequência e bloqueador de celular.

bloco_mecanico:
  imposicao: Diff 7 (Físico/Tático) | Diff 6 (Social/Carteirada) | Diff 5 (Intelectual/Hack)
  pressao: Diff 7 (Disparos de Pistola 9mm / Táticas de Contenção)
  impacto: 3 Pontos de Dano Letal
  relogio_vitalidade: 5 Caixas de Vitalidade Físico-Corporal
  resistencia_dano: RD 1 (Acerto Parcial de 1s causa Efeito Zero no Relógio)
---
```

### B. Espírito de Fuligem da Cidade (Oposição Menor)

```yaml
---
ameaca: Espírito da Fuligem (Gaffling Urbano da Penumbra)
nivel: 2 (Oposição Rápida)

aspectos_diegaticos:
  - "[Matéria Efêmera Desmaterializada]": Imune a danos físicos mundanos.

bloco_mecanico:
  dificuldade_resolucao: Diff 6 (Espírito/Misticismo)
  consequencia_falha: 2 Pontos de Dano Letal (Fúria Eletrostática)
---
```
