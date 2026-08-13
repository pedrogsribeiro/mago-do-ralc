---
type: regra
summary: "Estudo 08: Guia Prático de Conversão de Fichas de NPCs (Mortais, Criaturas da Noite e Espíritos) para o Sistema Player-Faced Total nos 4 Níveis."
tags: [estudo, game-design, player-faced, conversao, npcs, fichas, mortais, lobisomens, vampiros, espiritos]
---

# Estudo 08: Guia Prático de Conversão de Fichas de NPCs para o Sistema Player-Faced Total

Este guia instrui qualquer Narrador a pegar qualquer ficha de antagonista ou NPC de *Mago: A Ascensão 20 Anos* (seja um Mortal, Tecnocrata, Criatura da Noite como Vampiro/Lupino ou Espírito Umbróide) e traduzi-la instantaneamente para o sistema **Player-Faced Total**.

---

## 🧭 O Método de Conversão em 4 Passos

```
+---------------------------------------------------------------------------------------------------+
|                        FLUXO DE CONVERSÃO DE FICHAS DE NPCS                                       |
|                                                                                                   |
|  PASSO 1: Classificar a Carga Narrativa  ==> Escolher entre Nível 1, 2, 3 ou 4.                    |
|  PASSO 2: Definir Aspectos Diegéticos    ==> Mapear Campos Semânticos (estilo Fate Core).         |
|  PASSO 3: Converter Parada de Dados M20 ==> Mapear Dificuldade (5 a 8), Relógio e RD/Limiar.      |
|  PASSO 4: Mapear as 4 Dimensões          ==> Preencher variações (Físico, Social, Intel, Místico).|
+---------------------------------------------------------------------------------------------------+
```

---

## 📌 PASSO 1: Classificar o Nível de Carga Narrativa

Antes de olhar os atributos do NPC, o Narrador decide a **importância dramática** da cena:

* **Nível 1 (Obstáculo Passivo):** O NPC é estático ou irrelevante (ex: arrombar porta trancada por um porteiro dormindo). Resolvido em 1 rolagem ($Diff 6 + \text{Limiar de Sucessos}$).
* **Nível 2 (Oposição Rápida / Menor):** NPCs menores em cenas rápidas (ex: subornar um guarda, nocautear um capanga, ultrapassar patrulha). Resolvido em **1 única rolagem do PJ** ($Diff 5 \text{ a } 8$).
* **Nível 3 (Ameaça Ativa):** Confrontos estruturados de múltiplos turnos (ex: Hit-Marks, Ternos Pretos, Jagglings Espirituais, Mestres Herméticos). Utiliza a **Ficha Sintética dos 4 Elementos Simétricos**.
* **Nível 4 (Ameaça Telegrafada / Chefe Climático) — [Visão Preliminar / Placeholder]:** Vilões climáticos, Incarnas arcanos ou Ritos de Grande Escala. Utiliza **Movimentos Telegrafados Declarados no início do turno**, Múltiplas Fases e Relógios Épicos de Chefe. *(Estrutura formal a ser detalhada no Estudo 09)*.

---

## 🏷️ PASSO 2: Definir Aspectos Diegéticos (Campos Semânticos)

Anote 2 a 3 tópicos curtos e evocativos sobre o NPC. Eles dizem à mesa **quais Atributos, Habilidades, Esferas ou Armas afetam o NPC**:

* `[Chassi de Titânio e Primium]`: Indica imunidade a armas pequenas e exige ataques pesados.
* `[Mente Lavada pela NOM]`: Bloqueia lábia comum, mas abre brecha para feitiços de *Mente 3* ou memórias passadas.
* `[Matéria Efêmera Desmaterializada]`: Bloqueia dano físico mundano (Efeito Zero); exige *Espírito 3* ou Fetiches.

---

## 🧮 PASSO 3: Matriz de Conversão da Parada de Dados M20

Localize a maior parada de dados do NPC na ficha clássica (Atributo + Habilidade ou Arete/Fúria) e converta usando a tabela:

| Parada de Dados no Livro M20 | Perfil de Competência | Dificuldade da Ameaça (Imp / Pres) | Relógio de Resolução | Resistência a Dano (RD) / Limiar |
| :---: | :---: | :---: | :---: | :---: |
| **3 a 4 dados** | Amador / Capanga / Gaffling | **Diff 5** | **3 Caixas** | **RD 0** (Sem Armadura) |
| **5 a 6 dados** | Treinado / Agente / Jaggling Menor | **Diff 6** | **5 Caixas** | **RD 0 ou 1** (Armadura Leve) |
| **7 a 8 dados** | Elite / Terno Preto / Jaggling | **Diff 7** | **6 Caixas** | **RD 1** (Anula 1s em Acerto Parcial) |
| **9 ou + dados** | Mestre / Hit-Mark / Incarna | **Diff 8** | **7 Caixas** | **RD 2** ou **Limiar Mínimo 2** (Efeito Zero em 1s) |

