h, w = map(int, input().split())
c = [input() for _ in range(h)]

used = [[False]*w for _ in range(h)]

def dfs(i, j, count):
    global start_i
    global start_j
    global c
    ans = -1

    if(used[i][j]):
        if(start_i == i and start_j == j and count >= 3):
            ans = count
        return ans

    used[i][j] = True

    if(i+1 < h and c[i+1][j] == "."):
        ans = max(ans, dfs(i+1, j, count+1))
    if(i-1 >= 0 and c[i-1][j] == "."):
        ans = max(ans, dfs(i-1, j, count+1))
    if(j+1 < w and c[i][j+1] == "."):
        ans = max(ans, dfs(i, j+1, count+1))
    if(j-1 >= 0 and c[i][j-1] == "."):
        ans = max(ans, dfs(i, j-1, count+1))

    used[i][j] = False
    return ans

ans = -1
for i in range(h):
    for j in range(w):
        start_i = i
        start_j = j
        if c[i][j] == ".":
            ans = max(ans, dfs(i, j, 0))

print(ans)