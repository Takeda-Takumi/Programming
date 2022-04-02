#include <bits/stdc++.h>
using namespace std;
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

// int main() {
//     cin >> n;
//     rep (i, 0, n) cin >> a[i];

//     int ok = 0;
//     int ng = 100000+1;
//     int ans = 0;
//     while (abs(ok-ng) > 1) {
//         int mid = (ng - ok) / 2;

//         int r = 0;
//         int tmp_ans = 0;
//         int cnt = 0;
//         rep (l, 0, n) {
//             while (r < n && mid <= a[r]) {
//                 cnt++;
//                 r++;
//             }
//             tmp_ans = max(tmp_ans, cnt);
//             if (r == l) ++r;
//             else cnt--;
//         }
//         ans = max(tmp_ans, ans);
//         if (tmp_ans == 0) ng = mid;
//         else ok = mid;
//     }
//     cout << ok*ans << endl;

//     return 0;
// }

int a[10010];
int main() {
    int n;
    cin >> n;
    rep(i, 0, n) cin >> a[i];

    int ans = 0;
    rep(l, 0, n) {
        int x = a[l];
        rep(r, l, n) {
            x = min(x, a[r]);
            ans = max(ans, x * (r - l + 1));
        }
    }
    cout << ans << endl;
    return 0;
}