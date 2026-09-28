---
type: estudo
status: em_andamento
summary: "PT-8: conversão em lote de Despertos e usuários de mágika, usando a régua DRP existente e sucessos fixos para as antigas rolagens de Arete do ST."
tags: [player-faced, pt-8, despertos, magika, arete, esferas, paradoxo, drp]
---

# PT-8 — Despertos e Usuários de Mágika

## 1. Regra de condução

Este pacote não cria um segundo motor para mágika.

O corpo, as competências mundanas, iniciativa, Proteção e Persistência usam as mesmas regras já homologadas para os demais NPCs.

A diferença é que um Desperto possui **Arete, Esferas, paradigma/focos, recursos e consequências mágickas próprias**. Esses elementos permanecem visíveis e não são dissolvidos no Perfil DRP.

A ficha final precisa ser menor que a ficha original. Portanto, não se converte cada Habilidade em Ação e não se lista um catálogo de todos os Efeitos possíveis das Esferas.

---

# 2. Operador geral de mágika do NPC

A antiga rolagem de Arete do ST é tratada como qualquer outra ação própria do Obstáculo:

```text
definir o Efeito
→ calcular a Dificuldade normal de M20
→ aplicar modificadores normais
→ Arete + Dificuldade real
→ converter pela régua já homologada pool + Dificuldade → S fixos
→ usar esses S como sucessos da conjuração
```

Isso vale tanto para Efeitos hostis quanto utilitários.

O jogador não ganha nova defesa. Se a regra original já lhe concede Força de Vontade, contramágika, absorção, resistência de Esfera ou outra reação, ela continua existindo exatamente como antes.

Se não havia reação do PJ, os S fixos resolvem a antiga rolagem unilateral do NPC do mesmo modo que já foi aceito para outras ações de NPC.

### 2.1 Tabela curta para Arete 3–7

A tabela abaixo apenas materializa o operador ofensivo já homologado para a faixa de Arete presente neste corpus. Não é uma calibração nova.

| Arete | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 3 | 2S | 2S | 2S | 1S | 1S | 1S | 0S | 0S |
| 4 | 3S | 2S | 2S | 2S | 1S | 1S | 1S | 0S |
| 5 | 4S | 3S | 3S | 2S | 2S | 1S | 1S | 0S |
| 6 | 4S | 4S | 3S | 2S | 2S | 1S | 1S | 0S |
| 7 | 5S | 4S | 4S | 3S | 2S | 2S | 1S | 0S |

`0S` significa que, naquela combinação, a compressão determinística não produz sucesso. O NPC precisa alterar as condições da conjuração — preparação, Quintessência, foco ou outra redução de Dificuldade prevista em M20 — se quiser alcançar um resultado diferente.

A perda da cauda probabilística de sucesso/botch em dificuldades extremas é a mesma limitação conhecida da compressão de rolagens exclusivas do ST e não abre um estudo por NPC.

---

# 3. Efeito, dano e duração

Os S da conjuração alimentam diretamente as regras originais.

Para dano/cura:

```text
1S de Arete → 2 níveis de dano/cura
```

O tipo C/L/A continua definido pela origem do Efeito e pelo uso de Primórdio/Quintessência quando a regra exigir.

Para duração:

```text
1S → 1 turno
2S → 1 cena
3S → 1 dia
4S → 1 história
5S+ → permanente, com o custo previsto
```

Se um Efeito exigir sucessos mínimos ou ação estendida, os S fixos são aplicados ao mesmo requisito. Não se cria um Relógio adicional além de uma eventual interface visual dos sucessos já exigidos.

---

# 4. Contramágika

## PJ usa contramágika

Preservar a rolagem normal do PJ.

## NPC usa contramágika básica

O NPC consome a ação completa normalmente.

```text
Arete do NPC em D7
→ S fixos pela tabela
→ cada S cancela 1 sucesso da conjuração do PJ
```

Prime, Quintessência e dificuldades 8/9 das variações protetora/ofensiva permanecem quando aplicáveis.

## Contramágika Inata

Mantém a decisão já homologada no PT-7:

```text
pool de Contramágika Inata
→ reduz diretamente a parada do PJ quando aplicável
```

Nenhum dado é rolado pelo ST.

---

# 5. Paradoxo do NPC

A geração normal permanece ligada à classificação Coincidente/Vulgar e aos resultados da conjuração.

Como a conjuração do NPC usa S fixos, `0S` é tratado como falha simples para operação player-faced. A compressão não cria um botch artificial.

Quando uma Reação de Paradoxo precisar ser resolvida, a antiga rolagem `Paradoxo d10, D6` é igualmente comprimida pela régua geral de sucessos fixos. Os S resultantes consultam **as mesmas faixas de consequência** da regra original.

