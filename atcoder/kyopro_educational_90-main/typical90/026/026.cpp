#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;


int v_color[1<<18] = {0};
vector<vector<int>> g(1<<18);

void dfs(int i, int color){
    v_color[i] = color;
    for (auto nx : g[i]) {
        if(v_color[nx] == 0){
            dfs(nx, 3-color);
        }
    }
}

int main() {
    int n;
    cin >> n;
    rep(i, 0, n-1){
        int a, b;
        cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }
    dfs(1, 1);
    // cout << count(v_color+1, v_color+n+1, 1) << endl;
    int cnt = count(v_color+1, v_color+n+1, 1);
    int tar = 0;
    if (cnt >= n/2) tar = 1;
    else tar = 2;

    int k = 0;
    rep(i, 1, n+1){
        if(v_color[i] == tar){
            cout << i << " ";
            k++;
        }
        if(k == n/2) break;
    }
    cout << endl;

    return 0;
}