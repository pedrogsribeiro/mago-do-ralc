# Plano temporário de execução — Regras de M20 orientadas por valor

**Repositório:** `pedrogsribeiro/mago-do-ralc`  
**Branch de execução:** `chatgpt/consulta-regras-por-valor-piloto-2026-10-31`  
**Estado:** EM EXECUÇÃO (não homologado, `master` intocada).  
**Objetivo de produto:** acesso direto e completo às unidades de informação **presentes nas regras** (tabelas, fórmulas, escalas, dificuldades, modificadores, custos, requisitos, efeitos, exceções e procedimentos). Não projetar situações hipotéticas de mesa como critério de organização.

## Contrato inegociável

- **Proibido modificar qualquer conteúdo original**: nenhuma palavra, número, sinal, célula de tabela, vínculo interno, pontuação, linha ou espaço dos textos-fonte pode ser corrigido ou reescrito.
- Fontes originais em `00_biblia/` permanecem imóveis e intactas. Os índices, etiquetas, registros de proveniência e receitas de consulta são **apenas metadados externos**.
- A extração tem que permitir reconstruir **byte a byte** o documento original, com SHA de blob Git como referência. A consulta gerada precisa reproduzir exatamente os fragmentos originais declarados no manifesto.
- Não converter estudos `08_estudos_player_faced/` em regras M20, nem resolver discrepâncias entre fontes; registrar divergências separadamente.
- Não confundir **cobertura de arquivos** com **cobertura de unidades úteis**; ambos têm critérios específicos.
- Não fazer `merge` na `master` sem auditoria final e decisão explícita. **Este plano é descartável e será removido ao concluir efetivamente o projeto**, não ao terminar apenas uma etapa.

## Dimensionamento e etapas (gates verificáveis)

**P0 — Congelar baseline e dimensionar (CONCLUÍDO).**
Inventariar árvore do `00_biblia/`; distinguir índices, narrativa e fontes de instruções; registrar SHA de cada arquivo e 16 fontes já no manifesto. Critério: relação completa de candidatos, estado de classificação e versões de origem.

**P1 — Inventariar as unidades de valor do acervo (EM EXECUÇÃO).**
Ler cada fonte candidata, capturar títulos, tabelas, listas, fórmulas, parâmetros e blocos implícitos; atribuir tipo de unidade e caminho. Armazenar inventário persistente em `11_consulta_regras/auditoria/` (não no plano transitório). Não assumir que só títulos identificam unidades. Critério: 100% dos documentos classificados; todas as fontes de regras mapeadas e cada seção com status (unidade, contextual ou revisão).

**P2 — Converter em lotes pequenos, com prova de reversibilidade.**
Lotes de aproximadamente 6–12 arquivos-fonte, por grupos existentes: núcleo/criação; combate/riscos; mágika/Esferas; Umbra; parafernália/aliados; demais fontes classificadas. Primeiro extrair de cada fonte para corpus, atualizar manifesto e auditar. **Nunca enviar árvores enormes ou entradas sem caminho**; lotes mínimos, paths checados, comparar SHA antes/depois. Critério por lote: todas as fontes reconstruídas, hashes preservados, duplicação controlada, tabelas íntegras.

**P3 — Publicar referências por valor.**
Criar entradas diretas para as unidades identificadas, com nomes semânticos (ex.: duração, custos, tabela de dano, dificuldades de Película) e contexto mínimo **literal**; índices por categoria e lista de origem. Reutilizar um único trecho canônico na receita quando pertinente; manter versões divergentes visíveis, sem corrigi-las. Critério: cada unidade inventariada tem acesso verificável; a pessoa encontra o valor sem procurar capítulo de origem.

**P4 — Auditoria global de cobertura e experiência de consulta.**
Executar e conferir: SHA original de cada fonte; correspondência de cada segmento; reconstrução exata; regeneração e SHA de todas as consultas; links e destinos; seções sem referência; tabelas truncadas, duplicadas ou sem cabeçalho; critérios de legibilidade da navegação. Registrar números e lacunas reais. Critério: **zero falhas**, 100% dos blocos/unidades classificados e endereçáveis, sem texto alterado.

