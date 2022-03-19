from operator import mod


n = int(input())

a = [[int(x) for x in input().split()] for i in range(n)]
mod = 10**9 + 7
ans = 1
for i in range(n):
    ans *= sum(a[i]) % mod

print(ans% mod)