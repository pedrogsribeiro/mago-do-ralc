---
type: regra
summary: "Estudo 6 do Sistema Player-Faced: formalização do Nível 2 (Ameaça Ativa), quatro dimensões como mapa de competência e limites da compressão de dano, resistência e conflitos prolongados."
tags: [srd, design, player-faced, nivel-2, ameaca-ativa, dimensoes, relogios, regras]
---

# Estudo 06: Nível 2 — Ameaça Ativa e as Dimensões de Competência

Este estudo formaliza a representação de **ameaças persistentes** no sistema player-facing: antagonistas, constructos, entidades ou fenômenos que permanecem em cena, possuem ações próprias, ocupam iniciativa e exigem acompanhamento por vários turnos.

A evolução dos Estudos 00–05 impõe duas restrições:

1. a compressão deve permanecer **do lado do Storyteller**, preservando para os jogadores as decisões e procedimentos reconhecíveis de M20;
2. parâmetros comprimidos só podem ser tratados como equivalentes quando sua relação com as regras originais tiver sido calibrada. Dificuldade isolada já foi rejeitada; **Dificuldade + Limiar oculto** é o baseline experimental atual para oposição resistida.

---

## 🌐 1. As 4 Dimensões como Mapa de Competência

Para reduzir consulta de ficha, uma ameaça pode ser descrita em quatro grandes dimensões:

1. **Físico-corporal:** combate, atletismo, perseguição, força, resistência física.
2. **Social-ideológica:** persuasão, intimidação, autoridade, política, manipulação.
3. **Intelectual-técnica:** hacking, ciência, investigação, criptografia, engenharia.
4. **Místico-arcana:** Arete, Esferas, contramágica, rituais, interação espiritual.

Essas dimensões são uma **ferramenta de indexação para o Storyteller**, não quatro subsistemas simétricos e nem uma interface obrigatória para toda criatura. O Estudo 07 mostra um limite importante: espíritos já possuem em M20 uma ficha compacta própria (Força de Vontade, Fúria, Gnose e Essência), e substituí-la por quatro novas dimensões pode aumentar, em vez de reduzir, a carga. O objetivo é responder rapidamente:

> “Qual competência deste NPC realmente importa para a ação que está acontecendo agora?”

Um mesmo antagonista pode ter paradas muito diferentes em cada dimensão. A conversão player-facing deve partir da **parada efetivamente relevante**, e não de um “nível geral” do NPC.

As regras próprias de cada domínio continuam valendo. Combate físico conserva ataque, dano e absorção; mágika conserva Arete, Esferas, vulgaridade, Paradoxo e demais procedimentos; ações sociais e intelectuais seguem o tipo de teste que M20 pediria para aquela situação.

---

## 🧮 2. Perfil Operacional de uma Ameaça Ativa

A versão inicial deste estudo propunha quatro números perfeitamente simétricos — Oposição, Ameaça, Consequência e Relógio. A pesquisa posterior mostrou que essa simetria era prematura.

O perfil operacional deve separar **o que já possui calibração** do que ainda precisa de estudo:

### A. Oposição à ação do PJ
Quando M20 usaria uma rolagem resistida do NPC contra uma ação do jogador, converte-se a **parada relevante do NPC** pelo baseline experimental de **Dificuldade + Limiar oculto**.

### B. Pressão exercida pelo NPC
O NPC continua tendo ações próprias e lugar na iniciativa. Quando sua ação ameaça algo sob agência de um PJ, o jogador faz a rolagem apropriada para determinar o desfecho. A competência ofensiva relevante do NPC precisa ser convertida pelo mesmo princípio matemático de oposição, respeitando o tipo de ação e as regras específicas de M20.

### C. Consequência
A consequência **não deve ser presumida como dano fixo universal**. Em M20, dano físico e místico frequentemente resulta de paradas de dano, sucessos excedentes, tipo de dano e absorção. Reduzir tudo a “2–5 pontos fixos” é uma hipótese separada que precisa de auditoria probabilística.

### D. Persistência / resistência
Relógios podem ser uma ferramenta útil de acompanhamento do ST, especialmente quando correspondem a testes estendidos ou objetivos de cena. Porém, um relógio não é automaticamente equivalente à Vitalidade, Essência, Força de Vontade, Quintessência ou outra reserva de M20. Cada conversão precisa demonstrar o que está preservando.

---

## 📊 3. Estado das Simulações Multidimensionais

As simulações originalmente registradas neste estudo comparavam PJs de 3d, 5d e 7d contra ameaças descritas por Dificuldade de Imposição, Dificuldade de Pressão, dano fixo e relógio.

Elas demonstraram que **o motor proposto possuía comportamento interno previsível** e que diferenças entre dimensões criavam incentivos para buscar brechas. Elas não demonstraram equivalência com M20 porque:

* usavam a antiga conversão por Dificuldade sem o Limiar oculto atualmente estudado;
* tratavam dano e resistência por parâmetros fixos ainda não calibrados contra dano/absorção de M20;
* mediam vitória no motor novo, sem baseline completo do mesmo confronto pelas regras originais.

Portanto, as taxas de vitória e duração dessas simulações deixam de ser parâmetros normativos. Seu valor histórico permanece como indicação de uma ideia que merece preservar:

> **fraquezas reais do NPC devem importar, e escolher um campo em que ele é menos competente deve produzir vantagem porque a ficha original também produziria essa vantagem.**

A recompensa tática deve nascer da **competência efetiva do antagonista em cada abordagem**, não de bônus artificiais criados pela taxonomia.

