from dataclasses import dataclass

from generated.StockLangVisitor import StockLangVisitor
from src.diagnostics import Diagnostic


@dataclass(frozen=True)
class ProductSymbol:
    name: str
    initial_stock: int
    line: int


class SemanticAnalyzer(StockLangVisitor):
    """Dos controles estáticos. No interpreta ni modifica el inventario."""

    def __init__(self):
        self.symbols = {}
        self.diagnostics = []

    def _error(self, token, code, message):
        self.diagnostics.append(
            Diagnostic("SEMANTICO", code, token.line, token.column + 1, message)
        )

    def _require_product(self, node):
        token = node.getSymbol()
        if token.text not in self.symbols:
            self._error(
                token, "E002", f"Producto '{token.text}' usado sin declarar."
            )

    def visitDeclaracion(self, ctx):
        token = ctx.ID().getSymbol()
        if token.text in self.symbols:
            first = self.symbols[token.text]
            self._error(
                token, "E001",
                f"Producto '{token.text}' duplicado; primera declaración "
                f"en línea {first.line}."
            )
        else:
            self.symbols[token.text] = ProductSymbol(
                token.text, int(ctx.NUMERO().getText()), token.line
            )

    def visitMovimiento(self, ctx):
        self._require_product(ctx.ID())
        self.visit(ctx.expresion())

    def visitAjuste(self, ctx):
        self._require_product(ctx.ID())
        self.visit(ctx.expresion())

    def visitConsulta(self, ctx):
        self._require_product(ctx.ID())

    def visitFactor(self, ctx):
        if ctx.ID() is not None:
            self._require_product(ctx.ID())
        else:
            return self.visitChildren(ctx)

    # visitChildren recorre condiciones y bloques, incluso si están anidados.
