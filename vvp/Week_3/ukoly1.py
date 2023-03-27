def root(a,n):
    x = a
    if (x == 0):
        x = a
    else:
        for i in range (n):
         x = (a/x + x)/2

    return x

print(root(4,100))

def aprox(n):
    a = 1
    b = 1
   
    for i in range(n):
         v = root(a - (b/2)**2, 100)
         n = 6*b*v/2 * 2**i
         b = root((b/2)**2 + (1-v)**2,100)
    return n

print(aprox(96))

def newton(n):
    a = (1/2)*(1/2**3)
    s = 0

    for i in range (1,n):
        s += a/(2*i+1)
        a = (2*(i+1)-3)/(2*(i+1))*a/(2**2)

    return 12*(root(3,1000)/(-8)+0.5-s)
    

print(newton(20))


