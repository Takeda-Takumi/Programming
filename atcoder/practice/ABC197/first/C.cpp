/**
*    author:  Takeda Takumi
*    created: 30.03.2021 16:14:34
**/

#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main() {
   
   int n;
   cin >> n;
   vector<int> a(n);
   rep(i, 0, n) cin >> a[i];
   int ans = 1<<30;
   rep(s, 0, 1<<(n-1))
   {
       int now = 0;
       int o = 0;
       rep(i,0,n)
       {
           o |= a[i];
           if(s>>i&1){
               now ^= o;
               o = 0;
           }
       }
       now ^= o;
       ans = min(ans, now);
   }
   cout << ans << endl;
   return 0;
}