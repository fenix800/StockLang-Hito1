"""Semántica estática determinista. Todas las ramas se validan.

El lenguaje no tiene entradas externas ni ciclos: el valor de cada expresión
es conocido. Las ramas reciben copias del estado de entrada; solo el estado
de la rama elegida se propaga. Un error nunca modifica el estado válido.
"""
from dataclasses import dataclass
from generated.StockLangVisitor import StockLangVisitor
from src.diagnostics import Diagnostic

MAX_STOCK = 2**31 - 1
MIN_INT = -(2**31)

@dataclass(frozen=True)
class ProductSymbol:
    name: str
    initial_stock: int
    line: int

class SemanticAnalyzer(StockLangVisitor):
    def __init__(self):
        self.symbols = {}
        self.values = {}
        self.diagnostics = []

    def _error(self, token, code, message):
        self.diagnostics.append(Diagnostic('SEMANTICO', code, token.line,
                                           token.column + 1, message))

    def _require_product(self, node):
        token = node.getSymbol()
        if token.text not in self.symbols:
            self._error(token, 'E002', f"Producto '{token.text}' usado sin declarar.")
            return False
        return True

    def _bounded(self, value, token):
        if value is not None and not MIN_INT <= value <= MAX_STOCK:
            self._error(token, 'E007', 'Desbordamiento de entero de 32 bits.')
            return None
        return value

    def visitDeclaracion(self, ctx):
        token = ctx.ID().getSymbol()
        value = int(ctx.NUMERO().getText())
        if token.text in self.symbols:
            self._error(token, 'E001', f"Producto '{token.text}' duplicado; primera declaración en línea {self.symbols[token.text].line}.")
            return
        self.symbols[token.text] = ProductSymbol(token.text, value, token.line)
        if value > MAX_STOCK:
            self._error(ctx.NUMERO().getSymbol(), 'E003', f'Stock inicial fuera de [0, {MAX_STOCK}].')
            self.values[token.text] = None
        else:
            self.values[token.text] = value

    def visitMovimiento(self, ctx):
        exists = self._require_product(ctx.ID())
        amount = self.visit(ctx.expresion())
        if amount is None:
            return
        if amount <= 0:
            self._error(ctx.expresion().start, 'E004', 'La cantidad del movimiento debe ser mayor que cero.')
            return
        if not exists:
            return
        name = ctx.ID().getText()
        old = self.values[name]
        if old is None:
            return
        if ctx.tipoMovimiento().SALIDA():
            if amount > old:
                self._error(ctx.ID().getSymbol(), 'E006', f"Stock insuficiente en '{name}': disponible {old}, retiro {amount}.")
                return
            new = old - amount
        else:
            new = self._bounded(old + amount, ctx.ID().getSymbol())
        if new is not None:
            self.values[name] = new

    def visitAjuste(self, ctx):
        exists = self._require_product(ctx.ID())
        value = self.visit(ctx.expresion())
        if value is not None and value < 0:
            self._error(ctx.expresion().start, 'E005', 'El ajuste no puede dejar stock negativo.')
        elif exists and value is not None:
            self.values[ctx.ID().getText()] = value

    def visitConsulta(self, ctx):
        self._require_product(ctx.ID())

    def visitCondicion(self, ctx):
        left, right = [self.visit(e) for e in ctx.expresion()]
        if left is None or right is None:
            return None
        op = ctx.comparador().getText()
        return {'<':left < right, '<=':left <= right, '>':left > right,
                '>=':left >= right, '==':left == right, '!=':left != right}[op]

    def visitCondicional(self, ctx):
        condition = self.visit(ctx.condicion())
        entry = self.values.copy()
        self.visit(ctx.bloque(0))
        then_values = self.values.copy()
        self.values = entry.copy()
        if len(ctx.bloque()) == 2:
            self.visit(ctx.bloque(1))
        else_values = self.values.copy()
        # La rama inactiva también se verifica, pero no altera el flujo posterior.
        self.values = then_values if condition is True else else_values if condition is False else entry

    def visitExpresion(self, ctx):
        if ctx.expresion() is None:
            return self.visit(ctx.termino())
        left, right = self.visit(ctx.expresion()), self.visit(ctx.termino())
        if left is None or right is None:
            return None
        return self._bounded(left + right if ctx.SUMA() else left - right,
                             ctx.SUMA().getSymbol() if ctx.SUMA() else ctx.RESTA().getSymbol())

    def visitTermino(self, ctx):
        if ctx.termino() is None:
            return self.visit(ctx.factor())
        left, right = self.visit(ctx.termino()), self.visit(ctx.factor())
        if left is None or right is None:
            return None
        return self._bounded(left * right, ctx.MULTIPLICAR().getSymbol())

    def visitFactor(self, ctx):
        if ctx.NUMERO():
            return self._bounded(int(ctx.NUMERO().getText()), ctx.NUMERO().getSymbol())
        if ctx.ID():
            return self.values[ctx.ID().getText()] if self._require_product(ctx.ID()) else None
        return self.visit(ctx.expresion())
