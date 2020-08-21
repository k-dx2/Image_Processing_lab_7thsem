import numpy as np
v = []
n = input("Enter a integer:")
n = int(n)
for i in range(0, n): 
    ele = int(input()) 
    v.append(ele)
print(np.fft.fft(v))
