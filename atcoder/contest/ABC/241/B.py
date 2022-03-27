n, m = (int(x) for x in input().split())

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

d = {}
for i in range(n):
    if not a[i] in d:
        d[a[i]] = 0
    d[a[i]] += 1

ans = "Yes"
for i in range(m):
    if b[i] in d:
        if d[b[i]] > 0:
            d[b[i]] -= 1
        else:
            ans = "No"
    else:
        ans = "No"
print(ans)