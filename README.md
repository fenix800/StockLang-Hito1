# StockLang - Lenguaje para gestión de inventarios

StockLang es un lenguaje de dominio específico (DSL) orientado a describir
operaciones básicas de inventario de forma clara y verificable. Este repositorio
contiene el front-end correspondiente al **Hito 1** del curso **Teoría de
Compiladores**, implementado con Python y ANTLR4.

## Estado del proyecto

| Componente | Implementación |
| --- | --- |
| Analizador léxico | Reconoce palabras reservadas, identificadores, números, operadores y delimitadores |
| Analizador sintáctico | Valida declaraciones, movimientos, ajustes, consultas, expresiones y condicionales |
| Analizador semántico inicial | Construye la tabla de símbolos y detecta productos duplicados o no declarados |
| Driver de consola | Permite ejecutar cada etapa y mostrar tokens, árbol sintáctico o salida JSON |
| Pruebas | 26 pruebas automáticas y 30 muestras de construcciones del lenguaje |

## Ejemplo de StockLang

```stocklang
producto lapiz stock 100;
producto cuaderno stock 25;

entrada lapiz 20;
salida cuaderno 3;
ajustar lapiz = lapiz + 2 * 5;

si cuaderno < 10 {
    entrada cuaderno 15;
    mostrar cuaderno;
}

mostrar lapiz;
```

## Construcciones principales

- `producto`: declara un producto y su stock inicial.
- `entrada`: registra una entrada de unidades.
- `salida`: registra una salida de unidades.
- `ajustar`: asigna una expresión aritmética al stock de un producto.
- `mostrar`: consulta un producto declarado.
- `si`: agrupa instrucciones condicionadas por una comparación.

Las expresiones admiten suma, resta, multiplicación y paréntesis. La
multiplicación tiene mayor precedencia que la suma y la resta; los operadores
aritméticos son asociativos por la izquierda. Las condiciones admiten `<`,
`<=`, `>`, `>=`, `==` y `!=`.

## Tecnologías

- Python 3.10 o superior.
- ANTLR 4.13.2.
- Runtime oficial de ANTLR para Python.
- `unittest` para las pruebas automáticas.

## Estructura del repositorio

| Ruta | Propósito |
| --- | --- |
| `grammar/StockLang.g4` | Gramática y reglas léxicas de StockLang |
| `generated/` | Lexer, parser y visitor generados por ANTLR |
| `src/compiler.py` | Coordinación de las fases de análisis |
| `src/diagnostics.py` | Recolección y presentación de diagnósticos |
| `src/semantic.py` | Tabla de símbolos y validaciones semánticas |
| `examples/` | Programas válidos e inválidos para demostración |
| `tests/` | Pruebas automáticas y datos de prueba |
| `tools/generate.py` | Regeneración de los reconocedores de ANTLR |
| `driver.py` | Interfaz de línea de comandos |
| `requirements.txt` | Dependencias del proyecto |

## Instalación y ejecución

### Windows

Desde la raíz del repositorio:

```powershell
py -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe driver.py examples/valido.stock --tokens --tree
```

Si tu instalación utiliza `python` en lugar de `py`, reemplaza el primer
comando. No es necesario activar el entorno virtual.

### Linux o macOS

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python driver.py examples/valido.stock --tokens --tree
```

Los reconocedores ya están incluidos en `generated/`, por lo que Java solo es
necesario cuando se modifica la gramática y se desea regenerarlos.

## Uso del driver

```bash
python driver.py ARCHIVO.stock [--stage lex|syntax|semantic] [--tokens] [--tree] [--json]
```

Ejemplos:

```bash
# Análisis léxico y listado de tokens
python driver.py examples/tokens.stock --stage lex --tokens

# Análisis sintáctico y árbol de análisis
python driver.py examples/valido.stock --stage syntax --tree

# Análisis semántico completo
python driver.py examples/valido.stock

# Resultado estructurado
python driver.py examples/valido.stock --json
```

El driver devuelve código `0` cuando la entrada es aceptada, `1` cuando se
detectan errores y `2` cuando no puede leerse el archivo.

## Diagnósticos implementados

| Código | Fase | Descripción |
| --- | --- | --- |
| `L001` | Léxica | Carácter no reconocido |
| `S001` | Sintáctica | Entrada que no cumple la gramática |
| `E001` | Semántica | Producto declarado más de una vez |
| `E002` | Semántica | Producto utilizado sin declaración previa |

## Pruebas

Ejecuta la suite desde la raíz del repositorio:

```bash
python -m unittest discover -s tests -v
```

Los archivos de `examples/` también permiten comprobar manualmente casos
válidos y errores léxicos, sintácticos y semánticos.

## Regeneración de ANTLR

Si se modifica `grammar/StockLang.g4`, descarga
`antlr-4.13.2-complete.jar` desde el sitio oficial de ANTLR y ejecuta:

```bash
python tools/generate.py /ruta/a/antlr-4.13.2-complete.jar
```

Después de regenerar los reconocedores, vuelve a ejecutar las pruebas. Los
archivos generados no deben editarse manualmente.

## Alcance del Hito 1

Esta entrega implementa el análisis léxico, sintáctico y una primera etapa del
análisis semántico. Todavía no ejecuta los movimientos de inventario ni genera
código. La validación de stock insuficiente, valores negativos y otras reglas
de ejecución se incorporará en los siguientes hitos.

## Referencias

- Enunciado del curso Teoría de Compiladores, Trabajo Parcial/Final 2026-2.
- [ANTLR - Descargas oficiales](https://www.antlr.org/download.html)
- [ANTLR - Target de Python](https://github.com/antlr/antlr4/blob/master/doc/python-target.md)
