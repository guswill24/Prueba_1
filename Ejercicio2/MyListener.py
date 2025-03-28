from ExprListener import ExprListener

class MyListener(ExprListener):
    def exitExpr(self, ctx):
        print("Salí de expr:", ctx.getText())
