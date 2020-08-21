'''Write  a program to obtain 1d discrete Fourier transform of a given 1d vector consists of integer numbers generated randomly
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft


print(x)

y =fft(x)
print(y)
plt.plot(y.real,y,imag)
plt.show()
'''

import numpy as np


def DFT(x):
    """
    Compute the discrete Fourier Transform of the 1D array x
    :param x: (array)
    """

    N = x.size
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    return np.dot(e, x)
    
    
x=np.random.randint(1,10,10)
print(x)

y=[]
y.append(DFT(x))

print(y)



