---
type: auditoria
status: aplicada_parcialmente
summary: "Auditoria corretiva dos PT-2 a PT-8, separando cada achado em aplicação válida de regra homologada, inferência dos agentes, decisão autoral explícita ou erro factual/conversão."
tags: [player-faced, auditoria, corretiva, pt-2, pt-3, pt-4, pt-5, pt-6, pt-7, pt-8, homologacao]
---

# Auditoria corretiva — PT-2 a PT-8

## 1. Escopo e método

Esta auditoria aplica exatamente quatro classes:

1. **Aplicação válida de regra homologada** — transformação já autorizada para a mesma função e aplicada corretamente.
2. **Inferência dos agentes** — extrapolação, preenchimento, organização ou proposta produzida sem decisão autoral explícita suficiente.
3. **Decisão autoral explícita** — decisão inequivocamente aprovada pelo autor.
4. **Erro factual/conversão** — dado incorreto, cálculo incorreto, contradição com fonte/contrato ou homologação registrada sem base autoral válida.

A classificação usa como precedência:

```text
Contrato do produto
→ decisões autorais explícitas
→ regras/fontes consolidadas
→ transformações já homologadas para a mesma função
→ estudos e propostas dos agentes
```

Uma inferência mecanicamente plausível continua sendo **inferência** até decisão autoral explícita.

---

# 2. Achado transversal: homologações inválidas

## Classe 4 — Erro factual/conversão

Os PT-2, PT-3, PT-4, PT-5, PT-6 e PT-7 foram marcados em momentos diferentes como `CONCLUÍDO E HOMOLOGADO` após comandos genéricos de progressão como “segue”.

Pela regra agora explicitada — e já exigida em substância pela EAP anterior ao falar em “homologação autoral” — isso não constitui aprovação inequívoca do pacote.

### Consequência

O rótulo `homologado` desses pacotes **não pode ser usado como prova de aprovação autoral das inferências internas**.

Isso não invalida automaticamente as transformações que já possuíam base homologada anterior. Cada conteúdo precisa ser classificado individualmente abaixo.

O PT-8 não chegou a ser marcado como homologado, mas contém implementações de decisões novas sem autorização prévia.

---

# 3. PT-2 — Animais e Bestiário Mundano

## Classe 1 — Aplicação válida de regra homologada

- conversão das paradas de defesa física para D/R pela tabela já existente;
- conversão de soak para P dentro da faixa já coberta;
- conversão de ataques naturais por parada ofensiva + dificuldade para S, quando a ação usa a mesma função física já estudada;
- conversão do pool-base de dano para efeito C/L;
- iniciativa fixa por `Destreza + Raciocínio + 6`;
- preservação das trilhas de Vitalidade e Força de Vontade;
- manutenção do efeito específico de Assédio do Pássaro Pequeno, que já vem da fonte como penalidade fixa;
- enxugamento da lista de Ações para evitar reproduzir a ficha original inteira, desde que nenhuma capacidade mecânica necessária seja apagada.

## Classe 2 — Inferência dos agentes

- atribuir automaticamente `L0·A0` a animais mundanos sem uma regra animal específica de absorção por tipo consolidada no pacote;
- tratar “armadura natural 1” de Tigre/Leão, Cavalo e Crocodilo apenas como característica quando sua cobertura por tipo de dano não estava confirmada;
- descrições como “caçador em grupo”, “predador de emboscada”, “atento e treinável”, “intimidador” e similares quando não derivadas literalmente da ficha/regra consolidada;
- assumir que ausência de uma Habilidade listada equivale operacionalmente a valor 0 para toda situação sem registrar a regra geral de uso destreinado pertinente.

## Classe 3 — Decisão autoral explícita

- trabalhar os animais **em lotes**, evitando homologação perfil a perfil;
- manter as fichas finais **menores que as originais**;
- não transformar toda Habilidade em Ação;
- Gato Doméstico recebeu aprovação explícita antes da aceleração em lote.

## Classe 4 — Erro factual/conversão

