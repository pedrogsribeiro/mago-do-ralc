---
type: regra
summary: "Estudo 12: constructos, objetos e hipertecnologia sob o olhar de Obstáculos, distinguindo agentes de objetos com Durability + Structure."
tags: [srd, design, player-faced, constructos, objetos, hit-marks, hipertecnologia, durability, structure, regras]
---

# Estudo 12: Constructos, Objetos e Hipertecnologia

Este domínio revelou uma distinção central para a ontologia de Obstáculos:

> **nem toda máquina é um NPC.**

M20 já fornece a objetos dois valores especialmente compatíveis com player-facing:

* **Durability:** resistência fixa do material;
* **Structure:** integridade funcional.

Isso permite tratar grande parte de portas, paredes, terminais, máquinas, veículos parados e estruturas sem inventar uma ficha sintética nova.

---

## 1. Primeiro classifique a natureza do alvo

### Objeto / estrutura
Não possui agência própria.

Exemplos:
* porta blindada;
* parede;
* servidor físico;
* reator;
* console;
* veículo estacionado;
* gerador.

Use **Durability + Structure** quando a regra original aplicável for a de objetos.

### Sistema ativo
Pode detectar, bloquear ou responder segundo um protocolo, mas não necessariamente precisa de uma ficha de personagem.

Exemplos:
* scanner;
* alarme;
* firewall;
* torre automatizada;
* ICE;
* lockdown.

Pode exigir oposição técnica, gatilhos e consequências, além de Durability/Structure para seus componentes físicos.

### Constructo-agente
Possui iniciativa, ações próprias e comportamento persistente.

Exemplos:
* Hit-Mark;
* golem;
* drone autônomo de combate;
* aberração biotecnológica.

É tratado mais como NPC, preservando suas capacidades originais.

---

## 2. Durability + Structure como Obstáculo nativo

A lógica básica é:

```
Durability = resistência
Structure  = integridade
```

O objeto não rola soak. O material já fornece uma resistência fixa.

Isso é extremamente próximo do objetivo player-facing e deve ser preservado sempre que possível.

Se mágika, ferramenta ou tipo de dano modifica Durability ou permite ignorá-la, aplica-se a regra original correspondente.

---

## 3. Dimensões como lente de abordagem

Um sistema pode ser:

* fisicamente muito resistente;
* tecnicamente vulnerável;
* mágickamente protegido;
* socialmente inacessível sem credencial.

Essas descrições ajudam o ST a dimensionar **como os jogadores podem atacá-lo**, sem exigir quatro relógios ou quatro fichas.

Exemplo:

```
Servidor militar

Físico: Durability/Structure altos
Mental/Técnico: segurança forte
Mágicko: proteção média
Social: credencial de diretor contorna parte do sistema
```

Cada abordagem usa a regra que M20 pedir para aquele tipo de ação.

---

## 4. Efeito Zero

Constructos são bons casos para Efeito Zero quando existe impossibilidade real:

* convencer emocionalmente uma torreta sem interface social;
* socar uma parede que o ataque não consegue fisicamente danificar;
* usar técnica incompatível com o sistema.

Mas comandos válidos, hacking, mágika ou exploração de protocolo podem abrir abordagens antes impossíveis.

---

## 5. Telegrafia em sistemas e máquinas

Uma instalação pode:

* fechar portas;
* começar a liberar gás;
* iniciar sobrecarga;
* travar um alvo;
* ligar bombas;
* armar autodestruição.

A primeira etapa pode ter efeito real e estabelecer a escalada seguinte.

Exemplo:

> comportas fecham e isolam o grupo **agora**; em seguida, o sistema começa a despressurizar o setor.

Isso preserva a formulação de telegrafia construída no Estudo 03.

---

## 6. Procedimentos de M20 acionados por este domínio

| Situação | Procedimentos principais |
| :--- | :--- |
| Objeto passivo | ataque/dano contra objeto, Durability, Structure |
| Sistema ativo | testes simples/resistidos/estendidos, hacking, gatilhos, consequência |
| Constructo-agente | iniciativa, Oposição, Ameaça, Consequência, Limiar de Efetividade, Vitalidade, poderes |
| Sistema hipertecnológico | Arete/Iluminação, Quintessência, contramágika, procedimentos |
| Veículo | condução, perseguição, colisão, dano estrutural |

Isso deixa claro por que “constructos e hipertecnologia” não podem ser comprimidos por uma única tabela.

---

## 7. Teste 1 — Porta blindada

A porta não possui agência.

