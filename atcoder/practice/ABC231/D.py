n, m = (int(x) for x in input().split())
a = [0] * m
b = [0] * m
for i in range(m):
    a[i], b[i] = map(int, input().split())

l = [0] * (10**5+1)

ans = "Yes"
for i in range(m):
    if(l[a[i]] == 2 or l[b[i]] == 2):
        ans = "No"
        break
    l[a[i]] += 1
    l[b[i]] += 1
print(ans)