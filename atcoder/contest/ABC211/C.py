s = input()

dp = [[0]*9 for _ in range(len(s)+1)]
mod = 10**9 + 7
t = "chokudai"

for i in range(len(s)+1):
    for j in range(9):
        if j == 0:
            dp[i][j] = 1
        elif i == 0 and j >= 1 and j <= 8:
            dp[i][j] == 0
        elif s[i-1] != t[j-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1] % mod

        
print(dp[len(s)][8] % mod)