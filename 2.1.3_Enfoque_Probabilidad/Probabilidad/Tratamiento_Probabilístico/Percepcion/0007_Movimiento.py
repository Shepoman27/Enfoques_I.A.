import cv2

# Cargar el video de entrada
cap = cv2.VideoCapture('video.mp4')

# Inicializar el primer fotograma
_, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (21, 21), 0)
first_frame = gray

# Loop para procesar cada fotograma
while True:
    # Leer el fotograma actual
    ret, frame = cap.read()

    if not ret:
        break

    # Convertir a escala de grises y aplicar desenfoque
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Calcular la diferencia de fotogramas entre el fotograma actual y el primero
    frame_diff = cv2.absdiff(first_frame, gray)

    # Aplicar umbral binario para resaltar el movimiento
    thresh = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)[1]

    # Dilatar la imagen para cerrar los huecos en el movimiento
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Encontrar los contornos del objeto en movimiento
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar un rectángulo delimitador alrededor del objeto en movimiento
    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    # Mostrar el fotograma actual
    cv2.imshow('frame', frame)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
