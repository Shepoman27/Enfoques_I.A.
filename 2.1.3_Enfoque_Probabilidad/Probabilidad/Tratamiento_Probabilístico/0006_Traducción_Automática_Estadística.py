import nltk
from nltk.translate import AlignedSent, Alignment, IBMModel1

# Corpus de ejemplo
corpus = [    AlignedSent(['this', 'is', 'a', 'test'], ['esto', 'es', 'una', 'prueba']),
    AlignedSent(['hello', 'world'], ['hola', 'mundo'])
]

# Entrenamiento del modelo de traducción estadística
ibm1 = IBMModel1(corpus, 5)

# Función de traducción de texto
def translate(texto, modelo):
    tokens = nltk.word_tokenize(texto.lower())
    traduccion = []
    for token in tokens:
        mejor_match = modelo.get(word, {}).keys()[0]
        traduccion.append(mejor_match)
    return ' '.join(traduccion)

# Ejemplo de uso
texto = "this is a test"
traduccion = translate(texto, ibm1)
print(traduccion)
