import sys
sys.setrecursionlimit(2000**2)

n, m = map(int, input().split())

G = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    G[a].append(b)

used = [False] * (n+1)
def dfs(i):
    used[i] = True
    count = 1

    for point in G[i]:
        if used[point] == False:
            count += dfs(point)
    
    return count

sum = 0
for i in range(1, n+1):
    sum += dfs(i)
    used = [False] * (n+1)

print(sum)