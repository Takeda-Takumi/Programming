h,w = (int(x) for x in input().split())
s = [input() for i in range(h)]


for i in range(h):
    s[i] = '#' + s[i] + '#'
new_w = w + 2

s.insert(h,'#'*(new_w))
s.insert(0,'#'*(new_w))

new_h = h + 2
'''
for i in range(new_h):
    print(s[i])
'''

check = [[0]*new_w for i in range(new_h)]

def dfs(i,j,color):
    if(s[i][j] == color and check[i][j] == 0):
        check[i][j] = 1
        dfs(i  , j+1, color)
        dfs(i-1, j  , color)
        dfs(i  , j-1, color)
        dfs(i+1, j  , color)
    return

color_count = [0]*3
for i in range(new_h):
    for j in range(new_w):
        current_color = s[i][j]
        if(check[i][j] == 0 and current_color != '#' ):
            if(current_color == 'R'):
                color_count[0] += 1
            elif(current_color == "G"):
                color_count[1] += 1
            else:
                color_count[2] += 1
            dfs(i,j,current_color)
        else:
            continue

print(color_count[0],color_count[1],color_count[2])


