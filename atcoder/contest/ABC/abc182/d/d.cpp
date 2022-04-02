#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main() {
    int n;
    cin >> n;
    vector<ll> a(n);
    rep (i, 0, n) cin >> a[i];
    ll sum = 0;
    ll ans = 0;

    ll tmp_max = 0;
    ll tmp_sum = 0;
    vector<ll> d(n);
    rep (i, 0, n) {
        tmp_sum += a[i];
        tmp_max = max(tmp_max, tmp_sum);
        d[i] = tmp_max;
    }

    ll x = 0;
    rep (i, 0, n) {
        ans = max(ans, x+d[i]);
        sum += a[i];
        x += sum;
    }
    cout << ans << endl;
    return 0;
}