- o status global `homologado` do PT-2 foi inferido de progressão de trabalho e não de homologação explícita do pacote.

### Estado após auditoria

A maior parte da matemática física pode ser reaproveitada. A tipagem de absorção animal e as características acrescentadas pelo agente precisam ser apresentadas/limpas antes de nova homologação global.

---

# 4. PT-3 — Obstáculos e Tarefas Mundanas

## Classe 1 — Aplicação válida de regra homologada

- preservar ações simples como teste do PJ;
- preservar ações estendidas com Dificuldade, alvo de sucessos e intervalo;
- preservar ações resistidas somente quando existe oposição ativa;
- preservar retries e cooperação conforme M20;
- usar Durability e Structure quando a fonte realmente fornece esses Traits;
- não criar rolagem do ST para objeto passivo.

## Classe 2 — Inferência dos agentes

- o exemplo `FECHADURA COMUM: 6` foi apresentado como exemplo concreto sem fonte específica dizendo que uma fechadura comum sempre é D6; D6 é dificuldade padrão geral;
- a forma de ficha `Dificuldade / Gatilho / Estado` é uma organização editorial útil, mas é interface proposta, não regra extraída diretamente da fonte;
- classificar toda segurança passiva de computador na mesma gramática mínima é uma organização arquitetural do agente quando a fonte específica não tiver sido consultada.

## Classe 3 — Decisão autoral explícita

- princípio anterior de que tarefas simples do tipo “roubar uma carteira, arrombar uma porta” usam a leitura simples e não precisam de relógio/pontos de vida;
- preservação do modelo 2+/1/0 para testes simples, conforme decisões anteriores do projeto.

## Classe 4 — Erro factual/conversão

- status global `homologado` sem homologação autoral inequívoca do pacote.

### Estado após auditoria

O núcleo do PT-3 é predominantemente preservação de M20 e pode ser mantido; exemplos concretos e interface precisam permanecer identificados como exemplos/propostas até aprovação.

---

# 5. PT-4 — Riscos Ambientais e Perigos

## Classe 1 — Aplicação válida de regra homologada

Derivam diretamente do corpus consolidado:

- queda: 1 nível C por 3 m, máximo 10, conversões para L e absorção do PJ quando prevista;
- fogo: pools de dano A por intensidade e teste do PJ quando previsto;
- fome, sede e sufocamento: limites temporais e dano automático;
- radiação: dano A, intensidade e intervalo;
- toxinas: Vigor do PJ, dificuldade 6–9 e sucessos reduzindo dados de dano;
- explosões: reação do PJ quando permitida, cobertura/Durability e consequências secundárias;
- relógios apenas como interface quando representam tempo/exposição já existente.

## Classe 2 — Inferência dos agentes

- declarar genericamente que esses perigos já estão “mecanicamente completos” sem determinar, em cada caso com **pool de dano**, quem rola esse pool no procedimento original e como a regra satisfaz o invariante de zero dados do ST;
- tratar “dano ambiental definido pela situação” como suficiente para resolver qualquer pool variável sem uma transformação explícita;
- considerar doenças fechadas apesar de a própria fonte consolidada registrar tabela/intervalos/progressão ainda não conferidos.

## Classe 3 — Decisão autoral explícita

Nenhuma decisão autoral nova específica ao PT-4 foi localizada no fluxo que autorizasse transformar pools ambientais variáveis ou encerrar o pacote como homologado.

## Classe 4 — Erro factual/conversão

- status global `homologado` sem aprovação autoral explícita;
- o gate “nenhum risco ambiental exige rolagem do ST” foi declarado sem demonstrar isso para os riscos cujo dano ainda aparece em **dados**. Isso contradiz a definição de pronto do próprio projeto até que a propriedade da rolagem ou sua transformação seja comprovada.

### Estado após auditoria

As regras-fonte estão bem preservadas. O fechamento player-faced dos **pools ambientais de dano** precisa ser reaberto como questão, não automaticamente convertido.

---