**P5 — Encerramento e limpeza.**
Emitir relatório final com universo escaneado, coberturas, fontes excluídas e justificativas, divergências e evidências auditáveis. Preparar eventual merge somente após homologação. Retirar **este arquivo e a pasta de progresso temporário** quando todos os gates forem atingidos (o inventário e as ferramentas de auditoria permanecem). Se não concluído, manter plano e marcar pendências para retomada.

## Registro de execução

- **2026-11-02 — P0 iniciado:** branch confirmada em `d718aad118620d3097b3b7bb4f530eb5546b889d`. Árvore contém **87 arquivos Markdown em `00_biblia/`**, incluindo índices, documentos literários, resumos e regras; **16 fontes**, **111 segmentos**, **25 consultas** no piloto anterior. Contagens não representam cobertura do acervo. Próxima ação: criar inventário integral classificado por conteúdo com SHA e títulos, e começar primeiro lote de fontes não cobertas.

- **2026-11-02 — P0 concluído:** inventário persistente criado em `11_consulta_regras/auditoria/inventario_fontes.json`, com os 87 caminhos e SHAs do baseline, 16 fontes do manifesto e categorias **provisórias por localização**. P0 cobre catálogo/SHAs, sem fingir que a classificação semântica está encerrada.
- **2026-11-02 — P1 em execução:** oito fontes lidas e classificadas, com unidades identificadas: tabelas de custos de bônus e XP, dificuldade e sucessos, vitalidade, valores de veículos/colisões, segurança e dano digital, fogo e qualidades/defeitos. Nas fontes de veículos e Teia Digital há mistura de regras com notas de design player-facing, a preservar como camadas distintas. **Próximo lote:** demais fontes de criação, tabelas das Esferas e riscos ambientais; registrar cada achado no inventário antes da extração.

- **2026-11-02 — P2 lote 1 parcial:** quatro documentos de criação, regras gerais e combate foram segmentados literalmente (38 seções), inseridos em manifesto com SHA e catalogados por seção. **Limite explícito:** inventário de títulos e detecção de termos não certificam cobertura de tabelas implícitas ou valores internos; leitura semântica por fonte ainda necessária. O projeto não está concluído. Próximos lotes: demais fontes normativas, segmentação completa, auditoria de unidades internas e vistas por valor.

- **2026-11-02 — P2 lote 2 parcial:** quatro arquivos de descritores de criação (Antecedentes, Arquétipos, Atributos, Conhecimentos) extraídos e reconstruídos literalmente; 64 segmentos adicionados. Total: 24 fontes, 213 segmentos. `auditoria/unidades_valor.json` contém 98 unidades catalogadas por título. Criado `auditoria/indice_unidades.md` para acesso sem números. **Atenção:** ainda não há revisão intrasseção integral; falta cobertura do restante do acervo.

- **2026-11-02 — P2 lote 3:** sete fontes adicionais extraídas literalmente (Essências, Perícias, Talentos, explosões, fogo/calor, fome/sede/sufocamento e quedas/impactos). Total: **31 fontes e 268 fragmentos**. Reconstrução textual verificada no momento da geração; **auditoria global continua pendente**. Ainda é necessário identificar e expor valores dentro de seções, inclusive os trechos que não possuem títulos próprios.

- **2026-11-02 — P2 lote 4:** oito fontes operacionais (desafios, duelos, Teia Digital, veículos, radiação/toxinas, procedimentos/rotinas, contramágika, focos) extraídas. **39 fontes, 389 fragmentos, 259 unidades catalogadas**. Índice por tipo de valor criado; classificação ainda heurística e sujeita a inspeção humana, especialmente conteúdo misto de adaptações player-facing. O plano continua ativo; faltam fontes, revisão intrasseção e auditoria global.

- **2026-11-02 — P2 lote 5:** oito fontes de Esferas (Correspondência, Entropia, Forças, Matéria, Mente, Primórdio, Tempo e Vida), 64 segmentos literais, oito referências diretas por Esfera. Totais: **47 fontes, 453 segmentos e 33 consultas**. SHAs das oito fontes conferidos; reconstrução garantida durante extração. Revisão interna e auditoria global permanecem pendentes. **Plano não pode ser removido.**

