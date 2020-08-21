import cv2 
import numpy as np


img= cv2.imread('image.jpeg', 0) 

cv2.imshow("Original",img)

he=cv2.equalizeHist(img)
#hm=cv2.hist_match(img)

cv2.imshow("HistEqualisation",he)
#cv2.imshow("Histmatch",hm)

cv2.waitKey(0)
cv2.destroyAllWindows() 
