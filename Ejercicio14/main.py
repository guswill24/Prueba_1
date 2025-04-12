from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener  # 👈 Importación necesaria

from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser

class VerboseErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"❌ Error de sintaxis en línea {line}, columna {column}: {msg}")

def parse_input(input_text):
    input_stream = InputStream(input_text)
    lexer = MiGramaticaLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiGramaticaParser(tokens)

    parser.removeErrorListeners()
    parser.addErrorListener(VerboseErrorListener())

    try:
        tree = parser.programa()
        print("✅ Entrada válida.")
    except Exception as e:
        print("⚠️ Excepción atrapada:", str(e))

if __name__ == "__main__":
    print("=== Entrada válida ===")
    parse_input("if (x > 10) { y = y + 1; } else { y = y - 1; };")

    print("\n=== Entrada con error 1 ===")
    parse_input("if (x * 10) { y = y + 1; } else { y = y - 1; };")

    print("\n=== Entrada con error 2 ===")
    parse_input("if(x > 10) { y = y + 1; } if { y = y - 1; };")
