import cv2 
import numpy as np 

img = cv2.imread('finger.jpg', 0) 

kernel = np.ones((3,3), np.uint8) 

img_erosion = cv2.erode(img, kernel, iterations=1) 

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

img_dilation = cv2.dilate(img, kernel, iterations=1) 

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Input', img) 
cv2.waitKey(0) 

cv2.imshow('opening', opening)
cv2.waitKey(0) 

cv2.imshow('Erosion', img_erosion) 
cv2.waitKey(0) 

cv2.imshow('Dilation', img_dilation) 
cv2.waitKey(0) 

cv2.imshow('closing', closing)
cv2.waitKey(0) 

cv2.destroyAllWindows()

