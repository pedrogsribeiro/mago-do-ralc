---
type: estudo
summary: "PT-1 concluído: conversão player-faced dos cinco perfis canônicos de Pessoas Comuns/Adormecidos para o padrão DRP."
tags: [player-faced, pt-1, adormecidos, npcs, drp, homologado]
status: homologado
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

### Regra homologada para sucessos excedentes

Quando uma ação ofensiva conserva mais de 1 sucesso líquido depois de qualquer defesa do PJ, o primeiro sucesso faz a ação produzir seu efeito-base. **A cada 2 sucessos líquidos excedentes além do primeiro, soma-se +1 sucesso automático ao dano/efeito.**

A conversão player-faced **não volta a acrescentar dados de dano** como fazia a regra original de M20. Essa regra é geral e, por isso, não precisa ser reescrita dentro de cada ação da ficha.

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
6

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

- `6` é o default esparso para uma tarefa sem oposição especial.
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

6
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

A competência de Intimidação não vira R ou P Social. Como ação própria do Bandido, porém, `Manipulação 2 + Intimidação 1 = 3d D6` é pré-convertida pela régua ofensiva para:

```text
Intimidar: 1S
```

O efeito continua sendo resolvido pelo procedimento social original pertinente; a ficha apenas elimina a rolagem do ST.

## 2.3 Ações físicas

Os ataques corpo a corpo usam `Destreza 2 + Briga/Armas Brancas 2 = 4d` em Dificuldade 6.

Na calibração ofensiva já realizada, `4d D6` produz **2 sucessos fixos de ação**.

Os pools-base de dano produzem:

- 2d C → efeito-base 1C;
- 4d C → efeito-base 2C;
- 3d L → efeito-base 1L.

A relação entre qualidade do acerto e dano é tratada pela regra geral homologada de sucessos excedentes: o primeiro sucesso líquido ativa o efeito-base e cada 2 sucessos excedentes acrescentam +1 sucesso automático ao dano/efeito. Não há aumento de dados.

A ficha registra apenas a ação e seu efeito-base:

```text
Ações:
Soco: 2S + 1C
Arma de Impacto: 2S + 2C
Arma de Corte: 2S + 1L
Intimidar: 1S
```

Esses valores são pré-convertidos; o ST não consulta os pools originais durante a cena.

### Limite conhecido do método

Quando o PJ usa uma defesa ativa que M20 já permite, ela continua sendo aplicada normalmente contra os sucessos fixos da ação.

Quando não há defesa ativa, a ação fixa comprime a antiga variância do ataque do NPC. Essa perda de variância já foi medida nos estudos matemáticos gerais e permanece registrada como limitação do método player-faced. Ela **não reabre calibração por NPC**.

O Bandido usa, portanto, a mesma régua de conversão que os demais NPCs: nenhum dado volta ao ST e nenhuma defesa nova é criada para o PJ.

## 2.4 Ficha player-faced candidata

> **Status:** convertida pela régua DRP homologada para o projeto.

### BANDIDO COMUM

Brigão de rua acostumado a intimidação, violência rápida e armas improvisadas. É capaz de perceber movimentações óbvias e se defender fisicamente, mas não possui proteção especial nem treinamento sofisticado.

**Bloco Mecânico:**

