Análisis y evaluación de estructuras for con Listener y Visitor
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
for (i = 0; i < 10; i = i + 1) {
    x = x + i;
}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
📦 1. Crear archivos de la gramatica
    antlr4 -Dlanguage=Python3 -visitor -listener MiGramatica.g4
📦 2. Configurar archivo MyListener.py y test_listener.py
📦 3. Configurar archivo EvalVisitor.py y test_visitor.py
📦 4.Ejecutar Patrones:

⚙️ Para ejecutar el patron Listener
    python3 test_listener.py

⚙️ Para ejecutar el patron Visitor
    python3 test_visitor.py
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
🔡 Finalizada el desarro del ejercicio realizar un:
git add .
git commit -m "Subir cambios"
git push