# Diretrizes Globais do Workspace - Mago: A Ascensão 20 Anos (Presencial)

## 1. Padrão de Fichas de NPCs e Entidades
* **Prioridade Diegética (Estilo Aspectos):** A descrição narrativa/diegética antecede a mecânica e deve ser escrita em frases e tópicos curtos e evocativos (estilo Aspectos do Fate Core), cobrindo conceito, comportamento em cena, marcas físicas/sobrenaturais e complicações.
  * *Não utilizar rótulos meta como "Dados Diegéticos Críticos", "Notas Diegéticas (Prioridade 1)" ou "Método B / Método C".* Basta integrar a narrativa naturalmente no topo da entrada e apresentar a mecânica sob a tag `**Bloco Mecânico:**`.
  * *Exemplo de Tópico Diegético:*
    * **Dissolução Autoclean:** Ao sofrer a morte física, dissolve-se instantaneamente em uma poça de líquido inodoro disforme que evapora em poucos segundos, erradicando qualquer rastro de DNA, prova biológica ou autópsia forense.
* **Formatação Mecânica Padronizada:**
  * **Magos, Tecnocratas e Mortais Especializados:** Bloco Tático Resumido (`**Bloco Mecânico:**`) com Parada Física/Tática, Arete, Esferas Principais, Absorção/Armadura, Força de Vontade e Recursos/Equipamentos.
  * **Entidades Espirituais e Umbróides:** Sistema de Ranks Espirituais (`**Bloco Mecânico:**`) com Gnose, Fúria, Força de Vontade, Essência, Encantos e Ressonância.

## 2. Taxonomia de Notas e Links do Antigravity
* **Padrão Exclusivo de Links:** Todos os arquivos citados tanto nos documentos `.md` quanto nas conversas do chat DEVEM utilizar exclusivamente o formato de link Markdown clicável com o esquema `file:///` (ex: `[Nome_Do_Arquivo.md](file:///c:/users/pedrogustavo/.../nome_do_arquivo.md)`).
* **Sem Wikilinks:** Não utilizar sintaxe de wikilinks (`[...](file:///c:/users/pedrogustavo/onedrive/documentos/rpg%20a%20la%20carte/mago%2c%20presencial/07_pjs/niki.md)`). O Antigravity é a única ferramenta de gestão deste workspace.
* Referências diretas às páginas do Livro Básico de M20 (Apêndice I, Págs. 618-641) e links locais para o acervo de SRD do workspace.

## 3. Diretrizes de Eficiência de Contexto e Economia de Tokens
* **Navegação Via ÍNDICE MESTRE (`INDEX.md`):** Sempre consulte o arquivo [`INDEX.md`](../index.md) na raiz do workspace como primeiro passo para localizar NPCs, Regras, Facções, Lugares ou Sessões. Evite usar `list_dir` recursivo ou varreduras cegas.
* **Leitura Parcial de Metadados (YAML Frontmatter):** Ao investigar arquivos, use `view_file` limitando o intervalo de linhas (ex: linhas 1 a 15) para checar o cabeçalho YAML (`type`, `summary`, `tags`). Leia o arquivo completo apenas se o resumo demonstrar relevância direta para a dúvida do usuário.
* **Busca Direcionada via Grep:** Prefira `grep_search` filtrando por tags do YAML (ex: `type: npc`, `tags: [paradoxo]`) com o parâmetro `Includes` restrito à pasta relevante para evitar consumo excessivo de tokens.
* **Padrão YAML Obrigatório:** Todo documento novo ou atualizado deve manter o cabeçalho YAML Frontmatter no topo com `type`, `summary` e `tags`.

## 4. Taxonomia de Carga Narrativa (Sistema Player-Faced Total)
Nas narrativas e regras deste workspace, a oposição é classificada em **3 Níveis de Carga Narrativa** conforme os estudos em [`08_estudos_player_faced`](../08_estudos_player_faced):

* **Nível 1 (Desafio Rápido / Oposição Pontual):** Tarefas estáticas/ambientais (arrombar, saltar, decodificar) ou atritos instantâneos com NPCs menores (guardas, informantes, patrulhas). Resolvido em **1 única rolagem do PJ** contra Dificuldade 5 a 8 ($\ge 2$ Sucessos Plenos, 1 Sucesso Parcial com custo, 0 Falha).
* **Nível 2 (Ameaça Ativa):** Combates sérios, perseguições estruturadas ou hacks ativos contra opositores estruturados (Hit-Marks, Agentes de Elite). Utiliza 4 Dimensões Simétricas, Dano Fixo, Relógios de Vitalidade (3 a 7 Impactos) e Regra do Efeito Zero.
* **Nível 3 (Ameaça Telegrafada / Chefe Climático):** Confrontos climáticos com vilões de arco, rituais de grande escala ou catástrofes. Utiliza Fases + Movimentos Telegrafados Declarados no início da rodada com escolhas táticas de Interrupção, Mitigação ou Ataque Total.


