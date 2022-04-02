#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

const int mod = 1000000007;
int main() {
    int k;
    cin >> k;
    if (k % 9 == 0){
        vector<int> dp(k+1);
        dp[0] = 1;
        rep(i, 1, k+1){
            for (int j = i-1; j >= i-9 && j >= 0; --j){
                dp[i] += dp[j];
                if (dp[i] >= mod) dp[i] %= mod;
            }
        }
        cout << dp[k] << endl;
    } else {
        cout << 0 << endl;
    }
    return 0;
}