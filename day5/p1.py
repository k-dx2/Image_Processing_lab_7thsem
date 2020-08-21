import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

def convolution2d(image, kernel):
    m, n = kernel.shape
    if (m == n):
        y, x = image.shape
        y = y - m + 1
        x = x - m + 1
        new_image = np.zeros((y,x),dtype=np.uint8)
        for i in range(y):
            for j in range(x):
                new_image[i][j] = np.sum(image[i:i+m, j:j+m]*kernel)
                
    return new_image

x = cv2.imread('image.jpeg',0)
print(x)

#1
kernel1= np.ones((3,3),np.float32)/9

#2
kernel2a=np.array([[-1,0,1],[-2,0,2],[-1,0,1]],dtype='float')
kernel2b=np.array([[1,2,1],[0,0,0],[-1,-2,-1]],dtype='float')
kernel2c=np.array([[0,0,0],[0,0,0],[0,0,0]],dtype='float')
kernel2d=np.array([[0,0,0],[0,0,0],[0,0,0]],dtype='float')

#3
kernel3a=np.array([[1,0],[0,-1]],dtype='float')
kernel3b=np.array([[0,1],[-1,0]],dtype='float')
kernel3c=np.array([[0,0],[0,0]],dtype='float')

#4
kernel4a=np.array([[-1,0,1],[-1,0,1],[-1,0,1]],dtype='float')
kernel4b=np.array([[1,1,1],[0,0,0],[-1,-1,-1]],dtype='float')




for i in range(0,3):
	for j in range (0,3):
		kernel2c[i][j]=math.sqrt(kernel2a[i][j]**2+kernel2b[i][j]**2)


for i in range(0,3):
	for j in range (0,3):
		kernel2d[i][j]=math.atan(kernel2b[i][j]/kernel2a[i][j])
		
		
for i in range(0,2):
	for j in range (0,2):
		kernel3c[i][j]=math.sqrt(kernel3a[i][j]**2+kernel3b[i][j]**2)



f1= convolution2d(x, kernel1)

f2a= convolution2d(x, kernel2a)
f2b= convolution2d(x, kernel2b)	
f2c= convolution2d(x, kernel2c)
f2d= convolution2d(x, kernel2d)

f3a= convolution2d(x, kernel3a)
f3b= convolution2d(x, kernel3b)
f3c= convolution2d(x, kernel3c)

f4a= convolution2d(x, kernel4a)
f4b= convolution2d(x, kernel4b)

			


print(f1)
plt.imshow(f1,cmap='gray')
plt.show()

print(f2a)
plt.imshow(f2a,cmap='gray')
plt.show()

print(f2b)
plt.imshow(f2b,cmap='gray')
plt.show()

print(f2c)
plt.imshow(f2c,cmap='gray')
plt.show()

print(f2d)
plt.imshow(f2d,cmap='gray')
plt.show()
    
print(f3a)
plt.imshow(f3a,cmap='gray')
plt.show()

print(f3b)
plt.imshow(f3b,cmap='gray')
plt.show()


print(f4a)
plt.imshow(f4a,cmap='gray')
plt.show()

print(f4b)
plt.imshow(f4b,cmap='gray')
plt.show()


