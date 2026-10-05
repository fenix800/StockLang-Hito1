# Generated from /workspace/scratch/8b3f85e848a7/stocklang_hito1/grammar/StockLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .StockLangParser import StockLangParser
else:
    from StockLangParser import StockLangParser

# This class defines a complete generic visitor for a parse tree produced by StockLangParser.

class StockLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by StockLangParser#programa.
    def visitPrograma(self, ctx:StockLangParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StockLangParser#declaracion.
    def visitDeclaracion(self, ctx:StockLangParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StockLangParser#instruccion.
    def visitInstruccion(self, ctx:StockLangParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StockLangParser#movimiento.
    def visitMovimiento(self, ctx:StockLangParser.MovimientoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StockLangParser#tipoMovimiento.
    def visitTipoMovimiento(self, ctx:StockLangParser.TipoMovimientoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StockLangParser#ajuste.
    def visitAjuste(self, ctx:StockLangParser.AjusteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StockLangParser#consulta.
    def visitConsulta(self, ctx:StockLangParser.ConsultaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StockLangParser#condicional.
    def visitCondicional(self, ctx:StockLangParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StockLangParser#condicion.
    def visitCondicion(self, ctx:StockLangParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StockLangParser#comparador.
    def visitComparador(self, ctx:StockLangParser.ComparadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StockLangParser#bloque.
    def visitBloque(self, ctx:StockLangParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StockLangParser#expresion.
    def visitExpresion(self, ctx:StockLangParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StockLangParser#termino.
    def visitTermino(self, ctx:StockLangParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StockLangParser#factor.
    def visitFactor(self, ctx:StockLangParser.FactorContext):
        return self.visitChildren(ctx)



del StockLangParser