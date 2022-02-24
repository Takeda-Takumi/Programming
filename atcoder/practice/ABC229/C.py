n , w = (int(x) for x in input().split())

cheese = [[0]*2 for _ in range(n)]

for i in range(n):
    cheese[i] = list(map(int, input().split()))

cheese.sort()
cheese.reverse()


ans = 0
for x in cheese:
    ans += x[0] * min(x[1], w)
    w -= min(x[1], w)

print(ans)

