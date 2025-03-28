from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalVisitor import EvalVisitor

input_stream = InputStream("3 + 5 * 2")
lexer = ExprLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = ExprParser(stream)
tree = parser.prog()

visitor = EvalVisitor()
result = visitor.visit(tree)
print("Resultado:", result)
