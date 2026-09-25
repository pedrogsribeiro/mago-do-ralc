---
type: regra
summary: "Estudo técnico sobre a matemática do player-facing em M20, limites da conversão por dificuldade e refinamento por dificuldade + limiar oculto."
tags: [srd, artigo, design, probabilidade, algoritmos, python, monte-carlo, estatistica, player-faced]
---

# Artigo Técnico: Da Variância Dupla à Resolução Player-Faced
### Análise Probabilística e Algoritmos de Simulação Aplicados ao Sistema Storyteller (Mago: A Ascensão 20 Anos)

**Autor:** Pedro Gustavo & Antigravity AI  
**Data:** 13 de Agosto de 2026  
**Área:** Game Design, Teoria Ludológica & Probabilidade Aplicada  

---

## 📄 Abstract (Resumo)

Este artigo formaliza matematicamente a tentativa de converter oposições de *Mago: A Ascensão 20 Anos* para resolução player-facing. A primeira hipótese testada — representar a competência do NPC apenas pela **Dificuldade do d10 do jogador** — mostrou-se insuficiente para reproduzir a distribuição de uma rolagem resistida clássica.

A pesquisa posterior refinou a hipótese para **Dificuldade + Limiar oculto**, reduzindo fortemente o erro, mas ainda identificando viés sistemático na curva de competência dos PJs. Portanto, este estudo deve ser lido como **etapa de calibração**, não como prova final de equivalência.

---

## 🎯 1. O Problema Ludológico: O Gargalo de Variância Dupla

No *Storyteller System* clássico, quando dois personagens realizam uma ação contestada ou resistida (ex: *Manipulação + Lábia* de ambos a Dificuldade 6), cada lado rola uma variável aleatória independente de contagem de sucessos líquidos:

$$X_{PJ} \sim \text{Trinomial}(N_{PJ}, p_s, p_1, p_0)$$
$$X_{NPC} \sim \text{Trinomial}(N_{NPC}, p_s, p_1, p_0)$$

A margem de vitória do jogador é dada por $D = X_{PJ} - X_{NPC}$. A variância da diferença entre duas variáveis aleatórias independentes é a **soma das variâncias**:

$$\sigma^2_{Total} = \text{Var}(X_{PJ}) + \text{Var}(X_{NPC})$$

### O Efeito Matemático e a Questão de Design
Como a variância da diferença soma as variâncias das duas rolagens, disputas simétricas produzem muitos empates e resultados em que o PJ não supera o NPC. Para duas paradas de 4 dados em Dificuldade 6, a margem $D \le 0$ ocorre em aproximadamente **60,5\%** dos casos segundo o modelo adotado.

Esse número descreve uma propriedade estatística; ele **não prova por si só “travamento narrativo”** nem autoriza chamar a variância do NPC de redundante. A questão correta é se essa segunda fonte de variância é importante para a experiência de M20 ou se pode ser comprimida sem distorção perceptível.

---

## 📐 2. Formalização do Modelo Player-Faced

No modelo player-facing investigado, a rolagem do NPC é eliminada quando a incerteza pode ser ancorada na agência de um jogador. O NPC continua agindo na ficção e na iniciativa.

A leitura dos resultados permanece ancorada nos graus de sucesso de M20:

$R(S) = \begin{cases}
\text{Sucesso sólido}, & \text{se } S \ge 2 \\
\text{Sucesso marginal que move a ficção}, & \text{se } S = 1 \\
\text{Falha simples}, & \text{se } S = 0 \\
\text{Falha crítica}, & \text{quando a regra de botch de M20 for satisfeita}
\end{cases}$

**1 sucesso não exige automaticamente custo ou complicação.** O Storyteller interpreta a qualidade marginal do êxito de acordo com a ficção.

---

## 💻 3. Algoritmos de Simulação e Auditoria Estatística

Os algoritmos abaixo registram etapas da pesquisa. Eles são úteis para entender o comportamento das hipóteses, mas os algoritmos 3–5 simulam o **motor proposto**, não um baseline completo de M20, e portanto não constituem prova de equivalência.

### Algoritmo 1: Cálculo Trinomial Exato de Probabilidades Storyteller

