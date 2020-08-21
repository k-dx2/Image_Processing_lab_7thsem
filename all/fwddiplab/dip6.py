import cv2
import numpy as np 
def modifyBit(n):
    for p in range(4, 8):
       mask = 1 << p
       n = (n & ~mask) | ((0 << p) & mask)
    return n
    
img = cv2.imread('1.jpg', 0)
img2 = cv2.imread('1.jpg', 0)

for i in range(img2.shape[0]):
   for j in range(img2.shape[1]):
      #print(img2[i][j])
      img2[i][j]  = modifyBit(img2[i][j])
      #print("changed :", img2[i][j])

sub = cv2.subtract(img, img2)
#print(sub)
equ = cv2.equalizeHist(sub) 
res = np.hstack((img, sub, equ)) 
cv2.imshow('image', res)
cv2.waitKey(0) 
#cv2.imshow('image', equ)
cv2.destroyAllWindows()
