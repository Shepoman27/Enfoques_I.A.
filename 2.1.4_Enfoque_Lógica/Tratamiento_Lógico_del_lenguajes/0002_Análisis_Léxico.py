import nltk

# Descargar los recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Definir el texto de entrada
texto = "El análisis léxico es una tarea importante en el procesamiento de lenguaje natural."

# Tokenización de palabras
palabras = nltk.word_tokenize(texto)

# Etiquetado POS (Part-of-speech)
pos_tags = nltk.pos_tag(palabras)

# Imprimir los resultados
print("Palabras tokenizadas:", palabras)
print("Etiquetas POS:", pos_tags)