```text
6

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
Arma de Corte: 2S + 1L
Intimidar: 1S

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

- [x] Intimidação convertida como ação própria sem transformar competência ofensiva em defesa Social;
- [x] limitação estatística de ações sem defesa ativa registrada no nível do método, sem recalibração individual.

### Gate

**BANDIDO COMUM: CONCLUÍDO PARA O PT-1.**

A ficha já contém os valores necessários para o ST operar o perfil sem consultar pools originais ou rolar dados.

**Próximo perfil: Durão Profissional.**


---

# 3. Durão Profissional

## 3.1 Fonte consolidada

O perfil canônico representa máfia, mercenários e segurança de elite. A própria fonte é uma faixa de competência, portanto a conversão preserva faixas onde o M20 também as preserva.

Valores relevantes:

- Destreza 3;
- Vigor 3;
- Manipulação 4;
- Percepção 2–4;
- Raciocínio 3–4;
- Armas Brancas 1–3;
- Armas de Fogo 3–5;
- Artes Marciais 0–4;
- Briga 3–4;
- Esportes 2–4;
- Furtividade 2;
- Intimidação 3;
- Lábia 2;
- Manha 3–5;
- Prontidão 2;
- Força de Vontade 6;
- Vitalidade padrão humana;
- Kevlar leve ou pesado, com 6–8 dados totais de absorção;
- Pistola Pesada 4L, Dificuldade 6;
- Submetralhadora 5L, Dificuldade 7;
- Briga 4C.

## 3.2 Conversão pela régua DRP

### Físico

A defesa ativa usa `Destreza 3 + Esportes 2–4 = 5d–7d`.

Pela tabela D/R:

- 5d–6d → `6/2`;
- 7d → `7/2`.

A absorção total de 6d–8d converte a Proteção Contundente em `C2–3`.

Como o personagem é Adormecido, Vigor não protege contra Letal. O Kevlar explicitamente acrescenta 3d–5d de absorção; essa parcela de armadura converte em `L1–2`.

Sem proteção específica contra Agravado:

```text
Físico: 6/2–7/2/C2–3·L1–2·A0
```

Ao instanciar um Durão concreto, escolhe-se uma combinação coerente dentro dessas faixas e a ficha usada em mesa mostra apenas os valores escolhidos.

### Mental/Técnico

Percepção 2–4 + Prontidão 2 produz 4d–6d para alerta:

```text
Percepção/Alerta: 7/1–6/2
```

Furtividade usa Destreza 3 + Furtividade 2 = 5d D6:

```text
Furtividade: 2S
```

### Social

Competências ofensivas sociais permanecem ações, não defesa genérica.

Manipulação 4 + Intimidação 3 = 7d D6:

```text
Intimidar: 3S
```

Manipulação 4 + Lábia 2 = 6d D6:

```text
Lábia: 2S
```

O default defensivo Social permanece `6` na ausência de uma oposição social específica já definida pelo procedimento original.

### Iniciativa

A conversão produz uma faixa de **12–13**, conforme Raciocínio 3–4.

A ficha concreta registra somente o valor escolhido:

```text
Iniciativa: 12 ou 13
```

## 3.3 Ações de combate

### Briga

Destreza 3 + Briga 3–4 = 6d–7d D6:

```text
Briga: 2–3S + 2C
```

O dano-base 4C converte para 2C. Sucessos excedentes seguem a regra geral homologada.

### Pistola Pesada

Destreza 3 + Armas de Fogo 3–5 = 6d–8d em Dificuldade 6:

```text
Pistola Pesada: 2–3S + 2L
```

### Submetralhadora

A mesma faixa de 6d–8d em Dificuldade 7 converte-se, pela régua ofensiva de pool + Dificuldade, em:

```text
Submetralhadora: 2S + 2L
```

O dano-base 5L converte para 2L. Qualquer aumento posterior vem apenas da regra geral homologada de sucessos excedentes.

## 3.4 Ficha player-faced candidata

> **Status:** HOMOLOGADO para o PT-1.

### DURÃO PROFISSIONAL

Mercenário, mafioso ou segurança de elite. É treinado para violência organizada, intimidação e operações discretas, podendo variar de um profissional competente a um operador de alto nível.

```text
6

Físico:
6/2–7/2/C2–3·L1–2·A0

Social:
6

Mental/Técnico:
6
Percepção/Alerta: 7/1–6/2

Mágicko/Poderes:
—

Ações:
Briga: 2–3S + 2C
Pistola Pesada: 2–3S + 2L
Submetralhadora: 2S + 2L
Furtividade: 2S
Intimidar: 3S
Lábia: 2S

Persistência:
Vitalidade padrão humana
OK, -1, -1, -2, -2, -5, Incapacitado

Recursos:
Força de Vontade 6

Iniciativa:
12–13

