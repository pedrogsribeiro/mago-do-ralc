---
type: estudo
status: em_revisao_corretiva
summary: "PT-4 em revisão corretiva: regras-fonte preservadas; pools ambientais variáveis reabertos quando a propriedade da rolagem do ST não está demonstrada."
tags: [player-faced, pt-4, riscos, ambiente, fogo, quedas, fome, sede, sufocamento, radiacao, toxinas, doencas, explosoes]
---

# PT-4 — Riscos Ambientais e Perigos

## Nota de revisão corretiva

As regras-fonte permanecem registradas. O pacote não pode ser considerado player-facing completo enquanto qualquer procedimento com **pool variável de dano** puder depender de rolagem do Storyteller sem transformação homologada para essa função.

Por isso, fogo, radiação, explosões e qualquer outro perigo com pool variável permanecem **abertos quanto à operação do lado do ST** até verificação específica.

## Decisão autoral de 2026-09-28

Foi aprovada a criação de uma **tabela própria de pool ambiental → dano/Impacto fixo**, seguindo o mesmo princípio já usado para converter pools de dano em efeitos fixos, mas calibrada para perigos ambientais.

Isso também resolve, por dependência, pools equivalentes como a autodestruição do HIT Mark X no PT-7.

Em 2026-09-28, o autor confirmou a opção compatível com o contrato: **não criar uma resistência universal nova para perigos ambientais**. O PJ só faz as resistências, reações e absorções que M20 já lhe concede.

Também foi autorizado explicitamente reutilizar, para pools ambientais de dano, a curva de conversão de pool de dano → efeito fixo já estudada no projeto. Esta é uma autorização autoral específica para esta função, não propagação por analogia.

Pipeline:

```text
perigo
→ preservar resistência/reação do PJ já existente em M20
→ aplicar essa resistência ao pool quando a regra original assim fizer
→ converter o pool de dano restante em Impacto fixo
→ aplicar soak/proteção do PJ quando M20 permitir
→ consequência
```

### Tabela ambiental homologável

| Pool ambiental restante | Impacto fixo |
| :---: | :---: |
| 0d | 0 |
| 1–3d | 1 |
| 4–5d | 2 |
| 6–8d | 3 |
| 9–10d | 4 |
| 11–13d | 5 |
| 14–15d | 6 |
| 16–18d | 7 |
| 19–20d | 8 |

O tipo de dano permanece o da fonte: C, L ou A.

---

## 1. Princípio do pacote

Os riscos ambientais do corpus já são, em grande parte, naturalmente player-facing. O ambiente não precisa receber agência, iniciativa, Perfil DRP ou uma ficha de NPC.

A regra de tradução é:

```text
condição/exposição
→ dano, dificuldade ou limite temporal da própria regra
→ PJ faz apenas as resistências/absorções que M20 já lhe concede
→ consequência
```

A camada player-facing não cria esquiva, soak, relógio ou teste adicional.

Relógios podem ser usados somente como interface de uma grandeza que já existe — tempo sem ar, exposição acumulada, duração até propagação — sem substituir a regra.

---

# 2. Quedas e impacto

A fonte consolidada determina:

- 1 nível de dano Contundente para cada 3 metros de queda;
- máximo de 10 níveis;
- superfície rígida/afiada pode converter o dano para Letal;
- acima de 30 metros, o dano torna-se Letal;
- magos podem absorver o dano com Vigor D6.

Representação operacional:

```text
QUEDA
Dano: 1C / 3 m, máximo 10
Superfície rígida/afiada: L
Acima de 30 m: L
Absorção: Vigor D6 do PJ
```

**Conversão adicional: nenhuma.**

---

# 3. Fogo e calor

A fonte consolidada usa dano Agravado por exposição:

```text
Pequena chama: 1A / turno
Chama média: 1A / turno
Grande chama: 1A / turno
```

Em fontes médias ou grandes, o PJ pode fazer o teste de Vigor ou Matéria previsto para evitar ignição de roupas/objetos. Um personagem em chamas continua sofrendo o dano médio indicado pela regra até apagar o fogo.

A conversão fixa elimina a rolagem de dano do ST. As três intensidades acima convergem para 1A pela quantização da curva 1–3d → 1; continuam distintas na ficção, no alcance, na possibilidade de ignição e em outras consequências que a fonte atribuir. Nenhuma nova rolagem universal de resistência é criada.

---

# 4. Fome, sede e sufocamento

## Fome

```text
Limite: 3 dias × Vigor
Depois: 1C automático / dia
Absorção: não
```

## Sede

```text
Limite: 1 dia × Vigor
Depois: 1L automático / dia
Absorção: não
```

## Sufocamento

```text
Limite: 30 s × Vigor
Esforço/pânico: metade do tempo
Depois: 1L automático / turno
Absorção: não
```

Essas regras já têm sua própria Persistência temporal. Não se cria outro relógio mecânico; uma trilha visual pode apenas exibir o tempo que já está sendo contado.

