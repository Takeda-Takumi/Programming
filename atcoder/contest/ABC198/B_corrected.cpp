/**
*    author:  Takeda Takumi
*    created: 2021.04.11 20:54:40
**/

#include <bits/stdc++.h>
using namespace std;
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main()
{
    int n;
    cin >> n;

    if (n == 0)
    {
        cout << "Yes" << endl;
        return 0;
    }

    while (n % 10 == 0)
        n /= 10;

    //cout << s << endl;
    string s = to_string(n);

    string rs = s;
    reverse(rs.begin(), rs.end());

    if (s != rs)
    {
        cout << "No" << endl;
    }
    else
    {
        cout << "Yes" << endl;
    }

    return 0;
}