n, m = map(int, input().split())
a = [int(x) for x in input().split()]

size = 10**5 + 5

def pfact(x):
    res = []
    for i in range(2, int(x**(0.5))+1):
        while(x%i==0):
            x //= i
            res.append(i)
    if(x != 1):
        res.append(x)
    return res

fl = [True] * size

for i in range(n):
    v = pfact(a[i])

    for nx in v:
        if(fl[nx]):
            for j in range(nx, size, nx):
                fl[j] = False

res = []
for i in range(1, m+1):
    if(fl[i]):
        res.append(i)

print(len(res))

for nx in res:
    print(nx)
