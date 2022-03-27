import math
a, b, c, d = (int(x) for x in input().split())

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if(x % i == 0):
            return False

    return True

ans_aoki = {}
for i in range(a, b+1):
    for j in range(c, d+1):
        if(isPrime(i+j)):
            ans_aoki[i] = j

ans = "Aoki"
for i in range(a, b+1):
    if(not i in ans_aoki):
        ans = "Takahashi"
print(ans)
