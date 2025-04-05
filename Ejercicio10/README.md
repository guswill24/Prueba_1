1.	Generar el parser y lexer de ANTLR:
antlr4 -Dlanguage=Python3 JSON.g4
Esto genera CSVLexer.py, CSVParser.py, y CSVListener.py.
2.	Ejecutar el script:
python json_to_xml.py t.json