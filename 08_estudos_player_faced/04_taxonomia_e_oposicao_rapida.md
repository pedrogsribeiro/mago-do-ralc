---
type: regra
summary: "Estudo 4 do Sistema Player-Faced: taxonomia de 3 níveis de carga narrativa e oposição rápida calibrada como hipótese de compressão de M20."
tags: [srd, design, player-faced, taxonomia, oposicao-rapida, oposicao-menor, regras]
---

# Estudo 04: Taxonomia de Carga Narrativa e Oposição Rápida
## 🏛️ 1. Taxonomia dos Obstáculos

A revisão posterior do Perfil DRP mostrou que três classificações diferentes estavam sendo sobrepostas. Elas passam a ser tratadas como **eixos independentes**.

### Eixo A — Passivo / Ativo

**Passivo** é o Obstáculo que não possui agência própria relevante na cena. Ele resiste, impede, exige progresso, causa risco ambiental ou mantém estados, mas não escolhe ações como um agente.

**Ativo** é o Obstáculo que possui agência: declara ações, escolhe alvos, ocupa iniciativa quando o procedimento exigir, reage estrategicamente e pode produzir consequências por decisão própria.

A distinção é ontológica. Um Obstáculo passivo e um agente ativo podem ter a mesma carga operacional e até usar a mesma notação curta, mas continuam sendo coisas diferentes na ficção e na resolução.

### Eixo B — Simples / Elaborado

**Simples** descreve um Obstáculo cuja operação exige pouca informação explícita. Pode ser apenas um default como `6`, ou `6` mais uma ação como `Soco: 2S + 2C`.

**Elaborado** descreve um Obstáculo que precisa de mais estrutura: dimensões distintas, ações próprias, Persistência, estados, poderes, exceções, comportamento, objetivos e conteúdo diegético.

Simples/elaborado mede **densidade operacional**, não agência. Portanto existem Obstáculos passivos simples, passivos elaborados, ativos simples e ativos elaborados.

### Eixo C — Pontual / Persistente / Alto Impacto

A antiga taxonomia de três níveis continua útil, mas passa a descrever **carga de cena**, não tamanho de ficha:

- **Pontual:** uma resolução curta sem acompanhamento persistente;
- **Persistente:** o Obstáculo permanece relevante por várias ações, turnos ou etapas;
- **Alto impacto/telegrafado:** uma ação, estado ou escalada exige cadeia causal legível e oportunidade significativa de intervenção.

O mesmo Obstáculo pode mudar de carga de cena sem mudar sua ontologia. Um guarda ativo simples pode ser pontual numa conversa e persistente numa perseguição. Uma ameaça ativa elaborada pode executar uma ação telegrafada de alto impacto.

### Relação com o Perfil DRP

O **Perfil DRP é a linguagem mecânica**, não uma dessas categorias. Ele pode representar qualquer combinação dos eixos acima com resolução progressiva e forma esparsa.

Exemplos:

```
Porta emperrada
6
```

= passivo, simples, normalmente pontual.

```
Capanga
6
Soco: 2S + 2C
```

= ativo, simples.

```
Sistema hipertecnológico
6
Mental/Técnico: 8/3/2
Mágicko: 7/2/2
Persistência: [...]
Estados: [...]
```

= passivo ou semiativo conforme a ficção, elaborado e possivelmente persistente.

```
Antagonista nomeado
Físico: [...]
Social: [...]
Mental/Técnico: [...]
Mágicko: [...]
Ações: [...]
Persistência: [...]
Motivações: [...]
Comportamento: [...]
```

= ativo, elaborado.

A quantidade de campos nunca deve ser confundida com potência. Um Obstáculo simples pode ser muito perigoso; um elaborado pode apenas exigir mais definição porque possui mais funções relevantes.

---

## ⚡ 2. Funcionamento da Oposição Rápida

Na oposição pontual existe um agente real — guarda, informante, motorista, hacker, espírito — mas a cena não merece estrutura persistente.

O NPC continua agindo ficcionalmente. Quando sua ação disputa diretamente algo sob agência de um PJ, a incerteza é ancorada na rolagem do jogador. Quando não há agência de jogador envolvida, o Storyteller decide o desfecho conforme a ficção e as capacidades estabelecidas.

### 2.1. Conversão matemática

