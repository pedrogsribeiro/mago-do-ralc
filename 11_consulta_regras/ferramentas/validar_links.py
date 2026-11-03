#!/usr/bin/env python3
"""Valida links Markdown da interface de consulta (sem alterar arquivos)."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
CONSULTAS = ROOT / "11_consulta_regras"
IGNORE = {"corpus", "corpus_integral", "auditoria", "_execucao_temporaria", "ferramentas"}
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")

def main() -> int:
    files = sorted(
        p for p in CONSULTAS.rglob("*.md")
        if not p.is_symlink() and not any(part in IGNORE for part in p.relative_to(CONSULTAS).parts)
    )
    checked = 0
    problems = []
    for doc in files:
        body = doc.read_text(encoding="utf-8")
        for match in LINK.finditer(body):
            raw = match.group(1).strip().split(" \"", 1)[0].strip("<>")
            if not raw or raw.startswith("#") or raw.startswith(("file:", "mailto:", "//")):
                continue
            target_url = urlsplit(raw)
            if target_url.scheme:
                continue
            relative = unquote(target_url.path)
            if not relative:
                continue
            dest = (doc.parent / relative).resolve()
            checked += 1
            if not dest.is_relative_to(ROOT.resolve()) or not dest.exists():
                problems.append(f"{doc.relative_to(ROOT)}: {raw} -> destino inexistente")
    for problem in problems:
        print("FAIL:", problem)
    print(f"Verificados {checked} links em {len(files)} arquivos; falhas: {len(problems)}.")
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main())
