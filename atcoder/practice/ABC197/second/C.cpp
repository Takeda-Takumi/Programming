/**
*    author:  Takeda Takumi
*    created: 06.04.2021 10:44:24
**/

#include <bits/stdc++.h>
using namespace std;
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int h, w;
string s[101];

int main()
{
    int n;
    cin >> n;
    vector<int> a(n);
    rep(i, 0, n) cin >> a[i];
    int ans = 1 << 30;
    rep(i, 0, 1 << (n - 1))
    {
        int xo = 0;
        int o = 0;
        rep(j, 0, n)
        {
            o |= a[j];
            if ((i >> j) & 1)
            {
                xo ^= o;
                o = 0;
            }
        }
        xo ^= o;
        ans = min(ans, xo);
    }
    cout << ans << endl;
    return 0;
}