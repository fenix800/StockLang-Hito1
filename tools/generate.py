"""Regenerar los reconocedores usando el JAR oficial, sin antlr4-tools."""

import argparse
from pathlib import Path
import subprocess


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("jar", type=Path, help="ruta a antlr-4.13.2-complete.jar")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    jar = args.jar.resolve()
    if not jar.is_file():
        parser.error(f"No existe el JAR: {jar}")
    subprocess.run([
        "java", "-jar", str(jar), "-Dlanguage=Python3", "-visitor",
        "-no-listener", "-Xexact-output-dir", "-o", str(root / "generated"),
        str(root / "grammar" / "StockLang.g4"),
    ], check=True)
    print("Reconocedores regenerados en generated/.")


if __name__ == "__main__":
    main()
