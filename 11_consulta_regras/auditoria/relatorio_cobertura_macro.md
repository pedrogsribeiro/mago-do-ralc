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
