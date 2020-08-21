#power spectrum
from scipy import fftpack, ndimage
import matplotlib.pyplot as plt

image = plt.imread('messi.jpg', 0)
fft2 = fftpack.fft2(image)

plt.imshow(abs(fft2))
plt.show()
