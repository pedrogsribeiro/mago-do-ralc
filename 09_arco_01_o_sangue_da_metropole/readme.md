---
type: index
summary: "Índice navegável do Arco 01 da Crônica: O Sangue da Metrópole, estruturado em Grafo de Nós (The Alexandrian) e oposição Player-Faced."
tags: [indice, readme, cronica, arco_01, alexandrian, 3_pistas, player_faced]
---
# Arco 01 da Crônica: O Sangue da Metrópole

Este diretório contém a estrutura completa do **Arco 01 da Crônica de Mago: A Ascensão (Presencial)**. O arco utiliza a metodologia **Node-Based Scenario Design** e a **Regra das 3 Pistas (The Three Clue Rule)** de *The Alexandrian*, conectada aos 3 Problemas Motores da campanha e resolvida através do motor **Player-Faced Total (Níveis 1 a 4)**.

---

## 🧭 Grafo de Nós do Arco 01 (The Alexandrian Node Graph)

```mermaid
graph TD
    A["Nó A: O Set de Filmagem<br/>(Incidente Inicial & Explosão do Delivery)"] -->|Pista 1A: Celular do Motoboy| B["Nó B: Fábrica Pasta da Nona<br/>(Refinaria de Carlito Heizenberg)"]
    A -->|Pista 2A: Frascos de Sangue| C["Nó C: Hospital CAPS Zona Sul<br/>(Surto de Viciados & Enfermeira Ângela)"]
    A -->|Pista 3A: Sinal Digital & ABIN| D["Nó D: Data Center & ABIN<br/>(Live de Bernardino & Infectologia)"]

    B -->|Pista 1B: Notas de Sangue Hospitalar| C
    B -->|Pista 2B: Servidores do Appetito| D
    B -->|Pista 3B: Canalização Mística| E["Nó E: Santuário de Lizander<br/>(Clímax: O Ritual de Raios pós-Pandemia)"]

    C -->|Pista 1C: Amostras de Quintessência| B
    C -->|Pista 2C: Registros de Viciados| D
    C -->|Pista 3C: Aparição de Joana Pipoquinha| E

    D -->|Pista 1D: Transmissões da ABIN| B
    D -->|Pista 2D: Pesquisas da Dra. Elizabeth| C
    D -->|Pista 3D: Coordenadas do Nódulo| E
```

---

## 📄 Estrutura de Documentos do Arco 01

* 📘 [`00_visao_geral_e_matriz_de_pistas.md`](00_visao_geral_e_matriz_de_pistas.md): A Matriz Alexandrian com a listagem completa das 3 pistas para cada nó e as regras de Pistas Proativas.
* 📍 [`01_no_a_set_de_filmagem.md`](01_no_a_set_de_filmagem.md): **Nó A (Incidente Inicial):** O estouro do gerador no set de filmagem em São Paulo.
* 🏭 [`02_no_b_fabrica_pasta_da_nona.md`](02_no_b_fabrica_pasta_da_nona.md): **Nó B (Logística & Refinaria):** A base do alquimista Carlito Heizenberg e dos Pastafarianos.
* 🏥 [`03_no_c_caps_zona_sul.md`](03_no_c_caps_zona_sul.md): **Nó C (Surto & Revelação Efêmera):** O drama do hospital com Ângela e a manifestação de Joana Pipoquinha.
* 💻 [`04_no_d_data_center_e_abin.md`](04_no_d_data_center_e_abin.md): **Nó D (Infiltração & Guerra de Informação):** Servidores da ABIN, transmissões de Bernardino e vacinas.
* ⚡ [`05_no_e_santuario_de_lizander.md`](05_no_e_santuario_de_lizander.md): **Nó E (O Clímax do Arco 01 - Nível 4):** O grande confronto épico contra Lizander Filho do Raio.