# 6. PT-5 — Veículos, Perseguições e Colisões

## Classe 1 — Aplicação válida de regra homologada

- preservar Safe Speed, Max Speed, Maneuverability, Durability e Structure;
- preservar Direção/Pilot do PJ;
- separar integridade do veículo de dano aos ocupantes;
- tratar Durability como resistência fixa e Structure como integridade;
- preservar obstáculos de pista como condições/passivos quando não há agente;
- manter condutor e veículo como funções diferentes.

## Classe 2 — Inferência dos agentes

- `Relógio de posição 0/N` como interface para sucessos acumulados é proposta de interface dos estudos, não regra original de M20 nem decisão autoral explícita localizada nesta auditoria;
- afirmar que toda perseguição com rival deve usar Perfil DRP do condutor sem demonstrar, procedimento a procedimento, qual parada original está sendo comprimida;
- declarar colisões completamente resolvidas sem verificar se algum pool de dano/impacto ainda exigiria rolagem do ST no procedimento concreto;
- ficha mínima universal de veículo é organização editorial do agente, ainda que construída a partir dos Traits da fonte.

## Classe 3 — Decisão autoral explícita

Nenhuma decisão autoral nova específica localizada que homologasse o relógio de posição ou o fechamento integral do PT-5.

## Classe 4 — Erro factual/conversão

- status global `homologado` sem homologação explícita do pacote.

### Estado após auditoria

Os Traits de veículo e procedimentos do PJ estão bem ancorados. Relógio de posição e qualquer compressão de oposição/impacto permanecem propostas até decisão explícita.

---

# 7. PT-6 — Hacking e Teia Digital

## Classe 1 — Aplicação válida de regra homologada

- preservar `Computação + Arete` do PJ quando a regra assim determina;
- preservar Quintessência e outros recursos próprios;
- preservar testes estendidos do PJ;
- usar oposição ativa apenas quando há agente real, dentro dos operadores já homologados para oposição;
- não criar uma ficha universal de ICE sem base na fonte;
- preservar feedback, de-rez, Icon Death, Chaos Dump e Whiteout como consequências/estados quando a fonte os distingue.

## Classe 2 — Inferência dos agentes

- a taxonomia `sistema passivo / operador consciente / programa-agente / ameaça sistêmica` é uma organização arquitetural útil, porém não foi localizada como decisão autoral explícita;
- as fichas mínimas universais para firewall, sysadmin, programa simples, programa-agente e Whiteout são propostas editoriais;
- afirmar que programa com ações próprias necessariamente usa a mesma gramática completa de constructo-agente é extrapolação até que um perfil/procedimento concreto confirme isso;
- declarar arquitetura do PT-6 inteiramente fechada apesar de várias regras específicas ainda dependerem de conferência de fonte.

## Classe 3 — Decisão autoral explícita

- não criar uma ficha genérica de ICE sem base na regra original é coerente com direções autorais anteriores de evitar sistemas artificiais, mas esta auditoria não encontrou uma homologação explícita específica do pacote PT-6; portanto isso não autoriza o status global.

## Classe 4 — Erro factual/conversão

- status global `homologado` sem homologação autoral inequívoca.

### Estado após auditoria

O pacote contém principalmente boa preservação e organização, mas a taxonomia e as fichas-modelo precisam ser tratadas como propostas até aprovação.

---

# 8. PT-7 — Operativos Extraordinários, Ciborgues e Constructos Tecnocráticos

## Classe 1 — Aplicação válida de regra homologada

- D/R físico derivado das paradas pertinentes;
- P físico dentro da régua já existente;
- sucessos fixos de ataques físicos pela régua ofensiva já adotada;
- iniciativa fixa;
- preservação de Vitalidade, munição, sensores, módulos, hacking e estados especiais;
- conversões de Victor e HIT Marks que apenas aplicam operadores já homologados para ações/defesas físicas.

## Classe 2 — Inferência dos agentes

