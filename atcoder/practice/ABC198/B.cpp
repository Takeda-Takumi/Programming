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

    int n;
    cin >> n;
    if (n == 0)
    {
        cout << "Yes" << endl;
        return 0;
    }
    while (n % 10 == 0)
        n /= 10;
    if (isPalindorome(to_string(n)))
    {
        cout << "Yes" << endl;
    }
    else
    {
        cout << "No" << endl;
    }

    return 0;
}