- **2026-11-02 — P2 lote 6:** sete fontes de mágika, parafernália, dispositivos, maravilhas e qualidades/defeitos extraídas integralmente (54 fragmentos adicionais). Totais: **54 fontes, 507 fragmentos**. Plano preservado. Seguem pendentes aliados, Umbra, capítulos mistos/contextuais, classificação intrasseção e auditoria global.

- **2026-11-02 — P2 lote 7:** dez documentos adicionais (aliados e antagonistas, fichas, Antecedentes, Força de Vontade e Umbra), 107 segmentos. **64 fontes, 614 fragmentos, 23 arquivos do universo inicial ainda não resolvidos.** O lote preservou o conteúdo integral durante extração. P1 (classificação semântica intrasseção), P3 (valores acessíveis) e P4 (auditoria final) permanecem abertos; não remover este plano.

- **2026-11-02 — P2 lotes 6–9 / inventário estrutural fechado:** lotes 6 (mágika/parafernália) e 7 (aliados, Antecedentes e Umbra) concluídos; os documentos restantes foram classificados e os textos de contexto extraídos quando não eram índices. Universo: **87 arquivos classificados, 73 fontes preservadas no manifesto e 674 segmentos**; **14 arquivos de índice, sumário ou ponteiro** preservados por link à origem. **P1 ainda requer cobertura semântica intrasseção e validação do universo de unidades; P3 exige referências diretas por valor em todo o corpus; P4 exige integridade global de blocos/consultas, links e detecção de valores ocultos. NÃO remover este plano.**

- **2026-11-02 — P1/P3:** foram adicionadas 15 consultas diretas, cobrindo XP, bônus, distribuição inicial, especialidades, tipos de ações, testes, Vitalidade, Qualidades/Defeitos, perturbações, Força de Vontade e riscos. Fontes e reconstruções verificadas neste lote. **Pendente** auditoria de vistas publicadas e levantamento de valores internos restantes; plano não removido.

- **2026-11-02 — P1/P3 lote temático:** 18 referências literais de veículos, Teia Digital, contramágika e Maravilhas publicadas. Seções `Consequência de design` e `Tradução player-facing` foram excluídas das consultas normativas. SHAs das quatro fontes confirmados e reconstrução verificada. Pendem revisão intrasseção e auditoria global; manter plano.

- **2026-11-02 — P3 registros nominais:** publicadas 47 consultas literais individuais para fichas de criaturas, adversários, aliados e dispositivos, separadas por nome original. Cinco fontes preservadas e recompostas. Critério de seleção: títulos de registros de ficha, sem transformação de estatísticas. Revisão sistemática intrasseção e auditoria integral ainda pendentes; plano mantido.

- **2026-11-02 — P1/P3 referência normativa:** mais 12 consultas diretas para testes, modificadores, limiares, falhas, cooperação, classificações da mágika, Quintessência, Ressonância, Paradoxo, Espírito, focos e riscos. Oito fontes verificadas por SHA e reconstruídas no ato. A análise de cobertura indica 255/674 fragmentos endereçados nas 113 vistas de valores anteriores, insuficiente para declarar cobertura semântica. Prosseguir auditoria. Plano mantido.

- **2026-11-02 — Auditoria parcial após atualização dos índices:** 73 fontes, 674 fragmentos e 125 vistas com caminhos/IDs verificados na árvore; 0 referências ausentes. O índice de 510 unidades foi regenerado. **Atenção: esta verificação não executou a comparação byte a byte de todos os 674 fragmentos/125 consultas nem a avaliação semântica; não encerrar P4 ou P5.**

- **2026-11-02 — Correção de granularidade HOMOLOGADA PELO USUÁRIO:** o usuário rejeitou páginas individuais para armas, manobras e fichas; a camada de consulta será **por macroassunto**. Entidades particulares permanecem como títulos dentro da página de seu grupo, e não como páginas. Nesta etapa, **47 fichas individuais + 4 consultas particulares de Do + 1 tabela isolada de Do** foram retiradas da camada publicada e substituídas por **7 páginas macro** (5 famílias de fichas, Do e armas de fogo). O corpus técnico não foi tocado. Continuar consolidação das demais consultas, revisar links e auditoria. **Não apagar este plano enquanto o projeto estiver aberto.**