Características:
Profissional de combate
Kevlar leve ou pesado
Treinamento com armas de fogo
Pode operar de forma furtiva
Veículo comum
```

### Regra de instanciação

O Durão Profissional é um template de faixa. Antes da cena, o ST escolhe os valores da faixa que descrevem o NPC concreto. Depois disso, usa apenas os valores finais; não retorna aos Atributos/Habilidades originais para recalcular a ficha.

## 3.5 Gate do Durão Profissional

- [x] D/R físico convertido;
- [x] Proteção Contundente e Letal separadas pela origem Vigor/armadura;
- [x] Mental/Técnico relevante convertido;
- [x] ações físicas convertidas;
- [x] ações sociais e furtividade convertidas;
- [x] Iniciativa convertida;
- [x] Persistência e Força de Vontade preservadas;
- [x] homologação autoral do perfil.

**DURÃO PROFISSIONAL: CONCLUÍDO PARA O PT-1.**

**Próximo perfil: Policial de Rua.**


---

# 4. Policial de Rua

## 4.1 Fonte consolidada

O perfil canônico representa uma ronda policial comum.

Valores relevantes:

- Destreza 2;
- Vigor 3;
- Manipulação 3;
- Percepção 3;
- Inteligência 2;
- Raciocínio 3;
- Armas Brancas 2;
- Armas de Fogo 3;
- Briga 2;
- Computação 1;
- Conhecimento de Área 3;
- Direção 2;
- Direito 2;
- Esportes 2;
- Furtividade 1;
- Intimidação 1;
- Investigação 2;
- Manha 2;
- Prontidão 2;
- Tecnologia 2;
- Força de Vontade 5;
- Vitalidade padrão humana;
- colete Kevlar leve, com 5 dados totais de absorção;
- Pistola Pesada 4L;
- Bastão de Choque 3C;
- Taser com teste de Vigor do alvo para evitar atordoamento;
- rádio, algemas, spray de pimenta e autoridade institucional;
- possibilidade de escalar a resposta para reforços/SWAT.

## 4.2 Conversão pela régua DRP

### Físico

A defesa ativa usa:

`Destreza 2 + Esportes 2 = 4d`

Pela tabela D/R:

```text
7/1
```

A absorção Contundente total é 5d e converte para `C2`.

O personagem é Adormecido, portanto Vigor não absorve Letal. O Kevlar fornece 2d da absorção total declarada e essa parcela converte para `L1`.

Sem proteção específica contra Agravado:

```text
Físico: 7/1/C2·L1·A0
```

### Mental/Técnico

Percepção 3 + Prontidão 2 = 5d para percepção/alerta:

```text
Percepção/Alerta: 6/2
```

Percepção 3 + Investigação 2 = 5d D6 em investigações baseadas em observação:

```text
Investigar: 2S
```

Inteligência 2 + Conhecimento de Área 3 = 5d D6:

```text
Conhecimento de Área: 2S
```

Destreza 2 + Direção 2 = 4d D6:

```text
Dirigir: 2S
```

### Social

A autoridade policial permanece uma Característica, pois ela altera permissões, acesso e reação ficcional sem equivaler automaticamente a uma Resistência Social.

Manipulação 3 + Intimidação 1 = 4d D6:

```text
Intimidar: 2S
```

O default defensivo Social permanece `6` quando não houver oposição social específica definida pelo procedimento original.

### Iniciativa

A conversão produz:

`Destreza 2 + Raciocínio 3 + 6 = 11`

Na ficha final:

```text
Iniciativa: 11
```

## 4.3 Ações de combate

### Pistola Pesada

Destreza 2 + Armas de Fogo 3 = 5d D6:

```text
Pistola Pesada: 2S + 2L
```

### Bastão de Choque

Destreza 2 + Armas Brancas 2 = 4d D6.

O dano-base de 3C converte para 1C. Qualquer aumento por qualidade do acerto usa a regra geral homologada de sucessos excedentes, sem acrescentar dados:

```text
Bastão de Choque: 2S + 1C
```

### Taser

O corpus consolidado registra a consequência do equipamento — teste de Vigor do alvo para evitar atordoamento — mas não traz, neste documento, uma dificuldade numérica específica nem uma linha própria de dano.

A ficha preserva apenas o que está sustentado:

```text
Taser: ao atingir, o PJ faz o teste de Vigor previsto pela regra do equipamento para evitar atordoamento
```

A ausência da dificuldade numérica fica registrada como lacuna de fonte, sem inventar um valor para completar a ficha.

## 4.4 Ficha player-faced candidata

> **Status:** HOMOLOGADO para o PT-1.

### POLICIAL DE RUA

Agente de ronda treinado para perceber problemas, conter suspeitos, investigar ocorrências simples e escalar rapidamente a resposta quando a situação foge ao controle.

```text
6

Físico:
7/1/C2·L1·A0

Social:
6

Mental/Técnico:
6
Percepção/Alerta: 6/2

Mágicko/Poderes:
—

Ações:
Pistola Pesada: 2S + 2L
Bastão de Choque: 2S + 1C
Investigar: 2S
Conhecimento de Área: 2S
Dirigir: 2S
Intimidar: 2S
Taser: ao atingir, teste de Vigor do PJ para evitar atordoamento

