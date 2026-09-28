---
type: estudo
status: em_revisao_corretiva
summary: "PT-8 reaberto após auditoria: camada física reaproveitável preservada; conjuração, contramágika ativa e Reação de Paradoxo retornam a dívidas abertas."
tags: [player-faced, pt-8, despertos, magika, arete, esferas, paradoxo, drp]
---

# PT-8 — Despertos e Usuários de Mágika

## Nota de revisão corretiva

A versão anterior propagou por analogia a régua de ações físicas para Arete, contramágika ativa e Reação de Paradoxo. Essa propagação foi retirada.

Este arquivo agora separa a camada física/mundana reaproveitável das dívidas mágickas já reconhecidas pelo Contrato e pelo Estudo 14.

A revisão das regras de dano confirmou uma correção importante: **Magos/Despertos podem absorver dano Letal com Vigor**. Portanto, para Terno Preto, Hacktivista, Músico Xamã, Pelourinho, Colmeia, Widderslainte e Homem de Cinza, a Proteção Letal usa o pool total de absorção aplicável, não apenas a parcela de armadura.

## 1. Regra de condução

Este pacote não cria um segundo motor para mágika.

O corpo, as competências mundanas, iniciativa, Proteção e Persistência usam as mesmas regras já homologadas para os demais NPCs.

A diferença é que um Desperto possui **Arete, Esferas, paradigma/focos, recursos e consequências mágickas próprias**. Esses elementos permanecem visíveis e não são dissolvidos no Perfil DRP.

A ficha final precisa ser menor que a ficha original. Portanto, não se converte cada Habilidade em Ação e não se lista um catálogo de todos os Efeitos possíveis das Esferas.

---

## Decisão autoral de 2026-09-28 — forma do Efeito mágicko

A saída player-faced da mágika de NPC deve ser expressa como **Efeito + sucessos já produzidos**, por exemplo:

```text
Efeito de Mente: 3S
```

Esses sucessos representam a força efetiva do Efeito que alcança o personagem jogador.

Quando a regra original concede ao PJ uma resistência, defesa, contramágika, Força de Vontade, Avatar ou procedimento equivalente, o jogador usa **essa mesma operação de M20** para reduzir, cancelar ou resistir aos sucessos do Efeito.

Quando a regra original não concede uma rolagem ao PJ, o contrato atual não autoriza criar uma apenas para acomodar a conversão. Nesse caso, o Efeito chega com seus sucessos fixos e produz a consequência prevista pela regra original.

Ainda falta definir o operador que transforma a antiga conjuração do NPC em `N S` para o Efeito, preservando Arete, dificuldade e modificadores sem reabrir uma rolagem do ST.

A **Reação de Paradoxo** permanece deliberadamente aberta e deve ser repensada separadamente.

---

## Decisão autoral de 2026-09-28 — operador simples de conjuração

A mágika de NPC usa uma quantidade-base de sucessos derivada de Arete e recebe **no máximo um ajuste simples de ±1S conforme o julgamento do Storyteller sobre as condições da conjuração**.

Não existem estados formais separados de “normal/favorável/desfavorável”, nem soma de vários modificadores circunstanciais. A regra é apenas:

```text
sucessos-base do Efeito
→ se as condições ajudarem claramente: +1S
→ se as condições atrapalharem claramente: -1S
→ caso contrário: sem ajuste
```

O Storyteller julga isso pela ficção e pelos elementos que M20 normalmente faria pesar na conjuração — Coincidente/Vulgar, testemunhas, preparação, Quintessência, instrumentos, pressão, fast-casting e equivalentes — sem reconstruir a conta original de dificuldade.

A saída continua sendo:

```text
Efeito de [Esfera]: N S
```

O PJ usa somente resistências, contramágika, Força de Vontade, Avatar, soak ou outras operações que M20 já lhe conceda. Se a regra original manda sucessos do PJ cancelar sucessos do Efeito, eles cancelam esses `S`.

### Tabela-base homologada

Para manter a regra no mesmo grau de simplicidade decidido pelo autor, a proposta é usar **somente Arete para definir os sucessos-base**:

| Arete | Sucessos-base do Efeito |
| :---: | :---: |
| 1–3 | 1S |
| 4–6 | 2S |
| 7–8 | 3S |
| 9–10 | 4S |

A tabela não cria um novo cálculo em mesa. Sua aplicação a Arete foi **homologada explicitamente pelo autor em 2026-09-28** como regra específica deste subsistema.

Depois de obter os sucessos-base, o Storyteller apenas julga a situação:

