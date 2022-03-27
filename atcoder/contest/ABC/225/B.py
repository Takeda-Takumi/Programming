n = int(input())

a = [[] for i in range(n)]
b = [[] for i in range(n)]

for i in range(1, n):
    a[i], b[i] = map(int ,input().split())

g = [[] for i in range(n+1)]
for i in range(1, n):
    g[a[i]].append(b[i])
    g[b[i]].append(a[i])

ans = "No"
for i in range(1, n+1):
    if(len(g[i]) == n - 1):
        ans = "Yes"
        break

print(ans)