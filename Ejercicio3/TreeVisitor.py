from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

class TreeVisitor(ExprVisitor):
    def __init__(self):
        self.nivel = 0

    def visitProg(self, ctx):
        # Inicia el recorrido con la regla inicial
        return self.visit(ctx.expr())

    def visitExpr(self, ctx):
        children = list(ctx.getChildren())

        if len(children) == 1:
            # Es un número (INT)
            token = children[0].getSymbol().type
            texto = children[0].getText()
            print(" " * self.nivel + f"{ExprParser.symbolicNames[token]} ({texto})")
        else:
            # Es una operación binaria (+, -, *, /)
            operador = ctx.op.text
            print(" " * self.nivel + f"OPERADOR ({operador})")

            self.nivel += 1
            self.visit(children[0])  # lado izquierdo
            self.visit(children[2])  # lado derecho
            self.nivel -= 1
