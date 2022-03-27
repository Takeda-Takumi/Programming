n = int(input())
a = [int(x) for x in input().split()]

# left = 0
# right = 360
# angle = 0
# for i in range(n):
#     angle = (angle + a[i]) % 360
#     ditstanceLeftToRight = right - left
#     halfLength =  ditstanceLeftToRight / 2
#     if(angle >= left and angle <= right):
#         distanceAngleToLeft = angle - left
#         if(halfLength > distanceAngleToLeft):
#             left = angle
#         else:
#             right = angle
# print(right - left)

l = [0, 360]
angle = 0
for i in range(n):
    angle = (angle + a[i]) % 360
    l.append(angle)

l.sort()

s = [0] * len(l)
ans = -1
for i in range(1, len(l)):
    s[i] = l[i] - l[i-1]
    ans = max(ans, s[i])
print(ans)