h, w = map(int, input().split())
c = [input() for i in range(h)]

f = [[0]*(w+1) for i in range(h+1)]
for i in range(h-1, -1, -1):
    for j in range(w-1, -1, -1):
        if(c[i][j] == '#'): 
            continue
        f[i][j] = max(f[i+1][j], f[i][j+1]) + 1

print(f[0][0])