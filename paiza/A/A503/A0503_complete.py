n, m = (int(x) for x in input().split())
s = [input() for i in range(n)]
x = [list(map(int, input().split())) for i in range(m)]

s_1n = [[]*n for i in range(n)]

for i in range(n):
    s_1n[i] = '#' + s[i] + '#'
s_1n.insert(n, '#'*(n+2))
s_1n.insert(0, '#'*(n+2))
s_1n_length = len(s_1n)

dx_dy = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
rgb = ['R', 'G', 'B']

for i in range(m):
    s_1n[x[i][1]] = s_1n[x[i][1]][:x[i][0]] + \
        rgb[i % 3] + s_1n[x[i][1]][x[i][0]+1:]
    for j in range(8):
        corrent_y = x[i][1]
        corrent_x = x[i][0]
        while True:
            corrent_x += dx_dy[j][1]
            corrent_y += dx_dy[j][0]
            if(s_1n[corrent_y][corrent_x] == '#'):
                break
            if(s_1n[corrent_y][corrent_x] == '.'):
                break
            if(s_1n[corrent_y][corrent_x] == rgb[i % 3]):
                tmp_x = corrent_x
                tmp_y = corrent_y
                while True:
                    tmp_x += dx_dy[j][1]*(-1)
                    tmp_y += dx_dy[j][0]*(-1)
                    if(tmp_x == x[i][0] and tmp_y == x[i][1]):
                        break
                    s_1n[tmp_y] = s_1n[tmp_y][:tmp_x] + \
                        rgb[i % 3] + s_1n[tmp_y][tmp_x+1:]
                break

for k in range(1, s_1n_length-1):
    print(s_1n[k][1:s_1n_length-1])

max_str = ''
max_count = 0

for str in rgb:
    count = 0
    for i in range(s_1n_length):
        count += s_1n[i].count(str)
    if(max_count <= count):
        max_str = str
        max_count = count
print(max_str)
