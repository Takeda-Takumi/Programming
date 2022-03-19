
n = int(input())

G = [[] for i in range(n)]

col = [-1] * (10**6)

def dfs(pos, cur):
    col[pos] = cur
    for i in G[pos]:
        if(col[i] == -1):
            dfs(i, 1-cur)

for i in range(n-1):
    a, b = (int(x)-1 for x in input().split())
    G[a].append(b)
    G[b].append(a)

dfs(0, 0)

G1 = []
G2 = []

for i in range(n):
    if(col[i] == 0): G1.append(i)
    if(col[i] == 1): G2.append(i)

if len(G1) > len(G2):
    for i in range(int(n/2)):
        if(i):
            print(" ", end='')
        print(G1[i]+1, end='')
    print()
else:
    for i in range(int(n/2)):
        if(i):
            print(" ", end='')
        print(G1[i]+1, end='')
    print()