```python
import math

def exact_storyteller(N, D=6):
    """
    Calcula analiticamente a probabilidade exata de cada faixa de resultado 
    para uma parada de N dados d10 em Dificuldade D.
    Considera a regra onde dados com valor 1 anulam sucessos.
    """
    p_s = (11 - D) / 10.0  # Probabilidade de Sucesso por dado
    p_1 = 0.10             # Probabilidade de valor 1 por dado
    p_0 = 1.0 - p_s - p_1  # Probabilidade de valor Neutro

    botch = 0.0
    fail = 0.0
    partial = 0.0
    full = 0.0

    for s in range(N + 1):
        for o in range(N - s + 1):
            z = N - s - o
            # Coeficiente Multinomial N! / (s! * o! * z!)
            prob = (math.factorial(N) / (math.factorial(s) * math.factorial(o) * math.factorial(z))) * (p_s**s) * (p_1**o) * (p_0**z)
            net = s - o
            
            if net < 0 and s == 0:
                botch += prob
            elif net <= 0:
                fail += prob
            elif net == 1:
                partial += prob
            else: # net >= 2
                full += prob

    return botch, fail, partial, full

# Exemplo de execução para 4 dados em Dificuldade 6:
b, f, p, ful = exact_storyteller(4, 6)
print(f"Botch: {b*100:.1f}%, Falha: {f*100:.1f}%, Marginal (1s): {p*100:.1f}%, Total (>=2s): {ful*100:.1f}%")
```

---

### Algoritmo 2: Simulador Monte Carlo Comparativo (Resistido Clássico vs. Player-Faced)

```python
import numpy as np

def sim_comparative_opposed(p_dice, npc_dice, target_diff_pf, n_sims=100000):
    """
    Simula 100.000 iterações comparando a rolagem contestada dupla clássica do M20
    contra a rolagem única Player-Faced com Dificuldade Ajustada.
    """
    np.random.seed(42)
    
    # 1. Simulação do Modelo Clássico M20 (Rolagem Dupla)
    p_rolls = np.random.randint(1, 11, size=(n_sims, p_dice))
    p_net = np.sum(p_rolls >= 6, axis=1) - np.sum(p_rolls == 1, axis=1)
    
    npc_rolls = np.random.randint(1, 11, size=(n_sims, npc_dice))
    npc_net = np.sum(npc_rolls >= 6, axis=1) - np.sum(npc_rolls == 1, axis=1)
    
    margin = p_net - npc_net
    c_clean = np.mean(margin >= 2)
    c_marginal = np.mean(margin == 1)
    c_fail = np.mean(margin <= 0)
    
    # 2. Simulação do Modelo Player-Faced (Rolagem Única)
    pf_rolls = np.random.randint(1, 11, size=(n_sims, p_dice))
    pf_net = np.sum(pf_rolls >= target_diff_pf, axis=1) - np.sum(pf_rolls == 1, axis=1)
    
    pf_clean = np.mean(pf_net >= 2)
    pf_marginal = np.mean(pf_net == 1)
    pf_fail = np.mean(pf_net <= 0)
    
    return {
        'classic': (c_clean, c_marginal, c_fail),
        'player_faced': (pf_clean, pf_marginal, pf_fail)
    }
```

---

### Algoritmo 3: Simulador de Resposta Tática em Movimentos Telegrafados

```python
import numpy as np

def sim_telegraphed_decision(choice='A', player_pool=5, n_sims=10000):
    """
    Simula as 3 decisões táticas do jogador diante de um Ataque Telegrafado de Chefe (5 de Dano):
      - Opção A: Tentar Interromper a Carga (Diff 7)
      - Opção B: Focar 100% em Defesa/Esquiva (Diff 6)
      - Opção C: Ignorar o Aviso e Atacar com Tudo (Troca de Dano Fixo)
    """
    np.random.seed(42)
    diff = 7 if choice in ['A', 'C'] else 6
    rolls = np.random.randint(1, 11, size=(n_sims, player_pool))
    succs = np.sum(rolls >= diff, axis=1) - np.sum(rolls == 1, axis=1)
    
    boss_damage_taken = []
    player_damage_taken = []
    
    for net in succs:
        if choice == 'A': # Interromper
            if net >= 2:
                boss_damage_taken.append(2)
                player_damage_taken.append(0)
            elif net == 1:
                boss_damage_taken.append(1)
                player_damage_taken.append(1)
            else:
                boss_damage_taken.append(0)
                player_damage_taken.append(5)
        elif choice == 'B': # Esquivar 100%
            boss_damage_taken.append(0)
            if net >= 2:
                player_damage_taken.append(0)
            elif net == 1:
                player_damage_taken.append(1)
            else:
                player_damage_taken.append(5)
    return np.mean(boss_damage_taken), np.mean(player_damage_taken)
```

