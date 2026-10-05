# StockLang - base de trabajo para el hito 1

Propuesta de un lenguaje de dominio específico para describir operaciones de
inventario. Implementación en Python 3.10 o superior con ANTLR 4.13.2.

**Estado:** propuesta pendiente del visto bueno del profesor. El equipo debe
revisar y adaptar esta base, completar sus datos y poder explicar cada parte.
El enunciado exige originalidad y trabajo del equipo.

## Primeros pasos en Windows

Descomprime el ZIP y abre una terminal en la carpeta `stocklang_hito1`.

```powershell
py -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe driver.py examples/valido.stock --tokens --tree
.venv\Scripts\python.exe -m unittest discover -s tests -v
```

No es necesario activar el entorno ni cambiar la política de PowerShell.
Si tu instalación usa `python` en lugar de `py`, reemplaza el primer comando.

## Primeros pasos en Linux o macOS

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python driver.py examples/valido.stock --tokens --tree
.venv/bin/python -m unittest discover -s tests -v
```

Los reconocedores ya están generados y se incluyen en `generated/`. Java solo
es necesario si modificas la gramática y quieres regenerarlos.

## Sintaxis del lenguaje

```text
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

Un producto declarado representa una cantidad entera. En una expresión,
su identificador denota su stock según la semántica prevista del lenguaje.
El programa contiene al menos una declaración, todas al inicio. Cada bloque
contiene al menos una instrucción y puede incluir condiciones anidadas.
Los identificadores distinguen mayúsculas y minúsculas.

`*` tiene mayor precedencia que `+` y `-`. Los operadores son asociativos
por la izquierda. Los paréntesis alteran la precedencia.
Las condiciones admiten `<`, `<=`, `>`, `>=`, `==` y `!=`.
Los comentarios empiezan con `//` y llegan hasta el fin de línea.

## Qué hace este hito

1. El lexer reconoce tokens y detecta caracteres inválidos.
2. El parser valida la estructura completa hasta EOF y construye un árbol.
3. El visitor semántico crea la tabla de símbolos y comprueba dos errores:
   E001, producto duplicado, y E002, producto usado sin declarar.

Si una fase falla, no se ejecuta la siguiente. El driver devuelve 0 cuando
la fase solicitada acepta el programa, 1 ante errores de análisis y 2 si no
puede leer el archivo. La salida JSON incluye diagnósticos y posiciones.

**Alcance:** este front end no ejecuta entradas, salidas ni condiciones y no
genera código. `stock_inicial` conserva la cantidad de la declaración.
Una salida superior al stock o una expresión que produzca una cantidad
negativa aún no se rechazan. Esas validaciones necesitan ampliar la semántica
y/o definir controles de ejecución en los siguientes hitos.

## Pruebas y demostración

```bash
python driver.py examples/tokens.stock --stage lex --tokens
python driver.py examples/valido.stock --stage syntax --tree
python driver.py examples/error_lexico.stock
python driver.py examples/error_sintactico.stock
python driver.py examples/error_duplicado.stock
python driver.py examples/error_no_declarado.stock
python driver.py examples/error_condicional.stock
python driver.py examples/valido.stock --json
python -m unittest discover -s tests -v
```

Los casos inválidos deben terminar con código 1. No es un fallo de instalación.
`tests/test_frontend.py` prueba las 30 muestras del lenguaje y otros casos
de aceptación, rechazo, precedencia y separación entre fases.

## Regeneración de ANTLR

Descarga `antlr-4.13.2-complete.jar` desde https://www.antlr.org/download.html
y usa la misma versión que `requirements.txt`.

```bash
python tools/generate.py /ruta/a/antlr-4.13.2-complete.jar
```

Equivalente desde la raíz del proyecto:

```bash
java -jar /ruta/a/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -no-listener -Xexact-output-dir -o generated grammar/StockLang.g4
```

Después de regenerar, ejecuta otra vez las pruebas. No edites a mano los
reconocedores generados.

## Archivos

| Ruta | Contenido |
| --- | --- |
| `grammar/StockLang.g4` | Reglas del lexer y del parser |
| `generated/` | Lexer, parser y visitor producidos por ANTLR |
| `src/semantic.py` | Tabla de símbolos y controles semánticos |
| `src/compiler.py` | Coordinación de las tres fases |
| `driver.py` | Interfaz de consola |
| `examples/` | Programas válidos e inválidos |
| `tests/` | Pruebas automáticas y datos de prueba |
| `tools/generate.py` | Regeneración del lexer, parser y visitor con ANTLR |

## Entrega y GitHub

El repositorio remoto todavía debe crearlo el equipo en su cuenta de GitHub.
En GitHub, crea un repositorio vacío y copia su URL. Desde esta carpeta:

```bash
git init
git add .
git commit -m "Base del hito 1: front end de StockLang"
git branch -M main
git remote add origin URL_REAL_DEL_REPOSITORIO
git push -u origin main
```

Si Git pide nombre y correo, configúralos con tus datos reales antes del commit.
Reemplaza el ejemplo de URL con la URL de tu repositorio. No publiques datos
privados. El ZIP de entrega debe reflejar la misma versión del repositorio.

Registra el trabajo real del grupo mediante commits y, de ser necesario,
GitHub Issues o Projects. No atribuyas tareas ni commits a integrantes que no
los hayan realizado.

## Fuentes

- Enunciado del curso: Teoría de Compiladores, Trabajo Parcial/Final 2026-2.
- ANTLR, descargas oficiales: https://www.antlr.org/download.html
- ANTLR, documentación del target Python:
  https://github.com/antlr/antlr4/blob/master/doc/python-target.md

ANTLR se usa como dependencia de terceros. Los archivos `generated/*.py`
incluyen la marca del generador y la versión. El diseño de StockLang y la
implementación manual están separados de esos artefactos generados.
