n, m = map(int, input().split())
a = [0] * (m)
b = [0] * (m)
for i in range(m):
    a[i], b[i] = map(int, input().split())

k = int(input())
c = [0] * (k)
d = [0] * (k)
for i in range(k):
    c[i], d[i] = map(int, input().split())



ans = 0
for i in range(1<<k):
    dish = [0] * (1+n)

    for j in range(k):
        if ((i>>j) & 1):
            dish[c[j]] = 1
        else:
            dish[d[j]] = 1

    sum = 0
    for j in range(m):       
        if(dish[a[j]] == 1 and dish[b[j]] == 1):
            sum += 1
    ans = max(sum, ans)

print(ans)





