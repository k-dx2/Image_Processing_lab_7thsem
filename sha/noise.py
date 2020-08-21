import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('cat.jpg',0)
row, col = img.shape

gauss = np.random.normal(10,10,(row,col))
rayleigh = np.random.rayleigh(50,(row,col))
gamma = np.random.gamma(10,10,(row,col))
exponential = np.random.exponential(50,(row,col))
uniform = np.random.uniform(10,50,(row,col))

noisy = img + gauss
smooth_part = noisy[1:100,189:270]

plt.subplot(221),plt.imshow(smooth_part,cmap = 'gray')
plt.title('Smooth Part'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(noisy,cmap = 'gray')
plt.title('Noisy Image'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.hist(smooth_part.ravel(),256,[0,256])
plt.title('Smooth Part Histogram'), plt.xticks([]), plt.yticks([])

plt.subplot(224),plt.hist(noisy.ravel(),256,[0,256])
plt.title('Noisy Image Histogram'), plt.xticks([]), plt.yticks([])
plt.show()