Persistência:
Vitalidade padrão humana
OK, -1, -1, -2, -2, -5, Incapacitado

Recursos:
Força de Vontade 5

Iniciativa:
11

Características:
Autoridade policial
Colete Kevlar leve
Rádio de patrulha
Algemas
Spray de pimenta
Taser
Pode chamar reforços e escalar a resposta para SWAT/Choque
```

## 4.5 Escalada para SWAT/Choque

A fonte trata SWAT/Choque como **escalada de resposta**, não como ficha canônica independente neste corpus. Portanto, ela permanece ligada ao Policial de Rua como consequência de escalada:

- fuzil de assalto: 6L;
- colete tático reforçado: 8 dados totais de absorção;
- blindado de transporte.

Esses números não são completados por inferência em uma nova ficha de SWAT porque o corpus consolidado não fornece os demais Atributos/Habilidades necessários para uma conversão completa.

## 4.6 Gate do Policial de Rua

- [x] D/R físico convertido;
- [x] Proteção Contundente e Letal separadas;
- [x] Percepção/Alerta convertida;
- [x] ações profissionais recorrentes convertidas;
- [x] Pistola e Bastão convertidos;
- [x] Iniciativa convertida;
- [x] Persistência e Força de Vontade preservadas;
- [x] autoridade institucional preservada como Característica;
- [x] escalada SWAT preservada sem inventar ficha ausente;
- [ ] dificuldade numérica específica do teste de Vigor do Taser não está presente no corpus consolidado;
- [x] homologação autoral do perfil.

**POLICIAL DE RUA: CONCLUÍDO PARA O PT-1.**

A lacuna do Taser permanece documental e não bloqueia a conversão do perfil.

**Próximo perfil: Agente do Governo.**


---

# 5. Agente do Governo

## 5.1 Fonte consolidada

O perfil canônico representa agentes de FBI, CIA, NSA e equivalentes. Assim como o Durão Profissional, é um template em faixa.

Valores relevantes:

- Destreza 2–3;
- Vigor 3–4;
- Manipulação 3–5;
- Percepção 3–4;
- Inteligência 3–4;
- Raciocínio 3–5;
- Armas Brancas 2–3;
- Armas de Fogo 3–4;
- Artes Marciais 1–3;
- Briga 2–3;
- Computação 2–3;
- Consciência 1;
- Direção 2–3;
- Direito 4;
- Enigmas 1–3;
- Erudição 3;
- Esportes 2;
- Furtividade 2;
- Investigação 3–5;
- Manha 3;
- Mídia 1–3;
- Pesquisa 2–4;
- Política 2–4;
- Prontidão 3;
- Tecnologia 2–4;
- Força de Vontade 7;
- Vitalidade padrão humana;
- colete oculto à prova de balas, com 5 dados totais de absorção declarados;
- Pistola Pesada 4L;
- Submetralhadora Leve 5L.

## 5.2 Conversão pela régua DRP

### Físico

A defesa ativa usa:

`Destreza 2–3 + Esportes 2 = 4d–5d`

Pela tabela D/R:

```text
7/1–6/2
```

A absorção total declarada é 5d, portanto a Proteção Contundente é `C2`.

Como o Agente é Adormecido, Vigor não absorve Letal. A fonte não discrimina de forma estável quantos dos 5 dados totais vêm do colete quando o template usa Vigor 3–4. Isso deixa a parcela Letal do colete entre 1d e 2d, que pela régua atual equivale a `L0–1`.

Sem proteção específica contra Agravado:

```text
Físico: 7/1–6/2/C2·L0–1·A0
```

Ao instanciar um agente concreto, escolhe-se uma combinação coerente da faixa e a ficha usada em mesa mostra apenas o valor final.

### Mental/Técnico

Percepção 3–4 + Prontidão 3 = 6d–7d:

```text
Percepção/Alerta: 6/2–7/2
```

Percepção 3–4 + Investigação 3–5 = 6d–9d em investigações baseadas em observação:

```text
Investigar: 2–4S
```

Inteligência 3–4 + Computação 2–3 = 5d–7d:

```text
Computação: 2–3S
```

Inteligência 3–4 + Tecnologia 2–4 = 5d–8d:

```text
Tecnologia: 2–3S
```

Destreza 2–3 + Furtividade 2 = 4d–5d:

```text
Furtividade: 2S
```

Destreza 2–3 + Direção 2–3 = 4d–6d:

```text
Dirigir: 2S
```

### Social

A autoridade federal e o acesso institucional permanecem como Características.

A ficha possui Manipulação 3–5, Direito 4, Manha 3 e Política 2–4. Como essas competências podem sustentar ações sociais diferentes, são convertidas apenas onde a função é clara:

```text
Direito: 3S
Manha: 2–3S
Política: 2–4S
```

O default defensivo Social permanece `6` quando não houver uma oposição social específica prevista pelo procedimento original.

### Iniciativa

A conversão produz uma faixa de **11–14**, conforme Destreza 2–3 e Raciocínio 3–5.

Na ficha concreta aparece apenas o valor escolhido:

```text
Iniciativa: 11–14
```

## 5.3 Ações de combate

### Pistola Pesada

Destreza 2–3 + Armas de Fogo 3–4 = 5d–7d em Dificuldade 6:

```text
Pistola Pesada: 2–3S + 2L
```

### Submetralhadora Leve

A mesma parada-base de 5d–7d em Dificuldade 7 produz:

```text
Submetralhadora Leve: 2S + 2L
```

Sucessos excedentes seguem a regra geral homologada: depois do primeiro sucesso líquido, cada 2 sucessos excedentes acrescentam +1 sucesso automático ao dano/efeito. A ficha não adiciona dados de dano.

## 5.4 Ficha player-faced candidata

> **Status:** HOMOLOGADO para o PT-1.

### AGENTE DO GOVERNO

Investigador federal, operador de inteligência ou agente de segurança nacional. É perigoso menos por força bruta isolada e mais pela combinação de investigação, vigilância, acesso institucional, preparo técnico e capacidade de escalar uma situação.

```text
6

