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
