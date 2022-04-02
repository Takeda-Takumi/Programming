#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

ll N, M;
ll A[100009], B[100009], C[100009];

ll dist[100009];
ll dist1[100009];
ll distN[100009];
vector<pair<int, ll>> G[100009];

void dijkstra(int stt) {
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> Q;
    for (int i = 1; i <= N; i++) dist[i] = (1LL << 60);
    dist[stt] = 0;
    Q.push(make_pair(0, stt));

    while(!Q.empty()) {
        int pos = Q.top().second; Q.pop();
        for (int i = 0; i < G[pos].size(); i++) {
            int to = G[pos][i].first;
            ll cost = G[pos][i].second;
            if (dist[to] > dist[pos] + cost) {
                dist[to] = dist[pos] + cost;
                Q.push(make_pair(dist[to], to));
            }
        }        
    }
}

int main() {

    cin >> N >> M;
    rep (i, 1, M+1) cin >> A[i] >> B[i] >> C[i];
    vector<vector<int>> g(100009);
    rep (i, 1, M+1) {
        G[A[i]].push_back(make_pair(B[i], C[i]));
        G[B[i]].push_back(make_pair(A[i], C[i]));
    }
    dijkstra(1);
    for (int i = 1; i <= N; i++) dist1[i] = dist[i];

    dijkstra(N);
    for (int i = 1; i <= N; i++) distN[i] = dist[i];

    for (int i = 1; i <= N; i++) {
        ll Answer = dist1[i] + distN[i];
        cout << Answer << endl;
    }
    return 0;
}