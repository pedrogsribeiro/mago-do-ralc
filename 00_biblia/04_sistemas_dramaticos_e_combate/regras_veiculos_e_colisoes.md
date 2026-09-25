---
type: regra
summary: "Regras consolidadas de veículos em M20: velocidade segura/máxima, manobrabilidade, Durability, Structure, direção, colisões e proteção de ocupantes."
tags: [srd, regras, veiculos, perseguicao, colisao, durability, structure, direcao]
---

# Sistemas de Veículos

> **Nota de proveniência:** consolidação por paráfrase de *Mage: The Ascension 20th Anniversary Edition*, especialmente pp. 458–462. Antes do texto comercial final, conferir números/tabelas contra a fonte licenciada/possuída.

## 1. Traits de veículo

M20 usa cinco propriedades operacionais principais.

### Safe Speed

Velocidade até a qual o veículo pode ser operado sem penalidade específica por excesso de velocidade.

Para cada incremento relevante acima dessa faixa, a dificuldade dos testes de operação aumenta.

### Max Speed

Limite prático de velocidade do veículo.

### Maneuverability

Limita a quantidade de dados que o condutor pode efetivamente usar em testes de operação/manobra.

Mesmo um condutor excepcional não consegue extrair de um veículo pesado a mesma resposta de um veículo ágil.

### Durability

Representa a resistência externa/material do veículo.

Funciona como proteção fixa contra dano e, em colisões, também participa da quantidade de impacto que o veículo pode causar/proteger.

### Structure

Representa a integridade funcional do veículo.

Quando o dano supera sua Structure, o veículo deixa de funcionar adequadamente e pode se tornar apenas destroço.

---

## 2. Direção e manobras

Manobras perigosas usam:

```
Destreza + Direção
```

ou Pilot/Ability equivalente.

A dificuldade depende de:

* complexidade da manobra;
* terreno;
* condições;
* dano no veículo;
* velocidade.

A **Maneuverability** limita o pool utilizável.

Exceder Safe Speed aumenta dificuldade.

### Tradução player-facing

Já é um procedimento do jogador.

**Preservar sem conversão.**

---

## 3. Perseguições

Perseguições continuam usando a família de testes estendidos-resistidos.

O Relógio de posição do Estudo 17 é uma interface válida quando representa os sucessos líquidos acumulados.

A ficha do veículo modifica a resolução por:

* Safe Speed;
* Max Speed;
* Maneuverability;
* condições/dano.

---

## 4. Durability e Structure

O veículo é um objeto com:

```
Durability = resistência
Structure = integridade
```

Essa estrutura já é quase ideal para a filosofia de Obstáculos.

Não se cria:

* HP novo;
* soak rolado pelo ST;
* Limiar genérico separado.

Durability já cumpre a função de resistência fixa.

---

## 5. Colisão contra personagem/objeto

M20 usa uma aproximação simples para evitar simulação física excessiva.

O impacto de um veículo parte de:

* **Durability do veículo**;
* acréscimo por **velocidade**;
* acréscimos por **massa/tamanho**, quando previstos pela categoria do veículo.

O dano básico é de impacto/Contundente, salvo circunstância/regra que modifique sua natureza.

### Consequência de design

Colisão já tem uma fórmula própria.

Ela **não deve ser convertida em Consequência fixa por tier**.

---

## 6. Dano aos ocupantes

Em colisão, ocupantes sofrem o dano do impacto com proteção fornecida pelo próprio veículo.

A regra-base:

* reduz o dano pela **Durability** do veículo;
* ocupantes presos por cinto recebem proteção adicional significativa;
* alguns tipos de veículo protegem melhor ou pior seus passageiros.

### Consequência de design

Dano aos ocupantes é derivado da colisão e da proteção do veículo.

Não é o mesmo que dano à Structure.

---

## 7. Dano ao veículo

Ataques contra veículo usam:

```
dano
→ Durability absorve
→ excedente reduz Structure
```

Quando Structure é excedida, o veículo deixa de cumprir sua função.

Dano muito além da Structure pode tornar o objeto irrecuperável.

### Tradução player-facing

Isso já é determinístico do lado do objeto.

**Preservar.**

---

## 8. Colisão entre veículos

Para cada veículo, separar:

1. dano do impacto;
2. Durability;
3. dano que atravessa para Structure;
4. dano transmitido aos ocupantes.

A mesma colisão pode portanto produzir quatro resultados diferentes:

* veículo A danificado;
* veículo B danificado;
* ocupantes A feridos;
* ocupantes B feridos.

Não fundir tudo em um único Relógio.

---

## 9. Massa

As tabelas de M20 atribuem modificadores de impacto a categorias maiores.

Em termos operacionais:

* carros podem adicionar dano por massa;
* caminhões adicionam mais;
* veículos militares adicionam ainda mais;
* algumas categorias também protegem melhor passageiros.

A tabela exata deve ser consultada na fonte final.

---

## 10. Stunt driving

Manobras cinematográficas usam a regra normal de Direção/Pilot:

* pool limitado por Maneuverability;
* dificuldade pela manobra;
* penalidade por excesso de Safe Speed;
* condições externas aplicadas normalmente.

Isso já é player-facing.

---

## 11. Matriz para ficha/interface

```
VEÍCULO

Safe Speed:
Max Speed:
Maneuverability:
Crew:
Durability:
Structure:
Weapons:

Estados:
- normal
- danificado
- incapacitado/destruído
```

O Relógio de perseguição, quando usado, fica separado:

```
POSIÇÃO DA PERSEGUIÇÃO
0 / N
```

---

## 12. Gate

A antiga lacuna de colisões está **resolvida em arquitetura e regra-base**.

Para publicação comercial ainda é necessário:

1. conferir as tabelas completas de veículos em M20 pp. 460–462;
2. conferir incrementos exatos de velocidade/massa;
3. parafrasear, não reproduzir tabelas protegidas sem base de licença;
4. decidir quais veículos exemplares realmente precisam aparecer no produto.
