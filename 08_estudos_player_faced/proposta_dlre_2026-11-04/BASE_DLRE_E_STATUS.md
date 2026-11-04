# Base de leitura — versão de trabalho DLRE (04/11/2026)

**Status: PROPOSTA PARA REVISÃO AUTORAL.** Esta pasta espelha o conteúdo de `08_estudos_player_faced/` sem sobrescrever nenhum arquivo. Cada documento derivado conserva o corpo integral da fonte, com notas de interpretação e conversões localizadas de assinaturas; isso **não equivale a homologar automaticamente os novos valores**. Em caso de divergência, o trecho de conversão colocado antes do corpo prevalece *somente como proposta*, e a regra já homologada do documento original continua sendo a referência até decisão autoral.

## Finalidade e limites

Converter a interface do Storyteller de DRP para **DLRE — Dificuldade, Limiar, Resistência e Esforço** sem modificar ficha, pools d10, botch, ação, defesa, absorção, Arete, Esferas, contramágika, recursos e escolhas de PJ do M20. O Storyteller rola **zero dados**. Mantenha autonomia ficcional e ações dos elementos do mundo. As conversões não podem criar testes adicionais, reação grátis do PJ, defesa sem custo, dano sem origem, ou economia de ações independente. Não importar regras de Tatangá.

## Gramática operacional candidata

- **D**: dificuldade-alvo do d10, respeitando a dificuldade própria da ação e a avaliação de botch prevista em M20.
- **L**: mínimo de sucessos que a oposição exige para haver concretização; não confundir com absorção posterior. Nas conversões da antiga oposição por cancelamento `R_antigo = r`, quando um sucesso efetivo era necessário para acertar, `L = r+1`. Nesta função específica, `S_efetivos = max(0, S_obtidos - (L-1))`. **Não generalizar a equação** para toda regra com limiar.
- **R**: redução da magnitude **após** a oposição ter sido superada, se e somente se a fonte tem proteção/absorção/resistência quantitativa pertinente. `P_antigo = p` pode migrar para `R = p` no mesmo vetor, respeitando tipagem C/L/A, hierarquia Letal→Contundente apenas na proteção compatível, e as regras originais sobre Agravado. Nunca somar C e L como parcelas.
- **E**: reserva pertinente de persistência, progresso ou integridade (Vitalidade, Structure, Essência e outras, se comportarem tal leitura); não criar `E` por padrão e não eliminar caixas, penalidades, estados ou procedimentos originais.
- Dimensões podem ser omitidas. Uma ficha pode ser `D6` ou `D7 L3 R2[C,L] E[trilha de Vitalidade conforme M20]`, conforme a relevância. **Esta notação é ilustrativa, não uma tabela de stats.**

### Traduções verificáveis de perfis históricos

| Notação DRP anterior | Leitura DLRE candidata | Condição |
|---|---|---|
| `6` (default `6/0/0`) | `D6 L1 R0` | quando bastava 1 sucesso para concretizar ação |
| `6/2` | `D6 L3 R0` | antigo R2 cancelava dois sucessos da oposição |
| `6/2/1` | `D6 L3 R1` | P1 era proteção quantitativa aplicável |
| `7/2/2[C,L]` | `D7 L3 R2[C,L]` | R2 antigo cancelava, P2 antigo protegia C e L |
| `7/2/C2·L1·A0` | `D7 L3 R[C2·L1·A0]` | tipagem de dano permanece explícita |

**Atenção:** quando L é requisito de um procedimento especial, o excedente pode ter outro tratamento. Primeiro consultar a regra original e a homologação da função. Botch não se decide simplesmente subtraindo L após os dados sem olhar a dificuldade-base.

### Baseline de oposição do guia (conversão formal, não nova homologação)

| Pool original da oposição | D | Antigo cancelamento | L candidato |
|---|---:|---:|---:|
| 2d/3d | 6 | 1 | 2 |
| 4d | 7 | 1 | 2 |
| 5d/6d | 6 | 2 | 3 |
| 7d/8d | 7 | 2 | 3 |
| 9d | 6 | 3 | 4 |
| 10d | 7 | 3 | 4 |
| 11d/12d | 7 | 3 | 4 |

Esta tabela apenas traduz a régua anterior sob a mesma função. Preservar a qualificação de playtest do material-fonte quando existir.

## Fractal, ações e movimentos

Qualquer elemento pertinente (pessoa, animal, item, edifício, veículo, sistema, ambiente, instituição, efeito mágicko ou Paradoxo) pode ser obstáculo DLRE, com subelementos independentes **apenas quando úteis à mesa**. Ações, estados, gatilhos, recursos e movimentos são camadas possíveis; não atribuir consciência a coisas.

**Movimentos concretos ficam sempre como sugestões a serem escolhidas, adaptadas ou rejeitadas pelo autor.** A distinção conceitual leve/pesado orienta exemplos, não fecha um catálogo: leve antecipa uma escalada posterior e pode desde já ferir, restringir e causar perdas graves; pesado, quando usado nessa cadeia, concretiza ameaça maior **depois**, com causa e oportunidade real de intervenção. Não exigir dois movimentos em toda cena, não criar relógios/turnos automáticos, e preservar as ações que o agente precisa gastar conforme M20.

## Ponto de parada: PT-8 e Paradoxo

O repositório registra `1d10 ≤ Paradoxo acumulado` como gatilho anterior. Discussão autoral posterior corrigiu o fluxo: **NPC conjura → recebe Paradoxo conforme M20 → soma ao total → se o ganho dessa conjuração for inferior a 5, acumula; se for ≥5, provoca Reação que descarrega o total acumulado**. O próprio autor rejeitou introduzir rolagem para ativar a Reação nesse novo desenho. As fontes estão cronologicamente divergentes: a documentação original não deve ser apagada, e não se deve mesclar gatilhos nem chamar a mudança de homologação integral do pacote. A **seleção e severidade das consequências** continuam abertas: dano, Defeitos, Paradoxo Permanente, Espíritos, Silêncio, banimento e outros efeitos previstos em M20 exigem procedimento player-facing ainda a aprovar. DLRE fractal e movimentos são apenas candidatos auxiliares.

São preservados de PT-8: sucessos-base de Arete (1–3=1S; 4–6=2S; 7–8=3S; 9–10=4S), ajuste circunstancial ±1S e contramágika ativa já decidida para sua função. **Pare neste ponto: não concluir a Reação nem avançar PT-9.**

## Governança e auditoria

Cada espelho tem seção anterior ao corpo com sua leitura DLRE e ideias de movimento, quando pertinentes. Mudanças de texto em exemplos de perfil são **traduções candidatas**, não autorização de implementar novos operadores. O corpo herdado pode conter trechos históricos sobre DRP, inclusive fórmulas e status declarados no passado; não tratá-los como norma DLRE atual quando divergirem desta folha. Nenhuma alteração ao original, nenhuma modificação fora de `08_estudos_player_faced/`, nenhum merge, nenhuma homologação atribuída ao agente.

**Próxima decisão autoral necessária:** qual procedimento sem rolagem escolhe a consequência da Reação de Paradoxo quando o ganho da conjuração é ≥5 e a reserva inteira descarrega?