- se as condições claramente favorecem a conjuração, acrescenta **+1S**;
- se claramente a prejudicam, reduz **-1S**;
- caso não haja razão forte para ajuste, usa o valor-base.

Isso é descrição de julgamento, não uma taxonomia de três estados nem uma soma de modificadores. O valor final nunca pode ser menor que 0S.

As Esferas continuam definindo **o que o NPC é capaz de fazer**. Requisitos mínimos de sucessos, dano, cura, duração, resistências e demais consequências continuam seguindo M20.

A tabela substitui as linhas pendentes de conjuração das fichas abaixo.

---

## Decisão autoral de 2026-09-28 — Reação de Paradoxo de NPC em um único dado

A Reação de Paradoxo de NPC usa **um único d10**, rolado por um jogador em nome da realidade.

```text
rola 1d10
se resultado ≤ Paradoxo atual do NPC
→ a Reação de Paradoxo dispara
se resultado > Paradoxo
→ não dispara
```

Quanto maior a reserva de Paradoxo do NPC, maior a chance de a realidade reagir.

Essa rolagem:

- não pertence ao personagem jogador;
- não usa Atributo, Habilidade, Arete, recurso ou ação do PJ;
- não concede escolha sobre a severidade ou a consequência;
- existe apenas para preservar a incerteza e a diversão da Reação sem rolagem do Storyteller.

A forma concreta da consequência quando a Reação dispara ainda deve reutilizar as categorias e efeitos de M20 sem inventar uma nova tabela antes da revisão específica.

---

# 2. Estado da mágika de NPC após revisão corretiva

A auditoria confirmou que o operador físico `pool + Dificuldade → S fixos` **não pode ser propagado por analogia** para Arete.

Portanto:

- **mágika hostil unilateral do NPC** deve terminar em um Efeito com sucessos fixos; falta definir e homologar o operador que produz esses sucessos;
- **contramágika ativa do NPC** permanece candidata a transformação por oposição, mas não está homologada;
- **Reação de Paradoxo** possui gatilho homologado em 1d10 ≤ Paradoxo; resta apenas revisar a tradução das consequências quando disparar;
- Arete, Esferas, paradigmas, focos, Quintessência e demais recursos permanecem registrados sem serem convertidos automaticamente;
- Contramágika Inata mantém a decisão autoral explícita do PT-7: reduz diretamente a parada do PJ quando aplicável.

Quando a mágika do NPC acionar uma rolagem que **já pertence ao PJ** na regra original, essa rolagem do jogador é preservada sem alteração.

Nenhuma tabela `Arete + Dificuldade → S` é regra vigente ainda; a forma de saída `Efeito: N S` está aprovada, mas o operador de derivação continua pendente.

---

# 3. Dano, cura, duração e Paradoxo

As regras originais de dano, cura, duração, classificação Coincidente/Vulgar, testemunhas e geração de Paradoxo permanecem registradas como fonte.

Elas só podem ser aplicadas ao NPC quando houver uma forma homologada de obter os sucessos da conjuração sem rolagem do ST e sem criar nova operação para o PJ.

O **gatilho da Reação de Paradoxo** está homologado em 1d10 ≤ Paradoxo. A tradução das consequências após o disparo permanece aberta até revisão específica.

---

## Decisão autoral de 2026-09-28 — contramágika ativa do NPC

A releitura da regra-fonte confirma que a contramágika básica:

- consome ação completa;
- exige perceber o Efeito;
- exige ao menos 1 ponto em uma Esfera pertinente;
- usa Arete;
- cada sucesso cancela 1 sucesso do Efeito.

Como o projeto já homologou uma única graduação `Arete → S` para mágika de NPC, a proposta de maior simplicidade é **não criar uma segunda tabela apenas para contramágika**.

```text
NPC usa Contramágika
→ verifica requisitos da regra original
→ gasta a ação completa
→ usa seus S-base de Arete
→ cada S cancela 1 sucesso do Efeito do PJ
→ o Storyteller pode ajustar ±1S se as condições claramente ajudarem ou atrapalharem
```

Exemplo:

```text
NPC Arete 6
Conjuração-base: 2S

usa Contramágika
→ 2S de cancelamento
→ se as circunstâncias atrapalham claramente: 1S
→ se ajudam claramente: 3S
```

Isso preserva a função da regra — **cancelar sucessos por ação ativa** — e a economia de ações, sem introduzir uma nova gramática ou uma nova tabela.

### Aegis / Certámen

A mesma leitura resolveria o Aegis do NPC:

```text
PJ rola Gladius normalmente
→ NPC declara Aegis e gasta sua ação
→ S-base de Arete do NPC cancelam sucessos do Gladius
→ excedente reduz o Locus normalmente
```

