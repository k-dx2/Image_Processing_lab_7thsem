''' Write a program to detect the point in the given gray level image with a suitable mask'''


import cv2
import numpy as np
from scipy import ndimage


image = cv2.imread('img3.jpeg',0)
cv2.imshow("original",image)

kernel_laplace1 = np.array([np.array([-1, -1, -1]), np.array([-1,6, -1]), np.array([-1, -1, -1])])
print(kernel_laplace1, 'point detection')


out_h = ndimage.convolve(image , kernel_laplace1, mode='constant')
print(out_h)
h=image.shape[0]
w=image.shape[1]

image_h = np.empty([h,w],dtype="uint8") 
	 		
for x in range(0,w):
	for y in range(0,h):
		if abs(out_h[y,x])==0:
			image_h[y,x]=255
		else :
			image_h[y,x]=0
			




cv2.imshow("Point ",image_h)
cv2.waitKey(0)
cv2.destroyAllWindows()
