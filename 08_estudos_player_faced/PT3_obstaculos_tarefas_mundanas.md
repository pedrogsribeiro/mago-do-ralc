---
type: estudo
status: homologado
summary: "PT-3 homologado após revisão corretiva: obstáculos e tarefas mundanas preservam os procedimentos player-facing de M20 e a interface compacta foi aprovada."
tags: [player-faced, pt-3, obstaculos, tarefas, acoes, drp, durability, structure]
---

# PT-3 — Obstáculos e Tarefas Mundanas

## Nota de revisão corretiva

O núcleo que preserva procedimentos já player-facing de M20 permanece válido. Em 2026-09-28, o autor aprovou explicitamente o PT-3 após a apresentação das pendências corretivas. A interface compacta permanece uma forma editorial de representar regras existentes, sem criar novos números ou procedimentos.

## 1. Princípio do pacote

Este pacote trata o mundo inanimado e tarefas sem agência própria.

A conclusão central das fontes e dos estudos anteriores é simples: **grande parte deste subsistema já é player-facing em M20**. Em testes simples e estendidos, quem rola é o próprio PJ. Portanto, a conversão deve principalmente organizar a informação do Storyteller e impedir que uma porta, pesquisa ou sistema passivo seja inflado até virar uma ficha de NPC.

A ficha mínima de um Obstáculo passivo só contém o que a regra realmente exige.

```text
OBSTÁCULO
Dificuldade: N
[Alvo de sucessos / intervalo, somente se estendido]
[Durability / Structure, somente se objeto material relevante]
[Consequência / gatilho, somente se houver]
```

Quando a dificuldade for a padrão de M20 e não houver outra propriedade relevante, a representação esparsa pode continuar sendo simplesmente:

```text
6
```

## 2. Regra de decisão

### 2.1 Tarefa simples

M20 exige um único teste e **1 sucesso líquido conclui a tarefa**.

Player-facing:

```text
Dificuldade
→ PJ rola sua parada normal
→ 1S já realiza a ação
→ sucessos adicionais qualificam o resultado segundo M20
```

Não se cria Resistência, Structure ou relógio apenas para dar "corpo" ao Obstáculo.

### 2.2 Tarefa estendida

Quando M20 já exige acumular sucessos:

```text
Dificuldade
Alvo de sucessos
Intervalo
```

O jogador continua fazendo as mesmas rolagens. Falha simples não produz progresso no intervalo; botch mantém as consequências previstas pela regra original.

Um relógio pode ser apenas a **interface visual do total de sucessos acumulados**. Ele não altera a mecânica.

### 2.3 Tarefa resistida

Uma tarefa só recebe D/R quando há **oposição ativa real**.

Exemplo estrutural:

```text
PJ se esconde
→ guarda percebe ativamente
→ parada do guarda é convertida para D/R
```

Uma fechadura, arquivo morto ou parede não recebe R porque não possui agência.

### 2.4 Estendida e resistida

Preserva-se o procedimento de competição prolongada. Se o oponente for um agente, sua contribuição é convertida pelos operadores já homologados do lado do NPC. Se não houver agente real, a tarefa é apenas estendida.

### 2.5 Tentativas repetidas

Preservar M20:

- cada tentativa falhada acrescenta +1 à Dificuldade;
- mudança radical de tática ou ferramenta zera essa penalidade.

Nenhuma camada player-facing adicional é necessária.

### 2.6 Cooperação

Preservar M20:

- em ação estendida, jogadores podem somar sucessos;
- botch de um participante pode arruinar o esforço coletivo, salvo a regra de assumir a falha;
- testes complementares reduzem a dificuldade do teste principal conforme a regra original.

Também aqui o Storyteller não precisa rolar.

---

# 3. Objetos materiais: Durability + Structure

Quando o objeto possui Traits materiais próprios, a arquitetura de M20 já é compacta:

```text
Durability = resistência fixa
Structure = integridade funcional
```

Pipeline:

```text
dano do PJ
→ Durability reduz
→ excedente reduz Structure
→ ao perder Structure suficiente, o objeto deixa de funcionar/quebra
```

Isso já é player-facing. Não se converte Durability em uma nova rolagem de soak nem se duplica Structure com outro relógio.

Para portas, paredes, máquinas e barreiras sem valores canônicos disponíveis no corpus atual, este pacote **não inventa tabelas numéricas**. O texto final deve usar os valores fornecidos pela fonte aplicável ou por uma futura tabela licenciada/conferida.

---

# 4. Famílias operacionais

## 4.1 Portas, fechaduras e barreiras

### Abrir / destravar

Se o problema é superar um mecanismo:

```text
Dificuldade: conforme a tarefa e as condições
1 sucesso conclui se for ação simples
```

Se a própria fonte tratar o trabalho como prolongado, acrescentam-se alvo de sucessos e intervalo.

### Arrombar / destruir

Se a barreira é tratada como objeto material:

```text
Durability
Structure
```