---

### Algoritmo 4: Simulador Histórico de Ameaça Ativa Simétrica (Monte Carlo)

```python
import numpy as np

def sim_active_threat_level3(p_atk_dice=5, p_def_dice=5, threat_diff_atk=7, threat_diff_def=7, threat_damage=4, threat_clock=6, n_sims=50000):
    """
    Simula 50.000 confrontos usando uma versão histórica da hipótese de ameaça ativa
    baseada em Diff_Atk, Diff_Def, Dano_Fixo e Relógio_Resistência.
    Este modelo não deve ser tratado como equivalência validada com M20.
    """
    np.random.seed(42)
    wins = 0
    total_rounds = 0
    hp_rem_list = []
    
    for _ in range(n_sims):
        clock = threat_clock
        hp = 7  # Trilha de Vitalidade do Mago (7 níveis)
        rounds = 0
        
        while clock > 0 and hp > 0:
            rounds += 1
            # Turno do PJ: Ataca a Dificuldade de Imposição (Diff_Atk)
            a_rolls = np.random.randint(1, 11, size=p_atk_dice)
            a_net = np.sum(a_rolls >= threat_diff_atk) - np.sum(a_rolls == 1)
            
            if a_net >= 2:
                clock -= 2  # Sucesso Total: 2 Impactos no Relógio
            elif a_net == 1:
                clock -= 1  # Sucesso Marginal: 1 Impacto no Relógio, 1 Dano de raspão no PJ
                hp -= 1
            else:
                # Turno da Ameaça: PJ resiste à Dificuldade de Pressão (Diff_Def)
                d_rolls = np.random.randint(1, 11, size=p_def_dice)
                d_net = np.sum(d_rolls >= threat_diff_def) - np.sum(d_rolls == 1)
                
                if d_net >= 2:
                    pass  # Esquiva Plena: 0 Dano
                elif d_net == 1:
                    hp -= 1  # Esquiva Marginal: 1 Dano de raspão
                else:
                    hp -= threat_damage  # Falha: Recebe Dano Fixo em cheio
                    
            if rounds > 20: break
            
        if hp > 0:
            wins += 1
            hp_rem_list.append(hp)
        total_rounds += rounds

    return {
        'win_rate': wins / n_sims,
        'avg_rounds': total_rounds / n_sims,
        'avg_hp_remaining': np.mean(hp_rem_list)
    }

# Execução da Simulação de Monte Carlo (50.000 iterações):
res3 = sim_active_threat_level3()
print(f"Taxa de Vitória do PJ: {res3['win_rate']*100:.1f}%")
print(f"Duração Média do Confronto: {res3['avg_rounds']:.2f} rodadas")
print(f"HP Restante do Vencedor: {res3['avg_hp_remaining']:.2f} de 7")
```

---

### Algoritmo 5: Simulador Histórico em 4 Domínios (Físico, Social, Intelectual, Místico)

```python
import numpy as np

def sim_multidim_threat(p_dice, diff_imp, diff_pres, threat_damage, threat_clock, n_sims=50000):
    """
    Simula o desempenho de PJs de diferentes Tiers (Inepto 3d, Hábil 5d, Mestre 7d) 
    em confrontos multidimensionais (Social, Intelectual, Místico, Físico).
    """
    np.random.seed(42)
    wins = 0
    total_rounds = 0
    hp_rem_list = []
    
    for _ in range(n_sims):
        clock = threat_clock
        player_res = 7  # HP ou Vontade
        rounds = 0
        
        while clock > 0 and player_res > 0:
            rounds += 1
            # Turno do PJ: Tenta impor ação no Domínio
            a_rolls = np.random.randint(1, 11, size=p_dice)
            a_net = np.sum(a_rolls >= diff_imp) - np.sum(a_rolls == 1)
            
            if a_net >= 2:
                clock -= 2
            elif a_net == 1:
                clock -= 1
                player_res -= 1
            else:
                # Turno da Ameaça: PJ resiste à Pressão no Domínio
                d_rolls = np.random.randint(1, 11, size=p_dice)
                d_net = np.sum(d_rolls >= diff_pres) - np.sum(d_rolls == 1)
                
                if d_net >= 2:
                    pass
                elif d_net == 1:
                    player_res -= 1
                else:
                    player_res -= threat_damage
                    
            if rounds > 20: break
            
        if player_res > 0:
            wins += 1
            hp_rem_list.append(player_res)
        total_rounds += rounds

    return (wins / n_sims) * 100, total_rounds / n_sims, np.mean(hp_rem_list)
```

