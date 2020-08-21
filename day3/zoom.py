import numpy as np

import cv2 
import math
img= cv2.imread('image.jpeg', 0) 
magnification=2
img_zoom = np.ones( (img.shape[0]*magnification, img.shape[1]*magnification), dtype=np.uint8 )

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        k=i*magnification
        l=j*magnification
        while(k<(i+1)*magnification and l<(j+1)*magnification):
            img_zoom[k][l]=img[i][j]
            k=k+1
            l=l+1


cv2.imshow('image', img_zoom)
cv2.waitKey(0) 
cv2.destroyAllWindows()


