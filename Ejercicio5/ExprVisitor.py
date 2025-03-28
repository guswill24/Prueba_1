# Generated from Expr.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#programa.
    def visitPrograma(self, ctx:ExprParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#sentencia.
    def visitSentencia(self, ctx:ExprParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#IfElse.
    def visitIfElse(self, ctx:ExprParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#CondicionSimple.
    def visitCondicionSimple(self, ctx:ExprParser.CondicionSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Assign.
    def visitAssign(self, ctx:ExprParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Variable.
    def visitVariable(self, ctx:ExprParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#MulDiv.
    def visitMulDiv(self, ctx:ExprParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#AddSub.
    def visitAddSub(self, ctx:ExprParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Parens.
    def visitParens(self, ctx:ExprParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Int.
    def visitInt(self, ctx:ExprParser.IntContext):
        return self.visitChildren(ctx)



del ExprParser