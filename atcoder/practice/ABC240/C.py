n, x = (int(z) for z in input().split())

dp = [[-1]*(x+1) for _ in range(n+1)]
for i in range(x+1):
    dp[0][i] = 0

dp[0][0] = 1
for i in range(n):
    a, b = (int(z) for z in input().split())
    for _ in range(x):
        dp[i+1][_] = 0
    for j in range(x):
        if(dp[i][j] == 1):
            if(j+a <= x):
                dp[i+1][j+a] = 1
            if(j+b <= x):
                dp[i+1][j+b] = 1

if(dp[n][x] == 1):
    print("Yes")
else:
    print("No")