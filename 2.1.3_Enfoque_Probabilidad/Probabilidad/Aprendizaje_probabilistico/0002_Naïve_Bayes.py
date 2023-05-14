from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Cargamos los datos de ejemplo
categorias = ['rec.autos', 'rec.motorcycles']
datos_entrenamiento = fetch_20newsgroups(subset='train', categories=categorias, shuffle=True, random_state=42)
datos_prueba = fetch_20newsgroups(subset='test', categories=categorias, shuffle=True, random_state=42)

# Vectorizamos los datos utilizando TfidfVectorizer
vectorizador = TfidfVectorizer()
vector_entrenamiento = vectorizador.fit_transform(datos_entrenamiento.data)
vector_prueba = vectorizador.transform(datos_prueba.data)

# Creamos el modelo de Naïve-Bayes y lo entrenamos
modelo = MultinomialNB()
modelo.fit(vector_entrenamiento, datos_entrenamiento.target)

# Realizamos la predicción en los datos de prueba
prediccion = modelo.predict(vector_prueba)

# Evaluamos la precisión del modelo
precision = accuracy_score(datos_prueba.target, prediccion)
print("Precisión del modelo:", precision)
