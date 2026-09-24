---
type: regra
summary: "Estudo 09: protocolo de conversão de fichas de NPCs para uma interface player-facing do Storyteller, com exemplos reais e gate de completude."
tags: [estudo, game-design, player-faced, conversao, npcs, fichas, competencias, validacao]
---

# Estudo 09: Protocolo de Conversão de Fichas de NPCs

Este estudo testa uma promessa concreta:

> **o Storyteller deve conseguir pegar uma ficha oficial de NPC de M20 e extrair dela uma interface operacional menor, preservando para os jogadores a experiência reconhecível do sistema.**

A ficha original continua sendo a **fonte normativa**. A conversão não recria o NPC do zero e não o reduz a um “nível de ameaça” genérico.

O teste deste capítulo é simples: depois da conversão, o ST deve saber rapidamente:

1. o que o NPC consegue fazer;
2. onde ele é forte ou vulnerável;
3. qual característica/parada original sustenta cada ação;
4. o que já pode ser resolvido player-facing;
5. quais operações ainda dependem de uma solução não validada.

---

# 1. O que significa converter

Converter não significa substituir toda a ficha.

A interface player-facing deve funcionar como uma **camada de consulta rápida** construída a partir dela.

A informação pode ser dividida em quatro grupos:

### A. Identidade operacional
O que define o NPC na ficção e muda possibilidades.

Exemplos:
* autoridade institucional;
* blindagem de Primium;
* treinamento de infiltração;
* Aura de Medo;
* incorporeidade;
* contramágika inata;
* autodestruição.

### B. Competências relevantes
As paradas originais que provavelmente entrarão em oposição com os PJs.

### C. Recursos e estados
Vitalidade, Força de Vontade, Arete, Quintessência, armadura, penalidades, munição e outros recursos que realmente importam.

### D. Procedimentos especiais
Mágika, hacking, regeneração, contramágika, venenos, autodestruição, possessão e outros subsistemas particulares.

A compressão só é boa se retirar consulta **sem apagar nenhuma dessas funções importantes**.

---

# 2. As quatro dimensões como índice da ficha

Físico, Social, Mental/Técnico e Mágicko são uma **lente de preparação do ST**.

Elas respondem:

> “em quais tipos de confronto este NPC tende a ser forte ou vulnerável para este grupo?”

Não são quatro atributos novos.

Exemplo:

```
AGENTE DO GOVERNO

Físico: competente
Social: forte
Mental/Técnico: forte
Mágicko: praticamente inexistente
```

Quando o jogador escolhe uma abordagem, o ST volta à competência original que sustenta aquela situação.

Se o personagem mente para o agente, importa a capacidade perceptiva/social pertinente.
Se tenta fugir dele, importam as capacidades físicas e de perseguição.
Se tenta hackear seu equipamento, importam as capacidades técnicas e o sistema atacado.

---

# 3. Os três níveis de carga

O nível não pertence permanentemente ao NPC.

### Nível 1 — Oposição pontual
Só uma competência importa naquele momento.

### Nível 2 — Ameaça ativa
O NPC permanece em cena, possui turnos e executa ações repetidamente.

### Nível 3 — Alto impacto
Alguma ação ou estado produz consequência excepcional e exige causalidade legível por telegrafia.

O mesmo HIT Mark pode ser Nível 1 enquanto os PJs tentam passar por seus sensores, Nível 2 quando entra em combate e Nível 3 quando inicia sua autodestruição.

---

# 4. Procedimento de extração

## Passo 1 — Leia a ficha original antes de converter

Identifique:

* Atributos;
* Habilidades;
* Iniciativa;
* Vitalidade;
* Vigor/armadura/absorção;
* ataques e dano;
* Força de Vontade;
* Arete e Esferas, quando houver;
* poderes e regras especiais.

Nenhum número é convertido ainda.

## Passo 2 — Marque o que muda possibilidades

Esses elementos ficam escritos literalmente na interface.

Exemplos:

```
[Armadura pesada de Primium]
[Contramágika inata 5d]
[Autodestruição ao ser capturado]
[Não possui treinamento social]
```

## Passo 3 — Organize as competências por dimensão

Não use “a maior parada da ficha”.

Mapeie as paradas relevantes em **Físico, Social, Mental/Técnico e Mágicko**, porque o mesmo NPC pode ser extremamente resistente em uma frente e quase inexistente em outra.

Registre apenas as paradas que realmente sustentam os valores daquela dimensão.

**Baixo ≠ zero.** Uma dimensão baixa ainda existe e oferece alguma oposição. Uma dimensão 0 indica ausência daquela capacidade/resistência para o Obstáculo.

## Passo 4 — Identifique quais rolagens pertenciam ao ST

Marque cada operação:

* oposição resistida;
* ataque;
* dano;
* absorção;
* mágika;
* poder especial.

Só essas operações são candidatas à transformação player-facing.