- converter a autodestruição do HIT Mark X de `8d L` diretamente para `3L` como se pool de explosão ambiental já estivesse homologado pela mesma régua de efeito físico ofensivo;
- algumas frases de caracterização operacional que não são necessárias para a conversão e não foram rastreadas diretamente à fonte;
- qualquer leitura de cobertura C/L/A anterior às decisões explícitas do autor.

## Classe 3 — Decisão autoral explícita

Foram explicitamente decididos pelo autor:

- **Contramágika Inata** permanece em dados e reduz diretamente a parada do PJ quando aplicável;
- extensão simples da régua de Proteção para a região adjacente, sem estudo matemático adicional: `10–11d → P4`, `12–13d → P5`;
- Proteção pode registrar **mais de um tipo de absorção** C/L/A; a coexistência de valores diferentes por tipo não é um problema operacional.

A aplicação concreta registrada depois dessa decisão foi:

```text
Ciborgue comum: C2·L0·A0
HIT Mark V:     C3·L2·A2
HIT Mark X:     C5·L2·A2
```

Como o autor respondeu à proposta de manter tipos separados com “pode fazer desse jeito”, essa tipagem é tratada aqui como decisão autoral explícita do fluxo.

## Classe 4 — Erro factual/conversão

- **Ciborgue com Módulo de Combate:** a fonte fornece Força 3–4, módulo +2 Força e garras `Força +1 L`. Isso gera pool-base de dano 6–7L. Pela própria régua usada no projeto, 6–8d → 3 de efeito. A linha `3S + 2–3L` está incorreta; o efeito-base deveria cair no mesmo degrau, `3L`;
- status global `homologado` do PT-7 foi registrado sem uma homologação explícita final do pacote. As três decisões acima são homologadas individualmente; o pacote inteiro não.

### Estado após auditoria

PT-7 é o pacote mais próximo de fechamento, mas precisa corrigir o módulo de combate, retirar/reabrir a conversão da autodestruição explosiva e receber homologação explícita do conjunto.

---

# 9. PT-8 — Despertos e Usuários de Mágika

## Classe 1 — Aplicação válida de regra homologada

- manter Arete, Esferas, paradigma/focos, Força de Vontade, Vitalidade e equipamentos;
- aplicar D/R/P **físicos** apenas onde a função física já está coberta;
- usar iniciativa fixa;
- converter ataques físicos/mundanos pela régua ofensiva quando forem a mesma função já homologada;
- preservar Aura de Medo do Terno Preto como teste do PJ, pois a regra-fonte já coloca a rolagem no jogador;
- preservar imunidade a Paradoxo dos Desauridos;
- preservar conectividade co-localizada da Colmeia.

## Classe 2 — Inferência dos agentes

- criar uma tabela geral `Arete + Dificuldade → S fixos` e aplicá-la a conjuração;
- tratar toda conjuração de NPC, hostil ou utilitária, como ação ofensiva comum;
- converter contramágika ativa de NPC automaticamente para S fixos;
- converter Reação de Paradoxo automaticamente pela mesma régua;
- tratar `0S` determinístico como falha simples sem botch como solução suficiente;
- concluir que as limitações probabilísticas dessas transformações são apenas “limitação geral do método” e não blockers;
- fichas mágickas finais que incorporam essas decisões como regra pronta.

## Classe 3 — Decisão autoral explícita

Nenhuma das transformações mágickas novas acima foi autorizada.

As decisões autorais anteriores aplicáveis ao PT-8 são apenas invariantes e decisões transversais já existentes, entre elas:

- experiência do PJ permanece M20;
- ST rola zero dados;
- mágika hostil unilateral e Reação de Paradoxo permaneciam dívidas abertas até solução homologada;
- Contramágika Inata mantém a decisão explícita do PT-7 quando surgir em entidades que a possuam.

## Classe 4 — Erro factual/conversão

Há contradições diretas com documentos normativos anteriores:

