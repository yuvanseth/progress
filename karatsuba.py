x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
n = int(input("Enter number of digits: "))

def prod(x,y,n):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        n = max(len(str(x)),len(str(y)))
        a = int(x/(10**(n/2)))
        b = x % (10**(n/2))
        c = int(y/(10**(n/2)))
        d = y % (10**(n/2))
        return (10**n * prod(a,c,n/2)) + (prod(b,c,n/2)) + (10**(n/2) (prod(a+b,c+d,n/2) - prod(a,c,n/2) - prod(b,c,n/2))) 

print(prod(x,y,n))
