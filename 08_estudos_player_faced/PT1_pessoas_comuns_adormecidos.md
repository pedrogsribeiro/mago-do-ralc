---
type: estudo
summary: "PT-1 em andamento: conversão player-faced de Pessoas Comuns/Adormecidos, começando pelo Cidadão Típico e registrando apenas transformações sustentadas pelo corpus e pelos baselines homologados."
tags: [player-faced, pt-1, adormecidos, npcs, drp, cidadao-tipico, em-andamento]
status: em_andamento
---

# PT-1 — Pessoas Comuns / Adormecidos

## Regra de condução deste pacote

Este documento executa o PT-1 da EAP `EAP_conclusao_player_faced_por_subsistemas.md`.

O trabalho é sequencial. Um perfil é fechado antes de abrir o próximo.

Ordem inicial:

1. Cidadão Típico;
2. Bandido Comum;
3. Durão Profissional;
4. Policial de Rua;
5. Agente do Governo.

Nenhum subsistema sobrenatural, veículo, hacking/Teia Digital, espírito ou Desperto é aberto aqui. Se uma regra dessas aparecer, ela é registrada como dependência futura.

O contrato superior permanece:

- o Storyteller rola zero dados;
- o PJ continua usando os procedimentos normais de M20;
- nenhuma nova rolagem é criada para o PJ;
- D/R/P descreve o lado do Obstáculo/NPC;
- ações do NPC permanecem separadas do Perfil DRP;
- recursos e características concretas não são apagados pela compressão.

---

# 1. Cidadão Típico

## 1.1 Fonte consolidada

A ficha canônica consolidada no repositório fornece:

- Força 2;
- Destreza 2;
- Vigor 2;
- Carisma 1–3;
- Manipulação 1–3;
- Aparência 1–4;
- Percepção 1–3;
- Inteligência 1–4;
- Raciocínio 2;
- Computação 1–3;
- Conhecimento de Área 1–3;
- Direção 1–2;
- Esportes 0–2;
- Ofícios 0–3;
- Tecnologia 1–3;
- 1–3 pontos adicionais em talentos ou conhecimentos profissionais;
- Força de Vontade 3;
- sete níveis normais de Vitalidade;
- nenhuma armadura;
- nenhuma habilidade de combate padronizada;
- diante de tiroteio ou mágika flagrante, tende a fugir ou chamar autoridades.

O perfil é deliberadamente um **template**, não uma pessoa de profissão única. Por isso, valores profissionais variáveis não devem ser colapsados em um único número inventado.

---

## 1.2 Operações que o Storyteller precisaria realizar na ficha original

### Defesa física ativa

Em combate corpo a corpo, se o Cidadão declarar esquiva:

`Destreza 2 + Esportes 0–2 = 2d–4d`.

Pelo baseline atual de oposição:

- 2d → `6/1`;
- 3d → `6/1`;
- 4d → `7/1`.

O D/R só existe quando a defesa ativa realmente seria declarada em M20. Não se concede defesa gratuita.

### Absorção

Vigor 2 produz 2d de soak contra dano Contundente.

Pelo baseline de Proteção:

`2d de soak → P1`.

Para um Adormecido:

- Contundente: Vigor pode absorver → `C1`;
- Letal: Vigor não absorve → `L0`;
- Agravado: Vigor não absorve → `A0`.

Logo, a assinatura passiva física é:

`C1·L0·A0`.

### Oposição profissional/técnica

A ficha não define uma única profissão. As combinações possíveis variam conforme o Cidadão instanciado.

No espaço explicitamente fornecido pela ficha, uma competência profissional pode produzir pools de aproximadamente 2d a 7d, dependendo do Atributo e da Habilidade efetivamente usados.

Quando houver uma oposição resistida real, usa-se a parada concreta já escolhida para aquele Cidadão e registra-se o D/R na ficha player-faced:

| Pool original do NPC | D/R |
| :---: | :---: |
| 2d | 6/1 |
| 3d | 6/1 |
| 4d | 7/1 |
| 5d | 6/2 |
| 6d | 6/2 |
| 7d | 7/2 |

A escolha da profissão é feita ao preparar/instanciar o NPC. O ST não deve reconstruir essa conta durante a cena.

