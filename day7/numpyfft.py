import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("image.jpg",0)
plt.imshow(img,cmap='gray')
plt.show()

f=np.fft.fft2(img)
hpf_fshift=np.fft.fftshift(f)
lpf_fshift=np.fft.fftshift(f)

ms=20*np.log(np.abs(hpf_fshift))

plt.imshow(ms,cmap='gray')
plt.show()

rows,cols=img.shape
crow,ccol=rows//2,cols//2

#HighPass filtering
hpf_fshift[ccol-30:crow+30,ccol-30:ccol+30]=0
hpf_f_ishift=np.fft.ifftshift(hpf_fshift)
hpf_img_back=np.fft.ifft2(hpf_f_ishift)
hpf_img_back=np.real(hpf_img_back)

plt.imshow(hpf_img_back,cmap='gray')
plt.show()


#lowpass filtering
mask=np.zeros((rows,cols),np.uint8)
mask[crow-30:crow+30,ccol-30:ccol+30]=1

fshift=lpf_fshift*mask
f_ishift=np.fft.ifftshift(fshift)
lpf_img_back=np.fft.ifft2(f_ishift)
lpf_img_back=np.real(lpf_img_back)

plt.imshow(lpf_img_back,cmap='gray')
plt.show()

