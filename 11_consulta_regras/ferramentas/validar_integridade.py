#!/usr/bin/env python3
"""Verifica integridade literal do piloto; apenas leitura, nenhuma correção automática."""
from __future__ import annotations
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "11_consulta_regras" / "manifesto.json"

def git_blob_sha(blob: bytes) -> str:
    header = ("blob " + str(len(blob)) + "\0").encode()
    return hashlib.sha1(header + blob).hexdigest()

def main() -> int:
    m = json.loads(MANIFEST.read_text(encoding="utf-8"))
    pieces = {}
    source_count = 0
    for src in m["baseline_sources"]:
        raw = (ROOT / src["path"]).read_bytes()
        got_sha = git_blob_sha(raw)
        assert got_sha == src["git_blob_sha"], (src["path"], "BLOB_ORIGINAL_ALTERADO", got_sha)
        source_lines = raw.splitlines(keepends=True)
        parts = []
        for seg_id in src["segment_ids"]:
            seg = next(x for x in m["segments"] if x["id"] == seg_id)
            content = (ROOT / seg["path"]).read_bytes()
            expected = b"".join(source_lines[seg["start_line"]-1:seg["end_line"]])
            assert content == expected, (seg_id, "BLOCO_DIFERENTE_DO_ORIGINAL")
            pieces[seg_id] = content.decode("utf-8")
            parts.append(content)
        assert b"".join(parts) == raw, (src["path"], "RECONSTRUCAO_NAO_IDENTICA")
        source_count += 1
    for view in m["views"]:
        expected = view["prefix"]
        for group in view["groups"]:
            expected += group["prefix"] + "".join(pieces[k] for k in group["parts"]) + group["suffix"]
        expected += view["suffix"]
        actual = (ROOT / view["path"]).read_bytes()
        assert actual == expected.encode("utf-8"), (view["path"], "CONSULTA_MODIFICADA")
    print("PASS: %d fontes inalteradas, %d blocos íntegros e %d consultas reproduzíveis" % (source_count, len(pieces), len(m["views"])))
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AssertionError, OSError, ValueError, KeyError) as err:
        print("FAIL: %s" % (err,), file=sys.stderr)
        sys.exit(1)
