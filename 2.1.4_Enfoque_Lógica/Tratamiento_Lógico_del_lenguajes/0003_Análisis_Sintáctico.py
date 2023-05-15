import nltk

# Definimos la gramática que queremos utilizar
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | V NP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat'
    V -> 'chased' | 'sat'
    P -> 'on' | 'in'
""")

# Creamos un analizador sintáctico a partir de la gramática
parser = nltk.ChartParser(grammar)

# Definimos la oración que queremos analizar
sentence = "the dog chased the cat in the garden"

# Convertimos la oración en una lista de palabras
tokens = nltk.word_tokenize(sentence)

# Utilizamos el analizador sintáctico para buscar todas las posibles estructuras de la oración
for tree in parser.parse(tokens):
    # Mostramos la estructura encontrada
    print(tree)
