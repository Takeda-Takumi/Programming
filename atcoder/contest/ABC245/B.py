n = int(input())
a = list(map(int, input().split()))

d = {}
for i in range(n):
    if a[i] in d:
        pass
    else:
        d[a[i]] = 1

for i in range(3000):
    if i in d:
        pass
    else:
        print(i)
        break


