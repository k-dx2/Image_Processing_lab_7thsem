import cv2
import numpy as np

img=cv2.imread("image.jpg",1)

h=img.shape[0]
w=img.shape[1]

for x in range(0,w):
	for y in range(0,h):
		img[y,x,0]=255 #0-blue 1-green 2-red

cv2.imshow("intensity",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
