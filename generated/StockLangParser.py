# Generated from /workspace/scratch/bc304d303e56/output/StockLang_Hito2/grammar/StockLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,27,122,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,4,0,30,8,0,11,0,12,0,31,1,0,5,0,35,8,0,10,0,12,0,38,9,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,3,2,52,8,2,1,3,1,3,1,
        3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,
        7,1,7,1,7,1,7,3,7,76,8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,10,1,10,4,10,
        86,8,10,11,10,12,10,87,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,5,
        11,98,8,11,10,11,12,11,101,9,11,1,12,1,12,1,12,1,12,1,12,1,12,5,
        12,109,8,12,10,12,12,12,112,9,12,1,13,1,13,1,13,1,13,1,13,1,13,3,
        13,120,8,13,1,13,0,2,22,24,14,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,0,3,1,0,3,4,1,0,9,14,1,0,16,17,118,0,29,1,0,0,0,2,41,1,0,0,0,
        4,51,1,0,0,0,6,53,1,0,0,0,8,58,1,0,0,0,10,60,1,0,0,0,12,66,1,0,0,
        0,14,70,1,0,0,0,16,77,1,0,0,0,18,81,1,0,0,0,20,83,1,0,0,0,22,91,
        1,0,0,0,24,102,1,0,0,0,26,119,1,0,0,0,28,30,3,2,1,0,29,28,1,0,0,
        0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,36,1,0,0,0,33,35,
        3,4,2,0,34,33,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,
        37,39,1,0,0,0,38,36,1,0,0,0,39,40,5,0,0,1,40,1,1,0,0,0,41,42,5,1,
        0,0,42,43,5,25,0,0,43,44,5,2,0,0,44,45,5,24,0,0,45,46,5,19,0,0,46,
        3,1,0,0,0,47,52,3,6,3,0,48,52,3,10,5,0,49,52,3,12,6,0,50,52,3,14,
        7,0,51,47,1,0,0,0,51,48,1,0,0,0,51,49,1,0,0,0,51,50,1,0,0,0,52,5,
        1,0,0,0,53,54,3,8,4,0,54,55,5,25,0,0,55,56,3,22,11,0,56,57,5,19,
        0,0,57,7,1,0,0,0,58,59,7,0,0,0,59,9,1,0,0,0,60,61,5,5,0,0,61,62,
        5,25,0,0,62,63,5,15,0,0,63,64,3,22,11,0,64,65,5,19,0,0,65,11,1,0,
        0,0,66,67,5,6,0,0,67,68,5,25,0,0,68,69,5,19,0,0,69,13,1,0,0,0,70,
        71,5,7,0,0,71,72,3,16,8,0,72,75,3,20,10,0,73,74,5,8,0,0,74,76,3,
        20,10,0,75,73,1,0,0,0,75,76,1,0,0,0,76,15,1,0,0,0,77,78,3,22,11,
        0,78,79,3,18,9,0,79,80,3,22,11,0,80,17,1,0,0,0,81,82,7,1,0,0,82,
        19,1,0,0,0,83,85,5,20,0,0,84,86,3,4,2,0,85,84,1,0,0,0,86,87,1,0,
        0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,89,1,0,0,0,89,90,5,21,0,0,90,
        21,1,0,0,0,91,92,6,11,-1,0,92,93,3,24,12,0,93,99,1,0,0,0,94,95,10,
        2,0,0,95,96,7,2,0,0,96,98,3,24,12,0,97,94,1,0,0,0,98,101,1,0,0,0,
        99,97,1,0,0,0,99,100,1,0,0,0,100,23,1,0,0,0,101,99,1,0,0,0,102,103,
        6,12,-1,0,103,104,3,26,13,0,104,110,1,0,0,0,105,106,10,2,0,0,106,
        107,5,18,0,0,107,109,3,26,13,0,108,105,1,0,0,0,109,112,1,0,0,0,110,
        108,1,0,0,0,110,111,1,0,0,0,111,25,1,0,0,0,112,110,1,0,0,0,113,120,
        5,24,0,0,114,120,5,25,0,0,115,116,5,22,0,0,116,117,3,22,11,0,117,
        118,5,23,0,0,118,120,1,0,0,0,119,113,1,0,0,0,119,114,1,0,0,0,119,
        115,1,0,0,0,120,27,1,0,0,0,8,31,36,51,75,87,99,110,119
    ]

