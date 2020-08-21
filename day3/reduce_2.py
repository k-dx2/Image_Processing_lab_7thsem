import numpy as np

import cv2 
import math
img= cv2.imread('image.jpeg', 0) 
print (img.shape)


rows=img.shape[0]
columns=img.shape[1]
colors=8
logCol=int(math.log(colors,2))
threshhold=2**(9-logCol)
threshhold=threshhold-1
dict={}
for i in range(rows):
    for j in range(columns):
        val=img[i][j]>>(8-logCol)
        img[i][j]=val*threshhold
       
list=[]
for i in range(8):
    list.append(img*(i+1))


index=7
print(img)
print(list[index])
cv2.imshow('image', list[index])
cv2.waitKey(0) 

