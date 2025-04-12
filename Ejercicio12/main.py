from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener  # 👈 Importación necesaria

from SimpleLexer import SimpleLexer
from SimpleParser import SimpleParser

class VerboseErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"❌ Error de sintaxis en línea {line}, columna {column}: {msg}")

def parse_input(input_text):
    input_stream = InputStream(input_text)
    lexer = SimpleLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = SimpleParser(tokens)

    parser.removeErrorListeners()
    parser.addErrorListener(VerboseErrorListener())

    try:
        tree = parser.prog()
        print("✅ Entrada válida.")
    except Exception as e:
        print("⚠️ Excepción atrapada:", str(e))

if __name__ == "__main__":
    print("=== Entrada válida ===")
    parse_input("class A { int x; }")

    print("\n=== Entrada con error 1 ===")
    parse_input("class B { int f(x) { a=3+4; } }")

    print("\n=== Entrada con error 2 ===")
    parse_input("class C { int f(x) { a = 3 + 5; } }")

    print("\n=== Entrada con error 3 ===")
    parse_input("class I { int f(x) { } }")

    print("\n=== Entrada con error 4 ===")
    parse_input("class G { int f(x) { a=5+2; } }")

    print("\n=== ===============================")

    print("\n=== Entrada con error ejercicio 2 -> 1 ===")
    parse_input("class A { int x; }")

    print("\n=== Entrada con error ejercicio 2 -> 2 ===")
    parse_input("class A { int x; }")
