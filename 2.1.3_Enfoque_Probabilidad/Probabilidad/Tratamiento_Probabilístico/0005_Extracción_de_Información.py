import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
from nltk.chunk import RegexpParser
from nltk.tree import Tree

# Cargar texto
text = "La Universidad Nacional Autónoma de México (UNAM) es una universidad pública mexicana. Es la más grande e importante de México, así como una de las más importantes de América Latina."

# Tokenizar palabras
tokens = word_tokenize(text)

# Eliminar stopwords y realizar stemming
stop_words = set(stopwords.words('spanish'))
ps = PorterStemmer()
clean_tokens = []
for token in tokens:
    if token.lower() not in stop_words:
        clean_tokens.append(ps.stem(token))

# Calcular frecuencia de cada palabra
freq = FreqDist(clean_tokens)

# Obtener las palabras más comunes
most_common = freq.most_common(5)

# Mostrar resultados
print("Palabras más comunes:")
for word, count in most_common:
    print(word, "-", count)

# Tokenizar oraciones
sentences = sent_tokenize(text)

# Definir patrones para extraer información
patterns = '''
    NP: {<DT>?<JJ>*<NN>*}
    VP: {<VB.*><NP|PP|CLAUSE>+$}
    CLAUSE: {<NP><VP>}
'''

# Procesar cada oración
for sentence in sentences:
    # Tokenizar palabras
    words = word_tokenize(sentence)
    # Eliminar stopwords y realizar stemming
    clean_words = []
    for word in words:
        if word.lower() not in stop_words:
            clean_words.append(ps.stem(word))
    # Analizar la estructura gramatical de la oración
    parser = RegexpParser(patterns)
    tree = parser.parse(nltk.pos_tag(clean_words))
    # Extraer información de la estructura gramatical
    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            print('Nombre:', ' '.join([word for word, tag in subtree.leaves()]))
        if subtree.label() == 'VP':
            print('Verbo:', ' '.join([word for word, tag in subtree.leaves()]))
