from bisect import bisect


import bisect

n, q = map(int, input().split())
a = [int(x) for x in input().split()]

c = [0] * n
c[0] = a[0]-1
for i in range(1, n):
    c[i] = a[i] - a[i-1] - 1 + c[i-1]

ans = []
for i in range(q):
    k = int(input())
    if c[n-1] < k:
        ans.append(a[n-1] + k-c[n-1])
    else:
        j = bisect.bisect_left(c, k)
        # ans.append((a[j]-1) - (c[j]-k))
        ans.append(a[j-1] + k - c[j-1])

for nx in ans:
    print(nx)