Não se mistura automaticamente "abrir a fechadura" com "destruir a porta". São abordagens diferentes e podem acionar regras diferentes.

## 4.2 Investigação e busca

Busca e investigação mundanas permanecem testes do PJ.

A ficha do Obstáculo precisa, no máximo, informar:

```text
Dificuldade
o que 1 sucesso encontra
o que sucessos adicionais qualificam, quando isso importar
consequência de falha/botch, se houver
```

Não há resistência automática do cenário.

Se alguém estiver **ativamente ocultando, mentindo, destruindo pistas ou disputando a busca**, essa pessoa é um agente e entra pela regra de oposição apropriada.

## 4.3 Infiltração e furtividade contra segurança passiva

Segurança passiva — fechadura, câmera automática simples, sensor, protocolo — é Obstáculo.

Pode ser representada por:

```text
Dificuldade
Gatilho de detecção/falha
[progresso, somente se a invasão for estendida]
```

Se existe guarda, operador ou perseguidor consciente, a interação deixa de ser puramente passiva e consulta o perfil do agente.

## 4.4 Reparos, pesquisa e trabalhos prolongados

A fonte já oferece a estrutura necessária:

```text
Dificuldade
Alvo de sucessos
Intervalo
```

O ST prepara esses três parâmetros e acompanha sucessos. Não precisa de uma ficha maior.

Trabalho em equipe e testes complementares continuam disponíveis exatamente como em M20.

## 4.5 Computadores e sistemas comuns

Antes de entrar no subsistema específico da Teia Digital, sistemas comuns seguem a mesma distinção:

- **barreira passiva**: Dificuldade / alvo / gatilho;
- **programa simples que apenas detecta ou bloqueia**: continua sistema;
- **operador consciente ou programa com agência própria**: pertence à oposição ativa e será tratado pelos pacotes correspondentes.

Não existe necessidade de criar uma ficha universal de "ICE" ou de computador para o PT-3.

---

# 5. Representações mínimas

As formas abaixo são **gramática**, não uma nova tabela de dificuldades.

### Exemplo estrutural de Obstáculo simples

```text
OBSTÁCULO SIMPLES
Dificuldade: valor definido pela regra/tarefa aplicável
```

A dificuldade padrão geral de M20 é 6, mas este documento não fixa toda fechadura comum em D6 sem fonte específica.

### Obstáculo simples com consequência

```text
ALARME PASSIVO
Dificuldade: conforme o sistema
Falha/Botch: dispara o alerta conforme a ficção/regra pertinente
```

### Trabalho prolongado

```text
REPARO COMPLEXO
Dificuldade: conforme condições
Alvo: N sucessos
Intervalo: conforme a tarefa
```

### Objeto resistente

```text
BARREIRA MATERIAL
Durability: valor da fonte
Structure: valor da fonte
```

### Obstáculo com agente

```text
SISTEMA + GUARDA
Sistema: dificuldade/gatilho passivo
Guarda: consultar Perfil DRP do NPC
```

A composição não transforma o sistema em NPC nem dissolve o agente em uma dificuldade.

---

# 6. O que o ST deixa de fazer

Neste pacote, o ganho de carga cognitiva vem principalmente de **não criar trabalho que M20 já não exigia**.

O ST não precisa:

- rolar por portas, arquivos, oficinas ou computadores passivos;
- preencher quatro dimensões para um Obstáculo que só precisa de Dificuldade;
- transformar uma tarefa simples em relógio;
- dar iniciativa ou ações a um sistema sem agência;
- recalcular pools de agentes quando o perfil DRP já existir;
- duplicar Durability/Structure com Proteção/Persistência paralelas.

---

# 7. Auditoria do escopo da EAP

- [x] portas, fechaduras, barreiras e objetos resistentes;
- [x] investigação e busca;
- [x] infiltração e furtividade contra segurança passiva;
- [x] reparos, pesquisa e trabalhos prolongados;
- [x] computadores e sistemas comuns fora do aprofundamento da Teia Digital;
- [x] ações simples;
- [x] ações estendidas;
- [x] ações resistidas somente com agente real;
- [x] ações estendidas-resistidas preservadas;
- [x] retries preservados;
- [x] cooperação e testes complementares preservados;
- [x] Durability/Structure usados somente quando pertinentes;
- [x] relógio tratado apenas como interface de progresso já existente.

## Exceções / limites documentais

O corpus atual não fornece, neste pacote, uma tabela geral confirmada de Durability/Structure para portas, paredes e materiais mundanos. Por isso, o PT-3 fecha **a gramática e o procedimento**, mas não inventa números de objetos.

Hacking detalhado e Teia Digital permanecem no PT-6. Riscos ambientais permanecem no PT-4. Veículos permanecem no PT-5.

## Gate

O Storyteller pode representar um Obstáculo mundano desde `6` até Dificuldade + progresso + gatilho ou Durability + Structure sem rolar dados e sem reconstruir subsistemas novos.

**PT-3: CONCLUÍDO E HOMOLOGADO APÓS REVISÃO CORRETIVA.**
