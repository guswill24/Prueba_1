from ExprListener import ExprListener

class TreePrinter(ExprListener):
    def __init__(self):
        self.nivel = 0

    def enterExpr(self, ctx):
        print(" " * self.nivel + f"Entrando a Expr: {ctx.getText()}")
        self.nivel += 2

    def exitExpr(self, ctx):
        self.nivel -= 2
        print(" " * self.nivel + f"Saliendo de Expr: {ctx.getText()}")
