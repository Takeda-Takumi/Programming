#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main() {
    int n;
    cin >> n;
    vector<ll> a(n+1);
    rep (i, 1, n+1) cin >> a[i];
    sort(a.begin()+1, a.end());
    vector<ll> s(n+1);
    s[0] = 0;
    rep (i, 1, n+1) s[i] = s[i-1] + a[i];
    ll sum = 0;
    rep (i, 1, n) {
        sum += (s[n]-s[i]) - (n-i)*a[i];
    }
    cout << sum << endl;
    return 0;
}