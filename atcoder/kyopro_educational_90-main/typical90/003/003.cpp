#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int n;
bool used[1<<18];
vector<int> g[1<<18];

int dfs(int i){
    used[i] = true;
    int v = 0;
    int cnt = 0;
    for(auto nx : g[i]){
        if(used[nx] == false){
            v = max(v, dfs(nx));
        }else{
            cnt++;
        }
    }
    used[i] = false;
    if (cnt == g[i].size()){
        return 0;
    }
    return v+1;
}

int main() {
    cin >> n;
    rep(i, 0, n-1){
        int a, b;
        cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }
    rep(i, 1, n+1) used[i] = false;
    cout << dfs(1)+1 << endl;
    return 0;
}