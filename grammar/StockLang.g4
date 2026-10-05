grammar StockLang;

// Todas las declaraciones preceden a las instrucciones.
programa
    : declaracion+ instruccion* EOF
    ;

declaracion
    : PRODUCTO ID STOCK NUMERO PUNTO_COMA
    ;

instruccion
    : movimiento
    | ajuste
    | consulta
    | condicional
    ;

movimiento
    : tipoMovimiento ID expresion PUNTO_COMA
    ;

tipoMovimiento
    : ENTRADA
    | SALIDA
    ;

ajuste
    : AJUSTAR ID ASIGNAR expresion PUNTO_COMA
    ;

consulta
    : MOSTRAR ID PUNTO_COMA
    ;

condicional
    : SI condicion bloque
    ;

condicion
    : expresion comparador expresion
    ;

comparador
    : MENOR
    | MENOR_IGUAL
    | MAYOR
    | MAYOR_IGUAL
    | IGUAL
    | DISTINTO
    ;

bloque
    : LLAVE_IZQ instruccion+ LLAVE_DER
    ;

// Recursión izquierda admitida por ANTLR4. Los niveles fijan precedencia.
expresion
    : expresion (SUMA | RESTA) termino
    | termino
    ;

termino
    : termino MULTIPLICAR factor
    | factor
    ;

factor
    : NUMERO
    | ID
    | PAREN_IZQ expresion PAREN_DER
    ;

// Las palabras reservadas preceden a ID para resolver empates de longitud.
PRODUCTO    : 'producto';
STOCK       : 'stock';
ENTRADA     : 'entrada';
SALIDA      : 'salida';
AJUSTAR     : 'ajustar';
MOSTRAR     : 'mostrar';
SI          : 'si';
MENOR_IGUAL : '<=';
MAYOR_IGUAL : '>=';
IGUAL       : '==';
DISTINTO    : '!=';
MENOR       : '<';
MAYOR       : '>';
ASIGNAR     : '=';
SUMA        : '+';
RESTA       : '-';
MULTIPLICAR : '*';
PUNTO_COMA  : ';';
LLAVE_IZQ   : '{';
LLAVE_DER   : '}';
PAREN_IZQ   : '(';
PAREN_DER   : ')';
NUMERO      : [0-9]+;
ID          : [a-zA-Z_] [a-zA-Z_0-9]*;
COMENTARIO  : '//' ~[\r\n]* -> skip;
ESPACIO     : [ \t\r\n]+ -> skip;
