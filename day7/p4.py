import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('image.jpg',0)


dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

#fourier = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

plt.imshow(img, cmap = 'gray')
plt.show()
histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
plt.plot(histr) 
plt.show() 
#plt.imshow(fourier, cmap = 'gray')
#plt.show()



rows, cols = img.shape
crow,ccol = rows/2 , cols/2

# create a mask first, center square is 1, remaining all zeros
#lowpass filter
mask1 = np.zeros((rows,cols,2),np.uint8)
mask1[crow-30:crow+30, ccol-30:ccol+30] = 1
print("lowpass filter",mask1)

mask2 = np.ones((rows,cols,2),np.uint8)
mask2[crow-30:crow+30, ccol-30:ccol+30] = 0
print("highpass filter",mask2)

# apply mask and inverse DFT
#highpass filter
fshift1 = dft_shift*mask1
f_ishift1 = np.fft.ifftshift(fshift1)
img_back1= cv2.idft(f_ishift1)
img_back1 = cv2.magnitude(img_back1[:,:,0],img_back1[:,:,1])

plt.imshow(img_back1, cmap = 'gray')
plt.show()


fshift2 = dft_shift*mask2
f_ishift2 = np.fft.ifftshift(fshift2)
img_back2 = cv2.idft(f_ishift2)
img_back2= cv2.magnitude(img_back2[:,:,0],img_back2[:,:,1])
plt.imshow(img_back2, cmap = 'gray')
plt.show()


