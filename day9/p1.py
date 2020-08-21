''' Write a program toapply a sequqence of following filtering operation on a noisyfingerprint image with a structuring element ofdimension 3x3 whose element are a1l 1.
 a.erosion
 b.opening of eroded image
 c.dilateion of result obtained by step(b)
 d. closing of the result obtained by (b)
 '''

import cv2 
import numpy as np


image = cv2.imread('image1.jpeg',0)
#ret,input_image=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
kernel = np.ones((3,3), np.uint8) 

erosion_image = cv2.erode(input_image, kernel, iterations=1)
opening_image = cv2.morphologyEx(erosion_image, cv2.MORPH_OPEN, kernel)
dilation_image = cv2.dilate(opening_image,kernel,iterations = 1)
closing_image=  cv2.morphologyEx(opening_image, cv2.MORPH_CLOSE, kernel)

cv2.imshow('1.Input', input_image)
cv2.imshow('2.Erosion', erosion_image)
cv2.imshow('3.Opening of Eroded image', opening_image)
cv2.imshow('4.Dilation', dilation_image)
cv2.imshow('5.Closing',closing_image)

cv2.waitKey(0)      
cv2.destroyAllWindows()
