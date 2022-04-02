#include <bits/stdc++.h>
using namespace std;
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int a[10010];
int main() {
    int n;
    cin >> n;
    rep(i, 0, n) cin >> a[i];

    int ans = 0;
    rep(l, 0, n){
        int x = a[l];
        rep(r, l, n){
            x = min(x, a[r]);
            ans = max(ans, x*(r-l+1));
        }
    }
    cout << ans << endl;
    return 0;
}