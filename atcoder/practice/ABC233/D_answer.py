from collections import defaultdict
n, k = (int(x) for x in input().split())
a = [int(x) for x in input().split()]


s = [0] * (n+1)
for i in range(n):
    s[i+1] = s[i] + a[i]

d = defaultdict(int)
ans = 0
for i in range(1, n+1):
    d[s[i-1]] += 1
    if s[i]-k in d:
        ans += d[s[i]-k]

print(ans)