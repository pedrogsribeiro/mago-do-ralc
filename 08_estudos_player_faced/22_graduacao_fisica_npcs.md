---
type: estudo
status: baseline_operacional
summary: "Graduação física preliminar de NPCs e Obstáculos a partir de fichas reais do corpus, usando D/R/P tipado e preservando camadas diegéticas."
tags: [player-faced, npc, obstaculo, graduacao, fisico, drp, diegese]
---

# Estudo 22 — Perfil DRP Multidimensional de NPCs e Obstáculos

## 1. Objetivo

Este estudo inicia a calibração **por NPC concreto** da assinatura física **D/R/P**, mas a ficha final é **multidimensional**.

A proposta operacional é evitar fórmulas universais durante a cena. Cada NPC ou Obstáculo recebe previamente **Perfis DRP** derivados de sua ficha original nas dimensões que realmente importam — **Físico, Social, Mental/Técnico e Mágicko/Poderes** — além de sua **Persistência** real quando houver Vitalidade, Integridade, Essência, Locus ou outra reserva equivalente.

O Storyteller consulta a assinatura pertinente quando uma ação exige resolução mecânica e consulta as demais camadas da ficha quando precisa interpretar, narrar ou decidir o comportamento da entidade.

As assinaturas são, portanto, um **núcleo mecânico compacto**, não a totalidade do NPC.

---

## 2. Convenções já homologadas usadas como baseline

### 2.1. Defesa ativa → D/R

| Parada original do NPC | D/R baseline |
| :---: | :---: |
| 2d | 6/1 |
| 3d | 6/1 |
| 4d | 7/1 |
| 5d | 6/2 |
| 6d | 6/2 |
| 7d | 7/2 |
| 8d | 7/2 |
| 9d | 6/3 |
| 10d | 7/3 |
| 11d | 7/3 |
| 12d | 7/3 |

Essa tabela é um baseline matemático. NPCs concretos poderão receber pequenos ajustes rastreáveis depois de comparação direta entre a ficha original e a convertida.

### 2.2. Absorção → Proteção

| Soak original | P baseline |
| :---: | :---: |
| 0–1d | 0 |
| 2–3d | 1 |
| 4–6d | 2 |
| 7–9d | 3 |
| 10–11d | 4 |
| 12–13d | 5 |

A extensão acima de 10d é uma **inferência operacional direta** homologada para evitar estudo desnecessário em uma região adjacente da curva.

### 2.3. Proteção física é tipada

A Proteção física deve preservar a distinção de M20 entre:

- **C** — Contundente;
- **L** — Letal;
- **A** — Agravado.

Quando o mesmo valor vale para mais de um tipo, pode-se escrever, por exemplo, `P2[C,L]`.

Quando os valores diferem, usa-se perfil explícito, por exemplo:

`C2·L1·A0`

A ausência de um tipo não pode ser preenchida por inferência apenas para completar a assinatura.

---

## 3. Estrutura multidimensional da ficha achatada

A Perfil DRP físico é apenas uma das dimensões possíveis. A ficha achatada completa deve poder assumir a forma:

```
NOME

Físico: D/R/P[tipo, se aplicável]
Social: D/R/P
Mental/Técnico: D/R/P
Mágicko/Poderes: D/R/P[tipo, se aplicável]

Persistência:
- Vitalidade / Integridade / Essência / outro recurso original

Características:
- [...]

Poderes / recursos:
- [...]

Comportamento:
- [...]

Telegrafia:
- [...]
```

Nem toda dimensão precisa existir e nem toda dimensão precisa usar os três componentes. **Social** e **Mental/Técnico** usam Proteção simples quando houver equivalente real. **Físico** pode tipar Proteção por C/L/A. **Mágicko/Poderes** pode tipar Proteção quando as regras originais distinguirem categorias de efeito, resistência ou imunidade.

A Perfil DRP de uma dimensão não deve apagar recursos canônicos que carregam função própria. A **Persistência** permanece explícita quando a entidade possui mais ou menos caixas do que o padrão humano, ou quando usa outra reserva estrutural.

