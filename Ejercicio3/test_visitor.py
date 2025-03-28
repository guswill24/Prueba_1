import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from TreeVisitor import TreeVisitor

def main():
    # Entrada de datos (desde consola o argumento)
    input_text = input("Ingrese una expresión: ")

    # Crear InputStream
    input_stream = InputStream(input_text)

    # Crear Lexer y Parser
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)

    # Obtener el árbol
    tree = parser.expr()

    # Recorrer el árbol con Visitor
    visitor = TreeVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()
