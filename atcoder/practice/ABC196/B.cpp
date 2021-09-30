/**
*    author:  Takeda Takumi
*    created: 26.03.2021 09:25:27
**/

#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main()
{
    string x;
    cin >> x;
    string ans;
    for (char c : x)
    {
        if (c == '.')
        {
            break;
        }
        ans += c;
    }
    cout << ans << endl;
    return 0;
}