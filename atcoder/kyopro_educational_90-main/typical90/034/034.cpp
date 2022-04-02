#include <bits/stdc++.h>
using namespace std;
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main() {
    int n, k;
    cin >> n >> k;
    vector<ll> a(n);
    rep(i, 0, n) cin >> a[i];
    int r = 0;
    map<int, int> m;
    int ans = 0;
    int tmp_k = 0;
    rep(l, 0, n) {
        while (r < n && tmp_k < k) {
            if(m[a[r]] == 0) tmp_k++;
            m[a[r]] += 1;
            r++;
        }
        while (r < n && m[a[r]] > 0) {
            m[a[r]] += 1;
            r++;
        }

        ans = max(ans, r - l);
        if (--m[a[l]] == 0) {
            tmp_k--;
        }
    }
    cout << ans << endl;

    return 0;
}