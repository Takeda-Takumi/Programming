n = int(input())

mod =  998244353
dp = [[0]*(9+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 10):
        if(i == 1): 
            dp[i][j] = 1
        elif(i > 1):
            if(j == 1):
                dp[i][j] = dp[i-1][j] + dp[i-1][j+1] % mod
            elif(j == 9):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1] % mod
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1] % mod

sum = 0
for x in dp[n]:
    sum += x
    sum = mod
print(sum)