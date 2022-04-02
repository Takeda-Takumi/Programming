#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<ll, int>;

int main() {
    int n;
    cin >> n;
    vector<ll> a(n);
    vector<ll> b(n);
    rep (i, 0, n) cin >> a[i] >> b[i];
    vector<P> s(n);
    ll A = 0;
    rep (i, 0, n) {
        s[i] = pair(a[i] + b[i], i);
        A += a[i];
    }

    sort(
        s.begin(),
        s.end(),
        [](const P& x, const P& y){return x.first > y.first;}
    );

    ll B = 0;

    rep (i, 0, n) {
        B += s[i].first;
        A -= a[s[i].second];

        if (B > A) {
            cout << i+1 << endl;
            break;
        }
    }



    return 0;
}