n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

a.sort()
b.sort()

sum = 0
for i in range(n):
    sum += abs(a[i] - b[i])

print(sum)