import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("image.jpeg",0)
h=img.shape[0]
w=img.shape[1]

cv2.imshow("Original",img)

contrast=float(input("enter the Contrast"))

plt.hist(img.ravel(),256,[0,256])
plt.show()



for x in range(0,w):
	for y in range(0,h):
		img[y,x]=contrast*img[y,x]
		

plt.hist(img.ravel(),256,[0,256])
plt.show()

hm=cv2.equalizeHist(img)


plt.hist(hm.ravel(),256,[0,256])
plt.show()

cv2.imshow("Result",hm)
cv2.waitKey(0)
cv2.destroyAllWindows() 


