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

Um mesmo Obstáculo pode ter **valores radicalmente diferentes em cada dimensão**. Isso não é apenas uma anotação qualitativa.

Exemplos conceituais:

* **Social baixo / Mágicko alto:** existe resistência social, mas ela é pequena; a principal força do Obstáculo está no campo mágicko.
* **Mágicko 0 / Físico alto:** não existe resistência mágicka relevante a ser vencida naquele eixo, enquanto a frente física é fortemente protegida.

**Zero não é sinônimo de “baixo”.** Zero indica ausência de capacidade, resistência ou atuação relevante naquela dimensão. Um valor baixo indica que a dimensão existe e pode opor-se aos PJs, apenas com pouca força.

A conversão player-facing deve partir da **dimensão e da parada efetivamente relevantes**, e não de um “nível geral” do NPC.

As regras próprias de cada domínio continuam valendo. Combate físico conserva ataque, dano e absorção; mágika conserva Arete, Esferas, vulgaridade, Paradoxo e demais procedimentos; ações sociais e intelectuais seguem o tipo de teste que M20 pediria para aquela situação.

---

## 🧮 2. A Ficha Achatada da Ameaça Ativa

A pesquisa já havia definido uma ficha operacional compacta para ameaças persistentes. Ela precisa ser preservada nas revisões posteriores:

1. **Oposição:** quão difícil é para o PJ superar a resistência ativa da ameaça quando o PJ age.
2. **Ameaça:** quão difícil é para o PJ evitar ou resistir à ação do NPC quando a ameaça age.
3. **Consequência:** o impacto causado quando a ação da ameaça se concretiza — dano, perda de Vontade, condição, exposição, bloqueio de recurso ou outro efeito pertinente.
4. **Integridade / Relógio:** quanto progresso efetivo ainda é necessário para resolver o Obstáculo naquela frente.
5. **Limiar de Efetividade:** resistência que reduz ou impede o Impacto produzido por uma ação bem-sucedida. Este campo nasceu como **RD fixa** para dano físico e foi renomeado para permitir o mesmo conceito em resistências sociais, mentais, técnicas e mágickas.

As quatro dimensões — Físico, Social, Mental/Técnico e Mágicko — formam uma **matriz de aplicação da ficha achatada**. Cada dimensão pode possuir seus próprios valores de **Oposição, Ameaça, Consequência, Integridade e Limiar de Efetividade**, conforme o que realmente existe na ficha, na ficção e no subsistema original.

Exemplo estrutural:

| Dimensão | Oposição | Ameaça | Consequência | Integridade | Limiar |
| :--- | :---: | :---: | :--- | :---: | :---: |
| Físico | alto | alto | alta | alta | alto |
| Social | baixo | baixo | baixa | baixa | baixo |
| Mental/Técnico | médio | médio | média | média | médio |
| Mágicko | 0 | 0 | — | — | — |

Os termos acima são apenas ilustrativos; os valores numéricos precisam vir da conversão/calibração apropriada.

Nem todo campo precisa existir em toda dimensão. Uma dimensão pode ter apenas Oposição, por exemplo, sem possuir Ameaça própria. **0 significa ausência real daquele vetor**, não “fracasso automático” nem “dificuldade mínima”.

As dimensões, portanto, não substituem os subsistemas de M20: elas dizem **qual versão da ficha achatada é acionada pela abordagem escolhida**.

### Oposição

Parte da parada original pertinente do NPC. A conversão probabilística ainda está em calibração.

> **Nota terminológica:** o **Limiar oculto** usado nos estudos matemáticos de Oposição é um parâmetro da transformação probabilística da rolagem resistida. Ele **não é** o **Limiar de Efetividade** da ficha achatada.

### Ameaça

O NPC continua agindo em sua iniciativa e declarando suas ações. **Ameaça** representa sua capacidade ofensiva naquela dimensão.

Quando o PJ possui uma defesa ativa, a melhor linha testada até aqui é preservar essa rolagem do jogador e converter a competência ofensiva do NPC atrás do escudo. Isso é promissor em ameaças fracas e médias, mas ainda perde fidelidade em pools altos.

