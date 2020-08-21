def modifyBit( n,  p,  b): 
    mask = 1 << p 
    return (n & ~mask) | ((b << p) & mask) 

n, p, b = [int(x) for x in input("Enter three value: ").split()] 
print(modifyBit(n, p, b))
