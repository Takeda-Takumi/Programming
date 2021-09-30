/**
*    author:  Takeda Takumi
*    created: 27.03.2021 21:02:59
**/

#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

string a[20];
int n;



int main()
{
    cin >> n;
    rep(i,n)
    {
        cin >> a[i]; 
    }

    rep(i,n)
    {
        cout << a[i] << endl; 
    }
    return 0;
}