from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

# Definición de namespaces
my_ns = Namespace("http://example.org/my_ns#")
FOAF = Namespace("http://xmlns.com/foaf/0.1/")

# Creación del grafo
g = Graph()

# Definición de la ontología
g.bind("my_ns", my_ns)
g.bind("foaf", FOAF)
g.add((my_ns.John, RDF.type, FOAF.Person))
g.add((my_ns.John, FOAF.name, Literal("John")))
g.add((my_ns.Mary, RDF.type, FOAF.Person))
g.add((my_ns.Mary, FOAF.name, Literal("Mary")))
g.add((my_ns.Mary, my_ns.hasFriend, my_ns.John))

# Definición de reglas
rule1 = """
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX my_ns: <http://example.org/my_ns#>
    CONSTRUCT {
        ?x my_ns:hasFriend ?y .
        ?y my_ns:hasFriend ?z .
    } WHERE {
        ?x foaf:knows ?y .
        ?y foaf:knows ?z .
    }
"""
rule2 = """
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX my_ns: <http://example.org/my_ns#>
    CONSTRUCT {
        ?x my_ns:hasBrother ?y .
    } WHERE {
        ?x foaf:gender "Male" .
        ?y foaf:gender "Male" .
        ?x foaf:parent ?z .
        ?y foaf:parent ?z .
    }
"""

# Aplicación de las reglas al grafo
g.update(rule1)
g.update(rule2)

# Consulta de información
qres = g.query("""
    PREFIX my_ns: <http://example.org/my_ns#>
    SELECT ?friend WHERE {
        my_ns.Mary my_ns:hasFriend ?friend .
    }
""")
for row in qres:
    print(row[0])
