import numpy as np
import cv2
#Importar una imagen al entorno de trabajo.
image = cv2.imread('Doge.jpg')
cv2.imshow('Imagen', image)


#Segmentar la composición Blue, Green and Red (BGR).
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

#Cambiar el nivel de brillo y contraste del componente Blue.
contrast = 0.5
brightness = 0.8
for b in range(image.shape[0]):
    for g in range(image.shape[1]):
        blue = image [b] [g] [0]
        image [b] [g] [0] =(contrast*image[b][g][0]) + brightness
cv2.imshow('Blue Contrast', image)


#Variar el nivel de brillo y contraste del componente Green
contrast = 0.5
brightness = 0.8
for b in range(image.shape[0]):
    for g in range(image.shape[1]):
        green = image [b] [g] [1]
        image [b] [g] [1] =(contrast*image[b][g][1]) + brightness
cv2.imshow('Grenn Contrast', image)


#Modificar el nivel de brillo y contraste del componente Red.
contrast = 0.5
brightness = 0.8
for b in range(image.shape[0]):
    for g in range(image.shape[1]):
        red = image [b] [g] [2]
        image [b] [g] [2] =(contrast*image[b][g][2]) + brightness
cv2.imshow('Red Contrast', image)
