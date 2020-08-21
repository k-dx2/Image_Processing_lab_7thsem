import cv2
import matplotlib.pyplot as plt 
import numpy as np
import random

def uniform_noise(image):
	row,col=image.shape
	uniform=np.random.uniform(0,100,(row,col))
	plt.hist(uniform.ravel(),255,[0,255])
	plt.title('uniform noise histogram')
	plt.show()
	#gauss=gauss.reshape(row,col)
	noisy=image+uniform
	return noisy


img=cv2.imread("messi.jpg",0)
noise_img=uniform_noise(img)
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
