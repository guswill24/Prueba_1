from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyListener import MyListener
from antlr4.tree.Tree import ParseTreeWalker

input_stream = InputStream(input('? '))
lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ExprParser(token_stream)
tree = parser.root()

walker = ParseTreeWalker()
walker.walk(MyListener(), tree)
