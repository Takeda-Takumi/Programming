n, k = (int(x) for x in input().split())
mod = 1000000007
# def power(x, n, m):
#     if(n == 0):
#         return 1
#     elif(n % 2 == 1):
#         return (x * power(x, n-1, m)) % mod
#     else:
#         tmp = power(x, n/2, m)
#         return (tmp * tmp) % mod

def binpower(a, b):
    ans = 1
    while(b != 0):
        if(b % 2 == 1):
            ans = ans*a % mod
        a = a * a % mod
        b //= 2
        # print("{0:f}".format(a), "{0:f}".format(b), ans)
    return ans

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
    print(k * (k-1) % mod * binpower(k-2, n-2) % mod)
    # print(k * (k-1) % mod * power(k-2, n-2, mod) % mod)