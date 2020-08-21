import cv2
import numpy as np


img=cv2.imread("image.jpeg",0)

h=img.shape[0]
w=img.shape[1]

m=0.8 
nh=int(h*m)
nw=int(w*m)

dim=(nh,nw)

img1=cv2.resize(img,dim)
cv2.imshow("res",img1)
cv2.waitKey(0) 
