---
type: regra
summary: "Estudo 00 do Sistema Player-Faced: problema de carga cognitiva do Storyteller, hipótese de compressão operacional e princípios de preservação da experiência de M20 para os jogadores."
tags: [srd, design, player-faced, ergonomia, problematica, estimativas, manifesto, regras]
---

# Estudo 00: A Problemática do M20 Clássico e o Manifesto de Ergonomia Cognitiva

Este documento estabelece a premissa central de *game design* que originou a pesquisa do **Motor Player-Faced** para *Mago: A Ascensão 20 Anos*: reduzir drasticamente a carga operacional do Storyteller **sem exigir que os jogadores reaprendam M20 ou tenham sua experiência mecânica descaracterizada**. Ele identifica o problema, formula hipóteses de solução e registra estimativas iniciais que precisam ser validadas pelos estudos posteriores.

---

## 🛑 1. A Problemática: O Gargalo Cognitivo em Mago M20

O sistema *Storyteller* de Mago M20 é reconhecido por sua profundidade interpretativa, mas carrega um peso mecânico severo de simulacionismo dos anos 1990. Esse peso recai desproporcionalmente sobre o **Narrador (Storyteller)**, criando um gargalo cognitivo que paralisa a fluidez das sessões.

### A Sobrecarga de Gestão Visual (Tracking)
A Memória de Trabalho humana é capaz de processar confortavelmente um número limitado de itens simultâneos. No entanto, ao gerenciar um único NPC médio (como um Agente da Tecnocracia), o Narrador do M20 precisa rastrear visualmente cerca de **50 a 60 variáveis numéricas dispersas em uma ficha de 2 páginas**:
* 9 Atributos, 30 Habilidades e 9 Esferas.
* Arete, Força de Vontade e Quintessência.
* Tabela de 7 Níveis de Vitalidade (com penalidades flutuantes de $-1$ a $-5$ nos dados).

### A Sobrecarga de Manipulação Mecânica (Dice Bloat)
Para resolver **um único turno de combate mútuo** entre um Jogador (PJ) e um NPC no M20 clássico, o sistema exige um ciclo exaustivo:
1. PJ rola Ataque $\rightarrow$ NPC rola Esquiva $\rightarrow$ PJ rola Dano $\rightarrow$ NPC rola Absorção.
2. NPC rola Ataque $\rightarrow$ PJ rola Esquiva $\rightarrow$ NPC rola Dano $\rightarrow$ PJ rola Absorção.

São **8 rolagens de dados por turno para 2 personagens**, além do esforço mental de subtrair sucessos de ataque vs esquiva, recalcular paradas baseadas na penalidade de dano atual e checar absorção em cada etapa. O resultado é a fadiga narrativa: a energia que o Mestre deveria investir na construção dramática e interpretação acaba afogada em matemática básica contínua.

---

## 💡 2. A Hipótese de Design e a Solução

**A Hipótese Central:** *É possível diminuir a carga cognitiva do Storyteller e o número de operações que ele executa, preservando para os jogadores a ficha, as decisões, os recursos, as rolagens e o comportamento probabilístico reconhecível de M20.*

### Hipóteses de Solução (A Raiz do Design)
A pesquisa parte de referências modernas de *game design* presentes em **Fate Básico / Fate Core** e nos jogos **Powered by the Apocalypse (PbtA)**, além de influências da tradição OSR. Elas servem como referências de ergonomia e estrutura, sem importar integralmente seus sistemas para M20.

