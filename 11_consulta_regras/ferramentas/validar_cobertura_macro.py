#!/usr/bin/env python3
"""Verifica partição do acervo em consultas macro e fragmentos residuais classificados."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "11_consulta_regras"

def main() -> int:
    manifest = json.loads((DIR / "manifesto.json").read_text(encoding="utf-8"))
    audit = json.loads((DIR / "auditoria/classificacao_residual_macro.json").read_text(encoding="utf-8"))
    segment_ids = [s["id"] for s in manifest["segments"]]
    source_ids = [s["key"] for s in manifest["baseline_sources"]]
    assert len(segment_ids) == len(set(segment_ids)), "Identificadores de segmentos repetidos"
    assert len(source_ids) == len(set(source_ids)), "Identificadores de fontes repetidos"

    used = {
        sid for view in manifest["views"] for group in view["groups"]
        for sid in group["parts"]
    }
    leftovers = {entry["id"] for entry in audit["classification"]}
    assert not used & leftovers, "Segmentos simultaneamente publicados e classificados como residuais"
    assert used | leftovers == set(segment_ids), "Segmentos não rastreados ou inexistentes na classificação"
    assert all(entry["source"] and entry["reason"] and entry["status"]
               for entry in audit["classification"]), "Classificação residual incompleta"
    assert audit["published_unique_segment_count"] == len(used)
    assert audit["not_published_count"] == len(leftovers)
    assert audit["segmented_count"] == len(segment_ids)
    assert audit["source_count"] == len(source_ids)

    views = [v["path"] for v in manifest["views"]]
    assert len(views) == len(set(views)) == 24, "Quantidade ou caminhos de macroconsultas inesperados"
    index = (DIR / "valores/readme.md").read_text(encoding="utf-8")
    for path in views:
        assert (ROOT / path).is_file(), ("Vista sem arquivo", path)
        relative = Path(path).relative_to(DIR / "valores").as_posix()
        assert re.search(r"\]\(" + re.escape(relative) + r"\)", index), ("Vista não indexada", path)

    original_sources = {s["path"] for s in manifest["baseline_sources"]}
    assert all((ROOT / path).is_file() for path in original_sources), "Fonte original ausente"
    assert all(entry["source"] in original_sources for entry in audit["classification"])
    visible = set(views)
    published_files = {
        p.relative_to(ROOT).as_posix()
        for d in [DIR / "consultas", DIR / "valores"]
        for p in d.rglob("*.md") if p.is_file() and p.name.lower() != "readme.md"
        and not p.is_symlink()
    }
    assert published_files == visible, (
        "Arquivos de consulta não registrados no manifesto ou ausentes",
        sorted(published_files - visible), sorted(visible - published_files)
    )
    print(f"PASS: {len(source_ids)} fontes; {len(segment_ids)} segmentos;"
          f" {len(used)} publicados; {len(leftovers)} classificados;"
          f" {len(views)} consultas macro; nenhuma consulta individual avulsa")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
