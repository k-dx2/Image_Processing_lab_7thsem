#q6

# from scipy.fftpack import fft

import numpy as np 
import cv2
import math as mt
import matplotlib.pyplot as plt
# import cmath 


img = cv2.imread('./black_rose.jpg', 0)
# print(img)

new_image=np.fft.fft2(img)
fshift = np.fft.fftshift(new_image)
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.imshow(magnitude_spectrum)
plt.show()
cv2.waitKey(0)

# cv2.destroyAllWindows() 

output=np.fft.ifft(new_image)
print(output)

hist_orig = cv2.calcHist([img],[0],None,[256],[0,256]) 
# hist_new = cv2.calcHist([magnitude_spectrum],[0],None,[256],[0,256]) 
# print(magnitude_spectrum)

# hist_match=cv2.compareHist(hist_orig, hist_new,) 
# plt.plot(hist_match)
plt.plot(hist_orig,'r')
# plt.plot(hist_new,'b')
plt.show()