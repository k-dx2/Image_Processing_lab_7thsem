import cv2
import matplotlib.pyplot as plt 
import numpy as np
import random

def rayleigh_noise(image):
	meanvalue=100
	modevalue=np.sqrt(2/np.pi)*meanvalue
	s=np.random.rayleigh(modevalue,(177,284))
	plt.hist(s.ravel(),255,[0,255])
	plt.title('exponential noise histogram')
	plt.show()
	noisy=image+s
	return noisy


img=cv2.imread("messi.jpg",0)
noise_img=rayleigh_noise(img)
plt.subplot(131)
plt.imshow(img,cmap='gray')
plt.xticks([]),plt.yticks([])
plt.title('Original')
plt.subplot(132)
plt.imshow(noise_img,cmap='gray')
plt.xticks([]),plt.yticks([])
plt.title('noisy image')
plt.subplot(133)
plt.hist(noise_img[100:200,100:200].ravel(),255,[0,255])
plt.title('histogram')
plt.show()
cv2.waitKey(0)
