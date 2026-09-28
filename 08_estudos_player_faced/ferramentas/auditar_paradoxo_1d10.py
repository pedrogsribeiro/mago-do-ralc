#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Auditoria exata: Reação de Paradoxo M20 -> proposta player-faced em 1d10.

OBJETIVO
-------
Comparar a matemática da regra original consolidada no repositório com uma
compressão operacional para uma escala 1..10 e uma única rolagem de d10.

Este script NÃO homologa regra alguma. Ele serve para diagnóstico.

BASELINE M20 USADO
------------------
- Reserva original de Paradoxo: 5..40.
- Reação original: rolar P d10 em Dificuldade 6.
- 6..10 = sucesso; 1 cancela um sucesso; 2..5 = neutro.
- sucessos líquidos <= 0 são tratados como 0 sucessos para esta auditoria.
- faixas:
    0       -> sem descarga
    1..5    -> C + Defeito Trivial; descarrega 1 Paradoxo por sucesso
    6..10   -> C + Defeito Pequeno; descarrega 1 Paradoxo por sucesso
    11..15  -> L OU Defeito Significativo OU Espírito OU Quiet moderado;
               descarrega toda a reserva
    16..20  -> L + 1 Paradoxo Permanente + Defeito Grave/Espírito/Banimento;
               descarrega toda a reserva
    21+     -> A + 2 Paradoxos Permanentes + Defeito Drástico/Banimento;
               descarrega toda a reserva

MODELO PLAYER-FACED TESTADO
---------------------------
Compressão linear:
    C = ceil(P / 4), limitada a 1..10

Gatilho já decidido no projeto:
    rola 1d10
    resultado <= C -> Reação dispara
    resultado > C  -> não dispara

Como ainda NÃO foi homologada a severidade, o script calcula:
1. distribuição exata da regra original;
2. erro introduzido apenas pelo novo gatilho;
3. a MELHOR tabela de severidade possível sob a restrição desse único d10,
   preservando ordem monotônica: resultados menores podem ser mais graves;
4. dano/descarga originais esperados por faixa, para ajudar a propor
   números fixos depois sem inventá-los.

IMPORTANTE
----------
As alternativas qualitativas (Defeito, Espírito, Quiet, banimento) são escolhas
do Storyteller na regra consolidada, não eventos com probabilidades próprias.
Logo, o script audita a probabilidade da FAIXA DE GRAVIDADE, mas não inventa
probabilidade para cada alternativa dentro da faixa.

Uso:
    python 08_estudos_player_faced/ferramentas/auditar_paradoxo_1d10.py

Salvar relatório:
    python 08_estudos_player_faced/ferramentas/auditar_paradoxo_1d10.py --output RELATORIO_PARADOXO.txt

CSV detalhado:
    python 08_estudos_player_faced/ferramentas/auditar_paradoxo_1d10.py --csv paradoxo_detalhado.csv
