from ExprListener import ExprListener

class MyListener(ExprListener):

    def __init__(self):
        self.expr_count = 0
        
    def exitExpr(self, ctx):
        print("Nodo expr:", ctx.getText())