import statistics

n = int(input())
x = [0]*n
y = [0]*n
for i in range(n):
    x[i], y[i] = map(int, input().split())

x.sort()
y.sort()

if len(x) % 2 == 0:
    px = (x[len(x)//2] + x[len(x)//-1]) // 2
else:
    px = x[len(x)//2]

if len(y) % 2 == 0:
    py = (y[len(y)//2] + y[len(y)//2-1]) // 2
else:
    py = y[len(y)//2]

px = statistics.median(x)
py = statistics.median(y)
ans = 0
for i in range(n):
    ans += abs(px-x[i]) + abs(py-y[i])

print(int(ans))