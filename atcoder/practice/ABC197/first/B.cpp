/**
*    author:  Takeda Takumi
*    created: 30.03.2021 15:07:25
**/

#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

   int H, W, X, Y;
   string S[101];
   int dx[4] = {0, 1, 0, -1}, dy[4] = { -1, 0, 1, 0};
   
int main() {

    cin >> H >> W >> X >> Y;
    X--;Y--;
    rep(i,0,H)
    {
        cin >> S[i];
    }

    int ans = 1;
    rep(d, 0, 4)
    {
        int x = X, y = Y;
        while(1){
            x += dx[d];
            y += dy[d];

            if (y < 0 || W <= y || x < 0 || H <= x) break;

            if(S[x][y] == '#') break;

            ans++;
        }
    }

    cout << ans << endl;

   return 0;
}