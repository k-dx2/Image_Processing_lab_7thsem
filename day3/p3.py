'''3. WAP to transform 256 geray level image into 8 different gary levels and then multiply 1,2,3.. with 8 different gary levels in decreascing  order. Display the output image'''

import cv2
import numpy as np

img=cv2.imread("image.jpeg",0)

h=img.shape[0]
w=img.shape[1]



for x in range(0,w):
	for y in range(0,h):
		if img[y,x]>=0 and img[y,x]<=31:
			img[y,x]=15
		if img[y,x]>=32 and img[y,x]<=63:
			img[y,x]=47
		if img[y,x]>=64 and img[y,x]<=91:
			img[y,x]=77
		if img[y,x]>=92 and img[y,x]<=123:
			img[y,x]=107		
		if img[y,x]>=124 and img[y,x]<=155:
		 	img[y,x]=139
		if img[y,x]>=156 and img[y,x]<=187:
			img[y,x]=171
		if img[y,x]>=188 and img[y,x]<=219:
			img[y,x]=203
		if img[y,x]>=220 and img[y,x]<=255:
			img[y,x]=237
			

cv2.imshow("image1",img)

for x in range(0,w):
	for y in range(0,h):
	    img[y,x]=img[y,x]*2;

cv2.imshow("image2",img)


for x in range(0,w):
	for y in range(0,h):
	    img[y,x]=(img[y,x]*3)/2;

cv2.imshow("image3",img)

	    
for x in range(0,w):
	for y in range(0,h):
	    img[y,x]=(img[y,x]*4)/3;

cv2.imshow("image4",img)
	    
for x in range(0,w):
	for y in range(0,h):
	    img[y,x]=(img[y,x]*5)/4;

cv2.imshow("image5",img)

	    
for x in range(0,w):
	for y in range(0,h):
	    img[y,x]=(img[y,x]*6)/5;

cv2.imshow("image6",img)
	    
for x in range(0,w):
	for y in range(0,h):
	    img[y,x]=(img[y,x]*7)/6;

cv2.imshow("image7",img)

for x in range(0,w):
	for y in range(0,h):
	    img[y,x]=(img[y,x]*8)/7;

cv2.imshow("image8",img)
	    


	
			

cv2.waitKey(0)
cv2.destroyAllWindows() 