Essa decisão elimina a última rolagem exclusiva do ST nesse procedimento sem transferi-la ao jogador. Resultados extremos tornam-se menos frequentes sob a compressão determinística; isso é registrado como limitação geral do método, não como blocker individual.

Desauridos permanecem imunes ao acúmulo e às reações comuns de Paradoxo conforme a fonte.

---

# 6. Quintessência, focos e paradigma

A reserva de Quintessência permanece recurso próprio quando a ficha/fonte fornecer um valor.

Os perfis consolidados deste corpus registram Arete, Esferas e paradigmas/focos, mas **não fornecem uma quantidade de Quintessência para todos os NPCs**. Nenhum valor é inventado.

Quando um custo de Quintessência for necessário, o NPC só o assume se a cena/fonte lhe atribuir uma reserva disponível.

Focos, tempo adicional, fast-casting e demais modificadores continuam alterando a Dificuldade antes da consulta à tabela de S.

---

# 7. Perfis convertidos em lote

## 7.1 Terno Preto

```text
TERNO PRETO

6

Físico:
6/2/C3·L3·A0

Mental/Técnico:
6
Percepção/Alerta: 7/3

Mágicko/Poderes:
Arete 3–5
Mente 2 + 2–4 Esferas entre níveis 2–4
Conjuração: S fixos por Arete + Dificuldade

Ações:
Arma de Energia: 2–3S + efeito da arma

Persistência:
OK, OK, OK, -1, -2, -2, -5, Vaporizado

Recursos:
Força de Vontade 8

Iniciativa:
12

Características:
Agente Iluminado da NOM
Aura de Medo: PJ testa Força de Vontade em D5 + 1 por Terno Preto, máximo D10
Terno balístico de alta densidade
Furtividade e investigação excepcionais
Dissolve-se após a morte
Procedimentos tecnomágickos
```

---

## 7.2 Hacktivista Desperto

```text
HACKTIVISTA DESPERTO

6

Físico:
6/2/C2·L2·A0

Mental/Técnico:
6
Percepção/Alerta: 6/2

Mágicko/Poderes:
Arete 3–4
Correspondência/Dados 3
Forças 2
Mente 2
Entropia ou Tempo 2
Conjuração: S fixos por Arete + Dificuldade

Ações:
Pistola leve: 2S + efeito da arma

Persistência:
OK, -1, -1, -2, -2, -5, Incapacitado

Recursos:
Força de Vontade 7

Iniciativa:
13

Características:
Hacker de realidade
Computação excepcional
Hacking de Realidade e Cibernética
Dispositivos trinários
Paradigma: Tudo são Dados / A Tecnologia é a Resposta
```

---

## 7.3 Músico Xamã Urbano

```text
MÚSICO XAMÃ URBANO

6

Físico:
7/1/C2·L2·A0

Mental/Técnico:
6
Percepção/Alerta: 6/2

Mágicko/Poderes:
Arete 3–4
Espírito 3
Forças 2
Primórdio 1
Tempo 2
Conjuração: S fixos por Arete + Dificuldade

Ações:
Revólver leve: 2S + efeito da arma

Persistência:
OK, -1, -1, -2, -2, -5, Incapacitado

Recursos:
Força de Vontade 6

Iniciativa:
12

Características:
Mediação com espíritos urbanos
Música e canto como instrumentos
Xamanismo urbano
Paradigma: A Criação é Divina e está Viva
```

---

## 7.4 Pelourinho

```text
PELOURINHO

6

Físico:
7/1/C2·L2·A0

Mental/Técnico:
Percepção mundana: Efeito Zero
Percebe o ambiente por Correspondência e Mente

Mágicko/Poderes:
Arete 6
Correspondência 4
Entropia 3
Espírito 4
Forças 2
Mente 4
Primórdio 2
Conjuração: S fixos por Arete + Dificuldade

Ações:
Chicote de Carne: 3S + 3L
Sino Silencioso: extingue som/comunicação em 10 m conforme a fonte
Gaiola de Borboletas: Efeito de Entropia/Espírito; resolver pela conjuração

Persistência:
OK, OK, OK, OK, OK, -1, -5, Incapacitado

Recursos:
Força de Vontade 8

Iniciativa:
15

Características:
Desaurida
Cega e surda mundanamente
Imune a Paradoxo comum
Delírio Dinâmico altera a realidade local
```

---

## 7.5 Colmeia

