l, r = (int(x) for x in input().split())

mod = 10**9 + 7

def modpow(a, b):
    p = 1
    q = a
    for i in range(30):
        if((b & (1 << i)) != 0):
            p *= q
            p %= mod
        q *= q
        q %= mod
    return p

def div(a, b):
    return (a * modpow(b, mod-2)) % mod

def f(n):
    v1 = n % mod
    v2 = (n+1) % mod
    v = v1 * v2 % mod
    return div(v, 2)

res = 0
for i in range(1, 20):
    vl = max(l, 10**(i-1))
    vr = min(r, 10**i-1)
    if vl > vr:
        continue
    val = (f(vr) - f(vl-1) + mod) % mod
    res += i * val 
    res %= mod

print(res)