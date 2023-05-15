import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import treebank

# Preprocesamiento de los datos
sentences = treebank.tagged_sents()
data = []
for sentence in sentences:
    tokens = [word.lower() for word, tag in sentence]
    tags = [tag for word, tag in sentence]
    data.append((tokens, tags))

# Entrenamiento del modelo
trainer = nltk.tag.hmm.HiddenMarkovModelTrainer()
tagger = trainer.train_supervised(data)

# Ejemplo de uso del modelo
sentence = "I am learning about natural language processing"
tokens = word_tokenize(sentence.lower())
tags = tagger.tag(tokens)
print(tags)