O Gladius do PJ, o Locus e a escolha de usar Aegis permanecem intactos.

### Proteger outro / refletir

As variantes que protegem outro alvo ou refletem o Efeito preservam seus requisitos adicionais de Prime, Quintessência e ação completa.

A proposta é **não criar tabelas D8/D9 separadas**. A dificuldade adicional da operação entra no mesmo julgamento circunstancial simples de ±1S quando o Storyteller considerar que ela torna a execução claramente mais difícil.

### Unweaving por NPC

Quando um NPC desfaz um Efeito persistente, a mesma unidade pode ser usada por intervalo:

```text
Integridade mágicka = sucessos armazenados do Efeito
NPC usa S-base de Arete por intervalo de unweaving
→ reduz a Integridade
```

Os requisitos de Prime, Esferas, tempo e Quintessência permanecem os da fonte.

Esta regra foi **homologada explicitamente pelo autor em 2026-09-28**. Ela resolve contramágika básica, Aegis e unweaving com a mesma graduação de Arete já usada pela conjuração do NPC, sem criar outra tabela.

---

# 4. Contramágika

## Contramágika do PJ

Preservar exatamente a rolagem normal do jogador quando a regra original a concede.

## Contramágika ativa do NPC

Regra homologada:

```text
NPC declara Contramágika
→ cumpre os requisitos da regra original
→ gasta ação completa
→ usa seus S-base de Arete
→ cada S cancela 1 sucesso do Efeito
→ ST pode ajustar ±1S quando as condições claramente ajudarem ou atrapalharem
```

Contramágika ativa continua sendo ação, não Proteção passiva.

## Contramágika Inata

Decisão autoral explícita já vigente:

```text
pool de Contramágika Inata
→ reduz diretamente a parada do PJ quando aplicável
```

Nenhum dado é rolado pelo ST.

---

# 5. Recursos, focos e paradigma

Arete, Esferas, paradigma/focos, Força de Vontade, Quintessência quando fornecida e demais recursos permanecem como propriedades próprias do NPC.

Nenhuma reserva ausente é inventada.

---

# 6. Regra de leitura dos perfis abaixo

Os blocos a seguir preservam apenas:

- conversões físicas/mundanas já cobertas;
- recursos e estados da fonte;
- poderes específicos que já vêm com procedimento próprio.

Linhas que dependam de uma rolagem de Arete do ST permanecem marcadas como **pendentes**, em vez de receber sucessos fixos por analogia.

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
Conjuração-base: 1–2S pelo Arete; ST pode ajustar ±1S pelas condições

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
Conjuração-base: 1–2S pelo Arete; ST pode ajustar ±1S pelas condições

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
Conjuração-base: 1–2S pelo Arete; ST pode ajustar ±1S pelas condições

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
Conjuração-base: 2S; ST pode ajustar ±1S pelas condições

Ações:
Chicote de Carne: 3S + 3L
Sino Silencioso: extingue som/comunicação em 10 m conforme a fonte; preservar como poder específico
Gaiola de Borboletas: Efeito de Entropia/Espírito; usar Conjuração-base de Pelourinho e ajustar ±1S pelas condições

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
Conjuração-base: 3S; ST pode ajustar ±1S pelas condições

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
Conjuração-base: 1S; ST pode ajustar ±1S pelas condições

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
Conjuração-base: 2S; ST pode ajustar ±1S pelas condições

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
- [x] mágika de NPC: sucessos-base derivados de Arete e ajuste circunstancial simples de ±1S;
- [x] dano/cura/duração originais preservados, condicionados a uma futura transformação homologada da conjuração do NPC;
- [x] resistências e defesas do PJ preservadas quando já existiam;
- [x] nenhuma defesa nova foi criada para o PJ;
- [x] contramágika ativa do NPC usa S-base de Arete; cada S cancela 1 sucesso do Efeito, preservando requisitos e ação completa;
- [x] Contramágika Inata preservada como redução direta de dados;
- [x] geração de Paradoxo preservada;
- [x] gatilho da Reação de Paradoxo definido: 1d10 ≤ Paradoxo;
- [ ] consequências da Reação de Paradoxo após o disparo ainda exigem revisão específica;
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

A camada física/mundana, os recursos canônicos e a conjuração dos sete perfis estão preservados em forma player-faced. O pacote ainda depende apenas da tradução final das **consequências da Reação de Paradoxo**.

**PT-8: CONJURAÇÃO E CONTRAMÁGIKA ATIVA HOMOLOGADAS; CONSEQUÊNCIAS DE PARADOXO AINDA ABERTAS.**