### Social

A fonte fornece Atributos Sociais em faixa, mas não fornece uma Habilidade Social padrão para o Cidadão Típico.

Portanto, este perfil não recebe uma Resistência Social fixa inventada.

O default esparso permanece `6/0/0` até que uma profissão/personagem concreto possua competência social explicitada.

### Iniciativa

A regra original usa:

`1d10 + Destreza + Raciocínio`.

A auditoria específica do PT-1 homologou a transformação de preparação:

```text
Iniciativa fixa do NPC = Destreza + Raciocínio + 6
```

Essa fórmula pertence ao **procedimento de conversão**, não à ficha final do Obstáculo/NPC. Depois de derivado o valor, a ficha final registra **somente a Iniciativa pronta**.

O valor é derivado somente da ficha do NPC. O PJ continua rolando sua iniciativa normalmente segundo M20.

Entre os candidatos testados, `+5` e `+6` apresentaram a mesma TV média ampla (7,296%) e o mesmo pior caso (15%). `+6` apresentou menor erro médio na probabilidade de o NPC agir antes do PJ no recorte do PT-1 (5,778% contra 6,356% de `+5`) e preserva empates possíveis. O candidato `+5,5` foi rejeitado porque elimina empates contra totais inteiros e piora a TV média.

Para o Cidadão Típico, a conversão produz **Iniciativa 10**.

Na ficha final aparece apenas:

```text
Iniciativa: 10
```

**Status: HOMOLOGADO.**

---

## 1.3 Primeira ficha player-faced candidata

> **Status:** arquitetura de apresentação homologada neste pacote; ainda não propagada para os textos finais.

A ficha usa explicitamente quatro camadas operacionais:

1. **Perfil DRP** — como o NPC resiste quando algo age contra ele;
2. **Ações** — o que o NPC entrega quando age;
3. **Persistência** — quanto tempo/quanto dano ele suporta antes de deixar de funcionar;
4. **Recursos e Características** — traços que continuam existindo porque possuem função própria em M20.

Vitalidade e Força de Vontade não são campos DRP. Vitalidade permanece como Persistência; Força de Vontade permanece como recurso/característica quando sua função original for necessária.

### CIDADÃO TÍPICO

Uma pessoa comum, sem treinamento de combate. Sua competência real depende do ofício, da rotina e da experiência profissional. Diante de violência grave ou de uma manifestação sobrenatural evidente, a reação típica é afastar-se, fugir ou chamar ajuda.

**Bloco Mecânico:**

```text
Perfil-base: 6

Físico:
6/1/C1·L0·A0
(7/1/C1·L0·A0 se possuir Esportes 2)

Social:
6
(a menos que o Cidadão concreto possua competência social explicitada)

Mental/Técnico:
6
+ especialidade profissional pré-convertida quando relevante

Mágicko/Poderes:
—

Ações:
nenhuma ação ofensiva padronizada pela ficha-base

Persistência:
Vitalidade padrão humana
OK, -1, -1, -2, -2, -5, Incapacitado

Recursos:
Força de Vontade 3

Iniciativa:
10

Características:
Pessoa comum
Sem treinamento de combate padronizado
Diante de violência grave ou sobrenatural evidente, tende a fugir ou chamar ajuda
```

### Leitura operacional

- `Perfil-base 6` é o default esparso para uma tarefa sem oposição especial.
- O `R1` Físico só entra quando o Cidadão usa a defesa ativa que M20 já permitiria.
- Contra ataque que não admite aquela defesa ativa, não se aplica R apenas porque ele aparece na ficha.
- `C1` continua valendo para Contundente porque deriva do soak de Vigor 2.
- `L0` e `A0` preservam a ausência de soak corporal de um Adormecido contra esses tipos.
- A especialidade profissional deve ser escolhida uma vez e anotada; não deve ser recalculada durante a sessão.
- O perfil não possui ação ofensiva padrão porque a ficha original também não fornece treinamento/ataque padronizado.

---

## 1.4 Exemplo de instanciação profissional

Exemplo apenas de uso da estrutura, sem criar uma nova regra:

