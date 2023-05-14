import nltk
from nltk.corpus import treebank
from nltk.grammar import Nonterminal
from nltk.parse import pchart

nltk.download('treebank')
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V | V NP
    Det -> 'the'
    N -> 'cat' | 'dog'
    V -> 'runs' | 'barks'
""")

productions = []
for production in grammar.productions():
    if production.is_nonlexical():
        productions.append(nltk.ProbabilisticProduction(
            production.lhs(), production.rhs(), prob=1.0))
    else:
        productions.append(nltk.ProbabilisticProduction(
            production.lhs(), production.rhs(), prob=0.5))

pcfg = nltk.grammar.induce_pcfg(Nonterminal('S'), productions)
parser = pchart.InsideChartParser(pcfg)

sentence = 'the cat runs'
tokens = sentence.split()

for tree in parser.parse(tokens):
    print(tree)

prob = parser.probability(tokens)
print(prob)
