import cv2
import numpy as np

img=cv2.imread("image.jpeg",0)
h=img.shape[0]
w=img.shape[1]
m=3

img1=np.zeros((m*h,m*w),dtype=np.uint8)




for i in range(w):
	for j in range(h):
		k=i*m
		l=j*m
		
		while(k<(i+1)*m and l<(j+1)*m):
			img1[k,l]=img[i,j]
			k=k+1
			l=l+1

cv2.imshow("result",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

		
