import json
from pathlib import Path
import unittest

from antlr4 import CommonTokenStream, InputStream
from generated.StockLangLexer import StockLangLexer
from generated.StockLangParser import StockLangParser
from src.compiler import analyze

ROOT = Path(__file__).resolve().parents[1]
DECLARATIONS = """producto lapiz stock 100;
producto cuaderno stock 25;
producto borrador stock 60;
producto regla stock 8;
producto mochila stock 5;
"""


class DocumentedExamples(unittest.TestCase):
    def test_five_examples_per_construction(self):
        cases = json.loads(
            (ROOT / "tests/fixtures/construcciones.json").read_text(encoding="utf-8")
        )
        self.assertEqual(len(cases), 6)
        for construction, examples in cases.items():
            self.assertEqual(len(examples), 5)
            for example in examples:
                with self.subTest(construction=construction, source=example):
                    if construction == "Declaración":
                        source = example
                    elif construction == "Expresión":
                        source = DECLARATIONS + f"ajustar lapiz = {example};"
                    else:
                        source = DECLARATIONS + example
                    result = analyze(source)
                    self.assertTrue(result.ok, result.diagnostics)


class FrontendTests(unittest.TestCase):
    def assert_error(self, source, phase, code):
        result = analyze(source)
        self.assertFalse(result.ok)
        self.assertEqual(result.diagnostics[0].phase, phase)
        self.assertEqual(result.diagnostics[0].code, code)
        return result

    def test_complete_program(self):
        result = analyze((ROOT / "examples/valido.stock").read_text(encoding="utf-8"))
        self.assertTrue(result.ok)
        self.assertEqual(set(result.symbols), {"lapiz", "cuaderno"})

    def test_lexemes_and_locations(self):
        tokens = analyze("producto lapiz stock 10;", "lex").tokens
        self.assertEqual([t["type"] for t in tokens],
                         ["PRODUCTO", "ID", "STOCK", "NUMERO", "PUNTO_COMA", "EOF"])
        self.assertEqual(tokens[1]["column"], 10)

    def test_reserved_prefix_is_identifier(self):
        result = analyze("producto entrada_extra stock 3; mostrar entrada_extra;")
        self.assertTrue(result.ok)

    def test_long_comparison_tokens(self):
        result = analyze("<= >= == != < > =", "lex")
        self.assertEqual([t["type"] for t in result.tokens[:-1]],
                         ["MENOR_IGUAL", "MAYOR_IGUAL", "IGUAL", "DISTINTO", "MENOR", "MAYOR", "ASIGNAR"])

    def test_comments_and_windows_newlines(self):
        result = analyze("// comentario\r\nproducto lapiz stock 10;\r\nmostrar lapiz;// fin")
        self.assertTrue(result.ok)
        self.assertEqual(result.tokens[0]["line"], 2)

    def test_illegal_character(self):
        result = self.assert_error("producto lapiz stock 10;\nentrada lapiz @5;", "LEXICO", "L001")
        self.assertEqual((result.diagnostics[0].line, result.diagnostics[0].column), (2, 15))
        self.assertIsNone(result.tree)

    def test_missing_semicolon(self):
        self.assert_error("producto lapiz stock 10; entrada lapiz 5", "SINTACTICO", "S001")

    def test_missing_brace(self):
        self.assert_error("producto lapiz stock 10; si lapiz > 0 { mostrar lapiz;", "SINTACTICO", "S001")

    def test_empty_program(self):
        self.assert_error("", "SINTACTICO", "S001")

    def test_empty_block(self):
        self.assert_error("producto lapiz stock 10; si lapiz > 0 {}", "SINTACTICO", "S001")

    def test_declaration_after_instruction(self):
        self.assert_error("producto a stock 1; mostrar a; producto b stock 2;", "SINTACTICO", "S001")

    def test_trailing_tokens_rejected(self):
        self.assert_error("producto a stock 1; 99", "SINTACTICO", "S001")

    def test_duplicate_product(self):
        result = self.assert_error("producto a stock 10;\nproducto a stock 20;", "SEMANTICO", "E001")
        self.assertEqual(result.symbols["a"].initial_stock, 10)

    def test_unknown_product_in_movement(self):
        self.assert_error("producto a stock 1; entrada b 5;", "SEMANTICO", "E002")

    def test_unknown_product_in_adjustment_target(self):
        self.assert_error("producto a stock 1; ajustar b = 5;", "SEMANTICO", "E002")

    def test_unknown_product_in_expression(self):
        self.assert_error("producto a stock 1; ajustar a = b + 5;", "SEMANTICO", "E002")

    def test_unknown_product_in_condition(self):
        self.assert_error("producto a stock 1; si b > 0 { mostrar a; }", "SEMANTICO", "E002")

    def test_nested_condition_is_checked(self):
        self.assert_error("producto a stock 1; si a > 0 { si a == 1 { mostrar b; } }", "SEMANTICO", "E002")

    def test_accumulates_semantic_errors(self):
        result = analyze("producto a stock 1; producto a stock 2; ajustar b = c + 5;")
        self.assertEqual([e.code for e in result.diagnostics], ["E001", "E002", "E002"])

    def test_symbols_do_not_leak_between_programs(self):
        self.assertTrue(analyze("producto a stock 1;").ok)
        self.assert_error("producto b stock 1; mostrar a;", "SEMANTICO", "E002")

    def test_syntax_phase_does_not_run_semantics(self):
        result = analyze("producto a stock 1; mostrar b;", "syntax")
        self.assertTrue(result.ok)
        self.assertEqual(result.symbols, {})

    def test_initial_symbols_are_not_runtime_results(self):
        result = analyze("producto a stock 10; entrada a 5; salida a 2;")
        self.assertEqual(result.symbols["a"].initial_stock, 10)

    def expression_value(self, source):
        # Evaluador exclusivo de pruebas: comprueba la estructura de la gramática.
        parser = StockLangParser(CommonTokenStream(StockLangLexer(InputStream(source))))
        tree = parser.expresion()
        self.assertEqual(parser.getNumberOfSyntaxErrors(), 0)
        self.assertEqual(parser.getCurrentToken().type, -1)

        def evaluate(ctx):
            if isinstance(ctx, StockLangParser.ExpresionContext):
                if ctx.expresion() is None:
                    return evaluate(ctx.termino())
                left, right = evaluate(ctx.expresion()), evaluate(ctx.termino())
                return left + right if ctx.SUMA() else left - right
            if isinstance(ctx, StockLangParser.TerminoContext):
                if ctx.termino() is None:
                    return evaluate(ctx.factor())
                return evaluate(ctx.termino()) * evaluate(ctx.factor())
            if ctx.NUMERO():
                return int(ctx.NUMERO().getText())
            return evaluate(ctx.expresion())
        return evaluate(tree)

    def test_multiplication_precedence(self):
        self.assertEqual(self.expression_value("2 + 3 * 4"), 14)

    def test_parentheses_change_precedence(self):
        self.assertEqual(self.expression_value("(2 + 3) * 4"), 20)

    def test_subtraction_is_left_associative(self):
        self.assertEqual(self.expression_value("10 - 3 - 2"), 5)


if __name__ == "__main__":
    unittest.main()