class StockLangParser ( Parser ):

    grammarFileName = "StockLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'producto'", "'stock'", "'entrada'", 
                     "'salida'", "'ajustar'", "'mostrar'", "'si'", "'sino'", 
                     "'<='", "'>='", "'=='", "'!='", "'<'", "'>'", "'='", 
                     "'+'", "'-'", "'*'", "';'", "'{'", "'}'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "PRODUCTO", "STOCK", "ENTRADA", "SALIDA", 
                      "AJUSTAR", "MOSTRAR", "SI", "SINO", "MENOR_IGUAL", 
                      "MAYOR_IGUAL", "IGUAL", "DISTINTO", "MENOR", "MAYOR", 
                      "ASIGNAR", "SUMA", "RESTA", "MULTIPLICAR", "PUNTO_COMA", 
                      "LLAVE_IZQ", "LLAVE_DER", "PAREN_IZQ", "PAREN_DER", 
                      "NUMERO", "ID", "COMENTARIO", "ESPACIO" ]

    RULE_programa = 0
    RULE_declaracion = 1
    RULE_instruccion = 2
    RULE_movimiento = 3
    RULE_tipoMovimiento = 4
    RULE_ajuste = 5
    RULE_consulta = 6
    RULE_condicional = 7
    RULE_condicion = 8
    RULE_comparador = 9
    RULE_bloque = 10
    RULE_expresion = 11
    RULE_termino = 12
    RULE_factor = 13

    ruleNames =  [ "programa", "declaracion", "instruccion", "movimiento", 
                   "tipoMovimiento", "ajuste", "consulta", "condicional", 
                   "condicion", "comparador", "bloque", "expresion", "termino", 
                   "factor" ]

    EOF = Token.EOF
    PRODUCTO=1
    STOCK=2
    ENTRADA=3
    SALIDA=4
    AJUSTAR=5
    MOSTRAR=6
    SI=7
    SINO=8
    MENOR_IGUAL=9
    MAYOR_IGUAL=10
    IGUAL=11
    DISTINTO=12
    MENOR=13
    MAYOR=14
    ASIGNAR=15
    SUMA=16
    RESTA=17
    MULTIPLICAR=18
    PUNTO_COMA=19
    LLAVE_IZQ=20
    LLAVE_DER=21
    PAREN_IZQ=22
    PAREN_DER=23
    NUMERO=24
    ID=25
    COMENTARIO=26
    ESPACIO=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(StockLangParser.EOF, 0)

        def declaracion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StockLangParser.DeclaracionContext)
            else:
                return self.getTypedRuleContext(StockLangParser.DeclaracionContext,i)


        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StockLangParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(StockLangParser.InstruccionContext,i)


        def getRuleIndex(self):
            return StockLangParser.RULE_programa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = StockLangParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.declaracion()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 248) != 0):
                self.state = 33
                self.instruccion()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(StockLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRODUCTO(self):
            return self.getToken(StockLangParser.PRODUCTO, 0)

        def ID(self):
            return self.getToken(StockLangParser.ID, 0)

        def STOCK(self):
            return self.getToken(StockLangParser.STOCK, 0)

        def NUMERO(self):
            return self.getToken(StockLangParser.NUMERO, 0)

        def PUNTO_COMA(self):
            return self.getToken(StockLangParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return StockLangParser.RULE_declaracion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = StockLangParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(StockLangParser.PRODUCTO)
            self.state = 42
            self.match(StockLangParser.ID)
            self.state = 43
            self.match(StockLangParser.STOCK)
            self.state = 44
            self.match(StockLangParser.NUMERO)
            self.state = 45
            self.match(StockLangParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def movimiento(self):
            return self.getTypedRuleContext(StockLangParser.MovimientoContext,0)


        def ajuste(self):
            return self.getTypedRuleContext(StockLangParser.AjusteContext,0)


        def consulta(self):
            return self.getTypedRuleContext(StockLangParser.ConsultaContext,0)


        def condicional(self):
            return self.getTypedRuleContext(StockLangParser.CondicionalContext,0)


        def getRuleIndex(self):
            return StockLangParser.RULE_instruccion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = StockLangParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruccion)
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.movimiento()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.ajuste()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.consulta()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.condicional()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MovimientoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipoMovimiento(self):
            return self.getTypedRuleContext(StockLangParser.TipoMovimientoContext,0)


        def ID(self):
            return self.getToken(StockLangParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(StockLangParser.ExpresionContext,0)


        def PUNTO_COMA(self):
            return self.getToken(StockLangParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return StockLangParser.RULE_movimiento

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMovimiento" ):
                return visitor.visitMovimiento(self)
            else:
                return visitor.visitChildren(self)




    def movimiento(self):

        localctx = StockLangParser.MovimientoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_movimiento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.tipoMovimiento()
            self.state = 54
            self.match(StockLangParser.ID)
            self.state = 55
            self.expresion(0)
            self.state = 56
            self.match(StockLangParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoMovimientoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTRADA(self):
            return self.getToken(StockLangParser.ENTRADA, 0)

        def SALIDA(self):
            return self.getToken(StockLangParser.SALIDA, 0)

        def getRuleIndex(self):
            return StockLangParser.RULE_tipoMovimiento

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoMovimiento" ):
                return visitor.visitTipoMovimiento(self)
            else:
                return visitor.visitChildren(self)




    def tipoMovimiento(self):

        localctx = StockLangParser.TipoMovimientoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tipoMovimiento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AjusteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AJUSTAR(self):
            return self.getToken(StockLangParser.AJUSTAR, 0)

        def ID(self):
            return self.getToken(StockLangParser.ID, 0)

        def ASIGNAR(self):
            return self.getToken(StockLangParser.ASIGNAR, 0)

        def expresion(self):
            return self.getTypedRuleContext(StockLangParser.ExpresionContext,0)


        def PUNTO_COMA(self):
            return self.getToken(StockLangParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return StockLangParser.RULE_ajuste

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAjuste" ):
                return visitor.visitAjuste(self)
            else:
                return visitor.visitChildren(self)




    def ajuste(self):

        localctx = StockLangParser.AjusteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ajuste)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(StockLangParser.AJUSTAR)
            self.state = 61
            self.match(StockLangParser.ID)
            self.state = 62
            self.match(StockLangParser.ASIGNAR)
            self.state = 63
            self.expresion(0)
            self.state = 64
            self.match(StockLangParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConsultaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOSTRAR(self):
            return self.getToken(StockLangParser.MOSTRAR, 0)

        def ID(self):
            return self.getToken(StockLangParser.ID, 0)

        def PUNTO_COMA(self):
            return self.getToken(StockLangParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return StockLangParser.RULE_consulta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConsulta" ):
                return visitor.visitConsulta(self)
            else:
                return visitor.visitChildren(self)




    def consulta(self):

        localctx = StockLangParser.ConsultaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_consulta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(StockLangParser.MOSTRAR)
            self.state = 67
            self.match(StockLangParser.ID)
            self.state = 68
            self.match(StockLangParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(StockLangParser.SI, 0)

        def condicion(self):
            return self.getTypedRuleContext(StockLangParser.CondicionContext,0)


        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StockLangParser.BloqueContext)
            else:
                return self.getTypedRuleContext(StockLangParser.BloqueContext,i)


        def SINO(self):
            return self.getToken(StockLangParser.SINO, 0)

        def getRuleIndex(self):
            return StockLangParser.RULE_condicional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = StockLangParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(StockLangParser.SI)
            self.state = 71
            self.condicion()
            self.state = 72
            self.bloque()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 73
                self.match(StockLangParser.SINO)
                self.state = 74
                self.bloque()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StockLangParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(StockLangParser.ExpresionContext,i)


        def comparador(self):
            return self.getTypedRuleContext(StockLangParser.ComparadorContext,0)


        def getRuleIndex(self):
            return StockLangParser.RULE_condicion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicion" ):
                return visitor.visitCondicion(self)
            else:
                return visitor.visitChildren(self)




    def condicion(self):

        localctx = StockLangParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.expresion(0)
            self.state = 78
            self.comparador()
            self.state = 79
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparadorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MENOR(self):
            return self.getToken(StockLangParser.MENOR, 0)

        def MENOR_IGUAL(self):
            return self.getToken(StockLangParser.MENOR_IGUAL, 0)

        def MAYOR(self):
            return self.getToken(StockLangParser.MAYOR, 0)

        def MAYOR_IGUAL(self):
            return self.getToken(StockLangParser.MAYOR_IGUAL, 0)

        def IGUAL(self):
            return self.getToken(StockLangParser.IGUAL, 0)

        def DISTINTO(self):
            return self.getToken(StockLangParser.DISTINTO, 0)

        def getRuleIndex(self):
            return StockLangParser.RULE_comparador

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparador" ):
                return visitor.visitComparador(self)
            else:
                return visitor.visitChildren(self)




    def comparador(self):

        localctx = StockLangParser.ComparadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comparador)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32256) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLAVE_IZQ(self):
            return self.getToken(StockLangParser.LLAVE_IZQ, 0)

        def LLAVE_DER(self):
            return self.getToken(StockLangParser.LLAVE_DER, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StockLangParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(StockLangParser.InstruccionContext,i)


        def getRuleIndex(self):
            return StockLangParser.RULE_bloque

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = StockLangParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(StockLangParser.LLAVE_IZQ)
            self.state = 85 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 84
                self.instruccion()
                self.state = 87 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 248) != 0)):
                    break

            self.state = 89
            self.match(StockLangParser.LLAVE_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self):
            return self.getTypedRuleContext(StockLangParser.TerminoContext,0)


        def expresion(self):
            return self.getTypedRuleContext(StockLangParser.ExpresionContext,0)


        def SUMA(self):
            return self.getToken(StockLangParser.SUMA, 0)

        def RESTA(self):
            return self.getToken(StockLangParser.RESTA, 0)

        def getRuleIndex(self):
            return StockLangParser.RULE_expresion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = StockLangParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.termino(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 99
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = StockLangParser.ExpresionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                    self.state = 94
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 95
                    _la = self._input.LA(1)
                    if not(_la==16 or _la==17):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 96
                    self.termino(0) 
                self.state = 101
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(StockLangParser.FactorContext,0)


        def termino(self):
            return self.getTypedRuleContext(StockLangParser.TerminoContext,0)


        def MULTIPLICAR(self):
            return self.getToken(StockLangParser.MULTIPLICAR, 0)

        def getRuleIndex(self):
            return StockLangParser.RULE_termino

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino" ):
                return visitor.visitTermino(self)
            else:
                return visitor.visitChildren(self)



    def termino(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = StockLangParser.TerminoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_termino, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 110
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = StockLangParser.TerminoContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                    self.state = 105
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 106
                    self.match(StockLangParser.MULTIPLICAR)
                    self.state = 107
                    self.factor() 
                self.state = 112
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(StockLangParser.NUMERO, 0)

        def ID(self):
            return self.getToken(StockLangParser.ID, 0)

        def PAREN_IZQ(self):
            return self.getToken(StockLangParser.PAREN_IZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(StockLangParser.ExpresionContext,0)


        def PAREN_DER(self):
            return self.getToken(StockLangParser.PAREN_DER, 0)

        def getRuleIndex(self):
            return StockLangParser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = StockLangParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_factor)
        try:
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(StockLangParser.NUMERO)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.match(StockLangParser.ID)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self.match(StockLangParser.PAREN_IZQ)
                self.state = 116
                self.expresion(0)
                self.state = 117
                self.match(StockLangParser.PAREN_DER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expresion_sempred
        self._predicates[12] = self.termino_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def termino_sempred(self, localctx:TerminoContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




