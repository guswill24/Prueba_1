from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

class EvalVisitor(ExprVisitor):
    def visitProg(self, ctx):
        return self.visit(ctx.expr())

    def visitExpr(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.op.text == '+':
            return self.visit(ctx.expr(0)) + self.visit(ctx.expr(1))
        elif ctx.op.text == '-':
            return self.visit(ctx.expr(0)) - self.visit(ctx.expr(1))
        elif ctx.op.text == '*':
            return self.visit(ctx.expr(0)) * self.visit(ctx.expr(1))
        elif ctx.op.text == '/':
            return self.visit(ctx.expr(0)) / self.visit(ctx.expr(1))
