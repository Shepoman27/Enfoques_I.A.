import nltk
from nltk.corpus import treebank
from nltk.grammar import PCFG, induce_pcfg
from nltk.parse import ViterbiParser

nltk.download('treebank')
productions = []
for sentence in treebank.parsed_sents():
    productions += sentence.productions()

pcfg = induce_pcfg(start=productions[0].lhs(), productions=productions)
parser = ViterbiParser(pcfg)

sentence = 'I saw the man in the park with a telescope'
tokens = sentence.split()

for tree in parser.parse(tokens):
    print(tree)

prob = parser.probability(tokens)
print(prob)