Para entidades como HIT Marks, por exemplo, a defesa físicamente compacta convive com **Contramágika Inata** e Vitalidade especial. Esses elementos precisam aparecer na ficha mesmo antes de sua conversão matemática definitiva.

---

## 4. Como extrair a Perfil DRP físico

A assinatura deve ser construída a partir das **funções reais da ficha original**.

Para oposição física ativa, a fonte preferencial é a parada que M20 realmente usaria para a defesa pertinente, como Destreza + Esportes/Atletismo para esquiva. Briga, Artes Marciais ou outra Habilidade só substituem essa fonte quando a manobra original realmente utilizar essa parada defensivamente.

Para Proteção, é obrigatório separar:

1. Vigor;
2. armadura ou proteção adicional;
3. quais tipos de dano cada fonte realmente pode absorver.

Isso impede, por exemplo, que o Vigor de um Adormecido seja transformado acidentalmente em proteção contra dano Letal.

---

## 5. Primeira amostra do corpus

A tabela abaixo é **diagnóstica**. Assinaturas com `?` expõem lacunas documentais que precisam ser confirmadas antes de homologação.

| NPC / Obstáculo | Fonte de defesa ativa | D/R baseline | Fonte de soak/proteção | Proteção física preliminar | Assinatura física preliminar | Outras dimensões / recursos | Persistência | Camada diegética que deve permanecer |
| :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- | :--- |
| **Bandido Comum** | Destreza 2 + Esportes 2 = 4d | 7/1 | Vigor 2; sem armadura; Adormecido | C1·L0·A0 | **7/1/C1·L0·A0** | Social/Mental comuns; Mágicko ausente | 7 níveis humanos | Brigão de rua; armas improvisadas; vulnerabilidade humana comum |
| **Policial de Rua** | Destreza 2 + Esportes 2 = 4d | 7/1 | Vigor 3 + colete Kevlar; 5d totais declarados | C2·L?·A0 | **7/1/C2·L?·A0** | Social: autoridade institucional; Mental/Técnico: treinamento policial | 7 níveis humanos | Autoridade policial; rádio; algemas; Taser; escalada para reforços |
| **Agente do Governo** | Destreza 2–3 + Esportes 2 = 4–5d | 7/1 a 6/2 | Vigor 3–4 + colete oculto; 5d totais declarados | C2·L?·A0 | **7/1–6/2 / C2·L?·A0** | Social forte; Mental/Técnico forte; Mágicko ausente | 7 níveis humanos | Autoridade federal; vigilância; investigação; armamento discreto |
| **Durão Profissional** | Destreza 3 + Esportes 2–4 = 5–7d | 6/2 a 7/2 | Vigor 3 + Kevlar; 6–8d totais | C2–3·L?·A0 | **6/2–7/2 / C2–3·L?·A0** | Mercenário/segurança de elite; treinamento; armamento pesado |
| **Hacktivista Desperto** | Destreza 3 + Esportes 2 = 5d | 6/2 | Vigor 3 + fibra blindada; 4d totais; Desperto | C2·L2·A0 | **6/2/C2·L2·A0** | Mental/Técnico muito forte; Mágicko: Arete 3–4 + Esferas | 7 níveis humanos | Hacker de realidade; dispositivos trinários; mobilidade e investigação |
| **Músico Xamã Urbano** | Destreza 3 + Esportes 1 = 4d | 7/1 | Vigor 3 + roupas de couro; 4d totais; Desperto | C2·L2·A0 | **7/1/C2·L2·A0** | Mediação espiritual; música e ritos; percepção de espíritos |
| **Victor** | Destreza 5 + Esportes 4 = 9d | 6/3 | Vigor 4; sem armadura | C2·L0*·A0 | **6/3/C2·L0*·A0** | Mágicko/Poderes: Contramágika Inata 2d | **9 níveis**; sem penalidades por ferimento | Clone geneticamente perfeito; imunidade à dor; contramágika inata 2d |
| **Ciborgue Metálico Comum** | Destreza 3 + Esportes 2 = 5d | 6/2 | Vigor 4 + implante; 5d totais | C2·L?·A? | **6/2/C2·L?·A?** | Corpo aumentado; interfaces integradas; módulos de combate/investigação/infiltração |
| **HIT Mark V** | Destreza 2 + Esportes 3 = 5d¹ | 6/2 | Vigor 5 + Primium 4; 9d totais | P3, tipagem pendente | **6/2/P3[tipagem pendente]** | **Mágicko/Poderes: Contramágika Inata 5d**; Mental/Técnico funcional | **7 níveis?** ficha especial: 5×OK, -1, -5 antes de Destruído; confirmar contagem operacional | Chassi de Primium; sensores; metralhadora integrada; garras; contramágika 5d |
| **HIT Mark X** | Destreza 4 + Esportes 3 = 7d¹ | 7/2 | Vigor 6 + armadura interna 6; 12d totais | P5 por extensão direta; tipagem pendente | **7/2/P5[tipagem pendente]** | **Mágicko/Poderes: Contramágika Inata 4d**; Mental/Técnico avançado | **9 níveis** antes de Destruído | Biomecânica; mudança facial; conectividade; autodestruição; contramágika 4d |
| **Terno Preto** | Destreza 3 + Esportes 2 = 5d | 6/2 | Vigor 3 + terno blindado 4; 7d totais; Iluminado | C3·L3·A0 | **6/2/C3·L3·A0** | Social/Mental fortes; Mágicko: Arete 3–5 + Esferas | 7 níveis especiais, terminando em Vaporizado | Aura de medo; investigação NOM; poderes; dissolução corporal após morte |
| **Tigre / Leão** | Destreza 4 + Esportes 3 = 7d | 7/2 | Vigor 4 + armadura natural 1; 5d totais | C2·L?·A? | **7/2/C2·L?·A?** | Predador grande; mordida/garras letais; Vitalidade ampliada |
| **Crocodilo** | Destreza 3 + Esportes 2 = 5d | 6/2 | Vigor 6 + couro escamoso 1; 7d totais | C3·L?·A? | **6/2/C3·L?·A?** | Couro escamoso; mordida letal; cauda contundente; corpo maciço |