A hipótese inicial deste estudo usava somente a Dificuldade do dado para representar a competência do NPC. Auditorias exatas posteriores mostraram que isso não preserva adequadamente uma rolagem resistida de M20.

O refinamento atual usa **Dificuldade + Limiar oculto**, ainda como hipótese experimental:

| Parada relevante do NPC | Diff do PJ | Limiar oculto |
| :---: | :---: | :---: |
| 2d | 6 | 1 |
| 3d | 6 | 1 |
| 4d | 7 | 1 |
| 5d | 6 | 2 |
| 6d | 6 | 2 |
| 7d | 7 | 2 |
| 8d | 7 | 2 |
| 9d | 6 | 3 |
| 10d | 7 | 3 |
| 11d | 7 | 3 |
| 12d | 7 | 3 |

Essa tabela reduz muito o erro da hipótese “apenas dificuldade”, mas não reproduz perfeitamente a variância de uma segunda rolagem independente. Ela deve permanecer sujeita a revisão enquanto a curva de competência dos PJs não estiver suficientemente preservada.

---

## 🎲 3. Leitura dos Resultados

A leitura continua sendo a de M20:

* **1 sucesso líquido:** sucesso marginal; faz a ficção andar.
* **2 sucessos:** resultado moderado/seguro.
* **3+ sucessos:** qualidade progressivamente maior.
* **0 sucessos:** falha simples.
* **Botch:** falha crítica conforme a regra aplicável.

Essa leitura vale tanto para testes pontuais quanto para ações dentro de conflitos persistentes. A diferença é o que acontece **depois**:

* em um **teste simples**, o resultado resolve aquela ação;
* contra um Obstáculo com **Integridade/Relógio**, um sucesso também produz Impacto mecânico sobre sua estrutura.

Assim, **1 sucesso continua sendo sucesso marginal e, em princípio, reduz 1 ponto/caixa da Integridade ou Relógio**, além de mover a ficção. Um Limiar de Efetividade legítimo pode reduzir o Impacto que atravessa, mas não transforma retroativamente o sucesso em falha.

Uma consequência, custo, atraso ou exposição pode acompanhar um resultado marginal quando a ficção justificar, mas **não é uma obrigação mecânica automática**.

---

## 🪄 4. Mágika e Oposição Pontual

Quando o PJ usa Arete/Mágika diretamente, permanecem válidas as dificuldades e regras próprias de M20 para o efeito mágico. A compressão da oposição não autoriza substituir a lógica de Arete, Esferas, vulgaridade, testemunhas, Paradoxo ou outros componentes de M20 por uma dificuldade genérica.

Quando a mágika altera uma ação mundana, aplica-se primeiro a regra mágica pertinente e depois se determina como o efeito modifica a ação mundana. A intenção é preservar a experiência de M20 para o jogador, não criar um atalho universal de “mágika reduz Diff”.

---

## 🎬 5. Exemplos de Uso

### Infiltração social
Hughie tenta enganar um porteiro. O porteiro é um agente ficcional real, mas a cena não merece estrutura persistente. A parada relevante do porteiro é convertida para a oposição experimental; Hughie faz sua rolagem normal. Um sucesso já permite a entrada em nível marginal, e o ST qualifica a qualidade desse êxito pela ficção.

### Percepção contra furtividade
Um agente tenta se ocultar. O agente continua sendo quem realiza a ação na ficção. O PJ rola para perceber contra a oposição comprimida do agente. Se ninguém relevante estiver em posição de perceber, o ST decide se a ocultação funciona sem rolar contra si mesmo.

### Perseguição curta
Um motorista da ABIN tenta manter contato com o carro dos PJs. Enquanto a situação não justificar uma perseguição estruturada, uma única resolução pode decidir uma mudança relevante de posição.

Se a perseguição se tornar o foco da cena, ela sobe para Nível 2 e passa a usar a lógica **estendida-resistida** documentada no Estudo 17. Nesse caso, o Relógio acompanha **posição/progresso**, não dano do veículo.

---

## 6. Critério de Transição

O nível muda quando muda a **carga necessária para representar a situação**, não porque a entidade pertence a uma categoria fixa.

O mesmo NPC pode ser:
* Nível 1 em uma interação de poucos segundos;
* Nível 2 quando se torna ameaça persistente;
* Nível 3 quando executa uma ação de alto impacto que exige estado, preparação ou escalada legível.
