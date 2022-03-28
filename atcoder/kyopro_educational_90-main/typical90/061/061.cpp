#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main() {
    int Q;
    cin >> Q;
    deque<int> dp;
    rep(i, 0, Q){
        int t, x;
        cin >> t >> x;
        if(t == 1){
            dp.push_front(x);
        }else if(t == 2){
            dp.push_back(x);
        }else{
            cout << dp[x-1] << endl;
        }
    }
    return 0;
}