¹ Os HIT Marks possuem graduação 3 nas demais Habilidades/Conhecimentos, salvo exceções explicitamente listadas no corpus; por isso Esportes 3 é usado como fonte provisória de esquiva.

* Para Victor, `L0` segue provisoriamente a regra geral de que um personagem não Desperto sem proteção específica não absorve Letal com Vigor. Deve ser confirmado contra a regra específica dos clones antes de homologação.

---

## 6. Persistência não deve ser achatada automaticamente

A assinatura D/R/P não substitui a quantidade de caixas de Vitalidade, Integridade ou recurso equivalente.

O corpus já contém diferenças relevantes:

- humanos comuns usam a faixa padrão de 7 níveis;
- **Victor** possui 9 níveis antes de Destruído e ignora penalidades por ferimento;
- **HIT Mark X** possui 9 níveis antes de Destruído;
- outras entidades usam arranjos especiais de Vitalidade, Essência ou estados finais próprios.

Essas diferenças afetam diretamente duração, pressão e expectativa do jogador e devem permanecer explícitas. Só podem ser comprimidas em relógio ou outra abstração quando um estudo específico demonstrar que a função original é preservada.

---

## 7. Padrões que já aparecem

Mesmo antes da calibração por confronto, algumas assinaturas de **defesa ativa** se repetem:

- **7/1** — oposição física modesta, como Bandido, Policial e Xamã;
- **6/2** — oposição competente e estável, como Hacktivista, Ciborgue, HIT Mark V e Terno Preto;
- **7/2** — oposição fisicamente forte/ágil, como grandes predadores e HIT Mark X;
- **6/3** — oposição excepcionalmente difícil de superar por volume de competência, como Victor.

A Proteção varia de forma independente. Isso confirma que a Perfil DRP físico não deve ser tratada como uma única escada linear em que D, R e P sobem juntos.

Um HIT Mark V pode, por exemplo, ter D/R semelhante ao de um agente competente e ser muito mais resistente graças a P e às demais características de seu chassi.

---

## 8. Graduação como espaço de perfis, não fórmula

Os Perfis DRP devem surgir de **clusters recorrentes de assinatura**, não de uma equação universal.

Um NPC pode avançar em apenas um eixo:

