import math

n, m = map(int, input().split())

b = [list(map(int, input().split())) for i in range(n)]


x = [[-1]*m for i in range(n)]
y = [[-1]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        x[i][j] = math.ceil((b[i][j]-1)/7) 
        y[i][j] = (b[i][j]-1)%7+1        

ans = "Yes"
for i in range(n):
    for j in range(m):
        if(j > 0 and y[i][j] != y[i][j-1]+1):
            ans = "No"
        if(i > 0 and x[i][j] != x[i-1][j]+1):
            ans = "No"

print(ans)
