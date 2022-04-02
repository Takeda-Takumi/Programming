#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> a(m);
    rep (i, 0, m) cin >> a[i];

    sort(a.begin(), a.end());

    vector<int> spaces;
    int pre = 0;
    int min_space = pow(10, 9) + 1;
    rep (i, 0, m) {
        int space = a[i] - pre-1;
        if (space != 0) {
            spaces.push_back(space);
            min_space = min(min_space, space);
        }
        pre = a[i];
    }
    if (n-pre != 0) spaces.push_back(n-pre);
    
    int ans = 0;
    rep (i, 0, (int)spaces.size()) {
        ans += (spaces[i]+min_space-1)/min_space;
    }
    cout << ans << endl;

    return 0;
}