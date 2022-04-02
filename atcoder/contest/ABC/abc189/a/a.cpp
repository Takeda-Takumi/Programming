#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main() {
    string s;
    cin >> s;
    if (s[0] == s[1] and s[1] == s[2]) {
        cout << "Won" << endl;
    } else {
        cout << "Lost" << endl;
    }
    
    return 0;
}