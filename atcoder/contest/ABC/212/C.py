import bisect
import math

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

ans = 10**9
for nx in b:
    j = bisect.bisect_left(a, nx)
    if j == 0:
        ans = min(ans, math.fabs(a[j]-nx))
    elif j == n:
        ans = min(ans, math.fabs(a[j-1]-nx))
    else:
        ans = min(ans, math.fabs(a[j]-nx), math.fabs(a[j-1]-nx))


print(int(ans))
