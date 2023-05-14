import nltk

nltk.download('reuters')
from nltk.corpus import reuters
from nltk.probability import FreqDist

fdist = FreqDist(word.lower() for word in reuters.words())
