---
name: mago-lookup
description: Procedimento de busca otimizada e de baixo consumo de tokens para localizar NPCs, PJs, Facções, Lugares, Itens e Sessões no workspace Mago Presencial.
---

# Skill: Mago Entity Lookup (Busca Rápida de Entidades)

Esta skill orienta os agentes a realizarem pesquisas ultra-eficientes no workspace da campanha, minimizando o consumo de tokens e o número de chamadas de ferramenta.

## Fluxo de Trabalho de Busca (3 Passos)

1. **Passo 1: Consultar o ÍNDICE MESTRE (`INDEX.md`)**
   - Em vez de listar diretórios ou fazer varreduras profundas, abra o arquivo [`INDEX.md`](file:///d:/OneDrive/Documentos/RPG%20a%20la%20Carte/Mago,%20presencial/INDEX.md).
   - Localize o nome do NPC, PJ, Lugar ou Facção na tabela correspondente.
   - Copie o link direto `file:///...` do documento.

2. **Passo 2: Leitura Parcial dos Metadados (Opcional)**
   - Se você precisa apenas de um resumo diegético rápido ou confirmação de papel na trama, execute `view_file` especificando `StartLine: 1` e `EndLine: 15`.
   - Leia o bloco YAML Frontmatter (`summary:`, `tags:`) no topo do arquivo.

3. **Passo 3: Leitura Completa Apenas se Necessário**
   - Se o usuário solicitou o Bloco Mecânico completo ou a ficha detalhada, abra o arquivo na íntegra.

## Diretrizes para Respostas do Agente
- Sempre inclua o link Markdown formatado no padrão `file:///` para a nota da entidade citada.
- Responda primeiro com a **Descrição Diegética** (conceito, comportamento em cena, características) antes dos dados mecânicos, respeitando o padrão das diretrizes do workspace em [`AGENTS.md`](file:///d:/OneDrive/Documentos/RPG%20a%20la%20Carte/Mago,%20presencial/.agents/AGENTS.md).
