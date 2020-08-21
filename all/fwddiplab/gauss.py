import cv2
import matplotlib.pyplot as plt 
import numpy as np
import random

def gaussian_noise(image):
	row,col=image.shape
	mean=0
	var=250
	sigma=var**0.5
	gauss=np.random.normal(mean,sigma,(row,col))
	gauss=gauss.reshape(row,col)
	noisy=image+gauss
	return noisy


img=cv2.imread("messi.jpg",0)
noise_img=gaussian_noise(img)
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
