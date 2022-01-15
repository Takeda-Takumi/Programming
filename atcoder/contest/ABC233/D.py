n, k = (int(x) for x in input().split())
a = [int(x) for x in input().split()]

dp = [[0] *(k+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,k+1):
        if(j >= a[i]):
            dp[i][j] = max(dp[i-1][j], dp[i][j-a[i]])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])