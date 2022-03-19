from operator import mod


l, r = (int(x) for x in input().split())


mod = 10**9 + 7
sum = 0

# def modpow(a, b):
#     if(b == 0):
#         return 1
#     else:
#         if(b % 2 == 0):
#             tmp = modpow(a, b//2)
#             return tmp * tmp % mod
#         else:
#             return a * modpow(a, b-1)
    
def modpow(a, b):
    p = 1
    q = a
    while(b > 0):
        if(b % 2 == 1):
            p *= q
            p %= mod
        q *= q
        q %= mod
        b //= 2

    return p

def Div(a, b):
    return a * modpow(b, mod-2) % mod

def Sum(n):
    a = n * (n+1) % mod
    return Div(a, 2)


for i in range(1, 20):
    vl = max(10**(i-1), l)
    vr = min(10**i-1, r)
    if vl > vr:
        continue
    sum += i * (Sum(vr) - Sum(vl-1))
    sum %= mod

print(sum)