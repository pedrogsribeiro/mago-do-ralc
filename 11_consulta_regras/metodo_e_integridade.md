---
type: guia
summary: "Procedimento de extração, navegação, rastreabilidade e prova de integridade literal da reorganização por valor."
tags: [regras, integridade, extração, migração, auditoria, piloto]
status: experimental
---
# Piloto de reorganização por valor — princípios e prova

## Objetivo

Responder à pergunta do jogador/Narrador (por exemplo, “como faço uma rasteira?”), recuperando, no mesmo local, **trechos de instrução existentes**, sem exigir que ele encontre primeiro o capítulo ou assunto que o livro utilizou.

## Invariantes absolutos

1. **Proibido reescrever** instruções: nenhuma alteração de palavra, pontuação, número, fórmula, ordem interna de frases ou Markdown original de cada fragmento.
2. **Proibido corrigir** contradições, erros, omissões ou sobreposições durante a reorganização.
3. **Proibido promover** interpretações dos estudos player-faced a regras de M20. Este piloto seleciona somente as cinco fontes em `00_biblia/`.
4. Tabelas recortadas preservam **literalmente** o cabeçalho, a linha de alinhamento, a linha selecionada e a legenda. A seleção pode **omitir linhas não pertinentes**, sem as modificar.
5. Títulos de consulta, organização dos grupos e hyperlinks editoriais são **metadados de navegação**, separados do texto extraído, e não têm força normativa.

## Camadas

- **Fontes originais**: cinco arquivos em `00_biblia/`, congelados como referência de comparação durante o piloto. O SHA do blob Git de cada um consta no manifesto.
- **Corpus de blocos**: `corpus/{combate,do,dano,resolucao,acoes}/*.md`, onde cada arquivo é **uma fatia literal e contígua** da sua fonte. Não possui frontmatter injetado nem edição textual.
- **Manifesto**: `manifesto.json` liga cada bloco a uma fonte, SHA do blob, linhas 1-based e posição ordenada; inclui a receita exata de montagem de cada consulta.
- **Consultas por necessidade**: `consultas/*.md` são vistas geradas. Possuem um cabeçalho e legendas editoriais e copiam exclusivamente os trechos originais apontados, sem parafraseá-los.

## Prova automática de integridade

Executar na raiz do clone:

```bash
python3 11_consulta_regras/ferramentas/validar_integridade.py
```

O teste compara o **hash de blob Git** de cada fonte com o valor registrado, compara cada fragmento à faixa literal de linhas da fonte, concatena todos os blocos **na ordem original para reconstruir exatamente os bytes do arquivo de entrada**, e regenera as consultas a partir do manifesto para comparar seus bytes ao arquivo versionado. Sai com código 1 se qualquer comparação falhar.

**Atenção:** preservar o corpo da regra não significa que as fontes originalmente consolidadas são idênticas ao livro comercial. Verificação contra publicação de origem e resolução de divergências de regras estão **fora do escopo**.

## Cuidado com referências relativas

Não movemos nem corrigimos os arquivos `00_biblia/` neste piloto. Arquivos originários com links relativos só poderiam ser fisicamente movidos sem quebrar vínculos após análise de dependências; mudar a string do link violaria a regra de edição zero. Links editoriais das consultas apontam para as fontes e blocos; não são alterações nos textos das instruções.

## Porta de expansão

O piloto permite medir: tempo para encontrar uma manobra, número de arquivos abertos para resolver a dúvida, suficiência do recorte, integridade literal. Se aprovado, repetir o método em mágika, Umbra, investigação e demais ações. **Não integrar ou substituir o corpus existente automaticamente** sem auditoria específica por conjunto de textos.