---

# 5. Radiação

A fonte consolidada estabelece:

- dano Agravado;
- 1–3 dados conforme gravidade;
- intervalo por dia em exposição crônica ou por turno em exposição massiva;
- possível debilitação permanente de Atributos Físicos;
- restauração mística específica por Vida 4 ou Matéria 4.

Representação:

```text
RADIAÇÃO
Dano: 1A
Intervalo: dia ou turno, conforme exposição
Efeito adicional: possível debilitação física permanente
```

Se a regra específica não oferece resistência mundana, nenhuma é criada.

---

# 6. Venenos e toxinas

A resistência já pertence ao jogador:

```text
TOXINA
PJ: Vigor
Dificuldade: 6–9 conforme letalidade
Cada sucesso do PJ reduz 1 dado do pool original
Pool restante → Impacto fixo pela tabela ambiental
Tipo: C ou L conforme substância
```

Toxinas letais preservam suas consequências próprias em caso de fracasso total.

Nenhuma Ameaça, iniciativa ou pool de ataque é criado para a substância.

---

# 7. Doenças

O corpus consolidado associa doenças à escala de Toxin Rating:

```text
Rating
→ dificuldade de resistência
→ tipo/gravidade do dano
→ PJ faz a resistência prevista
```

Doença é estado/perigo persistente, não agente.

### Limite documental

A tabela completa de Ratings, os intervalos entre testes e a progressão/cura de doenças específicas ainda precisam ser conferidos contra a fonte licenciada antes da publicação.

Isso é uma pendência de **fonte**, não de arquitetura player-facing.

---

# 8. Explosões

Explosão é dano ambiental de área, não ataque de NPC.

A estrutura recuperada é:

```text
pool de dano da explosão
→ PJ usa a reação prevista para minimizar o blast, quando permitida
→ cada sucesso dessa reação reduz 1 dado do pool
→ pool restante vira Impacto fixo pela tabela ambiental
→ cobertura/Durability e demais proteções são aplicadas quando a regra permitir
→ consequências secundárias usam suas próprias regras
```

Incêndio, queda, colapso, estilhaços e fumaça permanecem consequências separadas quando relevantes.

### Limite documental

A tabela completa de escala, dano e dificuldades de blast deve ser conferida contra a fonte licenciada antes do texto comercial.

Novamente, a pendência é documental; a arquitetura já é player-facing.

---

# 9. Clima hostil e perigos adicionais

A consolidação geral de Sistemas Dramáticos prevê testes contínuos de Vigor em temperaturas extremas e dano progressivo em ambientes mortais.

A forma operacional continua:

```text
condição ambiental
→ dificuldade/intervalo da regra
→ PJ rola Vigor quando previsto
→ consequência
```

Perigos compostos são decompostos. Exemplo: uma explosão pode gerar fogo e colapso; cada consequência consulta seu procedimento próprio em vez de ser fundida numa "ficha universal de perigo".

---

# 10. Matriz de consulta rápida

| Perigo | Forma player-facing |
| :--- | :--- |
| Queda | dano por altura + absorção do PJ |
| Fogo | exposição + Impacto A fixo + teste específico quando previsto |
| Fome | limite temporal + dano automático |
| Sede | limite temporal + dano automático |
| Sufocamento | limite temporal + dano automático |
| Radiação | Impacto A fixo + intervalo + efeitos colaterais |
| Toxina | Vigor do PJ reduz pool; restante vira Impacto fixo |
| Doença | Rating + resistência do PJ + progressão própria |
| Explosão | reação do PJ quando permitida → pool restante → Impacto fixo + cobertura |
| Clima hostil | condição + Vigor do PJ quando previsto |

---

# 11. Auditoria do escopo da EAP

- [x] quedas e impacto;
- [x] fogo e calor;
- [x] fome;
- [x] sede;
- [x] sufocamento/asfixia;
- [x] radiação;
- [x] venenos e toxinas;
- [x] doenças;
- [x] explosões;
- [x] climas hostis;
- [x] perigos compostos preservados como composição de procedimentos;
- [x] nenhum perigo recebeu agência ou iniciativa artificial;
- [x] nenhum teste novo foi transferido ao PJ;
- [x] relógios limitados a interface de grandezas temporais já existentes.

## Pendências de fonte antes da publicação

- [ ] conferir tabela completa de explosões;
- [ ] conferir tabela completa de Toxin Rating/doenças;
- [ ] conferir intervalos/progressão de doenças específicas.

Essas pendências não exigem estudo matemático novo.

## Gate

O ST pode operar os riscos ambientais consolidados sem rolar por um agente ambiental fictício e sem alterar as ações normais do jogador.

**PT-4: MECANICAMENTE COMPLETO APÓS REVISÃO CORRETIVA; AGUARDA HOMOLOGAÇÃO EXPLÍCITA DO PACOTE.**