Físico:
7/1–6/2/C2·L0–1·A0

Social:
6

Mental/Técnico:
6
Percepção/Alerta: 6/2–7/2

Mágicko/Poderes:
—

Ações:
Pistola Pesada: 2–3S + 2L
Submetralhadora Leve: 2S + 2L
Investigar: 2–4S
Computação: 2–3S
Tecnologia: 2–3S
Furtividade: 2S
Dirigir: 2S
Direito: 3S
Manha: 2–3S
Política: 2–4S

Persistência:
Vitalidade padrão humana
OK, -1, -1, -2, -2, -5, Incapacitado

Recursos:
Força de Vontade 7

Iniciativa:
11–14

Características:
Autoridade federal
Treinamento investigativo
Vigilância e coleta de informação
Colete oculto à prova de balas
Dispositivos de vigilância
Acesso institucional
Pode escalar a resposta para operações maiores
```

### Regra de instanciação

O Agente do Governo é um template em faixa. Antes da cena, o ST escolhe os valores que descrevem aquele agente concreto. A ficha em uso registra apenas os valores finais e não exige retorno aos Atributos/Habilidades de origem.

## 5.5 Gate do Agente do Governo

- [x] D/R físico convertido;
- [x] Proteção Contundente convertida;
- [x] faixa Letal do colete preservada sem inventar uma decomposição única;
- [x] Percepção/Alerta convertida;
- [x] competências investigativas e técnicas recorrentes convertidas;
- [x] competências sociais funcionais convertidas como ações;
- [x] Pistola e Submetralhadora convertidas;
- [x] Iniciativa convertida;
- [x] Persistência e Força de Vontade preservadas;
- [x] autoridade e acesso institucional preservados como Características;
- [x] homologação autoral do perfil.

**AGENTE DO GOVERNO: CONCLUÍDO PARA O PT-1.**

---

# 6. Fechamento do PT-1

Os cinco perfis canônicos de Pessoas Comuns / Adormecidos foram convertidos e homologados:

- [x] Cidadão Típico;
- [x] Bandido Comum;
- [x] Durão Profissional;
- [x] Policial de Rua;
- [x] Agente do Governo.

O Storyteller já pode operar esses perfis sem rolar dados nem reconstruir as paradas originais durante a cena. Faixas presentes nas fichas originais permanecem como faixas de template e são escolhidas antes do uso do NPC concreto.

As limitações estatísticas já conhecidas da compressão ofensiva permanecem registradas no método geral e não reabrem cada perfil individualmente.

**PT-1 — CONCLUÍDO E HOMOLOGADO.**

**Próximo pacote: PT-2 — Animais e Bestiário Mundano.**
