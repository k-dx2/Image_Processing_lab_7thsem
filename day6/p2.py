import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as img

img=img.imread("image.jpg")

plt.imshow(img,cmap='gray')
f = np.fft.fft2(img) 

fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))


plt.imshow(magnitude_spectrum,cmap='gray')
plt.show()




