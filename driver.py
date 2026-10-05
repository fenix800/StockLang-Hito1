"""Driver del hito 1. Ejecutar desde la raíz del proyecto."""

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

from src.compiler import analyze


def main():
    parser = argparse.ArgumentParser(description="Front end de StockLang (ANTLR4)")
    parser.add_argument("file", type=Path, help="archivo .stock en UTF-8")
    parser.add_argument("--stage", choices=["lex", "syntax", "semantic"], default="semantic")
    parser.add_argument("--tokens", action="store_true", help="mostrar tokens")
    parser.add_argument("--tree", action="store_true", help="mostrar árbol sintáctico")
    parser.add_argument("--json", action="store_true", help="salida estructurada")
    args = parser.parse_args()
    try:
        source = args.file.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        print(f"No se puede leer el archivo: {exc}", file=sys.stderr)
        return 2
    result = analyze(source, stage=args.stage)
    if args.json:
        payload = asdict(result)
        payload["ok"] = result.ok
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        if args.tokens:
            for token in result.tokens:
                print(f"{token['line']}:{token['column']} "
                      f"{token['type']:<14} {token['lexeme']!r}")
        if args.tree and result.tree is not None:
            print("ÁRBOL SINTÁCTICO:")
            print(result.tree)
        if result.diagnostics:
            for diagnostic in result.diagnostics:
                print(diagnostic)
            print(f"ANÁLISIS RECHAZADO: {len(result.diagnostics)} error(es).")
        else:
            labels = {"lex": "léxico", "syntax": "sintáctico", "semantic": "semántico inicial"}
            print(f"ANÁLISIS CORRECTO: {labels[args.stage]}.")
            if args.stage == "semantic":
                print("TABLA DE SÍMBOLOS (stock declarado, sin ejecutar movimientos):")
                for symbol in result.symbols.values():
                    print(f"  {symbol.name}: entero, stock_inicial={symbol.initial_stock}, "
                          f"línea={symbol.line}")
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