## Passo 5 — Aplique apenas transformações já sustentadas pela pesquisa

### Oposição resistida comum
O baseline experimental atual é **Dificuldade + Limiar oculto**:

| Parada relevante do NPC | Diff experimental | Limiar oculto |
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

Essa tabela **ainda é provisória** porque o Estudo 05 encontrou viés residual entre PJs fracos e fortes.

### Ameaça, Consequência e Limiar de Efetividade

A ficha achatada já possui os campos necessários para o combate do NPC:

* **Ameaça:** capacidade do NPC de impor sua ação ao PJ.
* **Consequência:** dano, estresse ou outro impacto aplicado quando a Ameaça se concretiza.
* **Limiar de Efetividade:** resistência do Obstáculo ao Impacto; é o nome generalizado da antiga RD fixa para funcionar também fora do dano físico.

O desenho desses campos já existe. O trabalho pendente é **calibrar seus valores** contra as paradas originais de ataque, dano e soak.

> O **Limiar de Efetividade** não deve ser confundido com o **limiar oculto** usado na investigação matemática da conversão de rolagens resistidas.

---

# 5. Ficha de interface provisória

A interface mínima pode assumir esta forma:

```
NOME

LENTES DO ST
Físico:
Social:
Mental/Técnico:
Mágicko:

CARACTERÍSTICAS QUE MUDAM A FICÇÃO
- [...]
- [...]

COMPETÊNCIAS PROVÁVEIS
- ação/oposição: parada original → conversão, se aplicável
- ação/oposição: parada original → conversão, se aplicável

RECURSOS PRESERVADOS
- Vitalidade:
- Força de Vontade:
- Arete / Esferas:
- outros:

FICHA ACHATADA POR DIMENSÃO

| Dimensão | Oposição | Ameaça | Consequência | Integridade / Relógio | Limiar de Efetividade |
| :--- | :---: | :---: | :--- | :---: | :---: |
| Físico |  |  |  |  |  |
| Social |  |  |  |  |  |
| Mental/Técnico |  |  |  |  |  |
| Mágicko |  |  |  |  |  |

Use **0** somente quando aquela capacidade/resistência realmente não existe naquela dimensão. Não use 0 como sinônimo de “fraco”.

AÇÕES E PODERES
- [...]

TELEGRAFIA POSSÍVEL
- [...]

LACUNAS / CALIBRAÇÕES PENDENTES
- [...]
```

O objetivo é o ST consultar muito menos informação durante a cena **sem perder a ficha que explica de onde aquilo veio**.

---

# 6. Teste 1 — Bandido Comum

A ficha original possui, entre outras coisas:

* Força 3;
* Destreza 2;
* Vigor 2;
* Briga 2;
* Armas Brancas 2;
* Esportes 2;
* Furtividade 2;
* Prontidão 2;
* Força de Vontade 3;
* sete níveis normais de Vitalidade;
* nenhum ponto de armadura;
* ataques mundanos simples.

### Interface extraída

```
BANDIDO COMUM

LENTES
Físico: médio
Social: baixo/médio
Mental/Técnico: baixo
Mágicko: nenhum

CARACTERÍSTICAS
[Brigão de rua]
[Sem proteção sobrenatural]

COMPETÊNCIAS PROVÁVEIS
Furtividade: Destreza 2 + Furtividade 2 = 4d
Percepção/alerta: Percepção 2 + Prontidão 2 = 4d
Briga: Destreza 2 + Briga 2 = 4d

RECURSOS
Vigor 2
Força de Vontade 3
Vitalidade normal de mortal
sem armadura
```

Para uma oposição de Furtividade 4d contra a percepção do PJ, o baseline experimental permite testar **Diff 7 + Limiar 1** do lado do jogador.

### Gate

**PASSA para oposição pontual.**

A estrutura de combate **já existe na ficha achatada** por Ameaça, Consequência e Limiar de Efetividade. O que ainda não está fechado é a calibração numérica desses campos contra ataque, dano e soak de M20.

---

# 7. Teste 2 — Agente do Governo

A ficha original apresenta:

* atributos mentais e sociais relativamente altos;
* Percepção 3–4;
* Investigação 3–5;
* Prontidão 3;
* Armas de Fogo 3–4;
* Força de Vontade 7;
* Vigor 3–4;
* colete oculto;
* armas de fogo.

A interface consegue mostrar imediatamente que o agente é muito mais perigoso em **investigação, vigilância e autoridade** do que um bandido comum.

Exemplo:

```
AGENTE DO GOVERNO

LENTES
Físico: competente
Social: forte
Mental/Técnico: forte
Mágicko: nenhum

CARACTERÍSTICAS
[Autoridade federal]
[Treinamento investigativo]
[Colete oculto]

COMPETÊNCIAS EXEMPLARES
Investigação: pode chegar a 8–9d conforme o perfil
Percepção/Prontidão: 6–7d
Armas de Fogo: 5–7d

RECURSOS
Força de Vontade 7
Vigor 3–4
armadura leve
Vitalidade humana
```