- **2026-11-02 — Agrupamento por macro significado:** confirmado no histórico autoral: nenhum tipo individual de manobra, arma, ficha, ou subtópico operacional deve virar página por conta própria. Primeiro grupo reorganizado: **Veículos** reúne condução, velocidade, manobras, perseguições, durabilidade e colisões. Manter as fontes e o corpus técnico intactos; continuar agrupando por domínios semânticos genuínos. P4/P5 ainda abertos.

- **2026-11-02 — Macroassunto Teia Digital:** cinco vistas operacionais reunidas em uma única página, corpus e fontes intactos. Demais macroassuntos e auditoria P4 pendentes.

- **2026-11-02 — Macroassunto Contramágika:** quatro vistas operacionais reunidas em uma única página, corpus e fontes intactos. Demais macroassuntos e auditoria P4 pendentes.

- **2026-11-02 — Macroassunto Maravilhas:** quatro vistas operacionais reunidas em uma única página, corpus e fontes intactos. Demais macroassuntos e auditoria P4 pendentes.

- **2026-11-02 — Macroassunto Riscos ambientais:** cinco vistas operacionais reunidas em uma única página, corpus e fontes intactos. Auditoria P4 pendente.

- **2026-11-02 — Macroassunto Criação e evolução:** quatro vistas operacionais reunidas em uma única página, fontes intactas. Auditoria P4 pendente.

- **2026-11-02 — Macroassunto Resolução de ações:** sete vistas operacionais reunidas em uma única página, fontes intactas. Auditoria P4 pendente.

- **2026-11-02 — Macroassunto Qualidades e Defeitos:** duas vistas de catálogo unificadas em uma única página preservando os fragmentos literais e suas origens. P4 ainda não concluída.

- **2026-11-02 — Macroassunto Esferas:** nove vistas de Esferas reunidas em página única, cada uma como subseção com valores literais e proveniência; corpus e textos originais intactos. P4 segue aberto.

- **2026-11-02 — Macroassunto Mágika:** classificação, dificuldades, duração, dano/cura, alcance/conexões e focos passam a uma consulta temática, sem reescrever regras. P4 pendente.

- **2026-11-02 — Macroassunto Quintessência e Ressonância:** duas vistas consolidadas. P4 pendente.

- **2026-11-02 — Macroassunto Combate:** seis consultas procedurais e a tabela de manobras reunidas em página única. Do e armas de fogo seguem como assuntos próprios. Textos originais e corpus não alterados. Atualizar os índices procedurais e executar auditoria P4.

- **2026-11-02 — Mágika com procedimentos:** conjugação, determinação de dificuldade e alcance passam para o macroassunto Mágika já existente. Três páginas de pergunta removidas da interface; conteúdo textual preservado. Atualizar índices e auditar P4.

- **2026-11-02 — Quintessência/Ressonância com procedimento:** a consulta de uso foi incorporada à página macro, sem perda de trechos. P4 aberto.

- **2026-11-02 — Paradoxo com procedimentos:** a consulta de consequências e reação foi absorvida pela página de Paradoxo, mantendo texto literal. P4 pendente.

- **2026-11-02 — Macroassunto Umbra e Espíritos:** Película, percepção/interação espiritual e travessia reunidos na mesma consulta; fragmentos originais preservados. Índices procedurais devem ser atualizados e P4 auditado.

- **2026-11-02 — Macroassunto Vitalidade:** níveis, penalidades e movimentação reunidos em página única. P4 ainda aberto.

- **2026-11-02 — Navegação macro:** índices principais da consulta, de valores e de mágika foram regenerados a partir da lista de 24 vistas em manifesto. Nomes e links conferidos programaticamente; auditoria de links externos a esses índices ainda pendente. P4 continua aberto.

- **2026-11-02 — Prova reproduzível preparada:** verificação de links internos de todas as páginas publicadas mais execução automática de `validar_integridade.py` em push da branch experimental. P4 será concluída apenas após prova efetiva em CI e revisão do resultado; P5 permanece aberto.

