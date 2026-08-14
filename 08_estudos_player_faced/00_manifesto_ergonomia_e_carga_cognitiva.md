---
type: regra
summary: "Estudo 00 do Sistema Player-Faced: Manifesto sobre o gargalo cognitivo do M20 clássico, a hipótese de design e as estimativas métricas de ganho de tempo e ergonomia mental do Narrador."
tags: [srd, design, player-faced, ergonomia, problematica, estimativas, manifesto, regras]
---

# Estudo 00: A Problemática do M20 Clássico e o Manifesto de Ergonomia Cognitiva

Este documento estabelece a premissa central de *Game Design* que originou a criação do **Motor Player-Faced Total** para *Mago: A Ascensão 20 Anos*. Ele detalha a problemática da sobrecarga do Narrador no sistema original e formaliza as estimativas métricas de ganho de tempo e redução de carga mental alcançadas pela nossa hipótese de design.

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

**A Hipótese Central:** *É possível diminuir a carga cognitiva do Storyteller e acelerar a experiência (diminuindo tanto o número de rolagens de dados quanto a quantidade de variáveis gerenciadas) sem perder a profundidade da experiência dos jogadores nem quebrar a matemática das rolagens do d10.*

### Como a Solução foi Alcançada (A Raiz do Design)
Para comprovar a hipótese, o sistema foi reestruturado utilizando as seguintes bases:
1. **Regra de Bronze do Fate Core:** Tudo no cenário (um feitiço, uma porta, um inimigo) pode ser modelado usando uma taxonomia de oposição unificada.
2. **Transferência Player-Faced (Influência PBTA/OSR):** O Narrador passa a rolar **Zero Dados**. As consequências do perigo são sempre ativadas pelos resultados das rolagens dos próprios jogadores (A Matemática Trinomial: $\ge 2s$ = Sucesso Pleno, $1s$ = Parcial com Custo, $0s$ = Falha Simples).
3. **Compressão Simétrica do NPC:** A longa lista de atributos é descartada em prol de uma Ficha Sintética estruturada em apenas 4 variáveis (Imposição, Pressão, Impacto/Dano Fixo e Relógio de Vitalidade).

---

## 📈 3. Estimativas de Ganho Cognitivo e de Tempo de Mesa

A transição para o modelo Player-Faced Total nos Níveis 2 (Ameaça Ativa) e 3 (Ameaça Telegrafada) gera impactos quantificáveis na fluidez da mesa:

### ⏱️ Ganho de Tempo e Agilidade (Redução de 75% a 85%)
Ao eliminar as rolagens defensivas do NPC (absorvidas pelo Dano Fixo, RD e Relógios de Cena), o ciclo muda radicalmente:
* **Turno Player-Faced:** O PJ declara a ação e rola **1 única vez**. Se o NPC atacar, o PJ rola **1 única vez** para se defender contra um perigo telegrafado.
* **Métrica:** Redução de 8 rolagens para apenas **2 rolagens de dados por turno**.
* **Impacto Prático:** Uma cena de infiltração tática ou um combate que levaria **45 minutos** no M20 clássico passa a ser resolvida em **10 a 15 minutos** de intensidade focada nas decisões dos jogadores.

### 🧠 Ganho de Ergonomia Mental (Redução de 90% do Rastreio)
A substituição das fichas exaustivas pela Simetria de 4 Dimensões limpa a interface visual do Narrador.
* **Métrica:** A carga de rastreio de variáveis (Tracking) cai de $\approx 50$ itens para apenas **4 atributos mecânicos diretos** (Diff do PJ atacar, Diff do PJ se defender, Dano que o PJ recebe, Caixas do Relógio) atrelados a campos semânticos (Aspectos descritivos).
* **Impacto Prático:** O Mestre não realiza mais subtrações de dados na própria cabeça, eliminando a fadiga de processamento matemático de fundo. **100% dessa energia cognitiva recuperada é redirecionada** para interpretar o vilão com maestria, gerenciar o drama dos personagens e descrever o cenário de forma imersiva.
