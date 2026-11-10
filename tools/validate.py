"""Ejecuta pruebas, casos CLI y derivaciones, y conserva evidencia reproducible."""
import io
import json
import platform
import subprocess
import sys
import unittest
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.derivations import all_derivations

CASES=[
 ('tokens.stock',['--stage','lex','--tokens'],0,None),
 ('valido.stock',[],0,None),
 ('demo.stock',['--run','--emit-ir','evidence/demo.ir.json'],0,None),
 ('error_lexico.stock',[],1,'L001'),
 ('error_sintactico.stock',[],1,'S001'),
 ('error_duplicado.stock',[],1,'E001'),
 ('error_no_declarado.stock',[],1,'E002'),
 ('error_condicional.stock',[],1,'E002'),
 ('error_stock_inicial.stock',[],1,'E003'),
 ('error_cantidad.stock',[],1,'E004'),
 ('error_ajuste_negativo.stock',[],1,'E005'),
 ('error_insuficiente.stock',[],1,'E006'),
 ('error_desbordamiento.stock',[],1,'E007')]

def main():
    out=ROOT/'evidence';out.mkdir(exist_ok=True)
    stream=io.StringIO();suite=unittest.defaultTestLoader.discover(str(ROOT/'tests'))
    result=unittest.TextTestRunner(stream=stream,verbosity=2).run(suite)
    (out/'pruebas.txt').write_text(stream.getvalue(),encoding='utf-8')
    cli=[]
    for name,args,expected,code in CASES:
        command=[sys.executable,'driver.py','examples/'+name,*args]
        p=subprocess.run(command,cwd=ROOT,capture_output=True,text=True)
        ok=p.returncode==expected and (code is None or code in p.stdout)
        cli.append(dict(file=name,command=['python','driver.py','examples/'+name,*args],expected_exit=expected,observed_exit=p.returncode,expected_code=code,ok=ok,stdout=p.stdout,stderr=p.stderr))
    ds=all_derivations()
    (ROOT/'docs/derivaciones.json').write_text(json.dumps(ds,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (out/'validacion_cli.json').write_text(json.dumps(cli,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    summary=dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),python=platform.python_version(),antlr_runtime='4.13.2',tests_run=result.testsRun,failures=len(result.failures),errors=len(result.errors),cli_cases=len(cli),cli_passed=sum(c['ok'] for c in cli),derivations=len(ds),construction_examples=30,random_programs=80,ok=result.wasSuccessful() and all(c['ok'] for c in cli))
    (out/'resumen_validacion.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False,indent=2))
    return 0 if summary['ok'] else 1
if __name__=='__main__':raise SystemExit(main())
