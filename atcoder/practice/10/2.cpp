/**
*    author:  Takeda Takumi
*    created: 2021.04.11 16:02:46
**/

#include <bits/stdc++.h>
using namespace std;
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main()
{

    string s;
    cin >> s;
    int count = 0;
    rep(i, 0, 3)
    {
        if (s[i] == '1')
            count++;
    }
    cout << count << endl;

    return 0;
}