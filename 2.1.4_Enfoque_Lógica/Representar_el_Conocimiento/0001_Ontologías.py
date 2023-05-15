from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF, RDFS

# Definimos las URIs para la ontología y los términos
ANIMAL = Namespace("http://example.com/animal/")
DOG = ANIMAL.Dog
CAT = ANIMAL.Cat
HAS_NAME = ANIMAL.hasName
HAS_COLOR = ANIMAL.hasColor
HAS_SOUND = ANIMAL.hasSound

# Creamos un grafo RDF
g = Graph()

# Añadimos los términos a la ontología
g.add((DOG, RDF.type, RDFS.Class))
g.add((CAT, RDF.type, RDFS.Class))

# Añadimos las propiedades a los términos
g.add((HAS_NAME, RDF.type, RDF.Property))
g.add((HAS_NAME, RDFS.domain, ANIMAL))
g.add((HAS_NAME, RDFS.range, RDFS.Literal))
g.add((HAS_COLOR, RDF.type, RDF.Property))
g.add((HAS_COLOR, RDFS.domain, ANIMAL))
g.add((HAS_COLOR, RDFS.range, RDFS.Literal))
g.add((HAS_SOUND, RDF.type, RDF.Property))
g.add((HAS_SOUND, RDFS.domain, ANIMAL))
g.add((HAS_SOUND, RDFS.range, RDFS.Literal))

# Añadimos información sobre algunos animales
g.add((DOG, HAS_NAME, "Fido"))
g.add((DOG, HAS_COLOR, "Brown"))
g.add((DOG, HAS_SOUND, "Bark"))
g.add((CAT, HAS_NAME, "Garfield"))
g.add((CAT, HAS_COLOR, "Orange"))
g.add((CAT, HAS_SOUND, "Meow"))

# Guardamos la ontología en un archivo
g.serialize(destination="animals.owl", format="turtle")