---

## 📊 4. Resultados Históricos das Hipóteses Simuladas

### 4.1. Resolução em Oposição Rápida (Nível 2)

| Parada do PJ | Perfil do NPC Opositor | Dificuldade $D_{PF}$ | Sucesso Total ($\ge 2s$) | Sucesso Marginal (1s) | Taxa Ativa ($\ge 1s$) | Falha / Complicação |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **3 Dados** | Inepto (2d) | **Diff 5** | $54,1\%$ | $27,0\%$ | **$81,1\%$** | $18,9\%$ |
| **4 Dados** | Médio (4d) | **Diff 6** | $55,2\%$ | $24,9\%$ | **$80,1\%$** | $19,9\%$ |
| **5 Dados** | Treinado (6d) | **Diff 7** | $51,0\%$ | $25,4\%$ | **$76,4\%$** | $23,6\%$ |
| **6 Dados** | Perito (8d) | **Diff 8** | $41,8\%$ | $27,0\%$ | **$68,8\%$** | $31,2\%$ |

---

### 4.2. Simulação Histórica em Ameaças Ativas

| Antagonista do Livro M20 | Domínio de Conflito | Tier do PJ | Dificuldades (Imp / Pres) | Taxa de Vitória | Rodadas Médias | Recurso Restante |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **Cientista Extraordinário** | **Intelectual** | PJ Inepto (3d) | Diff 7 / Diff 6 | **$81,5\%$** | 5,16 r | 4,06 / 7 |
| **Cientista Extraordinário** | **Intelectual** | PJ Hábil (5d) | Diff 7 / Diff 6 | **$98,1\%$** | 4,24 r | 5,36 / 7 |
| **Cientista Extraordinário** | **Físico (Ponto Fraco)** | PJ Inepto (3d) | Diff 5 / Diff 5 | **$99,9\%$** | 2,59 r | 5,99 / 7 |
| **Agente Terno Preto** | **Físico** | PJ Inepto (3d) | Diff 7 / Diff 7 | **$67,7\%$** | 4,73 r | 4,07 / 7 |
| **Agente Terno Preto** | **Físico** | PJ Hábil (5d) | Diff 7 / Diff 7 | **$93,5\%$** | 4,16 r | 5,15 / 7 |
| **Agente Terno Preto** | **Social (Brecha)** | PJ Inepto (3d) | Diff 6 / Diff 6 | **$97,3\%$** | 2,90 r | 5,42 / 7 |
| **Mestre Hermético** | **Místico (Supremacia)**| PJ Inepto (3d) | Diff 8 / Diff 7 | **$33,8\%$** | 5,64 r | 3,21 / 7 |
| **Mestre Hermético** | **Místico (Supremacia)**| PJ Hábil (5d) | Diff 8 / Diff 7 | **$75,9\%$** | 5,61 r | 4,15 / 7 |
| **Mestre Hermético** | **Místico (Supremacia)**| PJ Mestre (7d) | Diff 8 / Diff 7 | **$91,8\%$** | 5,13 r | 4,93 / 7 |
| **Mestre Hermético** | **Intelectual (Brecha)**| PJ Inepto (3d) | Diff 7 / Diff 6 | **$88,1\%$** | 4,27 r | 4,47 / 7 |


---

## 💡 5. Conclusões e Estado Atual da Hipótese

