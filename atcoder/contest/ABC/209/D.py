import heapq
import math

n, q = map(int, input().split())

G = [[] for _ in range(n+1)]
for i in range(1, n):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dist = [n] * (n+1)

heap = []
dist[1] = 0
heapq.heappush(heap, [dist[1], 1])

while len(heap) > 0:
    _, min_point = heapq.heappop(heap)
    for point in G[min_point]:
            if dist[min_point] + 1 < dist[point]:
                dist[point] = dist[min_point] + 1
                heapq.heappush(heap, [dist[point], point])

ans = []
for i in range(q):
    c, d = map(int, input().split())
    if(math.fabs(dist[c] - dist[d]) % 2 == 0):
        ans.append("Town")
    else:
        ans.append("Road")

for nx in ans:
    print(nx)






