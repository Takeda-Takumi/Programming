h, w = map(int, input().split())
c = [input() for i in range(h)]


used = [[False]*w for _ in range(h)]

def dfs(i, j, k):
    used[i][j] = True

    if(j+1 < w and used[i][j] == False):
        dfs(i, j+1, k+1)

    used[i][j] = False

ans = 0
for i in range(h):
    for j in range(w):
        ans += dfs(i, j, 0)

print(ans)
