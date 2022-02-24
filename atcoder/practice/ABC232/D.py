from collections import deque

h, w = map(int, input().split())
c = [input() for i in range(h)]

check = [[False]*w for _ in range(h)]

def dfs(i, j, count):
    global c
    global check
    check[i][j] = True
    count += 1
    a1 = -1
    a2 = -1
    if(i+1 < h and c[i+1][j] == '.' and check[i+1][j] == False):
        a1 = dfs(i+1, j, count)
    if(j+1 < w and c[i][j+1] == '.' and check[i][j+1] == False):
        a2 = dfs(i, j+1, count)

    check[i][j] = False
    return max(a1, a2, count)
    

print(dfs(0, 0, 0))






print()