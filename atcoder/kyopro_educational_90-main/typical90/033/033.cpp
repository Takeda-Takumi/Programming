#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main() {
    int H, W;
    cin >> H >> W;
    if(H == 1 || W == 1){
        cout << H*W << endl;
    }else{
        int a = ceil((W/2.0));
        int b = ceil((H/2.0));
        cout << ceil((W/2.0)) << " " << ceil((H/2.0)) << endl;
        int c = a * b;
        cout << (int)a*b << endl;
        cout << (int)(ceil(((W/2.0)) * ceil((H/2.0)))) << endl;
        cout << (ceil(((W/2.0)) * ceil((H/2.0)))) << endl;
        // cout << ((H + 1) / 2) * ((W + 1) / 2) << endl;
    }
    return 0;
}