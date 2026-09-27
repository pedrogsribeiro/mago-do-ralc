---
type: contrato
summary: "Contrato normativo do produto M20 Player-Faced Total: zero rolagens do Storyteller e preservação integral da experiência operacional do personagem jogador."
tags: [player-faced, contrato, produto, invariantes, storyteller, jogador, zero-dados]
---

# Contrato de Produto — M20 Player-Faced Total

Este documento define as premissas superiores do projeto. Em caso de conflito com estudos, simulações, auditorias matemáticas, exemplos ou textos posteriores, **este contrato prevalece** até decisão autoral explícita em contrário.

## 1. Definição de player-faced neste produto

**Player-faced significa aliviar a carga cognitiva e operacional do Storyteller sem alterar a experiência do personagem jogador.**

A transformação acontece do lado do Storyteller: fichas de NPCs, Obstáculos, cenas, ameaças, estados, resistências, consequências e outras estruturas usadas para operar o mundo podem ser comprimidas, reorganizadas ou convertidas.

Para o jogador, M20 continua sendo M20.

## 2. Invariantes do personagem jogador

Para o personagem jogador:

- a ficha permanece a ficha normal de M20;
- Atributos, Habilidades, Arete, Esferas e demais características mantêm sua função;
- as paradas que o jogador já faria continuam sendo as mesmas;
- nenhuma nova rolagem é criada apenas para absorver uma antiga rolagem do Storyteller;
- nenhuma rolagem de NPC, espírito, item, fenômeno ou outro elemento é transferida ao jogador;
- dificuldades, graus de sucesso, botches, recursos e economia de ações permanecem reconhecíveis segundo M20;
- declarar ou não defesa ativa mantém o mesmo custo e significado;
- não se concede defesa, reação ou ação gratuita para viabilizar a conversão;
- o jogador não precisa aprender um novo minissistema para que a camada player-faced funcione.

**Se uma solução exige que o personagem jogador faça algo que não faria normalmente em M20, essa solução viola o contrato.**

## 3. Invariante do Storyteller

**O Storyteller rola zero dados.**

Quando uma regra original exige uma rolagem do Storyteller, essa operação deve ser:

1. eliminada quando for desnecessária;
2. convertida em parâmetro derivado da ficha original;
3. representada pela assinatura defensiva **Dificuldade/Resistência/Proteção (D/R/P)**, por Ameaça, Consequência, estado, relógio ou outra estrutura adequada;
4. ancorada numa rolagem que o jogador já faria normalmente, quando isso não altera sua função;
5. ou registrada como **dívida de transformação ainda aberta**.

Manter uma rolagem do Storyteller não resolve a dívida.

## 4. O que pode mudar

Podem ser profundamente reorganizados do lado do Storyteller:

- fichas e interfaces de NPCs;
- fichas de Obstáculos;
- preparação de cenas;
- representação defensiva do Obstáculo por **Dificuldade, Resistência e Proteção**;
- dano e consequência produzidos por ameaças;
- relógios, estados e limiares;
- representação de sistemas, organizações, objetos, espíritos e fenômenos;
- procedimentos internos usados para substituir antigas rolagens do ST.

NPCs e entidades preservam agência ficcional. Continuam tendo intenção, iniciativa, objetivos, ações, poderes, movimentação e capacidade de produzir consequências.

### Perfil DRP homologado

Quando o PJ age contra um Obstáculo e a operação original exige compressão do lado do Storyteller, o método é o **Perfil DRP**, cuja notação-base é **D/R/P**:

- **Dificuldade**: valor-alvo no d10, preservando o conceito de M20;
- **Resistência**: sucessos cancelados pela oposição ativa;
- **Proteção**: Impacto absorvido depois que a ação produziu efeito quantitativo, com o **tipo de Impacto protegido explicitado**.

A forma curta **D/R** é suficiente quando não existe etapa de Impacto/Proteção. Na forma completa, a Proteção deve conservar o escopo original. Por exemplo, `7/2/2[C,L]` significa **Dificuldade 7, Resistência 2, Proteção 2 contra Contundente e Letal**. Quando os valores variarem por tipo, o terceiro campo pode ser um perfil, como `7/2/C2·L1·A0`.

**Impacto** é o efeito quantitativo produzido antes da Proteção; **Impacto efetivo** é o restante depois da Proteção. No Físico, uma Proteção tipada só reduz os tipos de dano cobertos. Em Social e Mental/Técnico, Proteção é um valor único quando existir. Em Mágicko/Poderes, a Proteção pode ser tipada quando as regras originais distinguirem categorias de efeito, resistência ou imunidade.

