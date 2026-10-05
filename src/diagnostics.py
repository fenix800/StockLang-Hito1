from dataclasses import dataclass

from antlr4.error.ErrorListener import ErrorListener


@dataclass(frozen=True)
class Diagnostic:
    phase: str
    code: str
    line: int
    column: int
    message: str

    def __str__(self):
        return f"{self.phase} {self.code} [{self.line}:{self.column}] {self.message}"


class CollectingErrorListener(ErrorListener):
    """Guarda errores sin imprimirlos ni considerarlos análisis exitosos."""

    def __init__(self, phase):
        super().__init__()
        self.phase = phase
        self.diagnostics = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        code = "L001" if self.phase == "LEXICO" else "S001"
        self.diagnostics.append(
            Diagnostic(self.phase, code, line, column + 1, msg)
        )
