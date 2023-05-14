from keras.models import Sequential
from keras.layers import Dense

# Crear modelo de red neuronal
model = Sequential()

# Agregar capas de neuronas
model.add(Dense(64, activation='relu', input_dim=100))
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Compilar modelo
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Entrenar modelo
model.fit(x_train, y_train,
          epochs=5,
          batch_size=32,
          validation_data=(x_test, y_test))

# Evaluar modelo
score = model.evaluate(x_test, y_test, batch_size=32)
print("Loss:", score[0])
print("Accuracy:", score[1])
