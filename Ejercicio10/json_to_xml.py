import sys
from antlr4 import *
from antlr4.tree.Tree import ParseTreeWalker
from JSONLexer import JSONLexer
from JSONParser import JSONParser
from JSONListener import JSONListener

# Manejador del árbol sintáctico que convierte JSON a XML
class XMLEmitter(JSONListener):
    def __init__(self):
        self.xml = {}
    
    def getXML(self, ctx):
        return self.xml.get(ctx, "")

    def setXML(self, ctx, value):
        self.xml[ctx] = value

    def exitAtom(self, ctx):
        self.setXML(ctx, ctx.getText())

    def exitString(self, ctx):
        text = ctx.getText()
        self.setXML(ctx, text[1:-1])  # Elimina comillas

    def exitObjectValue(self, ctx):
        self.setXML(ctx, self.getXML(ctx.jsonObject()))

    def exitArrayValue(self, ctx):
        self.setXML(ctx, self.getXML(ctx.array()))

    def exitPair(self, ctx):
        key = ctx.STRING().getText()[1:-1]
        value = self.getXML(ctx.value())
        self.setXML(ctx, f"<{key}>{value}</{key}>\n")

    def exitAnObject(self, ctx):
        content = "".join(self.getXML(p) for p in ctx.pair())
        self.setXML(ctx, f"\n{content}")

    def exitEmptyObject(self, ctx):
        self.setXML(ctx, "")

    def exitArrayOfValues(self, ctx):
        elements = "".join(f"<element>{self.getXML(v)}</element>\n" for v in ctx.value())
        self.setXML(ctx, f"\n{elements}")

    def exitEmptyArray(self, ctx):
        self.setXML(ctx, "")

    def exitJson(self, ctx):
        self.setXML(ctx, self.getXML(ctx.getChild(0)))  # jsonObject o array

# Punto de entrada del script
def main(argv):
    input_stream = FileStream(argv[1], encoding="utf-8")
    lexer = JSONLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = JSONParser(tokens)
    tree = parser.json()

    walker = ParseTreeWalker()
    emitter = XMLEmitter()
    walker.walk(emitter, tree)

    print(emitter.getXML(tree))

if __name__ == "__main__":
    main(sys.argv)
