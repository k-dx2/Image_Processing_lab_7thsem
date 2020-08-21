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

for i in range(w):
	for j in range(h):
		if img[j,i]>= 127:
			img1[j,i]=1
		else:
			img1[j,i]=0
				
		
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
			
			
			
			
cv2.imshow("result1",img1)
cv2.imshow("result2",img2)
#cv2.imshow("result3",img3)
#cv2.imshow("result4",img3)
#cv2.imshow("result5",img4)
#cv2.imshow("result6",img5)
#cv2.imshow("result7",img6)



cv2.waitKey(0)
cv2.destroyAllWindows()

