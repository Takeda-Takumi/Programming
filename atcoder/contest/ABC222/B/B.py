n, p = (int(x) for x in input().split())
a = [int(x) for x in input().split()]

cnt = 0
for i in range(n):
    if(a[i] < p):
        cnt += 1

print(cnt)