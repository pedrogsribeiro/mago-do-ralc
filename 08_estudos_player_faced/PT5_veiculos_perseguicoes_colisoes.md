---
type: estudo
status: homologado
summary: "PT-5 concluído e homologado: veículos, perseguições e colisões preservados em forma player-facing sem fundir condutor, posição, integridade e ocupantes."
tags: [player-faced, pt-5, veiculos, perseguicoes, colisoes, durability, structure, direcao]
---

# PT-5 — Veículos, Perseguições e Colisões

## 1. Princípio do pacote

M20 já fornece uma ficha veicular compacta. A camada player-facing deve preservá-la em vez de reconstruir o veículo como NPC.

A ficha operacional continua centrada em:

```text
Safe Speed
Max Speed
Maneuverability
Durability
Structure
[Weapons, quando houver]
```

O **condutor** e o **veículo** permanecem entidades funcionais distintas:

- o condutor possui agência, competências e decisões;
- o veículo possui limites, resistência e integridade;
- a perseguição possui posição/progresso;
- a colisão possui seu próprio procedimento de impacto.

Não se fundem essas quatro coisas numa única ficha ou relógio.

---

# 2. Direção e manobras

Manobras perigosas permanecem testes do jogador:

```text
Destreza + Direção/Pilot
Dificuldade: conforme manobra, terreno, condição, dano e velocidade
Pool limitado por Maneuverability
Excesso sobre Safe Speed aumenta a dificuldade conforme a regra
```

Isso já é player-facing.

**Conversão adicional: nenhuma.**

Max Speed continua sendo limite físico/prático do veículo, não uma dificuldade ou recurso.

---

# 3. Perseguições

Quando existe um rival ativo, a perseguição permanece uma ação estendida-resistida.

```text
PJ rola sua condução/manobra
→ competência do condutor rival é convertida pelo operador de Oposição já homologado
→ sucessos líquidos alimentam posição/progresso
```

Quando não há rival ativo, mas apenas trânsito, terreno, clima ou rota difícil, trata-se de Obstáculo passivo do PT-3/PT-4.

## Relógio de posição

O Relógio pode exibir os sucessos acumulados da perseguição:

```text
POSIÇÃO
0 / N
```

Ele representa vantagem posicional, não dano ao carro.

**1 sucesso líquido continua produzindo 1 avanço**, porque a interface apenas acompanha a ação estendida original.

---

# 4. Veículo como objeto persistente

Durability e Structure já resolvem resistência e integridade:

```text
dano
→ Durability reduz
→ excedente reduz Structure
```

Não se cria:

- soak rolado pelo ST;
- Proteção DRP duplicando Durability;
- Vitalidade paralela;
- relógio de dano paralelo à Structure.

Quando Structure é suficientemente reduzida, o veículo deixa de cumprir sua função conforme a regra original.

---

# 5. Colisões

Colisão é procedimento separado da perseguição.

O impacto parte dos elementos recuperados na fonte:

```text
Durability do veículo
+ velocidade
+ modificador de massa/categoria, quando aplicável
→ dano de impacto
```

O tipo-base é Contundente, salvo circunstância/regra específica.

A camada player-facing **não converte colisão em dano fixo por tier** e não inventa um Perfil DRP para o choque.

---

# 6. Dano aos ocupantes

O dano transmitido aos ocupantes permanece distinto do dano à Structure.

A fonte consolidada preserva:

- proteção fornecida pela Durability do veículo;
- proteção adicional relevante de cintos;
- diferenças de proteção entre categorias de veículo.

Pipeline operacional:

```text
impacto
→ proteção do veículo
→ proteção adicional prevista
→ dano ao ocupante
→ PJ usa apenas suas respostas normais quando a regra permitir
```

Nenhuma rolagem do veículo ou do ST é criada.

---

# 7. Colisão entre veículos

Para cada lado, registram-se separadamente:

1. impacto recebido;
2. Durability;
3. dano que atravessa para Structure;
4. dano transmitido aos ocupantes.

Assim, uma mesma colisão pode danificar um veículo sem ferir ocupantes, ferir ocupantes sem destruir o veículo ou afetar os dois de formas diferentes.

O Relógio de perseguição continua separado de todos esses resultados.

---

# 8. Obstáculos e condições de pista

Trânsito, chuva, gelo, multidão, estrada ruim e obras não possuem agência.

Eles alteram apenas o que M20 já permite alterar:

- dificuldade;
- condições da manobra;
- possibilidade de certas ações;
- consequência de falha;
- posição/progresso quando a situação for estendida.

Nenhum desses elementos recebe iniciativa, ação ou ficha de NPC.

---

# 9. Condutor rival

O veículo adversário não recebe D/R apenas por estar em oposição.

Quem oferece oposição ativa é o **condutor** quando a situação depende da competência dele.

Exemplo estrutural:

```text
SEDÃ DA NOM

Veículo:
Safe Speed: ...
Max Speed: ...
Maneuverability: ...
Durability: ...
Structure: ...

Condutor:
Direção relevante → Perfil/Oposição pré-convertida

Perseguição:
Posição 0 / N
```

Se o veículo for realmente autônomo e tiver agência própria, deixa de ser mero objeto e entra na categoria de constructo-agente, a ser tratada no pacote correspondente.

---

# 10. Armas veiculares

Quando a fonte de um veículo trouxer armas, elas permanecem **ações do agente/constructo que as opera**, usando o procedimento ofensivo já homologado pertinente.

O veículo não ganha uma "Ameaça" genérica apenas por possuir armamento.

Sem números específicos no corpus atual deste pacote, o PT-5 não inventa estatísticas de armas veiculares.

---

# 11. Ficha operacional mínima

```text
VEÍCULO

Safe Speed:
Max Speed:
Maneuverability:
Durability:
Structure:
[Weapons:]

Características:
[blindagem, tração, transporte, sensores etc., somente quando relevantes]
```

Se houver perseguição:

```text
POSIÇÃO
0 / N
```

Se houver condutor rival:

```text
CONDUTOR
Oposição relevante: D/R pré-convertido
```

Essa separação reduz consulta sem apagar as funções originais.

---

# 12. Auditoria do escopo da EAP

- [x] Safe Speed preservado;
- [x] Max Speed preservado;
- [x] Maneuverability preservada;
- [x] Durability preservada;
- [x] Structure preservada;
- [x] direção e manobras preservadas;
- [x] perseguições mantidas como estendidas-resistidas quando houver rival;
- [x] Relógio de posição separado de dano/integridade;
- [x] colisões preservadas como procedimento específico;
- [x] dano aos veículos preservado;
- [x] dano aos ocupantes preservado;
- [x] obstáculos de pista tratados como passivos;
- [x] condutor rival tratado como agente;
- [x] armas veiculares enquadradas como ações quando existirem;
- [x] nenhum veículo passivo transformado artificialmente em NPC.

## Pendências de fonte antes da publicação

- [ ] conferir tabelas completas de veículos em M20 pp. 458–462;
- [ ] conferir incrementos exatos de velocidade;
- [ ] conferir modificadores exatos de massa/categoria;
- [ ] conferir valores de proteção de cintos/categorias;
- [ ] selecionar exemplos de veículos para o produto final.

Essas pendências são documentais. A arquitetura não exige nova matemática.

## Gate

O Storyteller pode operar veículo, perseguição e colisão mantendo separados condutor, posição, integridade e ocupantes, sem introduzir novas rolagens do ST.

**PT-5: CONCLUÍDO E HOMOLOGADO. As conferências de tabelas permanecem pendências editoriais para publicação.**
