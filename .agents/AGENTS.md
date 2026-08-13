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
* **Padrão Exclusivo de Links:** Todos os arquivos citados tanto nos documentos `.md` quanto nas conversas do chat DEVEM utilizar exclusivamente o formato de link Markdown clicável com o esquema `file:///` (ex: `[Nome_Do_Arquivo.md](file:///c:/Users/pedrogustavo/.../Nome_Do_Arquivo.md)`).
* **Sem Wikilinks:** Não utilizar sintaxe de wikilinks (`[...](file:///c:/Users/pedrogustavo/OneDrive/Documentos/RPG%20a%20la%20Carte/Mago%2C%20presencial/07_PJs/Niki.md)`). O Antigravity é a única ferramenta de gestão deste workspace.
* Referências diretas às páginas do Livro Básico de M20 (Apêndice I, Págs. 618-641) e links locais para o acervo de SRD do workspace.

## 3. Diretrizes de Eficiência de Contexto e Economia de Tokens
* **Navegação Via ÍNDICE MESTRE (`INDEX.md`):** Sempre consulte o arquivo [`INDEX.md`](../INDEX.md) na raiz do workspace como primeiro passo para localizar NPCs, Regras, Facções, Lugares ou Sessões. Evite usar `list_dir` recursivo ou varreduras cegas.
* **Leitura Parcial de Metadados (YAML Frontmatter):** Ao investigar arquivos, use `view_file` limitando o intervalo de linhas (ex: linhas 1 a 15) para checar o cabeçalho YAML (`type`, `summary`, `tags`). Leia o arquivo completo apenas se o resumo demonstrar relevância direta para a dúvida do usuário.
* **Busca Direcionada via Grep:** Prefira `grep_search` filtrando por tags do YAML (ex: `type: npc`, `tags: [paradoxo]`) com o parâmetro `Includes` restrito à pasta relevante para evitar consumo excessivo de tokens.
* **Padrão YAML Obrigatório:** Todo documento novo ou atualizado deve manter o cabeçalho YAML Frontmatter no topo com `type`, `summary` e `tags`.

## 4. Taxonomia de Carga Narrativa (Sistema Player-Faced Total)
Nas narrativas e regras deste workspace, a oposição é classificada em 4 Níveis de Carga Narrativa conforme os estudos em [`08_Estudos_Player_Faced`](../08_Estudos_Player_Faced):

* **Nível 1 (Obstáculo Passivo):** Tarefas estáticas ou ambientais (arrombar, saltar, hackear sistemas sem IA). Resolvido em 1 rolagem contra Dificuldade 6 + Limiar de Sucessos.
* **Nível 2 (Oposição Rápida / Menor):** Interações sociais, furtivas ou de confronto instantâneo com NPCs menores (guardas, informantes, patrulhas). Resolvido em 1 rolagem do PJ contra Dificuldade 5 a 8.
* **Nível 3 (Ameaça Ativa):** Combates sérios ou hacks ativos contra opositores estruturados (Hit-Marks, Agentes de Elite). Utiliza Fator de Ameaça, Dano Fixo e Relógios de Vitalidade/Intrusão.
* **Nível 4 (Ameaça Telegrafada / Chefe):** Confrontos climáticos com vilões ou rituais de grande escala. Utiliza Movimentos Telegrafados Declarados no início da rodada e dilemas táticos de interrupção/defesa.


