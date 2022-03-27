n = int(input())
lx = [-1] * n
ly = [-1] * n
rx = [-1] * n
ry = [-1] * n

for i in range(n):
    lx[i], ly[i], rx[i], ry[i] = map(int, input().split())

table = [[0]*(1000+1) for _ in range(1000+1)]

for i in range(n):
    table[lx[i]][ly[i]] += 1
    table[lx[i]][ry[i]] -= 1
    table[rx[i]][ly[i]] -= 1
    table[rx[i]][ry[i]] += 1
    
    



for i in range(1000+1):
    for j in range(1, 1000+1):
        table[i][j] += table[i][j-1]

for j in range(1000+1):
    for i in range(1, 1000+1):
        table[i][j] += table[i-1][j]

ans = [0] * (n+1)

for i in range(1000+1):
    for j in range(1000+1):
        if table[i][j] >= 1:
            ans[table[i][j]] += 1

for i in range(1, 1+n):
    print(ans[i])






print()