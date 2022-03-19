import math

n = int(input())

def isPrime(x):
    for i in range(2, int(math.sqrt(n))+1):
        if(x % i == 0):
            return False
    return True

if isPrime(n):
    print(0)
else:
    c = 0
    m = n
    for i in range(2, int(math.sqrt(n))+1):
        while(m % i == 0):
            c += 1
            m //= i
    if(m != 1):
        c += 1

    for i in range(1, 41):
        if(2**i >= c):
            print(i)
            break