Quando o PJ **não possui defesa ativa**, Ameaça continua sendo necessária na ficha, mas não existe uma rolagem do jogador que carregue naturalmente toda a variância que M20 colocava no ataque do NPC. As auditorias mostraram que inventar uma defesa gratuita ou reduzir ataque+dano a uma Consequência fixa altera materialmente a experiência.

Sob o critério de fidelidade do Estudo 00, esse é um caso em que a rolagem ofensiva original do ST pode precisar ser preservada.

### Consequência

A ficha também precisa registrar **o que acontece se a Ameaça se concretiza**.

No físico, pode ser dano Contundente, Letal ou Agravado. Em outros domínios pode ser perda de Vontade, condição, exposição, perda de posição, bloqueio de recurso ou outro impacto previsto pelo conteúdo original.

Consequência é indispensável, mas **Consequência fixa não deve ser presumida como equivalência universal da parada de dano do NPC**. A auditoria V3 mostrou que isso funciona apenas como aproximação em parte da faixa de poder e degrada em ameaças fortes.

### Integridade / Relógio

Representa quanto progresso significativo ainda é necessário para resolver aquele Obstáculo naquela frente. Sua relação com Vitalidade, Essência ou outros recursos precisa respeitar o conteúdo original; não se presume que todo recurso canônico seja simplesmente comprimido em menos caixas.

A leitura de sucessos continua valendo dentro dessa estrutura:

* **1 sucesso** continua sendo sucesso marginal e normalmente produz **1 Impacto/1 caixa** sobre o Relógio, além de mover a ficção;
* sucessos adicionais produzem efeito proporcional conforme a regra da ação e o tipo de Obstáculo;
* **0 sucessos** não produz Impacto;
* um **Limiar de Efetividade** pode reduzir o Impacto final quando representa resistência real.

Portanto, relógio não transforma 1 sucesso em “resultado narrativo sem dano”. O sucesso afeta a história **e** a estrutura persistente do Obstáculo, salvo quando uma resistência legítima absorve esse Impacto.

### Limiar de Efetividade

É a generalização da antiga **RD fixa**.

No combate físico, representa o papel de Vigor, armadura, couraça ou material em reduzir o dano que efetivamente atravessa. Em outros domínios pode representar uma resistência equivalente: proteção institucional, segurança criptográfica, blindagem mental, barreira mágicka etc.

Um sucesso pode continuar sendo **sucesso na ação** e ainda produzir **Impacto zero após o Limiar**, do mesmo modo que em M20 um ataque pode acertar e a absorção anular todo o dano.

Isso não contradiz a regra de que **1 sucesso move a ficção**. O acerto, acesso, contato ou avanço aconteceu; a resistência do Obstáculo determinou quanto desse sucesso se converteu em Impacto.

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

## 🛡️ 4. Combate Físico e o Limiar de Efetividade

M20 separa ataque, defesa, dano e absorção. A ficha achatada reorganiza o lado do Storyteller:

* **Oposição** representa a resistência ativa ao ataque do PJ;
* **Ameaça** representa a ofensiva do NPC contra o PJ;
* **Consequência** registra o dano causado pela ameaça;
* **Integridade** registra quanto o Obstáculo ainda suporta naquela frente;
* **Limiar de Efetividade** representa a antiga RD/soak comprimido.

Quando o PJ ataca, suas rolagens próprias de M20 permanecem reconhecíveis, inclusive o dano quando aplicável. Depois de produzido o Impacto, o Limiar reduz o que efetivamente alcança a Integridade.

A arquitetura está definida e a auditoria exata já oferece um baseline experimental simples:

| Soak original | Limiar de Efetividade |
| :---: | :---: |
| 0–1d | 0 |
| 2–3d | 1 |
| 4–6d | 2 |
| 7–9d | 3 |
| 10d | 4 |

A aproximação é especialmente boa a partir de 2d; 1d continua sendo o ponto menos fiel da compressão determinística.

