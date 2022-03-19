import math

T = int(input())
L, X, Y = map(int, input().split())
q = int(input())

ans = []
PI = math.pi
for i in range(q):
    e = int(input())
    y = (-L / 2) * math.cos(2*PI/T * e - PI/2)
    z = L/2 + L/2 * math.sin(2*PI/T * e - PI/2)
    y1 = z
    y2 = math.sqrt((X)**2 + (Y - y)**2)
    a = math.atan2(z, math.sqrt((X)**2 + (Y - y)**2))
    ans.append(math.atan2(z, math.sqrt((X)**2 + (Y - y)**2)) / (2 *PI) * 360)

for x in ans:
    print(x)