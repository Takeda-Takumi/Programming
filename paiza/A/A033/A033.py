n, m = (int(x) for x in input().split())
b = [list(map(int, input().split())) for i in range(n)]
b.insert(0, [0]*2)

max_page = [[0]*(m+1) for i in range(n+1)]

for i in range(n+1):
    for j in range(m+1):
        if(i == 0 or j == 0):
            max_page[i][j] = 0
            continue
        if(b[i][1] > j):
            max_page[i][j] = max_page[i-1][j]
        else:
            max_page[i][j] = max(
                max_page[i-1][j], max_page[i-1][j-b[i][1]] + b[i][0])

print(max_page[n][m])
