n = int(input())
a = [int(x) for x in input().split()]

d = {}
count = 0
for i in range(n):
    if not a[i] in d:
        count += 1
        d[a[i]] = 1
print(count)