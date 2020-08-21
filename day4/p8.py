import cv2
import math
import numpy as np

img=cv2.imread("image.jpeg",0)
negative=cv2.imread("image.jpeg",0)
logt=cv2.imread("image.jpeg",0)
power=cv2.imread("image.jpeg",0)

h=img.shape[0]
w=img.shape[1]

cv2.imshow("Original",img)

for x in range(0,w):
	for y in range(0,h):
		negative[y,x]=255-img[y,x]
		logt[y,x]=50*math.log(1+img[y,x])
		power[y,x]=img[y,x]**0.9


cv2.imshow("Negative",negative)
cv2.imshow("Log",logt)
cv2.imshow("Power",power)
cv2.waitKey(0)
cv2.destroyAllWindows() 
