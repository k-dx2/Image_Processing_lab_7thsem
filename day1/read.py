import cv2
import numpy as np

img=cv2.imread("image.jpg",1)

cv2.imshow("picture",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

