---
type: regra
summary: "Estudo 18: Certámen e duelos estruturados no modelo player-facing, preservando Gladius, Aegis, Locus e economia de ações."
tags: [estudo, player-faced, certamen, duelos, gladius, aegis, locus, arete, quintessencia, regras]
---

# Estudo 18: Certámen e Duelos Estruturados

Este estudo aplica a arquitetura player-facing ao **Certámen**, um dos subsistemas mais bem delimitados da bíblia atual.

A regra-base é clara:

* **Locus:** reserva de Quintessência dedicada ao duelo;
* **Gladius:** ataque com Arete contra Dificuldade 6;
* **Aegis:** defesa ativa que consome a ação e cujos sucessos anulam sucessos do Gladius;
* **fim do duelo:** Locus reduzido a zero.

Isso torna o Certámen um excelente teste de fidelidade porque ele já possui:

* recurso persistente;
* ataque;
* defesa ativa;
* economia de ações;
* cancelamento de sucessos;
* condição clara de vitória.

---

## 1. Gate de fidelidade

A experiência do jogador precisa preservar:

* Arete;
* Dificuldade 6;
* escolha de Esfera;
* gasto/uso do Locus;
* decisão de usar ou não Aegis;
* custo de ação do Aegis;
* cancelamento de sucessos;
* término em zero de Quintessência.

A camada player-facing não deve:

* transformar Aegis em defesa automática;
* dar Aegis grátis quando o jogador não gastou ação;
* reduzir Gladius a dano fixo;
* trocar Locus por HP genérico;
* apagar escolha de Esfera.

---

## 2. Locus já é Integridade canônica

O Locus já funciona como uma reserva persistente:

```
Quintessência inicial
→ sucessos de Gladius reduzem a reserva
→ zero encerra o duelo
```

Logo, ele já é praticamente um **Relógio/Integridade canônico**.

A interface player-facing não precisa comprimi-lo.

### Gate

**PRESERVAR O LOCUS.**

---

## 3. Gladius do PJ

Quando o PJ ataca:

* escolhe a Esfera;
* rola Arete D6;
* cada sucesso líquido reduz 1 ponto do Locus adversário.

Isso já é player-facing.

### Gate

**PRESERVAR SEM CONVERSÃO.**

---

## 4. Aegis do NPC

Quando o NPC escolhe gastar sua ação em Aegis:

* ele possui uma defesa ativa real;
* essa defesa cancela sucessos do Gladius;
* a situação é estruturalmente uma oposição resistida.

Portanto, a defesa do NPC pode ser candidata à compressão por **Oposição**:

```
PJ rola Gladius
→ Aegis do NPC é convertido em Oposição
→ sucessos líquidos restantes reduzem o Locus
```

A economia de ações do NPC precisa ser preservada: se ele usou Aegis, não pode usar outra ação incompatível no mesmo espaço de ação.

### Gate

**PASSA COMO CANDIDATA À CONVERSÃO DE OPOSIÇÃO.**

---

## 5. Gladius do NPC contra PJ com Aegis

Quando o NPC ataca e o PJ escolhe Aegis:

* o PJ já possui uma rolagem defensiva própria;
* a escolha custa sua ação;
* os sucessos de Aegis cancelam Gladius.

Esse é exatamente o tipo de situação em que a arquitetura player-facing funciona melhor.

A competência ofensiva do NPC pode alimentar **Ameaça/Oposição convertida**, enquanto a rolagem defensiva do jogador permanece intacta.

### Gate

**PROMISSOR E COERENTE COM O MOTOR GERAL.**

---

## 6. Gladius do NPC contra PJ sem Aegis

Se o PJ não gasta ação com Aegis:

* não existe defesa ativa;
* não se concede defesa gratuita;
* o NPC rolaria Gladius no procedimento original.

Aplica-se a regra de precedência:

> **preservar a rolagem do ST quando removê-la exigiria alterar a economia de ações ou transferir custo ao jogador.**

### Gate

**EXCEÇÃO DE FIDELIDADE.**

---

## 7. 1 sucesso e Locus

No Certámen:

> **1 sucesso líquido do Gladius reduz 1 ponto do Locus.**

Isso confirma a regra geral do motor:

* 1 sucesso continua sendo sucesso;
* move a ficção;
* afeta a estrutura persistente em 1 ponto.

Não há justificativa para transformar 1 sucesso em “só pressão narrativa”.

---

## 8. Aegis como Limiar?

Não.

Aegis é **defesa ativa por sucessos**, não resistência passiva.

Logo:

* Aegis → Oposição / cancelamento;
* Limiar de Efetividade → apenas quando existir resistência passiva equivalente.

Confundir os dois apagaria a decisão de gastar ação com Aegis.

---

## 9. Telegrafia

Certámen não exige telegrafia universal.

Ela pode aparecer quando um duelista:

* prepara uma manobra de alto impacto;
* concentra Quintessência;
* estabelece estado;
* executa técnica especial.

Mas Gladius comum não precisa ser artificialmente telegráfico.

---

## 10. Matriz operacional

| Elemento | Tratamento |
| :--- | :--- |
| Locus | preservar |
| Gladius do PJ | preservar Arete D6 |
| Aegis do PJ | preservar |
| Aegis do NPC | candidata a Oposição |
| Gladius do NPC com Aegis do PJ | usar rolagem do jogador como âncora |
| Gladius do NPC sem Aegis | preservar rolagem do ST quando necessário |
| 1 sucesso | -1 Locus |
| zero Locus | derrota/exaustão |
| Quintessência | preservar |

---

## 11. Gate do Estudo 18

O Certámen passa com alto grau de compatibilidade.

### Resolvido

* Locus como Integridade canônica;
* 1 sucesso = 1 redução;
* Gladius do PJ preservado;
* Aegis do PJ preservado;
* Aegis do NPC como candidata a Oposição;
* economia de ações preservada;
* ausência de Aegis não gera defesa gratuita.

### Exceção

* Gladius do NPC sem defesa ativa do PJ pode permanecer rolagem do ST.

---

## 12. Propagação

Este estudo retroage sobre:

* Estudo 10 — Certámen;
* Estudo 14 — mágika e contramágika;
* Estudo 06 — distinção entre defesa ativa e Limiar.

O próximo subsistema é **Maravilhas, Fetiches, Talismãs e Dispositivos**, porque parte dele já foi tocada no Estudo 14, mas ainda falta separar ativação, recursos, autonomia e resistência.


---

## 13. Propagação da regra geral de contramágika

A recuperação da regra geral confirma a distinção usada neste estudo:

* contramágika básica e Aegis pertencem à família de **defesas ativas por cancelamento de sucessos**;
* Limiar de Efetividade continua reservado a resistência passiva;
* contramágika inata precisa de tratamento próprio e não deve ser fundida automaticamente com Aegis ou Limiar.

A regra geral de contramágika deve ser conferida contra a fonte licenciada antes da redação comercial final.
