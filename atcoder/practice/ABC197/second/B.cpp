/**
*    author:  Takeda Takumi
*    created: 06.04.2021 10:44:24
**/

#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int h,w;
string s[101];

int main() {
   
   int x, y;
   cin >> h >> w >> x >> y;
    x--; y--;
   rep(i,0,h){
       cin >> s[i];
   }
   //cout << "    " << s[2][2] << endl;

    int dx[4] = {0, -1, 0, 1};
    int dy[4] = {-1, 0, 1, 0};
    int ans = 1;
    rep(i, 0, 4)
    {
        int mx = x;
        int my = y;

        while(1)
        {
            mx += dx[i];
            my += dy[i];

            if(my < 0 || w <= my || mx < 0 || h <= mx) break;
            if(s[mx][my] == '#') break;

            ans++;
        }
        
    }

    cout << ans << endl;
   
   return 0;
}