```text
ASSISTENTE DE LABORATÓRIO

Perfil-base: 6
Físico: 6/1/C1·L0·A0
Mental/Técnico — laboratório: 6/2
Social: 6

Ações:
nenhuma ação ofensiva padronizada

Persistência:
Vitalidade padrão humana

Recursos:
Força de Vontade 3

Iniciativa:
10

Características:
Assistente de laboratório
Competência profissional já pré-convertida
```

O `6/2` só seria usado se a ficha concreta tivesse sido preparada com uma parada profissional de 5d ou 6d que realmente sustentasse aquela oposição.

---

## 1.5 Dívidas e gate do Cidadão Típico

### Resolvido o suficiente para este perfil

- [x] soak físico Contundente → Proteção;
- [x] ausência de soak Letal/Agravado preservada;
- [x] defesa ativa corporal convertível por D/R sem concedê-la gratuitamente;
- [x] faixa profissional pode ser pré-convertida no momento de instanciar o template;
- [x] ausência de competência Social padronizada não foi preenchida por chute;
- [x] Vitalidade foi preservada explicitamente como Persistência;
- [x] Força de Vontade foi preservada explicitamente como Recurso;
- [x] a arquitetura de apresentação Perfil DRP → Ações → Persistência → Recursos/Características foi homologada;
- [x] nenhuma ação ofensiva inexistente foi inventada;
- [x] iniciativa do NPC derivada por `Destreza + Raciocínio + 6` no procedimento de conversão;
- [x] ficha final registra somente o valor pronto de Iniciativa;
- [x] Cidadão Típico recebe `Iniciativa: 10` sem rolagem do Storyteller.

### Ainda aberto

- [ ] confirmar, no teste de mesa do perfil completo, que a apresentação do D/R físico não induz aplicação de defesa ativa onde M20 não a permitiria.

### Gate

**CIDADÃO TÍPICO: CONCLUÍDO PARA O PT-1.**

A ficha já pode ser operada pelo Storyteller sem rolagens próprias nas operações normais cobertas por este perfil. A observação sobre uso contextual de defesa ativa permanece como cuidado de apresentação/playtest, não como bloqueio mecânico.

**Próximo perfil: Bandido Comum.**


---

# 2. Bandido Comum

## 2.1 Fonte consolidada

A ficha canônica consolidada no repositório fornece:

- Força 3;
- Destreza 2;
- Vigor 2;
- Carisma 2;
- Manipulação 2;
- Aparência 2;
- Percepção 2;
- Inteligência 1;
- Raciocínio 2;
- Armas Brancas 2;
- Briga 2;
- Conhecimento de Área 1;
- Direção 1;
- Esportes 2;
- Intimidação 1;
- Manha 1;
- Ofícios 2;
- Prontidão 2;
- Tecnologia 1;
- Força de Vontade 3;
- Vitalidade padrão humana;
- nenhuma armadura;
- Soco: 2d C;
- arma de impacto: 4d C;
- arma de corte: 3d L.

## 2.2 Conversões que já estão sustentadas

### Iniciativa

A fórmula homologada de preparação produz:

`Destreza 2 + Raciocínio 2 + 6 = 10`.

Na ficha final aparece somente:

```text
Iniciativa: 10
```

### Perfil Físico

A defesa ativa típica usa:

`Destreza 2 + Esportes 2 = 4d`.

O baseline de oposição converte 4d em `7/1`.

Vigor 2 produz `P1` contra Contundente. Como Adormecido, Vigor não absorve Letal nem Agravado.

Portanto:

```text
Físico: 7/1/C1·L0·A0
```

O `R1` continua condicionado à existência de defesa/oposição ativa no procedimento original; ele não cria defesa gratuita.

### Mental/Técnico — percepção e alerta

`Percepção 2 + Prontidão 2 = 4d`.

Quando o Bandido oferece oposição ativa de percepção/alerta a uma ação do PJ, o valor pré-convertido é:

```text
Mental/Técnico — percepção/alerta: 7/1
```

Outras competências técnicas do perfil são baixas e não recebem um número separado sem necessidade concreta.

### Social

