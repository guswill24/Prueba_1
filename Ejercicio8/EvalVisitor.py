from MiGramaticaVisitor import MiGramaticaVisitor

class EvalVisitor(MiGramaticaVisitor):
    def __init__(self):
        self.variables = {}

    def visitPrograma(self, ctx):
        for sentencia in ctx.sentencia():
            self.visit(sentencia)
        return self.variables

    def visitAssign(self, ctx):
        var = ctx.ID().getText()
        value = self.visit(ctx.expresion())
        self.variables[var] = value
        print(f"📝 Asignación: {var} = {value}")
        return value

    def visitInt(self, ctx):
        return int(ctx.getText())

    def visitVariable(self, ctx):
        var = ctx.getText()
        if var not in self.variables:
            print(f"⚠️ Variable '{var}' no inicializada. Se asume 0.")
        return self.variables.get(var, 0)

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        op = ctx.op.text
        return left + right if op == '+' else left - right

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        op = ctx.op.text
        return left * right if op == '*' else left / right

    def visitParens(self, ctx):
        return self.visit(ctx.expresion())

    def visitCondicion(self, ctx):
        var = ctx.ID().getText()
        op = ctx.op.text
        valor_variable = self.variables.get(var, 0)
        valor_comparado = int(ctx.INT().getText())

        if op == '>':
            return valor_variable > valor_comparado
        elif op == '<':
            return valor_variable < valor_comparado
        elif op == '==':
            return valor_variable == valor_comparado
        elif op == '!=':
            return valor_variable != valor_comparado
        return False

    def visitInicializacion(self, ctx):
        var = ctx.ID().getText()
        value = self.visit(ctx.expresion())
        self.variables[var] = value
        print(f"⚙️ Inicialización: {var} = {value}")
        return value

    def visitActualizacion(self, ctx):
        var = ctx.ID().getText()
        value = self.visit(ctx.expresion())
        self.variables[var] = value
        print(f"🔄 Actualización: {var} = {value}")
        return value

    def visitForLoop(self, ctx):
        # Ejecutar inicialización
        self.visit(ctx.inicializacion())

        # Evaluar condición y ejecutar bloque
        while self.visit(ctx.condicion()):
            print("🔁 Iteración FOR")
            for stmt in ctx.sentencia():
                self.visit(stmt)
            self.visit(ctx.actualizacion())