- o contrato lista **mágika hostil unilateral** como dívida aberta; PT-8 declarou-a resolvida por S fixos sem decisão autoral;
- o contrato lista **Reação de Paradoxo** como dívida aberta; PT-8 declarou-a resolvida por S fixos sem decisão autoral;
- Estudo 14 diz que a competência mágicka do NPC só pode virar Oposição quando houver correspondência clara e mantém mágika unilateral aberta; PT-8 generalizou o operador físico;
- Estudo 14 exige validação específica para compressão de contramágika ativa; PT-8 pulou essa validação;
- o gate “PT-8 mecanicamente completo” é, portanto, inválido.

Há ainda erros de conversão física na ficha produzida:

A revisão posterior de `regras_dano_e_saude.md` corrigiu um erro desta própria auditoria: **Magos/Despertos podem absorver dano Letal com Vigor**. Logo, nos perfis Despertos do PT-8, a Proteção Letal deve usar o pool total aplicável de absorção. Assim, Terno Preto e Homem de Cinza mantêm `L3`; Hacktivista, Músico Xamã e Pelourinho usam `L2`; Colmeia e Widderslainte usam `L1`. Agravado permanece 0 sem proteção específica.

### Estado após auditoria

O PT-8 precisa ser reaberto. A camada física reaproveitável deve ser separada das propostas mágickas. Nenhuma transformação nova de Arete, contramágika ativa ou Paradoxo deve permanecer como regra vigente sem proposta e decisão autoral.

---

# 10. Resumo executivo por classe

## 1. Aplicação válida de regra homologada

Predomina em:

- conversões físicas D/R/P;
- iniciativa;
- persistência;
- ações físicas já cobertas;
- preservação de procedimentos que já são player-facing;
- Durability/Structure;
- Traits veiculares;
- recursos e estados originais.

## 2. Inferência dos agentes

Concentra-se em:

- tipagens sem fonte confirmada;
- interfaces apresentadas como se fossem regra;
- taxonomias arquiteturais úteis porém não homologadas;
- relógios e templates universais;
- propagação de operadores físicos para explosões, mágika, Paradoxo e outras funções distintas;
- prosa característica acrescentada sem necessidade/fonte.

## 3. Decisão autoral explícita

Confirmadas nesta faixa:

- trabalho em lote para acelerar sem perder rastreabilidade;
- fichas menores que as originais e sem transformar toda Habilidade em Ação;
- Contramágika Inata reduz diretamente dados do PJ;
- extensão `10–11d→P4; 12–13d→P5`;
- Proteção pode ser tipada por C/L/A sem problema operacional;
- decisões anteriores do projeto sobre testes simples, experiência intacta do PJ e zero dados do ST continuam normativas.

## 4. Erro factual/conversão

Confirmados:

- homologações de pacotes inferidas de “segue”;
- PT-4 declarado fechado sem provar eliminação de pools ambientais do ST;
- Ciborgue de Combate com efeito `2–3L` em vez do degrau único `3L`;
- autodestruição explosiva do HIT X convertida por analogia sem autorização;
- PT-8 contradizendo dívidas abertas de mágika/Paradoxo;
- a versão inicial desta auditoria classificou incorretamente a Proteção Letal de Despertos usando apenas a parcela de armadura; isso foi corrigido após releitura da regra de absorção de Magos.

---

# 11. Checkpoint corretivo

As correções autorizadas pelo autor foram aplicadas aos PT-2 a PT-8:

- homologações globais indevidas foram rebaixadas para revisão corretiva;
- erros factuais/conversões inequívocos foram corrigidos;
- inferências não homologadas foram removidas, marcadas como proposta ou reabertas;
- decisões autorais explícitas foram preservadas;
- PT-8 voltou a registrar mágika unilateral, contramágika ativa e Reação de Paradoxo como dívidas abertas.

A sequência restante é:

```text
1. apresentar ao autor somente as lacunas mecânicas restantes como opções;
2. registrar decisões autorais explícitas;
3. homologar explicitamente pacote por pacote depois da correção;
4. somente então avançar para PT-9.
```

Nenhuma propagação editorial posterior deve ocorrer antes disso.
