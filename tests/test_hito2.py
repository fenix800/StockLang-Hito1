"""Regresión de semántica y del backend con resultados independientes."""
import json
import random
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from src.compiler import analyze
from src.ir import execute

ROOT = Path(__file__).resolve().parents[1]
D = 'producto a stock 10;\n'

class SemanticCompleteTests(unittest.TestCase):
    def codes(self, source):
        return [e.code for e in analyze(source).diagnostics]
    def test_seven_distinct_semantic_errors(self):
        cases = {
          'E001': D + 'producto a stock 2;',
          'E002': D + 'mostrar b;',
          'E003': 'producto a stock 2147483648;',
          'E004': D + 'entrada a 0;',
          'E005': D + 'ajustar a = 1 - 2;',
          'E006': D + 'salida a 11;',
          'E007': 'producto a stock 2147483647; entrada a 1;'
        }
        for code,source in cases.items():
            with self.subTest(code=code):
                r = analyze(source, run=True)
                self.assertEqual([e.code for e in r.diagnostics], [code])
                self.assertEqual(r.ir, [])
                self.assertIsNone(r.execution)
    def test_negative_movement(self):
        self.assertEqual(self.codes(D+'salida a 1 - 2;'), ['E004'])
    def test_adjust_zero_and_withdraw_all(self):
        r = analyze(D+'salida a 10; ajustar a = 0;',run=True)
        self.assertTrue(r.ok)
        self.assertEqual(r.execution['stocks']['a'],0)
    def test_integer_boundaries(self):
        r = analyze('producto a stock 2147483647; ajustar a = 2147483647;',run=True)
        self.assertTrue(r.ok)
        self.assertEqual(r.final_stocks['a'],2147483647)
    def test_expression_overflow_in_all_contexts(self):
        for instruction in ['ajustar a = 2147483647 + 1;', 'entrada a 2147483647 * 2;', 'si 2147483647 + 1 > 0 { mostrar a; }']:
            with self.subTest(source=instruction):
                self.assertIn('E007', self.codes(D+instruction))
    def test_overflow_literal(self):
        self.assertEqual(self.codes(D+'ajustar a = 2147483648;'), ['E007'])
    def test_intermediate_negative_value_allowed(self):
        self.assertTrue(analyze(D+'ajustar a = (1 - 3) * (1 - 3);').ok)
    def test_failed_operation_keeps_previous_stock(self):
        r=analyze(D+'salida a 11; entrada a 2;')
        self.assertEqual(r.final_stocks['a'],12)
    def test_true_branch_state(self):
        r=analyze(D+'si a > 0 { entrada a 5; } sino { salida a 2; } salida a 14;',run=True)
        self.assertTrue(r.ok,r.diagnostics)
        self.assertEqual(r.final_stocks['a'],1)
        self.assertEqual(r.execution['stocks'],r.final_stocks)
    def test_false_branch_state(self):
        r=analyze(D+'si a < 0 { entrada a 5; } sino { salida a 2; }',run=True)
        self.assertTrue(r.ok)
        self.assertEqual(r.execution['stocks']['a'],8)
    def test_inactive_branch_still_checked(self):
        self.assertEqual(self.codes(D+'si a > 0 { mostrar a; } sino { salida a 11; }'),['E006'])
    def test_inactive_branch_cannot_pollute_else(self):
        r=analyze(D+'si a < 0 { ajustar a = 100; } sino { salida a 9; }',run=True)
        self.assertTrue(r.ok)
        self.assertEqual(r.execution['stocks']['a'],1)
    def test_false_without_else_keeps_state(self):
        r=analyze(D+'si a < 0 { entrada a 5; } mostrar a;',run=True)
        self.assertEqual(r.execution['output'],['a = 10'])
    def test_nested_else_binds_to_its_block(self):
        r=analyze(D+'si a > 0 { si a == 10 { ajustar a = 3; } sino { ajustar a = 4; } } sino { ajustar a = 5; } mostrar a;',run=True)
        self.assertTrue(r.ok)
        self.assertEqual(r.execution['output'],['a = 3'])
    def test_else_keyword_not_identifier(self):
        self.assertEqual(analyze('sino sino_extra', 'lex').tokens[0]['type'],'SINO')
        self.assertEqual(analyze('sino sino_extra', 'lex').tokens[1]['type'],'ID')
    def test_else_missing_block_rejected(self):
        self.assertEqual(self.codes(D+'si a > 0 { mostrar a; } sino'),['S001'])
    def test_empty_else_rejected(self):
        self.assertIn('S001',self.codes(D+'si a > 0 { mostrar a; } sino {}'))
    def test_undeclared_in_else(self):
        r=analyze(D+'si a > 0 { mostrar a; } sino { mostrar b; }')
        self.assertEqual([e.code for e in r.diagnostics],['E002'])
        self.assertEqual(r.diagnostics[0].line,2)
    def test_updated_state_drives_condition(self):
        r=analyze(D+'salida a 10; si a == 0 { entrada a 1; } sino { entrada a 2; }',run=True)
        self.assertEqual(r.execution['stocks']['a'],1)

