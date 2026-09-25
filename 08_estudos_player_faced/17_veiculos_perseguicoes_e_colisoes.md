---
type: regra
summary: "Estudo 17: veículos, perseguições e colisões sob o olhar player-facing, preservando testes estendidos-resistidos e separando posição, dano a ocupantes e integridade do veículo."
tags: [estudo, player-faced, veiculos, perseguicoes, colisoes, direcao, estrutura, regras]
---

# Estudo 17: Veículos, Perseguições e Colisões

Este estudo trata três problemas diferentes que não devem ser confundidos:

1. **perseguição / posição relativa**;
2. **dano aos ocupantes**;
3. **dano e integridade do veículo**.

A bíblia atual sustenta claramente que **perseguições de veículos são ações estendidas-resistidas**: os participantes acumulam sucessos líquidos ao longo de turnos e a disputa é decidida pelo resultado acumulado.

O corpus atual, porém, não contém um procedimento consolidado suficiente para homologar colisões, dano estrutural e interação entre velocidade, massa e ocupantes.

---

## 1. Gate de fidelidade

A experiência do jogador precisa preservar:

* Direção e outras Habilidades relevantes;
* testes estendidos-resistidos;
* economia de ações;
* modificadores de condição;
* mudanças de posição;
* possibilidade de colisão;
* dano aos ocupantes;
* integridade do veículo;
* equipamento e características especiais.

A camada player-facing não deve:

* reduzir perseguição a um único teste por padrão;
* transformar velocidade em HP;
* inventar dano fixo de colisão;
* misturar posição e dano estrutural num único relógio;
* transformar todo veículo em NPC.

---

## 2. Perseguições já são naturalmente compatíveis

A regra-base de M20 para perseguições é estendida-resistida.

Isso já oferece uma tradução direta:

```
PJ rola sua condução/manobra
→ oposição ativa do rival é convertida
→ sucessos líquidos alimentam progresso de posição
```

Se houver um condutor NPC adversário, sua parada pode alimentar **Oposição**.

Se não houver agente rival e o problema for apenas terreno, trânsito ou clima, trata-se de obstáculo passivo.

### Gate

**PASSA PELA ARQUITETURA EXISTENTE.**

---

## 3. Relógio de posição

Um Relógio pode representar **distância/progresso relativo**, desde que seja apenas uma interface para a lógica estendida original.

Exemplo:

```
PERSEGUIÇÃO

Alvo:
escapar do sedã da NOM

Progresso:
0 / 6

1 sucesso líquido:
+1 posição

2 sucessos:
+2 posição

3 sucessos:
+3 posição
```

Esse relógio não representa “vida do carro”.

Ele representa **vantagem posicional acumulada**.

### Gate

**PASSA.**

---

## 4. 1 sucesso continua valendo

Como em qualquer conflito persistente:

> **1 sucesso líquido continua sendo sucesso marginal e reduz 1 caixa do Relógio de posição**, além de mover a ficção.

Exemplos:

* abre meia quadra;
* força o perseguidor a perder linha de visão por alguns segundos;
* conquista uma faixa melhor;
* passa por um obstáculo antes do rival;
* cria distância suficiente para uma próxima manobra.

O ST qualifica a qualidade, mas não apaga o avanço.

---

## 5. Oposição ativa do condutor rival

Se um NPC conduz ativamente contra o PJ:

* consulta-se a parada original apropriada;
* aplica-se a família de conversão de Oposição;
* o jogador continua rolando sua própria ação.

Não se usa:

* “Ameaça de perseguição” genérica;
* nível do veículo;
* maior pool do NPC;
* dificuldade inventada por tier.

### Gate

**PASSA.**

---

## 6. Obstáculos ambientais

Trânsito, gelo, chuva, estrada ruim, multidão, obras e terreno não possuem agência.

Eles podem alterar:

* dificuldade;
* número de sucessos necessários;
* condições de manobra;
* consequência de falha;
* possibilidade de certas ações.

### Gate

**PRESERVAR COMO OBSTÁCULO PASSIVO.**

---

## 7. Veículo como objeto

Quando o foco é o veículo em si, ele não deve ser tratado automaticamente como NPC.

A pergunta correta é:

