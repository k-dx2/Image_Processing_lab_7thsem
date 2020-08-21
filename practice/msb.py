import cv2
import numpy as np

img=cv2.imread("image.jpeg",0)
h=img.shape[0]
w=img.shape[1]

lst=[]

for i in range(w):
	for j in range(h):
		lst.append(np.binary_repr(img[i,j],width=8))


eightbi=(np.array([int(i[0]) for i in lst],dtype=np.uint8)*128).reshape(h,w)
sevenbi=(np.array([int(i[1]) for i in lst],dtype=np.uint8)*64).reshape(h,w)
sixbi=(np.array([int(i[2]) for i in lst],dtype=np.uint8)*32).reshape(h,w)
fivebi=(np.array([int(i[3]) for i in lst],dtype=np.uint8)*16).reshape(h,w)
fourbi=(np.array([int(i[4]) for i in lst],dtype=np.uint8)*8).reshape(h,w)
threebi=(np.array([int(i[5]) for i in lst],dtype=np.uint8)*4).reshape(h,w)
twobi=(np.array([int(i[6]) for i in lst],dtype=np.uint8)*2).reshape(h,w)
onebi=(np.array([int(i[7]) for i in lst],dtype=np.uint8)*1).reshape(h,w)


res1=img-(onebi+twobi+threebi+fourbi)

cv2.imshow("1",res1)

m1=cv2.equalizeHist(res1)

cv2.imshow("2",m1)

res2=img-(eightbi+sevenbi+sixbi+fivebi)

cv2.imshow("3",res2)

m2=cv2.equalizeHist(res2)

cv2.imshow("4",m2)


cv2.waitKey(0)
cv2.destroyAllWindows()

