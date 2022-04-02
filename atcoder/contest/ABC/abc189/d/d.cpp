#include <bits/stdc++.h>
using namespace std;
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

ll dp[65][2];


int main() {
    int n;
    cin >> n;
    dp[0][0] = 1;
    dp[0][1] = 1;
    rep(i, 0, n){
        string s;
        cin >> s;
        if(s == "AND"){
            dp[i+1][0] = dp[i][0] * 2 + dp[i][1];
            dp[i+1][1] = dp[i][1];
        }else{
            dp[i+1][0] = dp[i][0];
            dp[i+1][1] = dp[i][0] + dp[i][1] * 2;

        }
    }
    cout << dp[n][1] << endl;
    return 0;
}