### Resolução progressiva e representação esparsa

O **Perfil DRP admite qualquer grau de resolução**, do Obstáculo incidental ao antagonista plenamente detalhado. A gramática é a mesma em todos os casos; muda apenas a quantidade de informação explicitada.

A leitura é cumulativa:

- `6` equivale a `6/0/0`;
- `6/2` equivale a `6/2/0`;
- `6/2/1` explicita Dificuldade, Resistência e Proteção.

Quando existir um **Perfil DRP genérico** para o Obstáculo, ele funciona como default das dimensões não especificadas. Dimensões explicitadas substituem esse default apenas naquele eixo. Por exemplo, `6` com `Social 7/2` significa que Físico, Mental/Técnico e Mágicko/Poderes herdam `6/0/0`, enquanto Social usa `7/2/0`.

Informação omitida nunca deve obrigar o Storyteller a reconstruir a ficha original em tempo de jogo. Defaults precisam ser definidos previamente pelo método.

As **ações do Obstáculo** são independentes do D/R/P defensivo. Quando uma ação substitui rolagens do Storyteller, ela deve trazer os sucessos fixos e, quando houver, o efeito correspondente, por exemplo `Tiro: 4S + 3L`. A ficha do PJ e suas rolagens permanecem integralmente M20; o Perfil DRP descreve somente aquilo que o Obstáculo entrega ou resiste.

A densidade da ficha acompanha a importância ficcional. Um Obstáculo pode ser apenas `6`; outro pode possuir quatro dimensões, ações próprias, Persistência, poderes, estados, motivações e texto diegético. Ambos usam o mesmo método.

### Eixos independentes de classificação

A representação esparsa do Perfil DRP não substitui a ontologia dos Obstáculos. Três classificações devem permanecer separadas:

- **Passivo / Ativo** descreve se o Obstáculo possui agência e ações próprias;
- **Simples / Elaborado** descreve quanta informação operacional precisa ser explicitada;
- **Pontual / Persistente / Alto impacto** descreve a carga da situação em cena.

Esses eixos podem combinar-se livremente. Um agente pode ser ativo e simples; um sistema pode ser passivo e elaborado. Um Obstáculo simples pode ser perigoso. Um Obstáculo elaborado não recebe potência adicional apenas por possuir mais campos.

O Perfil DRP é a linguagem comum usada por todas essas formas.

## 5. Fidelidade

A prioridade de fidelidade é a **experiência operacional e perceptível do jogador**.

Também se busca preservar suficientemente:

- relações de competência;
- perigo relativo de antagonistas;
- valor da especialização;
- risco de adversários fortes;
- duração e pressão dos conflitos;
- importância de defesas, resistências, armaduras e poderes.

Equivalência probabilística perfeita de procedimentos invisíveis do Storyteller é desejável, mas **não tem precedência sobre os invariantes do produto**.

Se uma transformação apresenta erro matemático excessivo, essa transformação é rejeitada ou recalibrada. O problema retorna ao estado **aberto**. A solução não pode ser reintroduzir dados do Storyteller nem transferir trabalho ao jogador.

## 6. Regra para auditorias futuras

Toda auditoria deve separar três perguntas:

1. **A experiência do jogador mudou?** Se sim, a solução falha.
2. **O Storyteller ainda precisa rolar?** Se sim, a transformação ainda não está resolvida.
3. **A aproximação preserva suficientemente competência, risco e efeito?** Se não, a solução precisa de nova calibração.

A matemática audita a qualidade da transformação. Ela não pode redefinir a premissa do produto.

## 7. Estado das antigas “exceções de fidelidade”

Qualquer procedimento anteriormente declarado resolvido por manter rolagem do ST deve ser reaberto como dívida de transformação player-faced.

Isso inclui, no mínimo:

- ataque/dano de NPC sem defesa ativa do PJ;
- Fúria ofensiva de espíritos;
- Gnose de Encantos quando a incerteza estava apenas no lado do espírito;
- mágika hostil unilateral;
- Gladius de NPC contra PJ sem Aegis;
- Reação de Paradoxo;

Esses casos permanecem **abertos** até existir solução que cumpra simultaneamente os invariantes do jogador e zero rolagens do Storyteller.
