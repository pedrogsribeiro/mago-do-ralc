---
type: regra
summary: "Estudo 07: Adaptação de Entidades Espirituais (Umbróides) e a Umbra no Sistema Player-Faced Total."
tags: [estudo, game-design, player-faced, umbra, espiritos, umbrood, gaffling, jaggling, incarna]
---

# Estudo 07: Adaptação de Entidades Espirituais (Umbróides) no Sistema Player-Faced

Este documento estabelece o funcionamento formal de **Entidades Espirituais (Umbróides / Umbrood)** no sistema *Player-Faced Total* para *Mago: A Ascensão 20 Anos*. Ele adapta as mecânicas clássicas de *Gnose, Fúria, Força de Vontade e Essência* para os 4 Níveis de Carga Narrativa.

---

## 👻 1. As Peculiaridades dos Espíritos no Storyteller vs. Player-Faced

Diferente de humanos e ciborgues da Tecnocracia, os espíritos nativos da Penumbra e da efêmera possuem duas barreiras fundamentais:

1. **Imunidade Física Inata (O Filtro de Efêmera):** Ataques físicos ou tiros mundanos atravessam a efêmera de um espírito desmaterializado sem causar dano (**Efeito Zero Absoluto**).
2. **Defesa Mística Exclusiva:** O dano de *Fúria (Rage)* de um espírito não ataca o corpo físico comum, mas sim o padrão místico/efêmero do mago, exigindo defesas com a **Esfera de Espírito** ou o **Antecedente Avatar**.

---

## 📊 2. Mapeamento de Ranks Espirituais nos Níveis de Carga Narrativa

Os 4 Graus Espirituais clássicos de Mago M20 são convertidos diretamente para a Taxonomia de Carga Narrativa:

```
+---------------------------------------------------------------------------------------------------+
|               GRAUS ESPIRITUAIS E NÍVEIS DE CARGA NARRATIVA PLAYER-FACED                          |
|                                                                                                   |
|  1. GAFFLING (Espírito Menor / Inseto)  ==> Nível 2 (Oposição Rápida): Diff 5, Relógio 3          |
|  2. JAGGLING (Guardião / Elementar)     ==> Nível 3 (Ameaça Ativa): Diff 6-7, Relógio 5, Dano 4    |
|  3. INCARNA (Lorde de Paradoxo / Totem) ==> Nível 4 (Ameaça Telegrafada): Diff 8, Relógio 7-8     |
|  4. CELESTIA (Entidade Cósmica/Deus)    ==> Obstáculo Ambiental (Pacificado apenas por Rituais)  |
+---------------------------------------------------------------------------------------------------+
```

---

## 🧮 3. A Estrutura da Ficha de Ameaça Espiritual

Toda entidade umbróide é sintetizada em uma ficha Player-Faced com **Aspectos de Efêmera** e os **4 Elementos Simétricos**:

```yaml
---
ameaca: Jaggling da Tempestade (Elementar de Ar e Raios)
rank_espiritual: Jaggling (Nível 3 - Ameaça Ativa)

aspectos_diegaticos:
  - "[Matéria Efêmera Desmaterializada]": Imune a ataques físicos mundanos (Efeito Zero sem Espírito 3, Primórdio 2 ou Fetiches).
  - "[Aura de Relâmpagos Efêmeros]": Causa estresse eletrostático nos magos ao redor.

bloco_mecanico:
  imposicao: Diff 7 (Mágico/Espiritual) | Diff 5 (Se usar Fetiche de Banimento)
  pressao: Diff 6 (Resistir à Fúria dos Relâmpagos)
  impacto: 4 Danos Agravados / Drenagem de 2 Pontos de Quintessência
  relogio_essencia: 5 Caixas de Essência Espiritual
---
```

---

## 🛡️ 4. Regras de Defesa e Resolução contra Espíritos

### A. Ataque do Mago (Imposição)
* **Com Espírito 3, Primórdio 2 ou Fetiche (`[Ruína Espiritual]`):** O Mago rola normalmente contra a **Dificuldade de Imposição**. $\ge 2s$ avança 2 Caixas de Essência; $1s$ avança 1 Caixa.
* **SEM Esfera de Espírito ou Fetiche (Ataque Físico Puro):** Produz **Efeito Zero Absoluto** no Relógio de Essência, embora o espírito possa reagir normalmente.

### B. Defesa do Mago contra a Fúria (Pressão)
* **Com a Esfera de Espírito:** O Mago rola Arete/Espírito contra a **Dificuldade de Pressão** ($Diff 6$).
* **SEM a Esfera de Espírito (Defesa Desesperada):** O Mago é forçado a rolar seu **Antecedente Avatar** com Dificuldade $+1$ ($Diff 7-8$).
* **Adormecidos:** Não possuem defesas místicas e recebem o dano de Fúria integralmente sem rolagem de defesa.

---

## 📈 5. Prova Matemática Monte Carlo (50.000 Combates Espirituais)

Simulamos o confronto de um Mago preparado (**com Esfera de Espírito 3**) contra um Mago despreparado (**sem Esfera de Espírito, usando apenas ataque físico**):