---

## 🛡️ 4. Combate Físico: Ataque, Dano e Absorção

M20 separa explicitamente várias etapas:

1. ataque;
2. eventual defesa;
3. sucessos excedentes podem aumentar a parada de dano;
4. dano é rolado;
5. o alvo pode realizar absorção quando aplicável.

Para preservar a experiência do jogador, quando um PJ ataca:

* o jogador continua usando sua parada e sua dificuldade apropriadas;
* continua rolando dano quando M20 mandar;
* sucessos excedentes continuam tendo o efeito correspondente;
* tipo de dano continua importando.

O problema a resolver está **atrás do escudo**: como representar defesa e absorção do NPC sem rolar suas paradas completas.

### RD fixa: hipótese, não solução homologada

A versão anterior propunha substituir a absorção do NPC por uma **Resistência a Dano fixa (RD)**. Isso reduz operações, mas uma absorção fixa não possui a mesma distribuição de uma parada de absorção rolada.

Portanto, dano/absorção exige um estudo matemático próprio, equivalente ao que foi feito para oposição resistida. Precisamos testar, entre outras possibilidades:

* absorção média fixa;
* absorção fixa + pequena fonte de variância;
* tabela compacta por parada de soak;
* outra transformação que preserve melhor a distribuição sem devolver ao ST uma parada completa.

Até essa auditoria existir, RD fixa permanece apenas uma hipótese de compressão.

---

## 🧠 5. Conflitos Sociais e Intelectuais

M20 já dispõe de ações simples, resistidas, estendidas e estendidas-resistidas. Portanto, conflitos sociais e intelectuais não precisam receber uma “barra de vida” universal.

Quando a situação for simples, **1 sucesso continua sendo sucesso** e move a ficção.

Quando M20 pedir vários sucessos acumulados — debate prolongado, invasão complexa, perseguição, pesquisa, ritual ou tarefa semelhante — o Storyteller pode usar um relógio como **interface de acompanhamento dos sucessos exigidos**, desde que o relógio represente a mesma lógica da tarefa original.

Um resultado marginal de 1 sucesso não deve ser apagado automaticamente por uma “RD social” apenas para tornar o oponente mais épico. Qualquer limiar de efetividade precisa decorrer:

* das regras originais;
* de uma resistência que a conversão esteja representando;
* ou da própria natureza ficcional do objetivo.

---

## 🚪 6. Limiar de Efetividade e Efeito Zero

O conceito de **Efeito Zero** continua útil, mas precisa ser aplicado de forma mais restrita.

Uma ação causa Efeito Zero quando **não possui, pela ficção ou pelas regras de M20, capacidade de afetar aquele alvo ou objetivo**. Exemplos posteriores podem incluir uma entidade incorpórea diante de um ataque puramente mundano ou uma barreira cuja natureza exige determinada abordagem.

Efeito Zero não deve funcionar como uma proteção genérica de “chefes” contra resultados de 1 sucesso. Se 1 sucesso seria capaz de produzir efeito em M20, ele continua sendo um sucesso marginal que move a ficção.

Da mesma forma, um Limiar pode existir quando representa uma exigência real do sistema ou da ficção, mas não deve ser adicionado apenas para evitar o chamado “efeito picada de mosquito”.

---

## 🎯 7. O que a Estrutura Multidimensional Realmente Acrescenta

A principal contribuição deste estudo não é criar quatro versões simétricas de combate.

É fornecer ao Storyteller um **mapa compacto de competências e vulnerabilidades**.

Para uma ameaça persistente de ficha extensa, o ST deve conseguir identificar rapidamente:

* em que ela é excepcional;
* em que é competente;
* em que é mediana;
* em que é vulnerável;
* quais recursos, imunidades ou limitações realmente constam de sua natureza ou ficha.

Quando o jogador escolhe uma abordagem, o ST consulta apenas a competência pertinente e aplica a conversão adequada. Para entidades que já possuem uma ficha canônica curta e funcional, como os espíritos estudados no Estudo 07, a melhor solução pode ser preservar essa ficha e comprimir apenas as rolagens do ST. Isso reduz a necessidade de carregar dezenas de números sem substituir a diversidade mecânica de M20 por um único minijogo universal.

---

## 🧠 8. Ergonomia: Hipótese a Medir

A ameaça ativa comprimida deve reduzir consulta, montagem de paradas e rolagens do Storyteller. Entretanto, afirmações como “85% mais rápido”, “3 linhas substituem toda ficha” ou “100% da energia mental é liberada” permanecem **hipóteses de design** até serem testadas em mesa.

O objetivo mensurável para os próximos estudos é comparar:

* tempo de preparação;
* tempo de resolução;
* quantidade de consultas à ficha;
* quantidade de operações do Storyteller;
* e percepção dos jogadores sobre dificuldade, competência e risco.

A redução operacional só é bem-sucedida se vier sem perda relevante da experiência de M20 para os jogadores.

---

## 9. Próxima Dívida de Pesquisa

Após este estudo, duas questões permanecem especialmente importantes:

1. **Dano e absorção:** encontrar uma compressão do lado do NPC que preserve adequadamente o comportamento das paradas de dano/soak de M20.
2. **Recursos e entidades não humanas:** verificar se Vitalidade, Essência, Gnose, Vontade, armaduras, imunidades e outras reservas podem ser simplificadas sem transformar sua função original.

Essas perguntas devem acompanhar os estudos seguintes e retroagir sobre este documento sempre que uma solução posterior for validada.
