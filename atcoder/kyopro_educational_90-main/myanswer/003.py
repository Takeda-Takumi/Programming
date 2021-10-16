import queue

n = int(input())
a = [list(map(int, input().split())) for i in range(n-1)]

g = [[] for i in range(n+1)]
INF = n * n
dist = []

def getdist(start):
    global dist
    dist = [INF for i in range(n+1)]
    q = queue.Queue()
    q.put(start)
    dist[start] = 0

    while not q.empty():
        pos = q.get()
        for to in g[pos]:
            if dist[to] == INF:
                dist[to] = dist[pos] + 1
                q.put(to)



for i in range(n-1):
    g[a[i][0]].append(a[i][1])
    g[a[i][1]].append(a[i][0])

getdist(1)
maxn1 = -1
maxid1 = -1
for i in range(1, n+1):
    if maxn1 < dist[i]:
        maxn1 = dist[i]
        maxid1 = i

getdist(maxid1)
maxn2 = -1
for i in range(1, n+1):
    maxn2 = max(maxn2, dist[i])

print(maxn2 + 1)