```text
COLMEIA — POR CORPO

6

Físico:
6/1/C1·L1·A0

Mental/Técnico:
6
Percepção/Alerta: 7/2

Mágicko/Poderes:
Arete 7
Correspondência 5
Entropia 2
Espírito 2
Forças 2
Mente 5
Primórdio 2
Tempo 3
Vida 5
Conjuração: S fixos por Arete + Dificuldade

Persistência:
OK, -1, -1, -2, -2, -5, Incapacitado por corpo

Recursos:
Força de Vontade 8 compartilhada

Iniciativa:
13

Características:
Desaurido co-localizado
Dezenas de corpos podem existir simultaneamente
Todos compartilham ficha, Arete e Força de Vontade
Sonho 5 para as identidades
Mágika coincidente inconsciente
Imune a Paradoxo comum
```

---

## 7.6 Cultista Widderslainte

```text
CULTISTA WIDDERSLAINTE

6

Físico:
6/1/C1·L1·A0

Mental/Técnico:
6
Percepção/Alerta: 6/2

Mágicko/Poderes:
Arete 3
Entropia 2
Espírito 2
Vida 2
Conjuração: S fixos por Arete + Dificuldade

Ações:
Revólver leve: 2S + efeito da arma

Persistência:
OK, -1, -1, -2, -2, -5, Incapacitado

Recursos:
Força de Vontade 5

Iniciativa:
10

Características:
Nefandus nato
Maleficia
Paradigma: Tudo é Caos / Viagem sem Volta para o Vazio
Diário de sigilos corruptos
```

---

## 7.7 Infiltrado na NOM / Homem de Cinza

```text
INFILTRADO NA NOM / HOMEM DE CINZA

6

Físico:
7/1/C3·L3·A0

Mental/Técnico:
6
Percepção/Alerta: 7/2

Mágicko/Poderes:
Arete 6
Ciência Dimensional 3
Correspondência/Dados 4
Entropia 3
Forças 3
Mente 4
Primórdio 3
Conjuração: S fixos por Arete + Dificuldade

Ações:
Pistola pesada: 3S + efeito da arma

Persistência:
OK, -1, -1, -2, -2, -5, Incapacitado

Recursos:
Força de Vontade 8

Iniciativa:
15

Características:
Nefandus infiltrado na NOM
Maleficia
Terno blindado corporativo
Hipertecnologia e infiltração
IVAE
Talismãs e ritos profanos
Paradigma: Viagem sem Volta para o Esquecimento
```

---

# 8. O que não virou Ação

Para manter as fichas enxutas:

- Computação, Investigação, Furtividade, Lábia, Intimidação, Política, Cosmologia e outras Habilidades não foram transformadas automaticamente em linhas de Ação;
- essas capacidades aparecem apenas quando definem um Perfil DRP realmente consultado ou uma Característica relevante;
- Esferas não viram uma lista de "feitiços";
- o ST cria/seleciona o Efeito normalmente dentro das Esferas e usa a única linha de Conjuração.

Isso preserva a abertura de M20 sem devolver a ficha original inteira ao ST.

---

# 9. Auditoria do pacote

- [x] corpo e competências mundanas convertidos pela régua DRP;
- [x] Arete preservado;
- [x] Esferas preservadas;
- [x] paradigmas/focos preservados;
- [x] Coincidente/Vulgar e testemunhas preservados;
- [x] modificadores de conjuração preservados;
- [x] antiga rolagem de Arete do NPC convertida para S fixos;
- [x] dano/cura/duração continuam derivados dos sucessos;
- [x] resistências e defesas do PJ preservadas quando já existiam;
- [x] nenhuma defesa nova foi criada para o PJ;
- [x] contramágika ativa do NPC convertida para S fixos em D7/D8/D9;
- [x] Contramágika Inata preservada como redução direta de dados;
- [x] geração de Paradoxo preservada;
- [x] Reação de Paradoxo sem rolagem do ST, usando S fixos em D6;
- [x] Desauridos preservam imunidade a Paradoxo;
- [x] sete perfis canônicos do PT-8 convertidos;
- [x] Terno Preto incorporado ao pacote correto;
- [x] fichas permanecem menores que as originais.

## Pendências documentais/editoriais

- [ ] conferir detalhes de contramágika contra M20 pp. 545–547 antes da publicação;
- [ ] conferir as tabelas completas de Paradoxo antes da publicação;
- [ ] valores universais de Quintessência não são inventados onde as fichas consolidadas não os fornecem;
- [ ] danos exatos de armas genéricas/equipamentos não especificados neste corpus devem vir da tabela de equipamento pertinente no produto final.

Nenhuma dessas pendências exige nova matemática.

## Gate

O Storyteller pode operar os sete Despertos do corpus com Arete, Esferas e efeitos mágickos sem rolar dados. A experiência do PJ permanece a mesma: suas próprias rolagens, resistências, soak, contramágika e recursos continuam sendo usados conforme M20.

**PT-8: MECANICAMENTE COMPLETO; AGUARDANDO HOMOLOGAÇÃO DO PACOTE.**
