#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main() {
    int n, w;
    cin >> n >> w;
    vector<int> s(n+1);
    vector<int> t(n+1);
    vector<int> p(n+1);
    rep (i, 1, n+1) cin >> s[i] >> t[i] >> p[i];
    vector<ll> imosu(2*pow(10, 5)+1, 0);
    rep (i, 1, n+1) {
        imosu[s[i]] += p[i];
        imosu[t[i]] -= p[i];
    }
    rep (i, 1, 2*pow(10, 5)+1) {
        imosu[i] += imosu[i-1];
    }

    string ans = "Yes";
    rep (i, 0, 2*pow(10, 5)+1) {
        if (imosu[i] > w) {
            ans = "No";
            break;
        }
    }
    cout << ans << endl;
    

    return 0;
}