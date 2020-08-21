def N4(a, i , j):
   s = set()
   if (i -1) >= 0:
     s.add(a[i-1][j])
   if (i+1) < len(a):
     s.add(a[i+1][j])
   if (j-1) >= 0:
     s.add(a[i][j-1])
   if (j+1) < len(a[0]):
     s.add(a[i][j+1])
   return s

def N8(a, i, j):
   s = set()
   row = len(a)
   col = len(a[0])
   for x in N4(a, i, j):
    s.add(x)
   if (i+1 < row) and (j+1 < col):
     s.add(a[i+1][j+1])
   if (i-1 >= 0) and (j-1 >= 0):
     s.add(a[i-1][j-1])
   if (i-1 >= 0) and (j+1 < col):
     s.add(a[i-1][j+1])
   if (i+1 < row) and (j-1 >= 0):
     s.add(a[i+1][j-1])
   return s
   
def Nm(a, i, j, v):
    s = set()
    s1 = N4(a, i, j)
    for x in s1:
      s.add(x)
    if (i+1) < len(a) and (j+1) < len(a[0]):
      s2 = N4(a, i+1, j+1)
      s3 = s1 & s2
      s4 = s3 - v
      for x in s4:
        s.add(x) 
    if (i-1) >= 0 and (j-1) >= 0:
      s2 = N4(a, i-1, j-1)
      s3 = s1 & s2
      s4 = s3 - v
      for x in s4:
        s.add(x)
    if (i+1) < len(a) and (j-1) >= 0:
      s2 = N4(a, i+1, j-1)
      s3 = s1 & s2
      s4 = s3 - v
      for x in s4:
        s.add(x)  
    if (i-1) >= 0 and (j+1) < len(a[0]):
      s2 = N4(a, i-1, j+1)
      s3 = s1 & s2
      s4 = s3 - v
      for x in s4:
        s.add(x)
    return s
    

arr = [[0, 1, 1 , 0, 1],
[1, 1, 0 , 1, 1],
[1, 0, 1 , 1, 1],
[0, 1, 0 , 1, 1],
[0, 1, 1 , 1, 0]]

v = {1}

for i in range(len(arr)):
  for j in range(len(arr[0])):
     print(N4(arr, i, j), end = " ")
     
print("\n")
     
for i in range(len(arr)):
  for j in range(len(arr[0])):
     print(N8(arr, i, j), end = " ")
print("\n")
     
for i in range(len(arr)):
  for j in range(len(arr[0])):
     print(Nm(arr, i, j, v), end = " ")
print("\n")
     
    
