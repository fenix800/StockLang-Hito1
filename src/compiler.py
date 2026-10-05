from dataclasses import dataclass, field

from antlr4 import CommonTokenStream, InputStream, Token

from generated.StockLangLexer import StockLangLexer
from generated.StockLangParser import StockLangParser
from src.diagnostics import CollectingErrorListener, Diagnostic
from src.semantic import ProductSymbol, SemanticAnalyzer


@dataclass
class AnalysisResult:
    stage: str
    tokens: list = field(default_factory=list)
    tree: str | None = None
    symbols: dict[str, ProductSymbol] = field(default_factory=dict)
    diagnostics: list[Diagnostic] = field(default_factory=list)

    @property
    def ok(self):
        return not self.diagnostics


def analyze(source: str, stage: str = "semantic") -> AnalysisResult:
    """Se detiene si hay errores en una fase. Las columnas empiezan en 1."""
    if stage not in {"lex", "syntax", "semantic"}:
        raise ValueError(f"Fase desconocida: {stage}")
    result = AnalysisResult(stage=stage)
    lexer = StockLangLexer(InputStream(source))
    lex_errors = CollectingErrorListener("LEXICO")
    lexer.removeErrorListeners()
    lexer.addErrorListener(lex_errors)
    stream = CommonTokenStream(lexer)
    stream.fill()
    result.tokens = [
        {
            "type": "EOF" if tok.type == Token.EOF else lexer.symbolicNames[tok.type],
            "lexeme": tok.text,
            "line": tok.line,
            "column": tok.column + 1,
        }
        for tok in stream.tokens
    ]
    result.diagnostics.extend(lex_errors.diagnostics)
    if result.diagnostics or stage == "lex":
        return result

    parser = StockLangParser(stream)
    syntax_errors = CollectingErrorListener("SINTACTICO")
    parser.removeErrorListeners()
    parser.addErrorListener(syntax_errors)
    tree = parser.programa()
    result.tree = tree.toStringTree(recog=parser)
    result.diagnostics.extend(syntax_errors.diagnostics)
    if result.diagnostics or stage == "syntax":
        return result

    semantic = SemanticAnalyzer()
    semantic.visit(tree)
    result.symbols = semantic.symbols
    result.diagnostics.extend(semantic.diagnostics)
    return result
