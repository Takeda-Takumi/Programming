n = int(input())

t = [0]*(n+1)
k = [0]*(n+1)
G = [[] for i in range(n+1)]

for i in range(1, n+1):
    inp = [int(x) for x in input().split()]
    t[i], k[i] = inp[0], inp[1]
    for j in range(1, k[i]+1):
        G[i].append(inp[1+j])

used = [False for _ in range(n+1)]
sum = 0
used[n] = True
for i in reversed(range(n+1)):
    if(used[i]):
        sum += t[i]
        for j in range(k[i]):
            used[G[i][j]] = True

print(sum)