- mais difícil de atingir/superar;
- mais capaz de cancelar sucessos;
- mais protegido contra certos tipos de dano;
- mais resistente por Vitalidade/Integridade;
- ou mais perigoso por Ameaça/Consequência, que pertence ao sentido ofensivo e ainda tem dívidas próprias de transformação.

Portanto, duas entidades com o mesmo `6/2` podem produzir experiências muito diferentes:

- um agente humano pode ter pouca Proteção e depender de cobertura;
- um HIT Mark pode possuir P alto, imunidades e sensores;
- um espírito pode ter regras de materialização que tornam certos ataques impossíveis.

A assinatura identifica a **resolução mecânica recorrente**. A diegese informa o que aquela resolução significa e quando ela se aplica.

---

## 8.1. Resolução progressiva do Perfil DRP

O Perfil DRP não exige uma ficha completa para existir. Ele admite **representação esparsa por defaults e exceções**.

Formas válidas:

```
6
```

equivale a `6/0/0` como perfil genérico.

```
6/2
```

equivale a `6/2/0`.

```
6
Social 7/2
```

usa `6/0/0` como default e substitui apenas a dimensão Social por `7/2/0`.

As ações ficam fora desse trio e só aparecem quando o Obstáculo precisa agir sobre o PJ:

```
Brigão: 6
Soco: 2S + 2C
```

Um Obstáculo maior pode acrescentar quatro dimensões, múltiplas ações, Persistência, poderes, estados e informação diegética sem trocar de motor.

A regra editorial é: **mais importância pode justificar mais definição; menos importância não obriga a preencher campos que não acrescentam operação real**. A omissão deve herdar defaults definidos pelo método e nunca exigir reconstrução improvisada da ficha M20 durante a cena.

## 9. Peso diegético e densidade da ficha

A Perfil DRP físico não determina o tamanho da ficha.

### Entidade simples

Pode ser suficiente registrar:

```
Bandido Comum
Físico 7/1/C1·L0·A0
[Brigão de rua]
[Foge quando a situação fica sobrenatural demais]
```

### Entidade elaborada

Um HIT Mark V exige mais:

```
HIT MARK V — "Rusty"

Físico 6/2/P3[tipagem pendente]
Vitalidade especial do modelo

[Chassi pesado de Primium]
[Contramágika inata 5d]
[Sensores infravermelhos/ultravioletas]
[Metralhadora integrada]
[Garras cibernéticas]

Comportamento:
- [...]
Telegrafia:
- [...]
Vulnerabilidades / limitações:
- [...]
Estados / consequências:
- [...]
```

O ganho player-faced vem de tornar a resolução frequente compacta, preservando toda informação que sustenta presença, intenção, comportamento e leitura ficcional.

---

## 10. Lacunas abertas antes da homologação da escala

1. Confirmar no material original a cobertura por tipo de dano das armaduras mundanas usadas por Policial, Agente do Governo e Durão Profissional.
2. Confirmar a regra específica de absorção de Ciborgues, HIT Marks e armadura de Primium para C/L/A.
3. Confirmar se Victor possui alguma exceção própria à regra comum de absorção Letal por não Despertos.
4. ~~Calibrar Proteção acima de 10d~~ — resolvido por extensão operacional: 10–11d→P4; 12–13d→P5.
5. Selecionar uma amostra de NPCs concretos representativos e comparar a experiência clássica contra a assinatura convertida, permitindo pequenos ajustes locais de D/R/P quando melhorarem a fidelidade.
6. Levantar, por NPC concreto, as assinaturas **Social**, **Mental/Técnico** e **Mágicko/Poderes**, sem assumir que a matemática física se transfere automaticamente.
7. Contramágika Inata permanece em dados como redução direta da parada do PJ quando aplicável; outras resistências mágickas continuam dependendo de seu procedimento específico.
8. Preservar explicitamente Vitalidade/Integridade especial e demais formas de Persistência.
9. Só depois dessa calibração nomear eventuais graduações editoriais ou clusters de referência.

---

## 11. Matriz multidimensional de extração — primeira amostra