1. **A conversão por Dificuldade isolada foi rejeitada como equivalência suficiente.** Auditoria exata posterior encontrou grandes diferenças de distribuição e de taxa de sucesso.
2. **Dificuldade + Limiar oculto é muito mais promissor.** Para PJs de 2–10 dados contra NPCs de 2–12 dados, o melhor ajuste global reduziu fortemente a distância entre as distribuições, mas ainda apresentou erro residual e viés.
3. **Viés observado:** com a conversão global, PJs de paradas menores tendem a ser levemente prejudicados e PJs de paradas maiores tendem a ser levemente favorecidos; parte dos sucessos sólidos também migra para resultados marginais.
4. **A equivalência matemática continua aberta.** Uma transformação determinística de dois números não pode reproduzir perfeitamente toda a variância de uma segunda rolagem independente. O critério futuro deve combinar distância probabilística, preservação da curva de competência e playtest perceptual.
5. **Ganhos de tempo e carga cognitiva ainda são hipóteses.** Simulação não mede tempo real de mesa; a magnitude desses ganhos precisa de playtests controlados.
6. **A experiência do jogador não pode ser declarada preservada apenas porque os mesmos d10 e dificuldades familiares continuam visíveis.** A promessa exige preservar de forma suficientemente próxima as relações de competência e risco de M20.
7. **A leitura 2+/1/0 permanece válida.** Ela descreve a qualidade do resultado em M20. Em Obstáculos persistentes, 1 sucesso continua sendo sucesso marginal e normalmente produz 1 Impacto/1 caixa antes de qualquer Limiar de Efetividade legítimo.
8. **Ameaça + Consequência não possuem uma transformação universal — e isso deixou de ser requisito do método.** A auditoria V3 rejeitou uma regra fixa para todos os casos. Quando o PJ não possui defesa ativa ou reação equivalente, a solução homologada por fidelidade é preservar a rolagem ofensiva necessária do Storyteller. Quando já existe rolagem defensiva do PJ, a compressão continua candidata a refinamento.


---

## 6. Refinamento Posterior: Dificuldade + Limiar Oculto

A auditoria exata posterior testou PJs de 2 a 10 dados contra NPCs de 2 a 12 dados. A hipótese “parada do NPC → Dificuldade” apresentou erro agregado muito alto. A inclusão de um **Limiar oculto** aproximou muito melhor a estrutura subtrativa da rolagem resistida.

Melhor ajuste global encontrado até aqui:

| NPC | Diff PJ | Limiar |
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

Esse resultado é **experimental**. Uma nova auditoria exata encontrou ajustes pontuais ligeiramente melhores para alguns pools, mas a tabela regular acima permanece um baseline operacional útil porque preserva uma progressão simples e perde pouco em distância probabilística. Na auditoria mais recente, a TV média por parada ficou aproximadamente entre **3,4% e 9,4%**, com alguns piores casos na faixa de **15–16%**.


---

## 7. Propagação do Estudo 06

O Estudo 06 refinou uma premissa importante deste artigo: as quatro dimensões (física, social, intelectual e mística) são úteis como **mapa de competência do NPC**, mas não implicam um motor universal simétrico.

Dano físico, absorção, mágika, oposição social, hacking e testes estendidos possuem procedimentos próprios em M20. Consequentemente:

* **Consequência fixa** não é assumida como equivalente universal a ataque+dano do NPC em conflitos persistentes;
* **Limiar de Efetividade** é a generalização da antiga RD fixa e mostrou comportamento promissor como substituto determinístico de soak;
* **relógios** não são automaticamente equivalentes a Vitalidade, Essência, Força de Vontade ou outros recursos;
* **1 sucesso em conflito persistente** continua produzindo avanço ficcional e, normalmente, 1 Impacto antes do Limiar;
* **Efeito Zero por impossibilidade** deve decorrer de impossibilidade ficcional ou regra efetiva, não de um simples status de “chefe”.

Os algoritmos históricos deste artigo continuam úteis para estudar comportamento interno de hipóteses antigas, mas qualquer validação futura precisa comparar cada subsistema comprimido contra o procedimento original correspondente de M20.


---

## 8. Auditorias V2/V3: estado atual da ficha achatada

### Oposição

A conversão **Dificuldade + Limiar oculto** continua sendo a parte mais madura da ficha achatada. Os erros residuais são suficientemente baixos para tratá-la como baseline experimental, mas ainda não como equivalência exata.

### Limiar de Efetividade

A auditoria exata de soak encontrou a seguinte curva operacional promissora:

| Soak original | Limiar de Efetividade experimental |
| :---: | :---: |
| 0d | 0 |
| 1d | preservar rolagem |
| 2–3d | 1 |
| 4–6d | 2 |
| 7–9d | 3 |
| 10d | 4 |

