'''
int num_colors = 4;
int divisor = 256 / num_colors;
int max_quantized_value = 255 / divisor;
int new_value = ((value / divisor) * 255) / max_quantized_value;
'''

import cv2
import numpy as np

img=cv2.imread("image.jpeg",0)
cv2.imshow("original",img)



h=img.shape[0]
w=img.shape[1]

img1=np.zeros((h,w))
img2=np.zeros((h,w),dtype=np.uint8)
img3=np.zeros((h,w),dtype=np.uint8)
img4=np.zeros((h,w),dtype=np.uint8)
img5=np.zeros((h,w),dtype=np.uint8)
img6=np.zeros((h,w),dtype=np.uint8)
img7=np.zeros((h,w),dtype=np.uint8)



#2
for i in range(w):
	for j in range(h):
		if img[j,i]>= 127:
			img1[j,i]=1
		else:
			img1[j,i]=0
				
#4		
for i in range(w):
	for j in range(h):
		if img[j,i]>=192:
			img2[j,i]=223
		elif img[j,i]>=128 and img[j,i]<=191:
			img2[j,i]=159
		elif img[j,i]>=64 and img[j,i]<=127:
			img2[j,i]=95
		else:
			img2[j,i]=31
			
#8			
for i in range(w):
	for j in range(h):
		x=img[i,j]/32  #divided by 32 since interval is of size 32 ie 0-31,32-63,....
		img3[i,j]=x*32+256/(8*2)
		
#16
for i in range(w):
	for j in range(h):
		x=img[i,j]/16  
		img4[i,j]=x*16+256/(16*2)

#32
for i in range(w):
	for j in range(h):
		x=img[i,j]/8  
		img5[i,j]=x*8+256/(32*2)
#64
for i in range(w):
	for j in range(h):
		x=img[i,j]/4  
		img6[i,j]=x*4+256/(64*2)
#128
for i in range(w):
	for j in range(h):
		x=img[i,j]/2  
		img7[i,j]=x*2+256/(128*2)
			


			
cv2.imshow("result1",img1)
cv2.imshow("result2",img2)
cv2.imshow("result3",img3)
cv2.imshow("result4",img4)
cv2.imshow("result5",img4)
cv2.imshow("result6",img5)
cv2.imshow("result7",img6)



cv2.waitKey(0)
cv2.destroyAllWindows()

