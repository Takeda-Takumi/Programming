
import bisect


n = int(input())
a = [int(x) for x in input().split()]

# a2 = a + a

# size = sum(a)
# r = 0
# sum = 0
# ans = "No"
# for l in range(2*n):
#     while(r < 2*n and sum < size/10):
#         sum += a2[r]
#         r += 1

#     if(sum == size//10):
#         ans = "Yes"
#         break

#     sum -= a2[l]

ans = "No"
b = [0] * (2*n+1)
b[0] = 0
for i in range(n):
    b[i+1] = b[i] + a[i]

for i in range(n):
    b[i+n+1] = b[i+n] + a[i]

for i in range(n):
    goal = b[i] + b[n] / 10
    pos1 = bisect.bisect_left(b, goal)
    if(b[pos1] == goal):
        ans = "Yes"
        break


print(ans)
