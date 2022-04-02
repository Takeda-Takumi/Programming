#include <bits/stdc++.h>
using namespace std;
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;



int main()
{
    int n;
    string s;
    cin >> n;
    cin >> s;
    int dp[8][100009] = {};
    rep(j, 0, n + 1)
    {
        dp[0][j] = 1;
    }
    int mod = 1000000007;
    rep(i, 1, 8){
        rep(j, 1, (int)s.size()+1){
            dp[i][j] += dp[i][j-1];
            if(s[j-1] == 'a' && i == 1) dp[i][j] += dp[i-1][j-1];
            if(s[j-1] == 't' && i == 2) dp[i][j] += dp[i-1][j-1];
            if(s[j-1] == 'c' && i == 3) dp[i][j] += dp[i-1][j-1];
            if(s[j-1] == 'o' && i == 4) dp[i][j] += dp[i-1][j-1];
            if(s[j-1] == 'd' && i == 5) dp[i][j] += dp[i-1][j-1];
            if(s[j-1] == 'e' && i == 6) dp[i][j] += dp[i-1][j-1];
            if(s[j-1] == 'r' && i == 7) dp[i][j] += dp[i-1][j-1];
            dp[i][j] %= mod;
        }
    }
    cout << dp[7][s.size()] % mod << endl;
    return 0;
}