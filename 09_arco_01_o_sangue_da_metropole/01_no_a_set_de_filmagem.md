---
type: no_investigativo
summary: "Nó A do Arco 01: O Portão do Dr. Hughie. O motoboy bateu no portão da casa do médico, os PJs saquearam o baú e encontraram a droga de sangue."
tags: [no_a, portao_de_hughie, inicio, investigacao, cronica, arco_01, sessao_01]
---
# Nó A: O Portão do Dr. Hughie — O Sangue da Metrópole

Este é o **Nó de Entrada Real da Crônica (Sessão 01 Jogada)**. Ele estabelece o ponto de partida efetivo do grupo com a droga em mãos no refúgio do médico Hughie.

---

## 🚪 1. O Ocorrido na Sessão 01 de Jogo

* **Local:** Portão da residência/consultório do [Dr. Hughie](../07_pjs/hughie.md).
* **O Impacto:** Um entregador do *Appetito Delivery* perde o controle da moto e colide com violência contra o portão de ferro da casa de Hughie.
* **A Ação do Grupo:** Os personagens saíram para verificar/socorrer a cena, revistaram a moto e abriram o **baú de entregas** do motoboy.
* **O Que Encontraram:**
  * Frascos com a droga sintética refinada a partir de sangue de mortos.
  * O smartphone do motoboy com mensagens criptografadas e rotas.
* **Estado Atual (Fim da Sessão 01 / Início da Sessão 02):** Após pegarem o material do baú, os jogadores se deslocaram e **estão reunidos no Centro de Treinamento Akashayano do Sr. Hu**, com a droga em mãos e o smartphone do motoboy, sem saber o que fazer com a substância enquanto deliberam sobre o próximo passo.

---

## 🔍 2. As 3 Pistas Extraídas do Baú da Moto

A posse da droga e do material no baú abre diretamente as 3 ramificações do **Ato II**:

### Pista 1A (Conduz ao Nó B: Fábrica Pasta da Nona)
* **Onde encontrar:** No smartphone trincado do entregador recolhido no baú.
* **Desafio Player-Faced (Intelectual/Computação - Diff 6):**
  * *$\ge 2$ Sucessos:* O grupo descriptografa o histórico de GPS e mensagens, revelando que a carga partiu dos fundos da **Fábrica Pasta da Nona** ([Fabrica Pasta da Nona](../03_lugares/fabrica_pasta_da_nona.md)), descobrindo a senha de abertura do depósito (`[Vantagem Tática]`).
  * *1 Sucesso:* Descobre o endereço da Fábrica, mas o celular emite um aviso de 'Falha de Entrega' aos servidores de Carlito.

### Pista 2A (Conduz ao Nó C: Hospital CAPS Zona Sul)
* **Onde encontrar:** Na análise médica/química dos frascos de sangue feita por Hughie (*Vida 4 / Medicina 4*).
* **Desafio Player-Faced (Medicina/Percepção - Diff 5):**
  * *$\ge 2$ Sucessos:* Hughie identifica que o sangue possui carimbo biológico de descarte de necrotério e sorologia ligada ao surto recente no **CAPS da Zona Sul**, revelando onde estão testando os efeitos.
  * *1 Sucesso:* Descobre a ligação com o CAPS Zona Sul, mas inalar o vapor da amostra causa tontura mística passageira (*1 de Estresse de Vontade*).

### Pista 3A (Conduz ao Nó D: Data Center & ABIN)
* **Onde encontrar:** Em um chip rastreador militar oculto sob a fita isolante do baú ou na van de vigilância nos arredores.
* **Desafio Player-Faced (Percepção/Furtividade - Diff 6):**
  * *$\ge 2$ Sucessos:* O grupo intercepta o sinal de beacon do baú e descobre que ele enviava telemetria para o **Data Center Corporativo** ([Sede Data Center](../03_lugares/sede_data_center.md)), sob vigilância da [ABIN](../05_faccoes/abin.md).
  * *1 Sucesso:* Localizam a frequência do rastreador antes que os agentes localizem a casa de Hughie, mas precisam desligá-lo às pressas.

---

## ⚔️ 4. Oposições Player-Faced do Nó A

### A. Agente de Campo da ABIN (Oposição de Elite)

```yaml
---
ameaca: Agente de Campo da ABIN (Operativo Federal)
nivel: 2 (Ameaça Ativa)

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
nivel: 1 (Desafio Rápido)

aspectos_diegaticos:
  - "[Matéria Efêmera Desmaterializada]": Imune a danos físicos mundanos.

bloco_mecanico:
  dificuldade_resolucao: Diff 6 (Espírito/Misticismo)
  consequencia_falha: 2 Pontos de Dano Letal (Fúria Eletrostática)
---
```
