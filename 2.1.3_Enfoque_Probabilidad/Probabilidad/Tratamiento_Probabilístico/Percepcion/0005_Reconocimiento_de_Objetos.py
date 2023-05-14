import cv2

# Cargamos las imagenes que utilizaremos para entrenamiento
imagen1 = cv2.imread("imagen1.jpg")
imagen2 = cv2.imread("imagen2.jpg")
imagen3 = cv2.imread("imagen3.jpg")

# Convertimos las imágenes a escala de grises
gray1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(imagen3, cv2.COLOR_BGR2GRAY)

# Creamos un detector de características SUR
surf = cv2.xfeatures2d.SURF_create()

# Detectamos las características en las imágenes de entrenamiento
kp1, des1 = surf.detectAndCompute(gray1, None)
kp2, des2 = surf.detectAndCompute(gray2, None)
kp3, des3 = surf.detectAndCompute(gray3, None)

# Creamos un objeto FLANN (Fast Library for Approximate Nearest Neighbors)
flann = cv2.FlannBasedMatcher()

# Hacemos la comparación de las características entre las imágenes de entrenamiento y la imagen de prueba
kp_test, des_test = surf.detectAndCompute(gray_test, None)
matches1 = flann.knnMatch(des1, des_test, k=2)
matches2 = flann.knnMatch(des2, des_test, k=2)
matches3 = flann.knnMatch(des3, des_test, k=2)

# Creamos una lista con las coincidencias encontradas en las imágenes de entrenamiento
good_matches1 = []
good_matches2 = []
good_matches3 = []
for m, n in matches1:
    if m.distance < 0.7 * n.distance:
        good_matches1.append(m)
for m, n in matches2:
    if m.distance < 0.7 * n.distance:
        good_matches2.append(m)
for m, n in matches3:
    if m.distance < 0.7 * n.distance:
        good_matches3.append(m)

# Si se encontraron suficientes coincidencias en alguna de las imágenes de entrenamiento, consideramos que se encontró un objeto
if len(good_matches1) > 10:
    print("Objeto encontrado en la imagen 1")
elif len(good_matches2) > 10:
    print("Objeto encontrado en la imagen 2")
elif len(good_matches3) > 10:
    print("Objeto encontrado en la imagen 3")
else:
    print("Objeto no encontrado")
