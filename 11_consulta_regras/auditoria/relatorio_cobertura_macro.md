# Auditoria de cobertura da consulta macro

## Escopo
- **73 fontes** preservadas e verificadas pelo manifesto.
- **674 segmentos** reconstruíveis a partir dos originais.
- **24 consultas macro** na interface do usuário.
- **487 segmentos** referenciados em pelo menos uma consulta.
- **187 segmentos** preservados fora da interface, com classificação por identificador no arquivo `classificacao_residual_macro.json`.

## Destino das unidades residuais
- **cabecalho_metadados: 65**
- **capitulos_paralelos: 26**
- **estudo_player_faced: 31**
- **rotulo_ja_coberto: 2**
- **antecedentes_paralelos: 12**
- **contexto_cenario_narracao: 51**

A ausência de uma unidade da camada de consultas não implica remoção nem alteração do texto original. Os arquivos de `00_biblia/`, `corpus/` e `corpus_integral/` continuam preservados, mesmo quando as versões paralelas não são republicadas.

**Limitação importante:** esta classificação é editorial e baseada em fonte/título mais leitura de amostras e casos normativos de maior risco. Não prova que duas versões paralelas tenham o mesmo texto nem que suas diferenças mecânicas sejam irrelevantes. As divergências já registradas permanecem vigentes em `divergencias_documentais.md`.

## Critérios de aceite
1. Provar por execução automática o SHA das fontes, a integridade byte a byte de todos os segmentos e a reprodução das consultas.
2. Verificar links internos da interface.
3. Não publicar estudos player-faced como regra oficial M20.
4. Não subdividir macroassuntos por arma, manobra, técnica, criatura ou vantagem individual.
5. Documentar qualquer divergência verificada sem alterar seus valores.

## Estado
Auditoria **mecânica automatizada** repetida em CI; a auditoria **editorial-semântica de equivalência entre fontes paralelas** não foi concluída e não pode ser declarada como PASS apenas pela classificação.

## Fontes paralelas consultáveis por assunto

Os capítulos-síntese abaixo podem apresentar redações ou valores diferentes. Eles permanecem acessíveis, mas esta organização **não os declara equivalentes** às consultas macro:

- **Criação e evolução:** [Capítulo 6](../../00_biblia/02_criacao_de_personagem/06_capitulo_06_criacao_personagens.md).
- **Resolução de ações:** [Capítulo 8](../../00_biblia/03_sistemas_e_regras/08_capitulo_08_regras.md).
- **Combate, Do e riscos:** [Capítulo 9](../../00_biblia/04_sistemas_dramaticos_e_combate/09_capitulo_09_sistemas_dramaticos.md).
- **Mágika e Paradoxo:** [Capítulo 10](../../00_biblia/05_regras_de_magika/10_capitulo_10_livro_da_magika.md).
- **Criaturas e fichas:** [Capítulo 11](../../00_biblia/06_aliados_e_antagonistas/11_capitulo_11_aliados_antagonistas.md).
- **Maravilhas, dispositivos, Qualidades e Defeitos:** [Capítulo 12](../../00_biblia/07_parafernalia/12_capitulo_12_parafernalia.md).
- **Antecedentes:** [Resumo alternativo de Antecedentes](../../00_biblia/resumos/antecedentes.md).

A consulta dos capítulos paralelos é feita na fonte intacta, evitando replicar tabelas e blocos narrativos como novas páginas de regras.
