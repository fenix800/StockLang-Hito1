"""Construye y verifica derivaciones izquierdas de la BNF documentada.

Cada nodo conserva la producción elegida. Antes de expandirlo se verifica que
sea el no terminal más a la izquierda y que su RHS pertenezca a la BNF.
"""
import json
import sys
from dataclasses import dataclass
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from antlr4 import InputStream,CommonTokenStream,Token
from antlr4.tree.Tree import TerminalNode
from generated.StockLangLexer import StockLangLexer
from generated.StockLangParser import StockLangParser

BNF = {
 'P':[['D','L','R','EOF']], 'L':[['D','L'],[]], 'R':[['I','R'],[]],
 'D':[['producto','id','stock','n',';']], 'I':[['M'],['A'],['C'],['S']],
 'M':[['K','id','E',';']], 'K':[['entrada'],['salida']],
 'A':[['ajustar','id','=','E',';']], 'C':[['mostrar','id',';']],
 'S':[['si','Q','B','H']], 'H':[['sino','B'],[]], 'Q':[['E','O','E']],
 'O':[[x] for x in ['<','<=','>','>=','==','!=']], 'B':[['{','I','R','}']],
 'E':[['E','+','T'],['E','-','T'],['T']], 'T':[['T','*','F'],['F']],
 'F':[['n'],['id'],['(','E',')']]
}
@dataclass
class Leaf:
    symbol:str
    lexeme:str
@dataclass
class Node:
    symbol:str
    children:list

def leaf(t):
    token=t.getSymbol()
    return Leaf('id' if token.type == StockLangLexer.ID else 'n' if token.type == StockLangLexer.NUMERO else 'EOF' if token.type == Token.EOF else token.text, token.text)

def seq(name,contexts):
    if not contexts:
        return Node(name,[])
    return Node(name,[convert(contexts[0]),seq(name,contexts[1:])])

def convert(ctx):
    if isinstance(ctx,TerminalNode):
        return leaf(ctx)
    name=type(ctx).__name__
    if name == 'ProgramaContext':
        ds=ctx.declaracion();return Node('P',[convert(ds[0]),seq('L',ds[1:]),seq('R',ctx.instruccion()),Leaf('EOF','<EOF>')])
    if name == 'BloqueContext':
        inst=ctx.instruccion();return Node('B',[Leaf('{','{'),convert(inst[0]),seq('R',inst[1:]),Leaf('}','}')])
    if name == 'CondicionalContext':
        bs=ctx.bloque();h=Node('H',[Leaf('sino','sino'),convert(bs[1])]) if len(bs)==2 else Node('H',[])
        return Node('S',[Leaf('si','si'),convert(ctx.condicion()),convert(bs[0]),h])
    names={'DeclaracionContext':'D','InstruccionContext':'I','MovimientoContext':'M','TipoMovimientoContext':'K','AjusteContext':'A','ConsultaContext':'C','CondicionContext':'Q','ComparadorContext':'O','ExpresionContext':'E','TerminoContext':'T','FactorContext':'F'}
    return Node(names[name],[convert(c) for c in ctx.getChildren()])

def render(items,concrete=False):
    return ' '.join(x.symbol if isinstance(x,Node) or not concrete else x.lexeme for x in items) or 'ε'

def derive(root,source):
    form=[root];steps=[]
    while any(isinstance(x,Node) for x in form):
        i=next(i for i,x in enumerate(form) if isinstance(x,Node));node=form[i]
        rhs=[x.symbol for x in node.children]
        assert rhs in BNF[node.symbol],(node.symbol,rhs)
        before=render(form);form=form[:i]+node.children+form[i+1:]
        steps.append(dict(step=len(steps)+1,production=node.symbol+' → '+(' '.join(rhs) or 'ε'),before=before,after=render(form)))
    lexer=StockLangLexer(InputStream(source));stream=CommonTokenStream(lexer);stream.fill()
    expected=[t.text for t in stream.tokens if t.type != Token.EOF]
    actual=[x.lexeme for x in form if x.symbol != 'EOF']
    assert actual == expected,(actual,expected)
    return dict(start=root.symbol,source=source,steps=steps,terminal_form=render(form),lexemes=actual,verified=True)

def all_derivations():
    cases=json.loads((ROOT/'tests/fixtures/construcciones.json').read_text(encoding='utf-8'))
    methods={'Declaración':'declaracion','Movimiento':'movimiento','Ajuste':'ajuste','Consulta':'consulta','Condicional':'condicional','Expresión':'expresion'}
    out=[]
    for construction,examples in cases.items():
        for i,source in enumerate(examples[:4],1):
            parser=StockLangParser(CommonTokenStream(StockLangLexer(InputStream(source))))
            tree=getattr(parser,methods[construction])()
            assert parser.getNumberOfSyntaxErrors()==0
            assert parser.getCurrentToken().type==Token.EOF
            case=derive(convert(tree),source);case.update(construction=construction,example=i)
            out.append(case)
    return out

if __name__ == '__main__':
    result=all_derivations()
    (ROOT/'docs/derivaciones.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'{len(result)} derivaciones izquierdas verificadas; cada paso pertenece a la BNF y produce los tokens esperados.')
