/**
*    author:  Dooloper
*    created: 20.03.2021 20:53:11
**/

#include <bits/stdc++.h>
#include <string>

using ll = long long;
using namespace std;

int main()
{
    string x;
    cin >> x;

    string ans;

    int n = x.size();

    int i = 0;
    while (x[i] != '.' && i < n)
    {
        ans.push_back(x[i]);
        i++;
    }

    cout << ans << endl;

    return 0;
}