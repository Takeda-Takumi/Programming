
n, k = (int(x) for x in input().split())
mod = 10**9 + 7


def binmod(a, b):
    if(b == 0):
        return 1
    else:
        if(b % 2 == 0):
            tmp = binmod(a, b//2)
            return tmp * tmp % mod
        else:
            return a * binmod(a, b-1) % mod

if(k == 1):
    if(n == 1):
        print(1)
    else:
        print(0)
elif(n == 1):
    print(k % mod)
elif(n == 2):
    print(k * (k-1) % mod)
else:
    print(k * (k-1) % mod * binmod(k-2, n-2) % mod)