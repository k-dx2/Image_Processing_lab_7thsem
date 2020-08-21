import cv2
import numpy as np

img=cv2.imread("image.jpg",1)

cv2.imshow("picture",img)
k=cv2.waitKey(0)

if k==27: #k==27 is the ascii value of esc
	cv2.destroyAllWindows()
elif k==ord('s'):
	cv2.imwrite("pic.png",img)
cv2.destroyAllWindows()
