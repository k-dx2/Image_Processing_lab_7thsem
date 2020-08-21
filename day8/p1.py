'''
Write a program to estimate a noise function in a noisy image displaying histogram of a sub region of the given input image.

HINT- Add some noise  such as Gaussian, Rayliegh,gamma ,exponential,uniform noise and then have the histogram of the corresponding patches or the sub region of the given image

'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("image.jpg",0)
mean = 0
var = 10
sigma = var ** 0.5

gaussian = np.random.normal(mean, sigma, (512,512)) 
uniform = np.zeros((512,512),dtype=np.uint8)
cv2.randu(uniform,0,255)

noisy_image1 = np.zeros(img.shape, np.float32)
noisy_image2 = np.zeros(img.shape, np.float32)

noisy_image1=img+15*gaussian
noisy_image2=img+uniform


cv2.normalize(noisy_image1, noisy_image1, 0, 255, cv2.NORM_MINMAX, dtype=-1)
noisy_image1 = noisy_image1.astype(np.uint8)

cv2.normalize(noisy_image2, noisy_image2, 0, 255, cv2.NORM_MINMAX, dtype=-1)
noisy_image2 = noisy_image2.astype(np.uint8)


cv2.imshow("img", img)
cv2.imshow("gaussian", gaussian)
cv2.imshow("uniform", uniform)

cv2.imshow("noisy1", noisy_image1)
cv2.imshow("noisy2", noisy_image2)
cv2.waitKey(0)

plt.hist(img .ravel(),256,[0,256])
plt.show()


plt.hist(noisy_image1.ravel(),256,[0,256])
plt.show()

plt.hist(noisy_image2.ravel(),256,[0,256])
plt.show()
