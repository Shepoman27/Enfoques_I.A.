import cv2
import numpy as np

# Cargamos la imagen
img = cv2.imread('ejemplo.jpg')

# Aplicamos el filtrado Gaussiano
img_filtrada = cv2.GaussianBlur(img, (5, 5), 0)

# Convertimos la imagen a escala de grises
img_gris = cv2.cvtColor(img_filtrada, cv2.COLOR_BGR2GRAY)

# Detectamos bordes con la transformada de Sobel
sobelx = cv2.Sobel(img_gris, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img_gris, cv2.CV_64F, 0, 1, ksize=5)

# Aplicamos la detección de sombras y texturas
sombra = np.zeros_like(img_gris)
textura = np.zeros_like(img_gris)

for i in range(img_gris.shape[0]):
    for j in range(img_gris.shape[1]):
        if sobelx[i][j] > 50 or sobely[i][j] > 50:
            textura[i][j] = 255
        if img_gris[i][j] < 100 and sobelx[i][j] < 50 and sobely[i][j] < 50:
            sombra[i][j] = 255

# Mostramos las imágenes resultantes
cv2.imshow('Imagen original', img)
cv2.imshow('Imagen filtrada', img_filtrada)
cv2.imshow('Bordes detectados', sobelx + sobely)
cv2.imshow('Sombra detectada', sombra)
cv2.imshow('Textura detectada', textura)
cv2.waitKey(0)
cv2.destroyAllWindows()
