from bisect import bisect, bisect_left
import math
import random

n = int(input())
a = [int(x) for x in input().split()]
a.sort()
q = int(input())


# n = random.randint(1, 300000)
# a = [random.randint(0, 10**9) for i in range(n)]
# q = random.randint(1, 300000)
# b = [random.randint(0, 10**9) for i in range(q)]

# def binsearch(x):
#     ok = -1
#     ng = n
#     while(math.fabs(ok - ng) > 1):
#         mid = int((ok + ng) / 2)
#         if(a[mid] == x):
#             return 0
#         elif(a[mid] > x):
#             ng = mid
#         else:
#             ok = mid
    
#     left = math.fabs(a[max(ok, 0)] - x)
#     right = math.fabs(a[min(ng, n-1)] - x)
#     if(left > right):
#         return int(right)
#     else:
#         return int(left)

# ans = []
# for i in range(q):
#     b = int(input())
#     ans.append(binsearch(b))

#     # ans.append(binsearch(b[i]))




ans = []
for i in range(q):
    b = int(input())
    pos1 = bisect_left(a, b)
    diff1 = 10**9 + 1
    diff2 = 10**9 + 1
    if(pos1 < n):
        diff1 = math.fabs(a[pos1] - b)
    if(pos1 > 0):
        diff2 = math.fabs(a[pos1-1] - b)
    ans.append(int(min(diff1, diff2)))

for x in ans:
    print(x)