O Bandido possui `Intimidação 1` com Atributos Sociais 2, mas a ficha original não estabelece por si só um procedimento social universal para converter essa competência em resistência defensiva.

Por isso:

```text
Social: 6
```

A competência de Intimidação permanece como característica de ação possível, mas não é transformada automaticamente em R ou P Social.

## 2.3 Ações físicas

Os ataques corpo a corpo usam `Destreza 2 + Briga/Armas Brancas 2 = 4d` em Dificuldade 6.

Na calibração ofensiva já realizada, `4d D6` produz **2 sucessos fixos de ação**.

Os pools-base de dano produzem:

- 2d C → efeito-base 1C;
- 4d C → efeito-base 2C;
- 3d L → efeito-base 1L.

A relação original entre sucessos excedentes e dano continua preservada pelos degraus já estudados. Para este perfil:

- Soco 2d: 1C com 1 sucesso líquido; continua 1C com um sucesso excedente; chega a 2C com dois excedentes;
- Arma de Impacto 4d: permanece 2C nos degraus relevantes deste perfil;
- Arma de Corte 3d: 1L com 1 sucesso líquido; sobe para 2L com um sucesso excedente.

A ficha candidata pode portanto registrar:

```text
Ações:
Soco: 2S + 1C
Arma de Impacto: 2S + 2C
Arma de Corte: 2S + 1L; 2L se restarem 2+ sucessos líquidos
```

Esses valores são pré-convertidos; o ST não consulta os pools originais durante a cena.

### Limite já conhecido

Quando o PJ usa uma defesa ativa que M20 já permite, o pipeline é utilizável:

```text
ação fixa do Bandido
→ defesa normal do PJ
→ sucessos líquidos restantes
→ efeito-base/degau por excedentes
→ soak normal do PJ, quando permitido
```

Quando o PJ **não** usa defesa ativa, os `2S` do Bandido tornam o acerto determinístico. O M20 original ainda continha chance de falha no ataque de 4d D6. A auditoria anterior mostrou que nenhum escalar determinístico simples preserva satisfatoriamente essa distribuição.

Isso é agora uma **dívida concreta do Bandido Comum**, e portanto uma dívida legítima do PT-1. Não será contornada criando uma defesa gratuita para o PJ nem reintroduzindo rolagem do ST.

## 2.4 Ficha player-faced candidata

> **Status:** parcialmente fechada; bloqueada somente pela ação ofensiva sem defesa ativa.

### BANDIDO COMUM

Brigão de rua acostumado a intimidação, violência rápida e armas improvisadas. É capaz de perceber movimentações óbvias e se defender fisicamente, mas não possui proteção especial nem treinamento sofisticado.

**Bloco Mecânico:**

```text
Perfil-base: 6

Físico:
7/1/C1·L0·A0

Social:
6

Mental/Técnico:
6
Percepção/Alerta: 7/1

Mágicko/Poderes:
—

Ações:
Soco: 2S + 1C
Arma de Impacto: 2S + 2C
Arma de Corte: 2S + 1L; 2L se restarem 2+ sucessos líquidos

Persistência:
Vitalidade padrão humana
OK, -1, -1, -2, -2, -5, Incapacitado

Recursos:
Força de Vontade 3

Iniciativa:
10

Características:
Brigão de rua
Armas improvisadas
Sem armadura
Intimidação baixa, mas presente
```

## 2.5 Gate do Bandido Comum

### Resolvido

- [x] Perfil Físico;
- [x] Proteção por tipo de dano;
- [x] Percepção/Alerta;
- [x] Iniciativa fixa;
- [x] Persistência;
- [x] Força de Vontade como Recurso;
- [x] ações corpo a corpo pré-convertidas para S + efeito;
- [x] degraus de dano por sucessos excedentes preservados onde relevantes.

### Bloqueio real

- [ ] resolver o comportamento das ações ofensivas do NPC quando o PJ não usa defesa ativa, sem criar nova rolagem para o jogador e sem devolver dados ao Storyteller.

### Gate

**BANDIDO COMUM: AINDA NÃO CONCLUÍDO.**

O próximo trabalho permanece dentro do PT-1: resolver somente esse bloqueio ofensivo concreto antes de avançar para o Durão Profissional.
