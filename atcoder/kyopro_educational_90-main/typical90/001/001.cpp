#include <bits/stdc++.h>
using namespace std;
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

ll n, k, l;
ll a[1<<18];

bool solve(ll m){
    ll cnt = 0, pre = 0;
    rep(i, 1, n+1){
        if(a[i]-pre >= m && l-a[i] >= m){
            cnt += 1;
            pre = a[i];
        }
    }
    if (cnt >= k) return true;
    return false;
}

int main(){
    cin >> n >> l;
    cin >> k;
    rep(i, 1, n+1) cin >> a[i];

    ll left = -1;
    ll right = l+1;
    while(right-left > 1){
        ll mid = left + (right-left) / 2;
        if (solve(mid) == false) right = mid;
        else left = mid;
    }
    cout << left << endl;
    return 0;
}