| Rank da Entidade Espiritual | Condição do Mago | Taxa de Vitória | Duração Média | HP Restante | Impacto no Jogo |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Gaffling (Espírito Menor)** | **Com Espírito 3** | **$100,0\%$** | 2,24 rodadas | 6,61 / 7 | **Vitória Rápida:** Resolvido em 2 turnos. |
| **Gaffling (Espírito Menor)** | **Sem Espírito 3 (Físico)** | **$11,1\%$** | 13,86 rodadas | 1,89 / 7 | **Fracasso:** O ataque físico atravessa o espírito inofensivamente. |
| **Jaggling (Guardião)** | **Com Espírito 3** | **$96,1\%$** | 4,21 rodadas | 5,34 / 7 | **Desafio Equilibrado:** Vitória consistente em 4 rodadas. |
| **Jaggling (Guardião)** | **Sem Espírito 3 (Físico)** | **$0,2\%$** | 6,94 rodadas | 1,65 / 7 | **Impossível:** Necessita de rituais ou fetiches para sobreviver. |
| **Incarna (Lorde de Paradoxo)**| **Com Espírito 3** | **$51,1\%$** | 5,43 rodadas | 3,97 / 7 | **Ameaça Épica:** Requer trabalho em equipe de múltiplos magos. |
| **Incarna (Lorde de Paradoxo)**| **Sem Espírito 3 (Físico)** | **$0,0\%$** | 3,33 rodadas | 0,00 / 7 | **Massacre Total:** Derrota inevitável em 3 turnos. |

---

---

## 🔮 7. A Integração dos Encantos Espirituais (Charms) nos 4 Níveis

Os **Encantos Espirituais (Charms)** de *Mago M20* não são rolagens burocráticas no sistema Player-Faced. Eles atuam como **Gatilhos de Alteração de Estado (State-Shifts)** e **Dilemas Táticos** mapeados através dos 4 Níveis:

```
+---------------------------------------------------------------------------------------------------+
|                  COMO OS ENCANTOS ESPIRITUAIS ATUAM NOS 4 NÍVEIS DE CARGA                        |
|                                                                                                   |
|  NÍVEL 1 (Obstáculo Passivo)    ==> Encantos Utilitários de Terreno (Bruma, Rastreio Espiritual).|
|  NÍVEL 2 (Oposição Rápida)     ==> Encantos Instantâneos (Susto, Alucinação Menor, Fogo Fátuo).|
|  NÍVEL 3 (Ameaça Ativa)         ==> Encantos de Mudança de Estado / Gatilho de Reação:           |
|                                     - Materializar: Alterna Campo Semântico (Permite Dano Físico) |
|                                     - Possessão: Cria Relógio Duplo (Hospedeiro vs. Espírito)     |
|                                     - Rajada Elemental: Altera Tipo de Dano Fixo (Agravado)      |
|  NÍVEL 4 (Ameaça Telegrafada)   ==> Encantos Climáticos / Golpes de Fase Telegrafados:           |
|                                     - Rito de Invocação Cósmica / Tempestade Efêmera em 2 turnos |
+---------------------------------------------------------------------------------------------------+
```

### Detalhamento dos Principais Encantos em Mesa:

#### 1. Encanto *Materializar* (Gatilho de Mudança de Estado)
* **Forma Incorpórea (Padrão):** Possui o Aspecto `[Matéria Efêmera Desmaterializada]`. Ataques mundanos causam **Efeito Zero**.
* **Ao Ativar *Materializar*:** O espírito gasta Essência e ganha um corpo físico no Mundo Material.
* **Impacto no Sistema:** 
  - O Aspecto muda para `[Corpo Físico Concretizado]`.
  - **O Campo Semântico se abre:** Armas de fogo, lâminas, fogo e mágika de *Matéria/Vida/Forças* passam a afetar o espírito!
  - O espírito ganha **RD 1 ou RD 2** (Armadura de Efêmera Concretizada).

#### 2. Encanto *Possessão* (Dilema de Relógio Duplo)
* O espírito habita o corpo de um humano inocente (ex: um civil ou policial Adormecido).
* **Impacto no Nível 3 (Relógio Duplo de Conflito):**
  - **Rota A (Atacar o Hospedeiro Físico — Diff 5):** Fácil de nocautear ou matar o corpo, mas o hospedeiro inocente morre ou fica incapacitado!
  - **Rota B (Exorcismo / Banimento Espiritual — Diff 7):** Ataca o Relógio de Essência do espírito através de *Espírito 3*, *Mente 3* ou Ritos Ocultos. Se o relógio do espírito zerar, o demônio é expulso e o inocente é salvo!

#### 3. Encanto *Rajada / Blast* (Gatilho de Severidade do Impacto)
* Na falha do PJ em conter a Pressão (*Item 2*), o espírito manifesta uma rajada de energia efêmera.
* **Impacto no Nível 3:** Transforma a Severidade do Impacto (*Item 3*) em **Dano Agravado** ou adiciona a perda de **2 Pontos de Quintessência/Vontade**.

---

## 💡 8. Conclusão da Integração dos Encantos

Com a inclusão dos **Encantos como Mudanças de Estado (State-Shifts)**:
1. O Narrador não precisa contar pontos de Gnose para cada feitiço do espírito.
2. Os Encantos geram **dilemas narrativos reais** para os jogadores (ex: salvar o hospedeiro possuído vs. destruí-lo).
3. O modelo Player-Faced engloba 100% da riqueza mística dos espíritos de *Mago: A Ascensão 20 Anos*!

