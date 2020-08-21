import cv2
import numpy as np
from scipy import ndimage

image = cv2.imread('img2.jpeg',0)
cv2.imshow("original",image)

'''sobel_horizontal = np.array([np.array([1, 2, 1]), np.array([0, 0, 0]), np.array([-1, -2, -1])])
print(sobel_horizontal, 'is a kernel for detecting horizontal edges')
 
sobel_vertical = np.array([np.array([-1, 0, 1]), np.array([-2, 0, 2]), np.array([-1, 0, 1])])
print(sobel_vertical, 'is a kernel for detecting vertical edges')

out_h = ndimage.convolve(image,sobel_horizontal, mode='reflect')
out_v = ndimage.convolve(image, sobel_vertical, mode='reflect')
'''

kernel_laplace = np.array([np.array([-1, -1, -1]), np.array([-1, 8, -1]), np.array([-1, -1, -1])])
print(kernel_laplace, 'is a laplacian kernel')


out_l = ndimage.convolve(image , kernel_laplace, mode='constant')

cv2.imshow("  result",out_l)
cv2.waitKey(0)
cv2.destroyAllWindows()