A ficha achatada passa a distinguir entre **dimensão existente** e **dimensão já convertida**. Uma dimensão pode estar claramente presente no NPC e ainda assim manter seus pools originais enquanto a transformação matemática específica permanece aberta.

| NPC | Físico | Social | Mental/Técnico | Mágicko/Poderes | Persistência |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bandido Comum** | **7/1/C1·L0·A0** | Manipulação 2, Intimidação 1, Manha 1; sem assinatura universal ainda | Percepção 2 + Prontidão 2 = 4d para alerta; demais ações situacionais | 0 | 7 níveis humanos |
| **Policial de Rua** | **7/1/C2·L?·A0** | autoridade institucional, Manipulação 3, Intimidação 1, Direito 2; conversão situacional | Percepção 3 + Prontidão 2 = 5d; Investigação 2; Computação/Tecnologia 1–2 | 0 | 7 níveis humanos |
| **Agente do Governo** | **7/1–6/2 / C2·L?·A0** | Manipulação 3–5, Direito 4, Política 2–4, Manha 3; frente social forte | Percepção 3–4 + Prontidão 3 = 6–7d; Investigação 3–5; Computação/Tecnologia 2–4 | 0 | 7 níveis humanos |
| **Hacktivista Desperto** | **6/2/C2·L2·A0** | Carisma/Manipulação 3; Lábia 4; Política 4 | Inteligência 4 + Computação 5 = 9d em hacking; Investigação 4; Tecnologia 4 | Arete 3–4; Correspondência/Dados 3, Forças 2, Mente 2 etc.; procedimentos mágickos preservados | 7 níveis humanos |
| **Músico Xamã Urbano** | **7/1/C2·L2·A0** | Carisma 4; expressão/artes forte; oposição social depende da situação | Percepção 4; Consciência 3; Cosmologia 3; frente perceptiva/espiritual forte | Arete 3–4; Espírito 3, Forças 2, Primórdio 1, Tempo 2 | 7 níveis humanos |
| **Pelourinho** | defesa física alta pela Destreza 4 e capacidades de combate; assinatura completa ainda a calibrar | presença social ordinária quase nula, Intimidação 6 como vetor específico | Raciocínio 5; Prontidão 4; percepção mundana anômala substituída por Correspondência/Mente | **Arete 6**; Correspondência 4, Espírito 4, Mente 4 etc.; poderes permanentes relevantes | 8 níveis: 5×OK, -1, -5, Incapacitado |
| **Victor** | **6/3/C2·L0*·A0** | Carisma 4; demais habilidades sociais variáveis | Percepção 3; Tecnologia 3; outras habilidades 1–4 conforme função | **Contramágika Inata 2d**; reduz diretamente 2 dados da parada do PJ quando aplicável | **9 níveis** antes de Destruído; sem penalidades por ferimento |
| **Ciborgue Metálico Comum** | **6/2/C2·L?·A?** | social baixo/médio e condicionado; Força de Vontade 5/3 conforme programação | Computação 2, Investigação 2, Tecnologia 3–5; módulos podem elevar drasticamente a frente técnica | módulos/poderes tecnológicos; sem assinatura mágicka universal | 8 níveis antes de Incapacitado |
| **HIT Mark V** | **6/2/P3[tipagem pendente]** | quase inexistente como frente persuasiva comum | Percepção 3 + Prontidão 3 = 6d; sensores especiais; programação técnica | **Contramágika Inata 5d por Primium**; reduz diretamente 5 dados da parada do PJ quando aplicável | ficha especial: 5×OK, -1, -5, Destruído |
| **HIT Mark X** | **7/2/P5[tipagem pendente]** | social funcional apenas por camuflagem/mudança facial; não implica defesa social alta | Percepção 5 + Prontidão 4 = 9d; sistemas de dados e conectividade contínua | **Contramágika Inata 4d por Primium**; reduz diretamente 4 dados da parada do PJ quando aplicável | **9 níveis** antes de Destruído |
| **Terno Preto** | **6/2/C3·L3·A0** | Manipulação 4, Intimidação 4, Lábia 3; **Aura de Medo** é regra própria e deve permanecer explícita | Percepção 5 + Prontidão 5 = 10d; Investigação 3, Computação 3, Hipertecnologia 3 | Arete 3–5; Mente 2+; outras Esferas 2–4; procedimentos e contramágika conforme regra | 7 níveis especiais, terminando em Vaporizado |

