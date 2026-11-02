---
type: guia
summary: "Método de auditoria literal e organização por necessidade de uso."
tags: [integridade, consulta, regras, piloto, metodo]
status: experimental
---
# Regras por valor de uso — método e integridade

Este piloto distingue **interface de consulta** de **corpus técnico**. As consultas em `consultas/` respondem a perguntas da mesa; os blocos em `corpus/` existem para rastrear e reconstruir os textos originais. Cada bloco possui **nome descritivo**, mas conserva todos os seus bytes, incluindo quebras de linha e pontuação.

Os títulos das consultas, o agrupamento e as referências são texto editorial de **navegação**, sem qualquer força de regra. Os conteúdos das instruções são reproduzidos literalmente da `00_biblia/`, inclusive números e eventuais contradições. Nenhuma correção, simplificação ou interpretação é permitida na transposição.

As fontes originais (combate, Do, mágika e Umbra) **não foram movidas nem editadas**. Cada trecho corresponde à faixa de linhas declarada em `manifesto.json`. A ordem total dos segmentos reconstrói os arquivos originais, sem perda. As tabelas selecionadas incluem literalmente suas linhas de cabeçalho, alinhamento e dados, com a definição de termos quando necessário.

## Valor na mesa

O índice principal e os índices específicos de Do, mágika e Umbra tornam possível buscar regras pelos verbos e objetivos do jogador ou Narrador. As consultas reúnem blocos por necessidade e apresentam primeiro o material mais diretamente relevante. Divergências permanecem identificadas em [registro separado](divergencias_documentais.md), sem qualquer alteração das regras.

## Verificação automatizada

Na raiz do clone:

```bash
python3 11_consulta_regras/ferramentas/validar_integridade.py
```

O validador compara o Git blob SHA das fontes, confere cada segmento byte a byte, reconstrói cada fonte original pela concatenação dos segmentos e confere a reprodução literal das vistas, geradas a partir do manifesto.

## Política de edição

Se for necessário melhorar a consulta, alterar apenas os metadados editoriais, a seleção, a posição dos trechos e os caminhos de navegação. Se desejar corrigir uma regra, isso é **outro processo**, fora deste piloto. A reorganização física dos originais depende de auditoria prévia dos links relativos e não foi feita.

**Esta biblioteca ainda é experimental, sem merge na `master`.** A verificação mecânica comprova fidelidade textual, não a exatidão das regras em relação ao livro publicado.
