import cv2
import matplotlib.pyplot as plt
import numpy as np


img=cv2.imread("image3.jpeg",0)

ret,th_img=cv2.threshold(img,127,255,cv2.THRESH_BINARY);

flood=th_img.copy()
h,w=th_img.shape

mask=np.zeros((h+2,w+2),np.uint8)

cv2.floodFill(flood,mask,(0,0),255)

res=cv2.bitwise_not(flood)

res2=res|th_img

cv2.imshow("result",res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
