import cv2
import numpy as np

# Cargar imagen
img = cv2.imread('imagen.jpg', 0)

# Aplicar filtro Sobel
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
grad = np.sqrt(sobelx**2 + sobely**2)

# Aplicar umbralización Otsu
th, thresh = cv2.threshold(grad, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Mostrar resultados
cv2.imshow('Original', img)
cv2.imshow('Gradiente', grad)
cv2.imshow('Umbralización', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
