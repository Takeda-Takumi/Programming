n = int(input())
a = [int(x) for x in input().split()]

dp = [[0]*(10) for i in range(n)]

dp[0][a[0]] = 1

for i in range(n-1):
    for j in range(10):
        dp[i+1][(j+a[i+1])%10] += dp[i][j]
        dp[i+1][(j*a[i+1])%10] += dp[i][j]

for i in range(10):
    print(dp[n-1][i])

