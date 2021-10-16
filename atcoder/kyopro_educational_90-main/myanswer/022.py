import math

def gcd(x, y):
    while y != 0:
        tmp = x
        x = y
        y = tmp%y 
    return x

a, b, c = map(int, input().split())


print(a, b, c)

r = gcd(a, gcd(b, c))

ans = (a//r - 1) + (b//r - 1) + (c//r - 1)

print(ans)

