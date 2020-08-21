import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Fast Fourier Transform'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.hist(magnitude_spectrum.ravel(),256,[0,256])
plt.title('Histogram'), plt.xticks([]), plt.yticks([])
plt.show()
