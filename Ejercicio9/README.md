1.	Generar el parser y lexer de ANTLR:
antlr4 -Dlanguage=Python3 CSV.g4
Esto genera CSVLexer.py, CSVParser.py, y CSVListener.py.
2.	Ejecutar el script:
python load_csv.py t.csv
