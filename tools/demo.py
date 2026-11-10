"""Recorrido reproducible de consola para la demostración."""
import subprocess
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SCENES=[
 ('Programa de inventario',['show','examples/demo.stock'],'El programa declara productos y utiliza dos decisiones con alternativa sino.',14),
 ('Análisis léxico',['driver.py','examples/tokens.stock','--stage','lex','--tokens'],'El lexer produce tokens con lexema, línea y columna, incluido EOF.',10),
 ('Error de sintaxis',['driver.py','examples/error_sintactico.stock'],'S001 rechaza el programa antes de entrar al análisis semántico.',10),
 ('Generación y ejecución',['driver.py','examples/demo.stock','--run','--emit-ir','evidence/demo.ir.json'],'La compilación válida genera IR. La VM devuelve lapiz = 15 y cuaderno = 5.',14),
 ('E001: producto duplicado',['driver.py','examples/error_duplicado.stock'],'Una segunda declaración del mismo producto se rechaza.',10),
 ('E002: producto no declarado',['driver.py','examples/error_no_declarado.stock'],'Todo producto utilizado debe aparecer en la tabla de símbolos.',10),
 ('E003: stock inicial inválido',['driver.py','examples/error_stock_inicial.stock'],'El stock inicial no puede superar 2147483647.',10),
 ('E004: movimiento no positivo',['driver.py','examples/error_cantidad.stock'],'La cantidad de una entrada o salida debe ser mayor que cero.',10),
 ('E005: ajuste negativo',['driver.py','examples/error_ajuste_negativo.stock'],'El ajuste no puede dejar un inventario negativo.',10),
 ('E006: stock insuficiente',['driver.py','examples/error_insuficiente.stock'],'No se pueden retirar 11 unidades cuando solo hay 10.',10),
 ('E007: desbordamiento',['driver.py','examples/error_desbordamiento.stock'],'La suma de stock y entrada también debe respetar el rango entero.',10),
 ('Derivaciones verificadas',['tools/derivations.py'],'Cada paso usa una producción BNF y expande el no terminal más a la izquierda.',10),
 ('Validación completa',['tools/validate.py'],'55 métodos aprobados, 13 casos de consola y 24 derivaciones verificadas.',14),
]
def collect():
 scenes=[]
 for title,args,caption,duration in SCENES:
  if args[0]=='show':
   command='Archivo: '+args[1];stdout=(ROOT/args[1]).read_text(encoding='utf-8');code=0
  else:
   command='python '+' '.join(args);p=subprocess.run([sys.executable,*args],cwd=ROOT,capture_output=True,text=True);stdout=p.stdout+p.stderr;code=p.returncode
  scenes.append(dict(title=title,command=command,stdout=stdout,exit_code=code,caption=caption,duration=duration))
 return scenes
if __name__=='__main__':
 for s in collect():
  print('\n=== '+s['title']+' ===\n'+s['command']+'\n'+s['stdout']+f"Salida: {s['exit_code']}")
