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

    int n;
    cin >> n;
    ll a[200];
    rep(i,0,n)  cin >> a[i];
    int count = 0;
    bool f = false;
    while(1)
    {
        rep(i,0,n)
        {
            if((a[i] % 2))
            {
                f = true;
                break;
            }else{
                a[i] /= 2;
            }
        }
        if(f) break;
        count++;
    }

    cout << count << endl;

    return 0;
}