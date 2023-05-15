import nltk

# Descargar los recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Definir una oración de ejemplo
sentence = "John is eating an apple"

# Tokenizar la oración
tokens = nltk.word_tokenize(sentence)

# Identificar el tipo de cada palabra en la oración
pos_tags = nltk.pos_tag(tokens)

# Definir un lematizador
lemmatizer = nltk.WordNetLemmatizer()

# Identificar el lema de cada palabra en la oración
lemmas = []
for token, pos in pos_tags:
    wn_pos = nltk.corpus.wordnet.NOUN
    if pos.startswith('V'):
        wn_pos = nltk.corpus.wordnet.VERB
    elif pos.startswith('J'):
        wn_pos = nltk.corpus.wordnet.ADJ
    elif pos.startswith('R'):
        wn_pos = nltk.corpus.wordnet.ADV
    lemma = lemmatizer.lemmatize(token, pos=wn_pos)
    lemmas.append(lemma)

# Imprimir los resultados
print("Tokens:", tokens)
print("POS tags:", pos_tags)
print("Lemmas:", lemmas)
