"""Backend de avance: código de tres direcciones y máquina virtual independiente."""
from generated.StockLangVisitor import StockLangVisitor
from src.semantic import MAX_STOCK, MIN_INT

class IRGenerator(StockLangVisitor):
    def __init__(self):
        self.code = []
        self.counter = 0
        self.label_counter = 0
    def emit(self, op, **args):
        self.code.append(dict(op=op, **args))
    def temp(self):
        self.counter += 1
        return f't{self.counter}'
    def label(self):
        self.label_counter += 1
        return f'L{self.label_counter}'
    def visitDeclaracion(self, ctx):
        self.emit('declare', name=ctx.ID().getText(), value=int(ctx.NUMERO().getText()))
    def visitConsulta(self, ctx):
        self.emit('print', name=ctx.ID().getText())
    def visitMovimiento(self, ctx):
        amount = self.visit(ctx.expresion())
        old, new = self.temp(), self.temp()
        name = ctx.ID().getText()
        self.emit('load', dest=old, name=name)
        self.emit('positive', arg=amount)
        self.emit('sub' if ctx.tipoMovimiento().SALIDA() else 'add', dest=new, left=old, right=amount)
        self.emit('store', name=name, arg=new)
    def visitAjuste(self, ctx):
        value = self.visit(ctx.expresion())
        self.emit('store', name=ctx.ID().getText(), arg=value)
    def visitCondicion(self, ctx):
        left, right = [self.visit(e) for e in ctx.expresion()]
        dest = self.temp()
        self.emit('cmp', dest=dest, left=left, right=right, comparator=ctx.comparador().getText())
        return dest
    def visitCondicional(self, ctx):
        cond = self.visit(ctx.condicion())
        other, end = self.label(), self.label()
        self.emit('branch_false', arg=cond, label=other)
        self.visit(ctx.bloque(0))
        self.emit('jump', label=end)
        self.emit('label', name=other)
        if len(ctx.bloque()) == 2:
            self.visit(ctx.bloque(1))
        self.emit('label', name=end)
    def visitExpresion(self, ctx):
        if ctx.expresion() is None:
            return self.visit(ctx.termino())
        left, right = self.visit(ctx.expresion()), self.visit(ctx.termino())
        dest = self.temp()
        self.emit('add' if ctx.SUMA() else 'sub', dest=dest, left=left, right=right)
        return dest
    def visitTermino(self, ctx):
        if ctx.termino() is None:
            return self.visit(ctx.factor())
        left, right = self.visit(ctx.termino()), self.visit(ctx.factor())
        dest = self.temp()
        self.emit('mul', dest=dest, left=left, right=right)
        return dest
    def visitFactor(self, ctx):
        if ctx.expresion():
            return self.visit(ctx.expresion())
        dest = self.temp()
        if ctx.ID():
            self.emit('load', dest=dest, name=ctx.ID().getText())
        else:
            self.emit('const', dest=dest, value=int(ctx.NUMERO().getText()))
        return dest

def execute(code):
    """Ejecuta IR generado en memoria. No recibe archivos IR externos."""
    stocks, temps, output = {}, {}, []
    labels = {i['name']:n for n,i in enumerate(code) if i['op'] == 'label'}
    pc = 0
    while pc < len(code):
        i = code[pc]; op = i['op']
        if op == 'declare':
            if i['name'] in stocks or not 0 <= i['value'] <= MAX_STOCK:
                raise ValueError('Declaración inválida en IR')
            stocks[i['name']] = i['value']
        elif op == 'const':
            temps[i['dest']] = i['value']
        elif op == 'load':
            temps[i['dest']] = stocks[i['name']]
        elif op in ('add','sub','mul'):
            a,b = temps[i['left']],temps[i['right']]
            value = a+b if op == 'add' else a-b if op == 'sub' else a*b
            if not MIN_INT <= value <= MAX_STOCK:
                raise ValueError('Desbordamiento en IR')
            temps[i['dest']] = value
        elif op == 'positive':
            if temps[i['arg']] <= 0:
                raise ValueError('Movimiento no positivo en IR')
        elif op == 'store':
            value = temps[i['arg']]
            if not 0 <= value <= MAX_STOCK:
                raise ValueError('Stock inválido en IR')
            stocks[i['name']] = value
        elif op == 'cmp':
            a,b = temps[i['left']],temps[i['right']]
            temps[i['dest']] = {'<':a<b,'<=':a<=b,'>':a>b,'>=':a>=b,'==':a==b,'!=':a!=b}[i['comparator']]
        elif op == 'branch_false':
            if not temps[i['arg']]:
                pc = labels[i['label']]
        elif op == 'jump':
            pc = labels[i['label']]
        elif op == 'print':
            output.append(f"{i['name']} = {stocks[i['name']]}")
        elif op != 'label':
            raise ValueError(f'Instrucción IR desconocida: {op}')
        pc += 1
    return dict(stocks=stocks, output=output)
