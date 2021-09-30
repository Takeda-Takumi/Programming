/**
*    author:  Takeda Takumi
*    created: 2021.04.12 16:06:36
**/

#include <bits/stdc++.h>
using namespace std;
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

bool isPalindorome(string s)
{
    string rs = s;
    reverse(rs.begin(), rs.end());
    return s == rs;
}

int main()
{
    double r,x,y;
    cin >> r >> x >> y;

    double distance = sqrt(x*x + y*y);
    int ans = ceil(distance / r);
    if(ans == 1 && distance != r) ans++;

    cout << ans << endl;


    return 0;
}