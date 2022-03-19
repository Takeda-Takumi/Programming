import sys

sys.setrecursionlimit(10**6)

n = int(input())

G = [[] for _ in range(n+1)]
used = [False] * (n+1)

for i in range(1, n):
    a, b = (int(x) for x in input().split())
    G[a].append(b)
    G[b].append(a)

for i in range(1, n+1):
    G[i].sort()

def dfs(i):
    used[i] = True
    print(i, "", end='')

    for nx in G[i]:
        if used[nx] == False:
            dfs(nx)
            print(i, "", end='')


dfs(1)