### Gate

**PASSA como ferramenta de leitura das assimetrias do NPC.**

A conversão probabilística de uma oposição específica é possível provisoriamente porque parte da parada efetiva correspondente.

O combate completo continua sujeito às lacunas já identificadas.

---

# 8. Teste 3 — HIT Mark V

O HIT Mark demonstra se o método preserva um NPC realmente complexo.

A ficha original inclui:

* Força 5;
* Destreza 2;
* Vigor 5;
* Briga 3;
* Prontidão 3;
* grande reserva de absorção por Primium;
* vários níveis de Vitalidade;
* contramágika inata 5d;
* metralhadora integrada;
* garras;
* sensores especiais;
* regras tecnocráticas específicas.

### Interface extraída

```
HIT MARK V

LENTES
Físico: excepcionalmente resistente; ofensiva forte, agilidade limitada
Social: quase inexistente
Mental/Técnico: funcional e programado
Mágicko: forte defesa por Primium

CARACTERÍSTICAS
[Chassi de Primium]
[Contramágika inata 5d]
[Sensores infravermelhos/ultravioletas]
[Metralhadora integrada]
[Garras cibernéticas]

COMPETÊNCIAS / FONTES
Briga: Destreza 2 + Briga 3 = 5d
Percepção/alerta: Percepção 3 + Prontidão 3 = 6d
soak total: 9d
contramágika: 5d
dano da metralhadora: 8d
dano das garras: 8d

RECURSOS
Vitalidade especial do modelo
Primium / armadura
```

### O que o teste revela

A interface é **muito menor que a ficha completa**, mas ainda preserva exatamente por que o HIT Mark é perigoso.

Ao mesmo tempo, ela mostra os limites atuais da pesquisa:

* 5d e 6d de oposição comum podem ser submetidos ao baseline experimental;
* 9d de soak devem alimentar o **Limiar de Efetividade** correspondente; a tabela precisa ser calibrada;
* 8d de dano devem alimentar a **Consequência** correspondente; a conversão numérica precisa ser calibrada;
* contramágika 5d precisa preservar o subsistema mágicko;
* sensores especiais continuam sendo características concretas, não um número abstrato.

### Gate

**PASSA como método de compressão informacional.**

**NÃO PASSA ainda como substituição completa das operações do ST.**

Isso é exatamente o tipo de NPC que deverá ser usado para validar dano, soak e contramágika antes do fechamento do método.

---

# 9. Magos antagonistas

Magos exigem cuidado adicional.

Um mago antagonista deve preservar:

* Arete;
* Esferas;
* paradigma/foco quando relevante;
* Quintessência;
* Força de Vontade;
* efeitos sustentados;
* Paradoxo e regras especiais;
* capacidades mundanas pertinentes.

As lentes ajudam a localizar força e fraqueza, mas **não substituem a ficha mágicka**.

A conversão de um mago só estará completa quando os estudos específicos de mágika player-facing demonstrarem quais operações do ST podem ser retiradas sem alterar a experiência dos jogadores.

---

# 10. Espíritos não entram neste mesmo molde

O Estudo 07 demonstrou que M20 já oferece uma ficha espiritual compacta:

* Força de Vontade;
* Fúria;
* Gnose;
* Essência;
* Encantos.

Portanto, “converter um espírito como NPC comum” adicionaria abstração desnecessária.

Eles usam o mesmo princípio geral — preservar a fonte, remover somente operações onerosas —, mas seu protocolo específico pertence aos Estudos 07/13.

---

# 11. Gate do Estudo 09

A proposta deste capítulo é válida **se entendida como método de extração e compressão da ficha**, e ainda não como conversão mecânica total.

### Entrega adequadamente
* identificação de competências relevantes;
* leitura de forças e vulnerabilidades;
* redução da quantidade de informação consultada;
* preservação de capacidades especiais;
* seleção da parada original que sustenta cada oposição;
* aplicação provisória da conversão de oposição resistida;
* classificação da carga da cena;
* identificação de movimentos telegrafados.

### Ainda impede chamar o método de conversão completa
* calibração de **Ameaça** contra a ofensiva original;
* calibração de **Consequência** contra o dano original;
* calibração de **Limiar de Efetividade** contra soak/armadura e resistências equivalentes;
* alguns efeitos de contramágika;
* vários subsistemas sobrenaturais.

---

## 12. Critério para o futuro capítulo final

O futuro guia comercial poderá realmente dizer:

> “Pegue qualquer NPC de M20 e converta para player-facing”

somente quando cada operação removida possuir uma resposta validada.

Até lá, este estudo cumpre outra função igualmente importante:

> **mostrar exatamente como comprimir a ficha sem perder sua identidade e localizar, com precisão, quais operações ainda precisam ser resolvidas pelo restante da pesquisa.**
