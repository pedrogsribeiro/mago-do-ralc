---
type: guia
summary: "Contrato de gestão de histórias por frentes com entidades e acontecimentos canônicos independentes."
tags: [frentes, gestao, entidades, acontecimentos, links, canon, procedimentos]
status: aprovado_para_organizacao
---
# Gestão de histórias por frentes

## Princípio de propriedade única

As **frentes** contêm *perigos/ameaças dentro de uma situação*, seus impulsos, presságios condicionais, desastres iminentes, movimentos, vínculos e stakes abertos. Não são repositórios da biografia, ficha, localização, propriedade ou histórico completo de um elemento. As duas frentes existentes são [[O Sangue da Metrópole]](01_o_sangue_da_metropole.md) e [[O Expurgo dos Despertos]](02_o_expurgo_de_lizander.md). O Problema Legado é histórico e **não gera frente ativa**.

**Cadastros únicos fora das frentes:**

| Tipo | Fonte de verdade | O que guardar |
|---|---|---|
| Pessoas, NPCs, entidades e espíritos | [[02_npcs]](../../02_npcs/readme.md) e [[07_pjs]](../../07_pjs/readme.md) | Identidade, paradigma, fichas, poderes, motivações, vínculos permanentes, paradeiro conhecido e dúvidas de identidade |
| Locais | [[03_lugares]](../../03_lugares/readme.md) | Identidade e geografia, domínio, propriedades, acesso, perigos próprios e estado atual verificado |
| Itens, recursos, provas | [[06_itens]](../../06_itens/readme.md) | Natureza, propriedades, quantidade confirmada, procedência, custódia e estado |
| Organizações/facções | [[05_faccoes]](../../05_faccoes/readme.md) | Identidade, poder, recursos, objetivos estruturais e relações |
| Acontecimentos | [[10_acontecimentos]](../../10_acontecimentos/readme.md) | **O que ocorreu**, onde, quando se souber, quem participou, fonte, mudanças e incertezas |
| Sessões | [[04_sessoes]](../../04_sessoes/readme.md) | Relato de jogo e materiais de preparação, distinguidos pelo estado de cada informação |
| Frentes | [[01_problemas/frentes]](readme.md) | Como as entidades **atuam especificamente no conflito**, evolução possível, relações e perguntas abertas |

## Convenção de links

**Convenção interoperável para esta camada de gestão:** `[[Nome do elemento]](CAMINHO_RELATIVO_PARA_NOTA.md)`. Visualmente mantém o aspecto de wikilink, mas utiliza sintaxe Markdown navegável no GitHub e em editores Markdown comuns. Não é o wikilink puro de Obsidian (`[[Nome]]`). Se algum editor exigir wikilink puro, será necessário um resolvedor explícito de aliases/caminhos antes da conversão.

**Prioridade:** caminhos relativos à nota atual, nome legível e um único arquivo canônico. Não usar URLs `file:///` dependentes de equipamento. **Mudança localizada e deliberada:** a antiga regra de `.agents/agents.md` que proibia wikilinks e impunha `file:///` fica substituída para notas narrativas e seus índices; a documentação técnica legada pode ser migrada depois, com auditoria.

Se nome se repete, use identificador estável e link inequívoco. Renomear a exibição do link é seguro; mover o arquivo exige revisar os vínculos. Uma entidade pode ser citada em várias frentes, mas não duplicada. O histórico de um item ou pessoa se refere aos `EVT-...` adequados.

## Situações de informação

Todo documento novo traz no frontmatter `type`, `summary`, `tags` e `status`. Quando relevante, um campo `id`. Distinguir:
- **Ocorrido/confirmado em mesa:** fato com fonte (sessão ou declaração do Narrador).
- **Verdade do cenário/definido pelo Narrador:** existe nos bastidores, mesmo não descoberto pelos PJs; não marcar como revelado.
- **Preparado/condicional:** local, proposta de cena, plano de NPC, presságio, obstáculo ainda não instanciado.
- **Incerto:** apresentar as possibilidades sem escolher uma resposta.

A pessoa que apareceu como Zhong Kui tem identidade **incerta**; a Mula sem Cabeça foi **invocada**, mas seus atributos e desdobramentos não foram dados pelo Narrador. Não inventar respostas em processos automáticos.

## Processo de Storyteller

**Ao preparar:** cadastrar pessoas, lugares, itens ou organizações novos em seus diretórios. Criar vínculos da frente para as fichas; escrever movimentos/presságios **somente no perigo correspondente dentro da frente**. Ligar pistas do grafo investigativo aos mesmos registros.

**Durante jogo:** consultar frente + fichas canônicas; movimento anuncia ou aplica consequência conforme recursos, situação, poderes e regras de M20. Lentes de Paradigma/Vidare, Ressonância/Jhor, Húbris e Avatar inspiram manifestações coerentes, sem forçar punição por sucesso.

**Depois da sessão:** registrar fatos num novo `EVT-XXX`; atualizar estado/posse/paradeiro **na ficha do elemento** com fonte; revisar presságios e relações **na frente** que abriga o perigo. Distinguir fato, interpretação, rumor e previsão. O mesmo acontecimento pode afetar ambas as frentes, sem ser duplicado.

**Ao encerrar frente:** marcar concluída, arquivar seu desenvolvimento e conservar fichas e acontecimentos como história persistente. Um perigo encerrado não reaparece automaticamente.

## Não interferir no motor de M20

Esta estrutura é documental. Mantém `08_estudos_player_faced/contrato_produto_player_faced_total.md`, as fichas M20 e a representação DRP quando cabível; não importa rolagens de PbtA nem obriga convergência por atos ou ao Nó E.

## Exemplos de referências

- [[Carlito Heizenberg]](../../02_npcs/carlito_heizenberg.md), [[Fábrica Pasta da Nona]](../../03_lugares/fabrica_pasta_da_nona.md), [[Néctar de Sangue]](../../06_itens/nectar_de_sangue.md), [[EVT-001 — Colisão]](../../10_acontecimentos/evt_001_colisao_motoboy.md).
- [[Lizander]](../../02_npcs/lizander_filho_do_raio.md), [[Santuário]](../../03_lugares/santuario_lizander.md), [[Sintonizador]](../../06_itens/sintonizador_ritual_quintessencia.md).
- [[EVT-003 — Mula sem Cabeça]](../../10_acontecimentos/evt_003_fuga_mula_sem_cabeca.md) e [[EVT-004 — Visitante de Zhong Kui]](../../10_acontecimentos/evt_004_visitante_zhong_kui.md) pertencem ao registro factual, **independentemente** de frentes.
