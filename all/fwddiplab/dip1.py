import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mplimg

img=cv2.imread("../Desktop/labimg.jpg",0)
cv2.imshow("image",img)
k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()
elif k == ord('s'):
	img1=cv2.imwrite("../Desktop/dip1.png",img)
	cv2.destroyAllWindows()
