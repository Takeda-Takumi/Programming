h, w = (int(x) for x in input().split())
s = [input() for i in range(h)]


check = [[0]*w for i in range(h)]


def dfs(i, j, color):
    if(s[i][j] == color and check[i][j] == 0):
        check[i][j] = 1
        if(j+1 < w):
            dfs(i, j+1, color)
        if(i-1 >= 0):
            dfs(i-1, j, color)
        if(j-1 >= 0):
            dfs(i, j-1, color)
        if(i+1 < h):
            dfs(i+1, j, color)
    return


color_count = [0]*3
for i in range(h):
    for j in range(w):
        current_color = s[i][j]
        if(check[i][j] == 0):
            if(current_color == 'R'):
                color_count[0] += 1
            elif(current_color == "G"):
                color_count[1] += 1
            else:
                color_count[2] += 1
            dfs(i, j, current_color)

print(color_count[0], color_count[1], color_count[2])
