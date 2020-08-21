import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('image.jpg',0)

dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

y = 20* np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

plt.imshow(img,cmap='gray')
plt.show()

plt.imshow(y,cmap='gray')
plt.show()

histr = cv2.calcHist([y],[0],None,[256],[0,256]) 
  
plt.plot(histr) 
plt.show() 

