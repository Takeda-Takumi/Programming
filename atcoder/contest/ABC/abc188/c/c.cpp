#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

vector<ll> a(1<<20);

P tournament(int i,int j) {
    if (j-i == 1) {
        if (a[j] > a[i]) {
            return make_pair(j, i);
        } else {
            return make_pair(i, j);
        }
    }
    int mid = i + (j-i)/2;
    P left = tournament(i, mid);
    P right = tournament(mid+1, j);

    if (a[left.first] > a[right.first]) {
        return make_pair(left.first, right.first);
    } else {
        return make_pair(right.first, left.first);
    }
}



int main() {
    int n;
    cin >> n;
    rep (i, 0, 1<<n) cin >> a[i];
    cout << tournament(0, (1<<n)-1).second+1 << endl;
    return 0;
}