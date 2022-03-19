import math
n = int(input())

x = [-1] * n
y = [-1] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())

s = set()
for i in range(n):
    for j in range(n):
        if i == j:
            continue

        xd = x[j] - x[i]
        yd = y[j] - y[i]
        d = math.gcd(xd, yd)
        s.add((xd//d, yd//d))

print(len(s))