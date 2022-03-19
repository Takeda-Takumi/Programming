import itertools


n = int(input())
a = [[int(x) for x in input().split()] for i in range(n)]
m = int(input())
x = [0] * m
y = [0] * m

kenaku = [[False for i in range(n)] for j in range(n)]
for i in range(m):
    x, y = (int(x)-1 for x in input().split())
    kenaku[x][y] = True
    kenaku[y][x] = True

ans = 1 << 30
for itr in itertools.permutations(range(n)):
    f = True
    sum = 0
    for i in range(n):
        if(i < n-1 and kenaku[itr[i]][itr[i+1]] == True):
            f = False
            break
        sum += a[itr[i]][i]
    else:
        if(f == True):
            ans = min(ans, sum)

if(ans == (1 << 30)):
    ans = -1
print(ans)