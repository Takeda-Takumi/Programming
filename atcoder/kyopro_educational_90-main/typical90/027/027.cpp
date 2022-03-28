#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main() {
    int n;
    map<string, bool> mp;
    cin >> n;
    rep(i, 0, n){
        string s;
        cin >> s;
        if(!mp[s]){
            cout << i+1 << endl;
            mp[s] = true;
        }
    }

    return 0;
}