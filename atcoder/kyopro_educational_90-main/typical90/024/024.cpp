#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    vector<int> b(n);

    rep(i, 0, n){
        cin >> a[i];
    }
    rep(i, 0, n){
        cin >> b[i];
    }

    int sum = 0;
    rep(i, 0, n){
        sum += abs(a[i]-b[i]);
    }

    string ans = "No";
    if(sum <= k){
        if((k-sum) % 2 == 0){
            ans = "Yes";
        }
    }
    cout << ans << endl;

    return 0;
}