Esta tabela não transforma automaticamente todos esses valores em D/R/P. Ela mostra **o que a ficha achatada precisa carregar** e qual é o estado de cada frente.

### 11.1. Estado por dimensão

**Físico** já possui dois operadores quantitativamente auditados: oposição ativa → D/R e soak → P. A calibração agora passa a ser feita por NPC concreto.

**Social** existe como dimensão, mas o corpus usa atributos, habilidades, autoridade, contexto e Força de Vontade em combinações diferentes. Não há base para uma defesa social universal única. Quando uma interação for uma disputa resistida real, aplica-se a conversão à parada pertinente; fora disso, preserva-se o procedimento original.

**Mental/Técnico** segue a mesma lógica. Percepção + Prontidão, Inteligência + Computação, Investigação, Hipertecnologia e outros pools representam tarefas diferentes. A dimensão serve como índice operacional e pode futuramente receber graduações recorrentes, mas não deve apagar essas diferenças antes da calibração.

**Mágicko/Poderes** possui fontes próprias e frequentemente tipadas. Contramágika básica é defesa ativa por sucessos; Contramágika Inata, como Primium, é proteção intrínseca; Força de Vontade pode resistir a intrusões mentais; efeitos persistentes podem armazenar sucessos; imunidades podem produzir Efeito Zero. Esses casos precisam permanecer identificáveis separadamente mesmo quando futuramente forem apresentados por uma assinatura compacta.

### 11.2. Persistência como eixo próprio

Persistência é ortogonal às quatro dimensões. Dois NPCs podem compartilhar a mesma assinatura física e suportar quantidades muito diferentes de dano ou progresso.

A ficha deve portanto manter, conforme o caso:

- Vitalidade e penalidades;
- Integridade/Structure;
- Essência;
- Locus;
- caixas especiais;
- estados finais como Incapacitado, Destruído ou Vaporizado;
- imunidade a penalidades de ferimento;
- transformações de fase ou outros estados persistentes.

Persistência só poderá ser comprimida quando houver estudo específico demonstrando preservação de função.

---

## 12. Procedimento operacional de conversão

A matemática acumulada já é suficiente para transformar fichas de NPCs para o padrão DRP sem recalibrar cada NPC individualmente.

A conversão segue esta ordem:

1. **Default esparso:** use `6` quando nenhuma resistência específica precisar ser explicitada.
2. **D/R por dimensão:** identifique a parada original que realmente faria oposição naquela dimensão e converta pela tabela de parada → D/R.
3. **Proteção:** converta soak/resistência passiva pela tabela de soak → P, preservando tipagem C/L/A quando a regra original distinguir os tipos.
4. **Ações:** converta a parada ofensiva por pool + Dificuldade → sucessos fixos usando os estudos ofensivos já realizados; converta o pool-base de efeito/dano para o efeito-base correspondente. Depois do primeiro sucesso líquido, **cada 2 sucessos excedentes acrescentam +1 sucesso automático ao dano/efeito**. Não se acrescentam dados de dano.
5. **Iniciativa:** derive nos bastidores por `Destreza + Raciocínio + 6`; a ficha final registra apenas `Iniciativa: N`.
6. **Persistência:** mantenha Vitalidade, Structure, Essência, Locus ou equivalente como eixo próprio.
7. **Recursos:** mantenha Força de Vontade, Quintessência, munição e outros recursos que ainda possuam função própria.
8. **Características e poderes:** preserve literalmente aquilo que muda possibilidades, imunidades, gatilhos ou comportamento.
9. **Representação final:** escreva apenas o valor convertido que o ST precisa usar em mesa; pools e fórmulas de origem pertencem ao processo de conversão, não à ficha final.

Limitações estatísticas já conhecidas — como a perda de variância de ações ofensivas sem defesa ativa — permanecem registradas no estudo matemático geral. Elas não exigem uma nova simulação para cada NPC.

Novo estudo matemático só é necessário quando surgir uma mecânica que não caiba em nenhum operador de transformação já existente.