1. **Regra de Bronze do Fate Básico / Fate Core:** elementos muito diferentes da ficção podem compartilhar uma gramática de representação. Isso inspira uma taxonomia comum para portas, inimigos, feitiços, fenômenos e outras fontes de oposição sem exigir que cada uma carregue uma ficha completa.
2. **Incerteza ancorada na agência do jogador — referência PbtA:** quando uma ação de NPC ou obstáculo interfere diretamente em algo sob agência de um PJ, a hipótese é fazer a incerteza nascer da rolagem do jogador. **O NPC continua agindo, ocupando iniciativa e produzindo causalidade ficcional.** Se não houver agência de jogador envolvida, o Storyteller decide o resultado em função da ficção e da história, em vez de simular o mundo rolando contra si mesmo.
3. **Leitura dos resultados permanece M20:** **1 sucesso continua sendo sucesso** — marginal, suficiente para mover a ficção. Dois ou mais sucessos representam resultados progressivamente mais sólidos conforme os graus de sucesso de M20. Não se importa como regra obrigatória a faixa PbtA de “sucesso com complicação”.
4. **Compressão do lado do Storyteller:** fichas extensas de NPCs podem ser reduzidas a poucos parâmetros operacionais, desde que essa compressão seja calibrada contra o comportamento matemático das fichas originais. A forma exata dessa compressão é objeto dos estudos seguintes; não é assumida pronta neste manifesto.

---

## 📈 3. Hipóteses de Ganho Cognitivo e de Tempo de Mesa

A motivação operacional é reduzir quatro fontes de trabalho do Storyteller: consulta de fichas extensas, montagem de paradas, rolagens próprias e atualização contínua de estados secundários.

As primeiras versões da pesquisa estimaram reduções de **75% a 85% no número de rolagens/tempo de resolução** e de cerca de **90% no rastreio de variáveis**. Esses números devem ser tratados como **hipóteses de magnitude**, não como resultados demonstrados. Simulações probabilísticas não medem tempo real de mesa nem carga cognitiva; esses ganhos exigem playtests cronometrados e comparação com mesas usando M20 sem a camada player-facing.

O critério de sucesso desta pesquisa não é alcançar uma porcentagem específica. É obter uma redução operacional grande o bastante para ser útil ao Storyteller **sem transferir custo, novas regras ou distorções relevantes para os jogadores**.

### Regra de precedência

As auditorias posteriores revelaram um conflito real entre objetivos. Em certos procedimentos de M20 — especialmente quando um NPC age contra um PJ que não declarou defesa ativa — toda a aleatoriedade original pode estar no lado do Storyteller.

Nesses casos, três objetivos não podem ser garantidos simultaneamente:

1. zero rolagens do Storyteller;
2. nenhuma nova rolagem ou custo para o jogador;
3. preservação da distribuição e economia de ações original.

Quando houver esse conflito, a prioridade desta pesquisa é **preservar a experiência do jogador**. A pureza de “100% player-faced” é subordinada a esse critério.

---

## 🎭 4. A Justificativa de Design: O Narrador Também Joga

A reestruturação proposta neste manifesto e as transformações da Crônica e Cenas em Relógios (Obstáculos de Nível 3) não visam apenas "facilitar" o fluxo mecânico para os jogadores. O objetivo mais profundo é **devolver o jogo ao Narrador**.

No sistema tradicional, o Mestre acaba rebaixado à função de "servidor" ou crupiê: ele queima a maior parte do seu tempo de atenção rolando dados irrelevantes, anotando pontinhos de absorção e simulando física de NPCs secundários, como se prestasse um *serviço computacional* invisível para que apenas os jogadores se divirtam.

Ao deslocar a aleatoriedade relevante para as interações com os jogadores e comprimir o que existe atrás do escudo, o Narrador recupera atenção para intenção, interpretação, descrição e consequência. Ele **continua jogando por meio dos NPCs**: declara suas ações, ocupa a iniciativa, escolhe objetivos e produz pressão sobre a cena. O que se pretende retirar é a obrigação de operar uma segunda máquina probabilística completa para cada entidade.

A telegrafia surge, nos estudos posteriores, como forma de tornar consequências excepcionais causalmente legíveis: uma ameaça pode avisar, preparar-se ou já produzir um efeito menor que estabelece o estado para uma escalada maior. O prazer do Narrador desloca-se do microgerenciamento numérico para a condução ativa da ficção, sem retirar a agência dos jogadores.
