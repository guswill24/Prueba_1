from MiGramaticaListener import MiGramaticaListener

class MyListener(MiGramaticaListener):
    def exitForLoop(self, ctx):
        print("🔁 Se detectó un bucle FOR")

    def exitInicializacion(self, ctx):
        print("⚙️ Inicialización:", ctx.getText())

    def exitCondicion(self, ctx):
        print("🔎 Condición:", ctx.getText())

    def exitActualizacion(self, ctx):
        print("🔄 Actualización:", ctx.getText())

    def exitAssign(self, ctx):
        print("✍️ Asignación:", ctx.getText())

    def exitAddSub(self, ctx):
        print("➕➖ Expresión suma/resta:", ctx.getText())

    def exitMulDiv(self, ctx):
        print("✖️➗ Expresión multiplicación/división:", ctx.getText())

    def exitVariable(self, ctx):
        print("🔡 Variable utilizada:", ctx.getText())

    def exitInt(self, ctx):
        print("🔢 Número:", ctx.getText())