class BackendTests(unittest.TestCase):
    def test_precedence_and_order_in_vm(self):
        r=analyze(D+'ajustar a = (10 - 3 - 2) + 3 * 4; mostrar a;',run=True)
        self.assertTrue(r.ok)
        self.assertEqual(r.execution['output'],['a = 17'])
    def test_all_comparators_both_outcomes(self):
        cases=[('<',9,10,True),('<=',10,10,True),('>',11,10,True),('>=',10,10,True),('==',10,10,True),('!=',9,10,True),('<',10,9,False),('<=',11,10,False),('>',9,10,False),('>=',9,10,False),('==',9,10,False),('!=',10,10,False)]
        for op,a,b,expected in cases:
            with self.subTest(op=op,a=a,b=b):
                r=analyze(D+f'si {a} {op} {b} {{ ajustar a = 1; }} sino {{ ajustar a = 2; }}',run=True)
                self.assertTrue(r.ok)
                self.assertEqual(r.execution['stocks']['a'],1 if expected else 2)
    def test_print_order_and_no_inactive_output(self):
        r=analyze(D+'mostrar a; si a == 10 { entrada a 2; mostrar a; } sino { mostrar a; } mostrar a;',run=True)
        self.assertEqual(r.execution['output'],['a = 10','a = 12','a = 12'])
    def test_emit_without_execution(self):
        r=analyze(D,emit_ir=True)
        self.assertTrue(r.ir)
        self.assertIsNone(r.execution)
        self.assertEqual(json.loads(json.dumps(r.ir)),r.ir)
    def test_invalid_program_never_emits(self):
        for s in [D+'@',D+'mostrar',D+'mostrar b;']:
            r=analyze(s,run=True)
            self.assertFalse(r.ok)
            self.assertEqual(r.ir,[])
    def test_reproducible_ir(self):
        s=D+'si a == 10 { entrada a 1; } sino { entrada a 2; }'
        self.assertEqual(analyze(s,emit_ir=True).ir,analyze(s,emit_ir=True).ir)
    def test_randomized_inventory_against_independent_oracle(self):
        rng=random.Random(20261110)
        for case in range(80):
            expected=100
            lines=['producto a stock 100;']
            for _ in range(20):
                if rng.randrange(2):
                    n=rng.randint(1,30);lines.append(f'entrada a {n};');expected+=n
                else:
                    n=rng.randint(1,max(expected,1))
                    if expected:
                        lines.append(f'salida a {n};');expected-=n
            lines.append('mostrar a;')
            r=analyze('\n'.join(lines),run=True)
            with self.subTest(case=case):
                self.assertTrue(r.ok)
                self.assertEqual(r.execution['stocks']['a'],expected)
                self.assertEqual(r.final_stocks['a'],expected)
    def test_cli_exit_codes_and_ir(self):
        with tempfile.TemporaryDirectory() as d:
            src=Path(d)/'test.stock';ir=Path(d)/'test.ir.json'
            src.write_text(D+'mostrar a;')
            p=subprocess.run([sys.executable,'driver.py',str(src),'--run','--emit-ir',str(ir),'--json'],cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(p.returncode,0)
            self.assertEqual(json.loads(p.stdout)['execution']['stocks']['a'],10)
            self.assertTrue(ir.is_file())
            src.write_text(D+'mostrar b;');ir.unlink()
            p=subprocess.run([sys.executable,'driver.py',str(src),'--emit-ir',str(ir)],cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(p.returncode,1)
            self.assertFalse(ir.exists())
            p=subprocess.run([sys.executable,'driver.py',str(Path(d)/'missing.stock')],cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(p.returncode,2)
    def test_vm_rejects_invalid_stock(self):
        with self.assertRaises(ValueError):
            execute([{'op':'declare','name':'a','value':-1}])

class DerivationTests(unittest.TestCase):
    def test_all_documented_derivations(self):
        from tools.derivations import all_derivations
        cases=all_derivations()
        self.assertEqual(len(cases),24)
        self.assertTrue(all(c['verified'] for c in cases))