O caso de **1d** é o mais imperfeito: Limiar 0 elimina toda a proteção e Limiar 1 a torna excessivamente estável. A solução de fidelidade adotada para o baseline é **preservar a rolagem de 1d**, cujo custo operacional é mínimo.

### Ameaça + Consequência

A auditoria V3 comparou três modelos para ataques do NPC:

* a regra histórica de uma única rolagem `2+/1/0`;
* defesa ativa do PJ preservada + soak preservado;
* ausência de defesa ativa com Consequência fixa + soak.

A leitura `2+/1/0` **não foi invalidada** como leitura geral de sucessos. O que falhou foi usá-la sozinha como compressão universal de todo o pipeline ataque+dano de uma Ameaça persistente.

Preservar defesa ativa + soak foi a melhor aproximação entre os modelos testados, especialmente em ameaças fracas e médias, mas o erro cresce em antagonistas fortes.

Quando não existe defesa ativa, o problema é estrutural: M20 possui variância em ataque e dano no lado do NPC, enquanto o jogador pode não possuir nenhuma rolagem anterior ao soak — e alguns tipos de dano sequer permitem soak. Uma compressão totalmente determinística necessariamente elimina parte dessa variância.

Portanto, o caso sem defesa ativa está **metodologicamente fechado por exceção de fidelidade**. A dívida matemática restante concentra-se apenas nas transformações que ainda pretendemos comprimir: Oposição, Limiar de Efetividade e Ameaça quando já existe uma rolagem do jogador capaz de carregar a incerteza.


---

## 9. Teorema prático de conservação da aleatoriedade

As auditorias de Ameaça + Consequência expuseram um limite estrutural do projeto.

Quando o procedimento original possui uma variável aleatória exclusivamente do lado do NPC e não existe rolagem correspondente do jogador, eliminar a rolagem do ST exige uma de três concessões:

1. **determinizar/comprimir a variável**, alterando sua distribuição;
2. **criar ou reaproveitar uma rolagem do jogador**, alterando seu procedimento ou economia de ações;
3. **transferir a própria rolagem do NPC ao jogador**, preservando a matemática mas transferindo carga operacional e informação.

Nenhuma dessas opções preserva simultaneamente distribuição, procedimento do jogador e zero rolagens do ST.

Logo, sob a hierarquia definida no Estudo 00, a solução conservadora é manter a operação original do Storyteller nos casos em que nenhuma transformação player-facing suficientemente fiel foi demonstrada.

Isso não invalida a ficha achatada: **Ameaça** e **Consequência** continuam reduzindo consulta e reconstrução de ficha. O que deixa de ser prometido é que todo campo comprimido necessariamente elimine toda rolagem do ST.


---

## 10. Auditoria de botch e ordem de resolução

A validação final identificou um problema que não aparecia quando se comparavam apenas sucesso/falha: elevar diretamente a dificuldade do PJ para representar Oposição também eleva sua chance de **botch**.

Isso é uma distorção, porque na ação resistida clássica:

1. o PJ faz sua própria rolagem;
2. o botch pertence a essa rolagem;
3. só depois os sucessos do oponente cancelam sucessos do PJ.

### Correção

A conversão de Oposição passa a preservar essa ordem:

```
rolagem do PJ
→ julgar botch pela dificuldade-base original
→ se não houve botch, aplicar a compressão da Oposição
→ dificuldade equivalente + Limiar oculto
→ determinar sucessos líquidos
```

Essa leitura permite manter a tabela regular já usada nos Estudos 02/09 sem aumentar artificialmente a frequência de falhas críticas.

### Resultado exato no espaço auditado

Para PJs de 2–10 dados contra NPCs de 2–12 dados:

* TV média agregada da tabela regular: **~6,75%**;
* pior TV por par observado: **~15,05%**;
* viés médio absoluto de chance de sucesso por faixa de NPC: **~2,7 pontos percentuais**;
* erro de botch: **essencialmente zero**.

A alternativa de usar apenas D6 + Limiar oculto preserva botch naturalmente, mas piora a aproximação para cerca de **8% de TV média** e produz casos próximos de **19%**.

### Estado

A tabela regular atual permanece a candidata principal para playtest perceptual.

Ela ainda não é declarada equivalência exata; o gate restante é **experiencial**, não mais correção de botch.
