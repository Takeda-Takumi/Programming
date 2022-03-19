n, l = (int(x) for x in input().split())

d = [0] * (n+1)
mod = 10**9 + 7

d[0] = 1
for i in range(1, n+1):
    if i >= l:
        d[i] = (d[i-1] + d[i-l]) % mod
    else:
        d[i] = d[i-1]

print(d[n])