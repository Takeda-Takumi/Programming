n = int(input())
s = input()

mod = 10**9 + 7

dp = [[0] * 8 for _ in range(1000009)]

dp[0][0] = 1

for i in range(len(s)):
    for j in range(8):
        dp[i+1][j] += dp[i][j]
        if(s[i] == 'a' and j == 0): dp[i+1][j+1] += dp[i][j]
        if(s[i] == 't' and j == 1): dp[i+1][j+1] += dp[i][j]
        if(s[i] == 'c' and j == 2): dp[i+1][j+1] += dp[i][j]
        if(s[i] == 'o' and j == 3): dp[i+1][j+1] += dp[i][j]
        if(s[i] == 'd' and j == 4): dp[i+1][j+1] += dp[i][j]
        if(s[i] == 'e' and j == 5): dp[i+1][j+1] += dp[i][j]
        if(s[i] == 'r' and j == 6): dp[i+1][j+1] += dp[i][j]
    
    for j in range(8):
        dp[i+1][j] %= mod

print(dp[len(s)][7])