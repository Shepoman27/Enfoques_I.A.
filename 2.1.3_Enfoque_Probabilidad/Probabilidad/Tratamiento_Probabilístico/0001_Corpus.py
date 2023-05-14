import re
import nltk
from collections import defaultdict
from nltk.probability import LidstoneProbDist
from nltk.tokenize import word_tokenize, sent_tokenize

# Descargar el corpus de prueba
nltk.download('gutenberg')

# Cargar el corpus de prueba
corpus = nltk.corpus.gutenberg.raw('shakespeare-hamlet.txt')

# Preprocesamiento del corpus
corpus = corpus.lower() # convertir a minúsculas
corpus = re.sub(r'\d+', '', corpus) # eliminar números
corpus = re.sub(r'[^\w\s]', '', corpus) # eliminar signos de puntuación

# Tokenizar el corpus en oraciones y palabras
sentences = sent_tokenize(corpus)
tokens = [word_tokenize(sent) for sent in sentences]

# Crear una lista de vocabulario
vocab = list(set([word for sent in tokens for word in sent]))

# Calcular la frecuencia de las palabras
word_freq = defaultdict(int)
for sent in tokens:
    for word in sent:
        word_freq[word] += 1

# Crear una matriz de frecuencia de palabras
word_matrix = []
for sent in tokens:
    row = []
    for word in vocab:
        row.append(sent.count(word))
    word_matrix.append(row)

# Entrenar el modelo utilizando Lidstone smoothing
lp = LidstoneProbDist(1.0, len(vocab))
model = {}
for i, word in enumerate(vocab):
    model[word] = lp.freq(word_matrix[j][i] for j in range(len(sentences)))
