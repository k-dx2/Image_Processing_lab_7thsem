def modifyBit(n):
    for p in range(0, 4):
       mask = 1 << p 
       n = (n & ~mask) | ((0 << p) & mask) 
    return n

n = int(input("Enter an integer: "))
print(modifyBit(n))
