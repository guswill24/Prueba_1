from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprListener import ExprListener
from TreePrinter import TreePrinter

def main():
    input_text = input("Ingrese una expresión: ")
    input_stream = InputStream(input_text)

    lexer = ExprLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ExprParser(tokens)

    tree = parser.prog()  # regla inicial

    # Listener personalizado
    listener = TreePrinter()

    # ParseTreeWalker
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main()