"""

from __future__ import annotations

import argparse
import csv
import math
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple


BANDS = (
    "0_sem_reacao",
    "1_5_menor",
    "6_10_forte",
    "11_15_grave",
    "16_20_extrema",
    "21mais_catastrofica",
)

BAND_LABEL = {
    "0_sem_reacao": "0: sem reação",
    "1_5_menor": "1–5: C + Defeito Trivial",
    "6_10_forte": "6–10: C + Defeito Pequeno",
    "11_15_grave": "11–15: L OU Defeito Significativo/Espírito/Quiet",
    "16_20_extrema": "16–20: L + 1 PP + Grave/Espírito/Banimento",
    "21mais_catastrofica": "21+: A + 2 PP + Drástico/Banimento",
}


@dataclass(frozen=True)
class OriginalStats:
    paradox: int
    distribution_net: Dict[int, float]
    band_probs: Dict[str, float]
    trigger_prob: float
    mean_net_successes: float
    mean_discharge: float
    mean_bashing_levels: float
    mean_damage_dice_if_high_band: float


def band_for_successes(successes: int) -> str:
    if successes <= 0:
        return "0_sem_reacao"
    if successes <= 5:
        return "1_5_menor"
    if successes <= 10:
        return "6_10_forte"
    if successes <= 15:
        return "11_15_grave"
    if successes <= 20:
        return "16_20_extrema"
    return "21mais_catastrofica"


def compressed_paradox(p: int) -> int:
    """Compressão linear 40 -> 10: ceil(P/4)."""
    return max(1, min(10, math.ceil(p / 4)))


def exact_net_distribution(n_dice: int) -> Dict[int, float]:
    """
    Distribuição exata dos sucessos líquidos em d10 D6:
      +1 para 6..10 (p=0.5)
      -1 para 1     (p=0.1)
       0 para 2..5  (p=0.4)

    Faz convolução dinâmica; não usa Monte Carlo nem dependências externas.
    """
    dist = {0: 1.0}
    steps = ((1, 0.5), (-1, 0.1), (0, 0.4))

    for _ in range(n_dice):
        nxt = defaultdict(float)
        for total, prob in dist.items():
            for delta, p_delta in steps:
                nxt[total + delta] += prob * p_delta
        dist = dict(nxt)

    return dist


def original_stats(p: int) -> OriginalStats:
    dist_raw = exact_net_distribution(p)

    # Para a reação, resultados <= 0 não produzem sucessos de descarga.
    dist = defaultdict(float)
    for net, prob in dist_raw.items():
        dist[max(0, net)] += prob
    dist = dict(sorted(dist.items()))

    band_probs = {band: 0.0 for band in BANDS}
    mean_net = 0.0
    mean_discharge = 0.0
    mean_bashing = 0.0
    mean_high_damage_dice = 0.0

    for successes, prob in dist.items():
        band = band_for_successes(successes)
        band_probs[band] += prob
        mean_net += successes * prob

        if successes <= 0:
            discharge = 0
        elif successes <= 10:
            discharge = min(successes, p)
        else:
            discharge = p

        mean_discharge += discharge * prob

        # Faixas 1..10 causam níveis C fixos iguais aos sucessos.
        if 1 <= successes <= 10:
            mean_bashing += successes * prob

        # Faixas 11+ usam pool de dano igual aos sucessos quando a opção dano se aplica.
        if successes >= 11:
            mean_high_damage_dice += successes * prob

    return OriginalStats(
        paradox=p,
        distribution_net=dist,
        band_probs=band_probs,
        trigger_prob=1.0 - band_probs["0_sem_reacao"],
        mean_net_successes=mean_net,
        mean_discharge=mean_discharge,
        mean_bashing_levels=mean_bashing,
        mean_damage_dice_if_high_band=mean_high_damage_dice,
    )


def mean_dict(dicts: Iterable[Dict[str, float]], keys: Iterable[str]) -> Dict[str, float]:
    rows = list(dicts)
    if not rows:
        return {k: 0.0 for k in keys}
    return {k: sum(row[k] for row in rows) / len(rows) for k in keys}


def bucket_original_stats(stats: List[OriginalStats]) -> Dict[int, dict]:
    buckets: Dict[int, List[OriginalStats]] = defaultdict(list)
    for st in stats:
        buckets[compressed_paradox(st.paradox)].append(st)

    out = {}
    for c, rows in sorted(buckets.items()):
        out[c] = {
            "p_min": min(x.paradox for x in rows),
            "p_max": max(x.paradox for x in rows),
            "trigger_prob": sum(x.trigger_prob for x in rows) / len(rows),
            "mean_net_successes": sum(x.mean_net_successes for x in rows) / len(rows),
            "mean_discharge": sum(x.mean_discharge for x in rows) / len(rows),
            "band_probs": mean_dict((x.band_probs for x in rows), BANDS),
        }
    return out


def largest_remainder_counts(probabilities: Dict[str, float], total_slots: int) -> Dict[str, int]:
    """
    Converte probabilidades condicionais em contagens inteiras de faces,
    preservando soma total_slots pelo método dos maiores restos.
    """
    if total_slots <= 0:
        return {b: 0 for b in BANDS[1:]}

    active = list(BANDS[1:])
    s = sum(probabilities.get(b, 0.0) for b in active)
    if s <= 0:
        # Se não houver massa original de reação, põe tudo na faixa menor.
        out = {b: 0 for b in active}
        out[active[0]] = total_slots
        return out

    exact = {b: total_slots * probabilities.get(b, 0.0) / s for b in active}
    floors = {b: int(math.floor(v)) for b, v in exact.items()}
    left = total_slots - sum(floors.values())

    order = sorted(
        active,
        key=lambda b: (exact[b] - floors[b], probabilities.get(b, 0.0)),
        reverse=True,
    )
    for b in order[:left]:
        floors[b] += 1
    return floors


def monotonic_face_table(c: int, target_band_probs: Dict[str, float]) -> Dict[int, str]:
    """
    Sob o gatilho r<=C, distribui as C faces que disparam entre as faixas
    de gravidade conforme a distribuição ORIGINAL condicionada a haver reação.

    Ordem monotônica:
      r=1 é reservado para o resultado mais grave presente;
      r=C para o menos grave.
    """
    counts = largest_remainder_counts(target_band_probs, c)
    severity_desc = [
        "21mais_catastrofica",
        "16_20_extrema",
        "11_15_grave",
        "6_10_forte",
        "1_5_menor",
    ]

    faces: Dict[int, str] = {}
    r = 1
    for band in severity_desc:
        for _ in range(counts[band]):
            if r <= c:
                faces[r] = band
                r += 1

    while r <= c:
        faces[r] = "1_5_menor"
        r += 1

    for face in range(c + 1, 11):
        faces[face] = "0_sem_reacao"

    return faces


def simplified_probs(face_table: Dict[int, str]) -> Dict[str, float]:
    probs = {b: 0.0 for b in BANDS}
    for face in range(1, 11):
        probs[face_table[face]] += 0.1
    return probs


def total_variation(a: Dict[str, float], b: Dict[str, float]) -> float:
    return 0.5 * sum(abs(a[k] - b[k]) for k in BANDS)


def weighted_abs_band_error(a: Dict[str, float], b: Dict[str, float]) -> float:
    """
    Erro absoluto simples em pontos percentuais somados.
    Útil como leitura complementar à TV.
    """
    return sum(abs(a[k] - b[k]) for k in BANDS)


def pct(x: float) -> str:
    return f"{100*x:6.2f}%"


def fnum(x: float) -> str:
    return f"{x:6.3f}"


def row_band_short(probs: Dict[str, float]) -> str:
    return " | ".join(
        [
            f"0={pct(probs['0_sem_reacao'])}",
            f"1-5={pct(probs['1_5_menor'])}",
            f"6-10={pct(probs['6_10_forte'])}",
            f"11-15={pct(probs['11_15_grave'])}",
            f"16-20={pct(probs['16_20_extrema'])}",
            f"21+={pct(probs['21mais_catastrofica'])}",
        ]
    )


def face_table_text(c: int, table: Dict[int, str]) -> str:
    parts = []
    for r in range(1, 11):
        band = table[r]
        if band == "0_sem_reacao":
            label = "—"
        elif band == "1_5_menor":
            label = "MENOR"
        elif band == "6_10_forte":
            label = "FORTE"
        elif band == "11_15_grave":
            label = "GRAVE"
        elif band == "16_20_extrema":
            label = "EXTREMA"
        else:
            label = "CATASTR."
        parts.append(f"{r}:{label}")
    return " ".join(parts)


def build_report(min_p: int = 5, max_p: int = 40) -> Tuple[str, List[dict]]:
    stats = [original_stats(p) for p in range(min_p, max_p + 1)]
    buckets = bucket_original_stats(stats)

    lines: List[str] = []
    csv_rows: List[dict] = []

    lines.append("=" * 88)
    lines.append("AUDITORIA EXATA — PARADOXO M20 -> 1d10 PLAYER-FACED")
    lines.append("=" * 88)
    lines.append("")
    lines.append("Premissas:")
    lines.append("- Original: P d10, D6; 6–10 sucesso; 1 cancela sucesso.")
    lines.append("- Reação original classificada pelas faixas 0 / 1–5 / 6–10 / 11–15 / 16–20 / 21+.")
    lines.append("- Compressão testada: C = ceil(P/4), de 1 a 10.")
    lines.append("- Gatilho player-faced: 1d10 <= C.")
    lines.append("- Severidade player-faced abaixo é DIAGNÓSTICA: melhor aproximação por faces do mesmo d10,")
    lines.append("  condicionada à reação, sem homologar números ou consequências.")
    lines.append("")

    lines.append("1) BASELINE ORIGINAL POR RESERVA")
    lines.append("-" * 88)
    lines.append("P  C  P(reação)  E[sucessos]  E[descarga]   distribuição de gravidade")
    for st in stats:
        c = compressed_paradox(st.paradox)
        lines.append(
            f"{st.paradox:2d} {c:2d}  {pct(st.trigger_prob)}   "
            f"{fnum(st.mean_net_successes)}      {fnum(st.mean_discharge)}    "
            f"{row_band_short(st.band_probs)}"
        )

    lines.append("")
    lines.append("2) AGREGAÇÃO POR PARADOXO COMPRIMIDO (C)")
    lines.append("-" * 88)
    lines.append(
        "Mostra o que, em média, os 4 valores originais de cada degrau faziam antes da compressão."
    )

    total_tv = []
    trigger_errors = []

    for c, bucket in buckets.items():
        target = bucket["band_probs"]
        faces = monotonic_face_table(c, target)
        simp = simplified_probs(faces)
        tv = total_variation(target, simp)
        trigger_new = c / 10.0
        trigger_err = trigger_new - bucket["trigger_prob"]
        total_tv.append(tv)
        trigger_errors.append(abs(trigger_err))

        lines.append("")
        lines.append(
            f"C={c}  <- P original {bucket['p_min']}–{bucket['p_max']} | "
            f"reação original média {pct(bucket['trigger_prob'])} | "
            f"1d10<=C {pct(trigger_new)} | erro {trigger_err*100:+.2f} pp"
        )
        lines.append(
            f"    E[sucessos orig.]={bucket['mean_net_successes']:.3f} | "
            f"E[descarga orig.]={bucket['mean_discharge']:.3f}"
        )
        lines.append("    Original:   " + row_band_short(target))
        lines.append("    Melhor 1d10:" + row_band_short(simp))
        lines.append(f"    TV={tv:.4f} | faces: {face_table_text(c, faces)}")

        for r in range(1, 11):
            csv_rows.append(
                {
                    "paradoxo_comprimido": c,
                    "p_original_min": bucket["p_min"],
                    "p_original_max": bucket["p_max"],
                    "face_d10": r,
                    "resultado_simplificado": faces[r],
                    "prob_reacao_original_media": bucket["trigger_prob"],
                    "prob_reacao_1d10": trigger_new,
                    "tv_bucket": tv,
                    "sucessos_originais_medios": bucket["mean_net_successes"],
                    "descarga_original_media": bucket["mean_discharge"],
                }
            )

    lines.append("")
    lines.append("3) ERRO IRREDUTÍVEL DO GATILHO LINEAR")
    lines.append("-" * 88)
    lines.append(
        "Como r<=C fixa a chance de reação em C*10%, parte do erro existe ANTES de escolher a severidade."
    )
    lines.append(
        f"Erro absoluto médio da chance de reação: "
        f"{100 * sum(trigger_errors)/len(trigger_errors):.2f} pontos percentuais."
    )
    lines.append(
        f"TV média da melhor tabela de faixas sob esse gatilho: "
        f"{sum(total_tv)/len(total_tv):.4f}."
    )
    lines.append("")

    lines.append("4) CONSEQUÊNCIAS CANÔNICAS QUE A TRADUÇÃO PRECISA PRESERVAR")
    lines.append("-" * 88)
    for band in BANDS[1:]:
        lines.append(f"- {BAND_LABEL[band]}")
    lines.append("")
    lines.append(
        "Observação: nas faixas 11+ o dano é uma opção/parte da consequência conforme a faixa; "
        "Defeito, Espírito, Quiet e banimento não recebem probabilidades artificiais neste teste."
    )

    lines.append("")
    lines.append("5) LEITURA PARA A PRÓXIMA DECISÃO")
    lines.append("-" * 88)
    lines.append(
        "Se o erro do gatilho 1d10<=C for aceitável, a tabela de faces acima mostra a melhor "
        "aproximação discreta de severidade que cabe no MESMO d10 sob a compressão linear."
    )
    lines.append(
        "Se o erro do gatilho for alto demais, o problema não está nas faixas de dano/Quiet/Defeitos; "
        "está na transformação 40->10 + chance C/10. Nesse caso vale comparar uma compressão "
        "não linear antes de mexer nas consequências."
    )
    lines.append(
        "Não homologue a tabela de faces só pelo relatório: ela é uma candidata matemática para "
        "playtest e ainda precisa ser julgada por ergonomia e legibilidade."
    )

    return "\n".join(lines), csv_rows


def write_csv(path: str, rows: List[dict]) -> None:
    if not rows:
        return
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audita a compressão da Reação de Paradoxo M20 para 1d10."
    )
    parser.add_argument(
        "--output",
        help="Salva o relatório textual neste arquivo além de imprimir no terminal.",
    )
    parser.add_argument(
        "--csv",
        help="Salva a tabela detalhada das faces do d10 em CSV.",
    )
    parser.add_argument("--min", type=int, default=5, dest="min_p")
    parser.add_argument("--max", type=int, default=40, dest="max_p")
    args = parser.parse_args()

    if args.min_p < 1 or args.max_p < args.min_p:
        raise SystemExit("Intervalo de Paradoxo inválido.")

    report, rows = build_report(args.min_p, args.max_p)
    print(report)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report)
            f.write("\n")
        print(f"\nRelatório salvo em: {args.output}")

    if args.csv:
        write_csv(args.csv, rows)
        print(f"CSV salvo em: {args.csv}")


if __name__ == "__main__":
    main()