> a bíblia original usa Durability/Structure ou outra regra de integridade veicular específica?

Se sim, essa estrutura deve ser preservada.

A pesquisa já estabeleceu para objetos:

```
resistência fixa
+
integridade estrutural
```

Isso é conceitualmente compatível com veículos.

### Gate

**ARQUITETURA COMPATÍVEL, PROCEDIMENTO ESPECÍFICO AINDA NÃO CONSOLIDADO.**

---

## 8. Colisões

Colisão é uma interação separada da perseguição.

Ela pode afetar:

* veículo A;
* veículo B;
* ocupantes;
* pedestres;
* cenário.

A bíblia disponível neste momento não fornece procedimento consolidado suficiente para definir:

* pool de dano por velocidade;
* modificador de massa;
* soak de veículo;
* dano aos ocupantes;
* perda de controle;
* Structure/Durability específicos.

Portanto:

> **não se homologa dano fixo de colisão nem tabela nova neste estudo.**

### Gate

**LACUNA DOCUMENTAL.**

---

## 9. Telegrafia em perseguições

Telegrafia pode existir naturalmente:

```
rival emparelha
→ fecha lateralmente
→ força contra barreira
```

ou:

```
caminhão perde estabilidade
→ começa a tombar
→ bloqueia a pista
```

A primeira etapa pode produzir efeito real.

Mas telegrafia não substitui a regra de colisão.

---

## 10. Ameaça e Consequência

Em perseguição:

* **Oposição** = competência do rival em disputar posição;
* **Ameaça** = manobra ofensiva ativa do rival;
* **Consequência** = perda de posição, colisão, dano, bloqueio ou outro efeito;
* **Integridade/Relógio** = progresso da perseguição;
* **Limiar** = apenas quando existir resistência equivalente real.

Esses campos não devem fundir posição e dano.

---

## 11. Exemplo estrutural

```
PERSEGUIÇÃO — SEDÃ DA NOM

Objetivo dos PJs:
escapar

Relógio de posição:
0 / 6

Condutor rival:
Direção relevante → Oposição convertida

Características:
[Veículo blindado]
[Rádio tático]
[Equipe coordenada]

Estados:
- em perseguição
- emparelhado
- linha de visão perdida
- rota bloqueada
```

Se ocorrer colisão, abre-se o **procedimento de colisão**, separado do Relógio de posição.

---

## 12. Matriz de decisão

| Situação | Tratamento |
| :--- | :--- |
| Perseguição com rival | estendida-resistida / Oposição |
| Perseguição contra ambiente | teste estendido/passivo |
| Relógio | posição/progresso |
| 1 sucesso | +1 posição |
| Manobra ofensiva | Ameaça |
| Perda de posição | Consequência |
| Colisão | procedimento específico |
| Dano aos ocupantes | procedimento específico |
| Dano ao veículo | Durability/Structure ou regra veicular original |
| Veículo parado | objeto |
| Veículo autônomo | constructo-agente se possuir agência real |

---

## 13. Gate do Estudo 17

### Resolvido

* perseguições como estendidas-resistidas;
* Oposição para condutor rival;
* Relógio como posição;
* 1 sucesso = 1 avanço;
* obstáculos ambientais;
* separação entre perseguição e colisão;
* veículo como objeto/constructo conforme natureza.

### Lacunas

* procedimento detalhado de colisão;
* dano por velocidade/massa;
* dano aos ocupantes;
* integridade veicular específica;
* perda de controle e capotamento;
* regras especiais de veículos.

---

## 14. Propagação

Este estudo retroage sobre:

* Estudo 10 — veículos/perseguições;
* Estudo 12 — constructos/objetos;
* Estudo 04 — exemplo de perseguição curta vs. persistente.

O próximo subsistema deve ser **Certámen e outros duelos estruturados**, porque já existe regra suficiente no corpus para uma tradução mais completa.


---

## 15. Propagação do Estudo 21

Perigos ambientais reforçam a separação já adotada neste estudo:

* dano ambiental automático não deve ser confundido com colisão;
* queda/impacto possuem regras próprias;
* colisões veiculares continuam dependendo de procedimento específico ainda não consolidado na bíblia;
* consequências ambientais podem afetar ocupantes sem transformar o veículo em NPC.