---

## 🌐 PASSO 4: Mapear as 4 Dimensões de Conflito

Preencha as variações de Dificuldade de Imposição para que o grupo possa atacar os **Pontos Fracos do Campo Semântico**:

1. **Dimensão Físico-Corporal:** Combates, tiros, atletismo.
2. **Dimensão Social-Ideológica:** Lábia, intimidação, política, autoridade.
3. **Dimensão Intelectual-Técnica:** Hacking, enigmas, ciência, criptografia.
4. **Dimensão Místico-Arcana:** Duelos de Esferas, contramágica, rituais, expulsão efêmera.

---

## 📋 Exemplos Práticos Completos de Tradução

### Exemplo 1: Mortal / Guarda Tático da NOM (Humano)

```yaml
---
ameaca: Guarda Tático da NOM (Adormecido Treinado)
nivel: 3 (Ameaça Ativa)

aspectos_diegaticos:
  - "[Colete Tático de Kevlar]": Armadura leve corporativa (RD 1 Físico).
  - "[Treinamento Militarizado da SWAT]": Foco e disciplina sob fogo.

bloco_mecanico:
  imposicao: Diff 6 (Físico/Tático) | Diff 5 (Social/Suborno)
  pressao: Diff 6 (Disparos de Fuzil Carbina)
  impacto: 3 Pontos de Dano Letal (Se o PJ falhar na defesa)
  relogio_vitalidade: 5 Caixas de Vitalidade Físico-Corporal
  resistencia_dano: RD 1 (Acerto Parcial de 1s causa Efeito Zero no Relógio)
---
```

### Exemplo 2: Criatura da Noite / Lobisomem Lupino em Crinos (Lupino)

```yaml
---
ameaca: Presa de Prata Garou em Forma Crinos (Criatura da Noite)
nivel: 3 (Ameaça Ativa) ou Nível 4 (Se Chefe Climático)

aspectos_diegaticos:
  - "[Fúria Incontrolável da Mãe Terra]": Imune a intimidação social (Campo Social Bloqueado).
  - "[Garras e Dentes de Prata Natural]": Causa Dano Agravado em cheio.
  - "[Regeneração Efêmera de Gaia]": Regenera 1 Caixa de Vitalidade por turno a menos que receba dano de Prata.

bloco_mecanico:
  imposicao: Diff 8 (Físico - Regeneração/Regalia) | Diff 6 (Intelectual/Enigmas de Espíritos)
  pressao: Diff 8 (Resistir a Garras de Crinos)
  impacto: 5 Pontos de Dano Agravado
  relogio_vitalidade: 7 Caixas de Vitalidade Lupina
  limiar_efetividade: Limiar Mínimo = 2 (Requer Prata ou Mágika Ofensiva para causar 2s)
---
```

### Exemplo 3: Espírito / Jaggling das Sombras (Umbróide)

```yaml
---
ameaca: Jaggling das Sombras (Entidade Efêmera)
nivel: 3 (Ameaça Ativa)

aspectos_diegaticos:
  - "[Matéria Efêmera Desmaterializada]": Imune a ataques físicos mundanos (Efeito Zero sem Espírito 3 ou Fetiches).
  - "[Encanto: Possessão]": Capaz de habitar corpos de civis inocentes.

bloco_mecanico:
  imposicao: Diff 7 (Místico/Espírito) | Diff 5 (Com Fetiche de Banimento)
  pressao: Diff 7 (Resistir à Fúria das Sombras)
  impacto: 4 Pontos de Dano Agravado / Drenagem de 2 de Vontade
  relogio_essencia: 6 Caixas de Essência Espiritual

relogio_duplo_possessao:
  relogio_hospedeiro: 4 Caixas (Corpo Físico do Inocente - Diff 5)
  relogio_demonio: 6 Caixas (Exorcismo com Espírito 3 - Diff 7)
---
```

---

## 💡 Conclusão do Guia

Com este documento, qualquer Narrador consegue traduzir qualquer ficha dos manuais de *Mago: A Ascensão*, *Vampiro*, *Lobisomem* ou *Cthulhu/WoD* em **menos de 60 segundos**, mantendo o equilíbrio matemático rigoroso e a alta ergonomia cognitiva na mesa!
