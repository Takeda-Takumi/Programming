#include <bits/stdc++.h>
using namespace std;
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

bool compare_by_b(pair<int, int> a, pair<int, int> b) {
    if (a.first != b.first) {
        return a.first < b.first;
    } else {
        return a.second > b.second;
    }
}

int main() {
    int N, K, X;
    cin >> N >> K >> X;
    int max_k = K;
    // priority_queue<int, vector<int>, less<int>> Q;
    // ll sum = 0;
    // rep (i, 0, N){
    //     int q;
    //     cin >> q;
    //     Q.push(q);
    //     sum += q;
    // }

    // while (K > 0) {
    //     int v = Q.top();
    //     sum -= v;
    //     Q.pop();
    //     int k = max(v/X, 1);
    //     K -= k;
    //     v = max(v-k*X, 0);
    //     sum += v;
    //     Q.push(v);
    // }
    // cout << sum << endl;

    vector<P> a(N);
    ll sum = 0;
    ll a_sum = 0;
    rep(i, 0, N) {
        int v;
        cin >> v;
        a_sum += v;
        int k = max(v / X, 1);
        int tmp1 = v - k * X;
        int tmp2 = v - ((k + 1) * X);
        if (tmp1 > tmp2) {
            a[i] = pair(tmp1, -k);
        } else {
            a[i] = pair(tmp2, -(k + 1));
        }
    }
    sort(a.begin(), a.end());

    rep(i, 0, N) {
        if (K <= 0) break;
        K += a[i].second;
        sum += a[i].first;
    }
    cout << a_sum - (K * max_k - sum) << endl;

    // sort(
    //     a.begin(),
    //     a.end(),
    //     [](const P& x, const P& y){return x.first > y.first;}
    // );

    return 0;
}