O antigo uso de Limiar 2/3 como simples “chefe ignora 1 sucesso” deve ser lido corretamente: o Limiar representa **resistência**, não status narrativo. Ele só deve ser alto quando a ficha original, equipamento, proteção ou ficção justificar resistência equivalente.

## 🧠 5. Conflitos Sociais e Intelectuais

M20 já dispõe de ações simples, resistidas, estendidas e estendidas-resistidas. Portanto, conflitos sociais e intelectuais não precisam receber uma “barra de vida” universal.

Quando a situação for simples, **1 sucesso continua sendo sucesso** e move a ficção.

Quando M20 pedir vários sucessos acumulados — debate prolongado, invasão complexa, perseguição, pesquisa, ritual ou tarefa semelhante — o Storyteller pode usar um relógio como **interface de acompanhamento dos sucessos exigidos**, desde que o relógio represente a mesma lógica da tarefa original. Nesse caso, **1 sucesso também reduz o relógio em 1**, além de produzir seu avanço ficcional marginal.

Um resultado marginal de 1 sucesso não deve ser apagado automaticamente por uma “RD social” apenas para tornar o oponente mais épico. Qualquer limiar de efetividade precisa decorrer:

* das regras originais;
* de uma resistência que a conversão esteja representando;
* ou da própria natureza ficcional do objetivo.

---

## 🚪 6. Limiar de Efetividade e Efeito Zero

**Limiar de Efetividade** é um valor geral de resistência. Ele pode reduzir o Impacto de uma ação bem-sucedida até zero.

Isso é diferente de dizer que a ação “falhou”.

Exemplos:

* um golpe acerta o HIT Mark, mas a proteção absorve todo o dano;
* uma tentativa social consegue uma concessão mínima, mas não reduz ainda a posição institucional do alvo;
* uma intrusão encontra uma brecha, mas a camada criptográfica impede avanço no núcleo protegido.

**Efeito Zero por impossibilidade** é um caso mais forte: a ação não possui sequer capacidade de afetar o alvo daquela forma, como um ataque mundano contra uma entidade efêmera desmaterializada.

Assim:

* **Limiar de Efetividade** = resistência quantitativa após uma ação válida;
* **Efeito Zero por impossibilidade** = a abordagem não pode produzir aquele tipo de Impacto sem mudar as condições.

## 🎯 7. O que a Estrutura Multidimensional Realmente Acrescenta

A principal contribuição deste estudo não é criar quatro versões simétricas de combate.

É fornecer ao Storyteller uma **matriz compacta de competências, resistências e vulnerabilidades por dimensão**.

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

## 9. Estado das dívidas após os estudos posteriores

Os Estudos 14–21 fecharam várias das questões que ainda estavam abertas quando este capítulo foi escrito. O estado atual é:

1. **Ameaças ofensivas com defesa ativa:** continuar refinando a compressão onde já existe rolagem do jogador.
2. **Ameaça + Consequência sem defesa ativa:** **resolvido por limite de fidelidade**; preserva-se a operação original do ST quando não existe transformação equivalente sem custo para o jogador.
3. **Recursos e entidades não humanas:** verificar se Vitalidade, Essência, Gnose, Vontade, armaduras, imunidades e outras reservas podem ser simplificadas sem transformar sua função original.

Essas perguntas devem acompanhar os estudos seguintes e retroagir sobre este documento sempre que uma solução posterior for validada.


---

## 10. Propagação do Estudo 18 — Certámen

O Certámen confirma uma distinção importante da ficha achatada:

* **Aegis é defesa ativa**, portanto pertence à família de Oposição/cancelamento de sucessos;
* **Limiar de Efetividade é resistência passiva**, portanto não deve substituir Aegis;
* **Locus** já funciona como Integridade canônica;
* **1 sucesso de Gladius reduz 1 ponto do Locus**;
* ausência de Aegis não concede defesa gratuita.

Isso reforça que defesa ativa e Limiar de Efetividade são funções diferentes e não devem ser fundidas.
