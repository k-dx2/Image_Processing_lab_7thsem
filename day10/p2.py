''' Write a program to detect the lines inn horizontal and verticle directions in the given image with suitable masks'''

import cv2
import numpy as np
from scipy import ndimage


image = cv2.imread('img1.jpeg',0)
cv2.imshow("original",image)

kernel_laplace1 = np.array([np.array([-1, -1, -1]), np.array([2, 2, 2]), np.array([-1, -1, -1])])
print(kernel_laplace1, 'is for horizontal')


out_h = ndimage.convolve(image , kernel_laplace1, mode='reflect')

kernel_laplace2 = np.array([np.array([-1, 2, -1]), np.array([-1, 2, -1]), np.array([-1, 2, -1])])
print(kernel_laplace2, 'is for verical')

out_v = ndimage.convolve(image , kernel_laplace2, mode='reflect')

cv2.imshow("Horizontal",out_h)
cv2.imshow("Vertical",out_v)

cv2.waitKey(0)
cv2.destroyAllWindows()