Se o grupo tenta destruí-la fisicamente, a referência correta é a regra de objetos:

* o ataque do PJ continua normal;
* o dano continua vindo do jogador;
* **Durability** reduz o que efetivamente atravessa o material;
* **Structure** mede quanto dano funcional a porta suporta.

### Gate

**PASSA.**

Esse caso já é quase naturalmente player-facing. Não há motivo para criar Oposição, Ameaça ou um relógio genérico no lugar de Durability + Structure.

Se o personagem usa Matéria, Entropia ou outra mágika que altera a resistência do material, aplica-se a regra mágicka correspondente.

---

## 8. Teste 2 — Scanner biométrico com lockdown

Aqui existem dois objetos diferentes no mesmo Obstáculo de cena:

1. o **hardware físico**, que pode possuir Durability + Structure;
2. o **sistema de segurança**, que pode exigir testes técnicos, credenciais ou mágika para ser contornado.

Se o scanner apenas compara uma assinatura, ele não precisa “rolar contra o hacker”.

O ST consulta a regra pertinente para a dificuldade/complexidade da intrusão. Se houver uma oposição ativa real — por exemplo, uma IA ou operador tentando impedir a invasão — entra a lógica de oposição resistida.

O lockdown pode produzir estados em sequência: normal → intrusão detectada → portas seladas → purga iniciada.

Esses estados podem ser telegrafados sem transformar o sistema numa criatura fictícia.

### Gate

**PASSA como Obstáculo híbrido.**

A classificação objeto + sistema evita duas distorções antigas:

* tratar todo terminal como NPC;
* reduzir toda segurança a uma única “Oposição Mental”.

Hacking/ICE completo continua dependendo da auditoria específica desse subsistema.

---

## 9. Teste 3 — HIT Mark V

O HIT Mark é constructo-agente.

Sua ficha de M20 já demonstra isso:

* possui atributos;
* Habilidades;
* iniciativa;
* Vitalidade;
* soak elevado;
* armas;
* contramágika;
* sensores;
* objetivos operacionais.

Logo, Durability + Structure **não substitui sua ficha de personagem** apenas porque ele é mecânico.

A interface do ST pode resumir:

    HIT MARK V

    Natureza: constructo-agente

    Lentes:
    Físico: excepcionalmente resistente
    Social: quase inexistente
    Mental/Técnico: programado
    Mágicko: forte defesa por Primium

    Características:
    [Primium]
    [Contramágika 5d]
    [Sensores especiais]
    [Armas integradas]

    Fontes relevantes:
    Briga 5d
    Percepção/Prontidão 6d
    soak total 9d
    dano das armas conforme ficha
    Vitalidade especial

Oposição resistida pode usar provisoriamente a conversão estudada.
A ficha achatada já oferece **Consequência** para o dano causado e **Limiar de Efetividade** para a resistência do constructo. O que permanece pendente é calibrar esses valores contra as paradas originais de dano e soak, além de traduzir contramágika quando necessário.

### Gate

**PASSA como classificação e compressão informacional.**

**NÃO está mecanicamente fechado para combate player-faced completo.**

---

## 10. Maravilhas e dispositivos

Maravilhas exigem ainda outra distinção.

Um Talismã ou Dispositivo pode ser simultaneamente:

* um objeto físico;
* uma reserva de Quintessência;
* uma fonte própria de Arete/Iluminação;
* um conjunto de Efeitos mágickos.

Portanto, “destruir o objeto” e “usar o poder do item” são problemas diferentes.

A parte física pode usar Durability + Structure quando aplicável.
A ativação continua usando Arete/Iluminação, Quintessência, Esferas e Paradoxo conforme as regras próprias.

Isso confirma novamente que Obstáculo é uma linguagem de organização, não um molde mecânico único.

---

## 11. Gate do Estudo 12

O capítulo cumpre sua proposta quando consegue classificar corretamente:

* **objeto/estrutura** → Durability + Structure;
* **sistema ativo** → procedimentos técnicos, estados e gatilhos;
* **constructo-agente** → protocolo de NPC;
* **dispositivo mágicko/hipertecnológico** → objeto físico + subsistema mágico próprio;
* **veículo** → aguarda tradução específica de veículos.

A principal contribuição deste domínio é mostrar um caso em que a filosofia “tudo é Obstáculo” se conecta diretamente a uma mecânica já existente em M20.

A melhor simplificação para muitos objetos não é convertê-los.

É **reconhecer que M20 já os modela de modo quase player-facing e colocar essa regra dentro da gramática geral de Obstáculos.**
