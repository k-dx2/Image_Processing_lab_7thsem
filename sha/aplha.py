import cv2

import matplotlib.pyplot as plt

import numpy as np

import random

def sp_noise(image,prob):

output=np.zeros(image.shape,np.uint8)

thres=1-prob

for i in range(image.shape[0]):

for j in range(image.shape[1]):

rdn=random.random()

if rdn <prob:

output[i][j]=0

elif rdn>thres:

output[i][j]=255

else:

output[i][j]=image[i][j]
return output

img=cv2.imread("messi.jpg",0)

noise_img=sp_noise(img,0.05)

plt.subplot(131)

plt.imshow(img,cmap='gray')

plt.title('original')

plt.xticks([]),plt.yticks([])

plt.subplot(132)

plt.imshow(noise_img,cmap='gray')

plt.title('noisy image')

plt.xticks([]),plt.yticks([])

plt.subplot(133)

plt.hist(noise_img[100:200,100:200].ravel(),255,[0,255])

plt.title('histogram')

plt.show()

cv2.waitKey(0)


