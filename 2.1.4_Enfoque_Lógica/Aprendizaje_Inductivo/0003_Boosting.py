from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Generar datos sintéticos para clasificación binaria
X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=1)

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Crear clasificador base
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(max_depth=1, random_state=1)

# Crear clasificador Boosting
boost = AdaBoostClassifier(base_estimator=clf, n_estimators=100, learning_rate=1.0, random_state=1)

# Entrenar el clasificador Boosting
boost.fit(X_train, y_train)

# Evaluar el clasificador Boosting en el conjunto de prueba
score = boost.score(X_test, y_test)

print("Exactitud en el conjunto de prueba: {:.2f}%".format(score * 100))
