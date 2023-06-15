import numpy as np
import cv2
#Importar una imagen al entorno de trabajo.
image = cv2.imread('Doge.jpg')
cv2.imshow('Image', image)

# Segmentar la composición Blue, Green and Red (BGR).
image_bgr = cv2.split(image)
image_blue = image_bgr[0]
print(image_blue.shape)
cv2.imshow('Azul', image_blue)
image_green = image_bgr[1]
print(image_green.shape)
cv2.imshow('Verde', image_green)
image_red = image_bgr[2]
print(image_red.shape)
cv2.imshow('Rojo', image_red)
print()
# Encontrar el histograma del componente Blue.
histogram_size = 256
histogram_range = (0, histogram_size)
accumulate = False
histogram_blue = cv2.calcHist(image_bgr, [0], None, [histogram_size],histogram_range, accumulate=accumulate)
histogram_w = histogram_size*2
histogram_h = histogram_size*2
bin_w = int(round(histogram_w/histogram_size))
histogram_image = np.zeros((histogram_h, histogram_w, 3), dtype=np.uint8)



# Calcular el histograma del componente Green.
histogram_size = 256
histogram_range = (0, histogram_size)
accumulate = False
histogram_green = cv2.calcHist(image_bgr, [1], None, [histogram_size],histogram_range, accumulate=accumulate)
histogram_w = histogram_size*2
histogram_h = histogram_size*2
bin_w = int(round(histogram_w/histogram_size))
histogram_image = np.zeros((histogram_h, histogram_w, 3), dtype=np.uint8)



# Determinar el histograma del componente Red.
histogram_size = 256
histogram_range = (0, histogram_size)
accumulate = False
histogram_red = cv2.calcHist(image_bgr, [2], None, [histogram_size],histogram_range, accumulate=accumulate)
histogram_w = histogram_size*2
histogram_h = histogram_size*2
bin_w = int(round(histogram_w/histogram_size))
histogram_image = np.zeros((histogram_h, histogram_w, 3), dtype=np.uint8)



# Aplicar el equailizador de histograma.
histogram_equalization_blue = cv2.equalizeHist(image_blue)
cv2.imshow('E_Azul ', histogram_equalization_blue)
histogram_equalization_green = cv2.equalizeHist(image_green)
cv2.imshow('E_Verde ', histogram_equalization_green)
histogram_equalization_red = cv2.equalizeHist(image_red)
cv2.imshow('E_Rojo', histogram_equalization_red)

