import cv2

# Cargar la imagen
imagen = cv2.imread('Doge.jpg')
cv2.imshow('Imagen ', imagen)

# Convertir la imagen en GRAY
imagen_gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow('GRAY', imagen_gray)

# Transformar la imagen en RGB
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', imagen_rgb)

# Cambiar la imagen en YUV
imagen_yuv = cv2.cvtColor(imagen, cv2.COLOR_BGR2YUV)
cv2.imshow('YUV', imagen_yuv)
cv2.waitKey(0)
cv2.destroyAllWindows()
