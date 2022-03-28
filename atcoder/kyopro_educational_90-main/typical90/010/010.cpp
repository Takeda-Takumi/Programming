#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main() {
    int n;
    cin >> n;
    vector<int> c(n+1);
    vector<int> p(n+1);
    rep(i, 1, n+1) cin >> c[i] >> p[i];
    vector<int> s1(n+1, 0);
    vector<int> s2(n+1, 0);
    rep(i, 1, n+1){
        if(c[i] == 1) s1[i] += p[i];
        if(c[i] == 2) s2[i] += p[i];
        s1[i] += s1[i-1];
        s2[i] += s2[i-1];
    }
    int q;
    cin >> q;
    int l, r;
    rep(i, 0, q){
        cin >> l >> r;
        cout << s1[r] - s1[l-1] << " " << s2[r] - s2[l-1] << endl;
    }
    return 0;
}