x = int(input("Enter number: "))
y = int(input("Enter number: "))

def prod(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        n = min(len(str(x)),len(str(y)))
        a = x // (10**(n//2))
        b = x % (10**(n//2))
        c = y // (10**(n//2))
        d = y % (10**(n//2))
        return ((10**n) * (prod(a,c))) + (prod(b,c)) + ((10**(n//2)) * (prod(a+b,c+d) - prod(a,c) - prod(b,c))) 

print(prod(x,y))
