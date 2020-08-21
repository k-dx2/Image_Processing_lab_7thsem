from math import e, pi

PI = pi

twodinput = []

M = int(input("give the no of rows\n"))

for i in range(M):

twodinput.append(list(map(int, input("Array[" + str(i) +

"]").split())))

= len(twodinput[0]) x, y = 0, 0

twodftransform = []

for i in range(M):

twodftransform.append([])

for j in range(N):

twodftransform[-1].append(0)

for x in range(M):

for y in range(N):

sum = 0

m, n = 0, 0

for m in range(M):

for n in range(N):

sum += twodinput[m][n] * e ** (-2j * pi * (((m * x) / M)

+ ((n * y) / N)))

twodftransform[x][y] = sum / (M * N)

for row in twodftransform:

print(row)

