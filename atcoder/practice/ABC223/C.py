n = int(input())

a = [0] * n
b = [0] * n

for i in range(n):
    a[i], b[i] = map(int, input().split())

time = 0
for i in range(n):
    time += a[i] / b[i]

t = time/2

length = 0
for i in range(n):
    t1 = min(a[i]/b[i], t)
    length += t1 * b[i]
    t -= t1

print(length)

