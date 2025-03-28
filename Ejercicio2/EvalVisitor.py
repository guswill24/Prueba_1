from ExprVisitor import ExprVisitor

class EvalVisitor(ExprVisitor):
    def visitRoot(self, ctx):
        return self.visit(ctx.expr())

    def visitExpr(self, ctx):
        if ctx.NUM():
            return int(ctx.NUM().getText())
        else:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            return left + right