- **2026-11-02 — Diagnóstico CI:** verificação literal PASS (73 fontes, 674 fragmentos, 24 consultas). Links: 11 falhas em 250, concentradas em links editoriais de divergências e um link relativo literal copiado da fonte Umbra. Correção: links editoriais ajustados; compatibilidade para link original da Umbra por symlink, sem modificar o fragmento fonte. Reexecutar prova P4.

- **2026-11-02 — Cobertura semântica adicional, sem novas páginas:** sete documentos de descritores de criação (Arquétipos, Atributos, Antecedentes, Conhecimentos, Perícias, Talentos, Essências/Avatar) foram incorporados literalmente a `Criação e evolução`. Os 7 conjuntos têm prova de reconstrução local no momento da edição; a prova global continua automatizada. Reavaliar outras fontes ainda não publicadas antes de P5.

- **2026-11-02 — Complementação macro de Mágika:** procedimentos/rotinas, zonas de realidade, focos e ilusões foram incorporados a Mágika, mantendo as mesmas 24 páginas macro; texto normativo copiado da fonte sem reformular e conferido por reconstrução. P1 requer revisar todas as outras fontes ainda sem vistas.

- **2026-11-02 — Complementação Umbra:** textos de camadas e Vidare, combate espiritual e navegação incorporados à consulta macro existente. Três origens verificadas por reconstrução; P4 revalidação automática, P1 restante aberto.

- **2026-11-02 — Complementação Paradoxo:** Silêncio (Quiet), sua recuperação e trechos pertinentes do capítulo de Mágika foram incorporados à consulta de Paradoxo, com proveniência por fonte e reprodução literal. P1/P4 ainda exigem revisão final.

- **2026-11-02 — Complementação de procedimentos:** duelos mágicos/virtuais incorporados a Combate e desafios/provações incorporados a Resolução de ações, sem criar novas páginas. Quatro blocos normativos adicionais, fontes intactas.

- **2026-11-02 — Checkpoint validado:** CI verde no commit `f07459e` (73 fontes preservadas, 674 fragmentos, 24 consultas macro e links verificáveis). 470/674 fragmentos constam ao menos uma vez das vistas; os 204 restantes incluem contexto, metadados, materiais redundantes, registros de design player-faced e alguns conteúdos a reavaliar semanticamente. A tentativa seguinte de incluir oito antecedentes adicionais foi bloqueada antes de commit (HEAD permanece `f07459e`); **não** registrar essa inclusão como concluída. P1/P4 semânticos e P5 permanecem abertos; manter plano temporário.

- **2026-11-02 — Revisão semântica:** etapas de criação, escala de feitos mágicos e visão geral de Espírito acrescentadas aos macroassuntos existentes (sem páginas extras); fragmentos reconstruídos diretamente das fontes. Validação CI pendente desta revisão.

- **2026-11-02 — Lacunas operacionais:** acesso/Ícones da Teia Digital e atributos dos veículos adicionados às páginas macro correspondentes. Procedimentos de tradução player-faced continuam fora da consulta normativa; auditoria integral automatizada preservada.

- **2026-11-02 — Inventário residual:** 187 fragmentos não publicados receberam categoria editorial, justificativa e referência de origem no arquivo `auditoria/classificacao_residual_macro.json`. Os itens de capítulos-síntese e Antecedentes paralelos são explicitamente classificados como fontes paralelas, sem pressupor igualdade textual. A auditoria semântica de equivalência permanece aberta. P4 e P5 não podem ser concluídos somente com essa classificação.

- **2026-11-02 — Critério automático de cobertura:** verificador novo exige que os 674 IDs de fragmento estejam disjuntos e exaustivamente divididos entre vistas e classificação residual; todas as 24 vistas devem estar no índice, e nenhuma página não catalogada pode existir na interface. Fluxo CI atualizado; aguardar a execução verde para registrar PASS.

- **2026-11-02 — Rastreabilidade de versões paralelas:** relatório de auditoria ganhou referências diretas por macroassunto aos capítulos 6, 8, 9, 10, 11 e 12 e ao resumo alternativo de Antecedentes, sem duplicação textual. Índice raiz aponta para relatório. P4 mecânico permanece automatizado; divergências semânticas não presumidas resolvidas.
