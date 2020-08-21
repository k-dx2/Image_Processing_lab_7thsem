'''use cross structing element for region filling
    0 1 0 
    1 1 1
    0 1 0
    '''
    
import cv2 
import numpy as np


image1 = cv2.imread('image3.jpeg',0)
image2= cv2.imread('image3.jpeg',0)
#kernel = np.ones((3,3), np.uint8) 

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
h=image1.shape[0]
w=image1.shape[1]

for x in range(0,w):
	for y in range(0,h):
		image2[y,x]=255-image2[y,x]
		

prev=image1
curr=np.empty([h,w])
invert=image2

while(True):
	res=cv2.dilate(prev,kernel,iterations = 1)
	curr= cv2.bitwise_and(res,invert)
	
	if prev.all()==curr.all():
		break
	
	prev=curr
	
	

f=cv2.bitwise_or(image1,curr)

cv2.imshow('Input',image1)
cv2.imshow('Region fill',f)

cv2.waitKey(0)      
cv2.destroyAllWindows()
