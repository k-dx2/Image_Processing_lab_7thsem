import cv2
import numpy as np
from scipy import ndimage

img=cv2.imread("img3.jpeg",0)

kernel=np.array([np.array([-1,-1,-1]),np.array([-1,8,-1]),np.array([-1,-1,-1])])

res=ndimage.convolve(img,kernel,mode='constant')

h=res.shape[0]
w=res.shape[1]

w=np.zeros([h,w],np.uint8)

for i in range(w):
	for j in range(h):
		if abs(res[j,i])==0:
			w[j,i]=0
		else:
			w[j,i]=255


cv2.imshow("result",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
			


