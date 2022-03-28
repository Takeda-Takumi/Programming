#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main() {
   int N;
   int M;
   cin >> N >> M;
   vector<vector<int>> G(N+1);
   rep(i, 0, M){
        int a, b;
        cin >> a >> b;
        G[a].push_back(b);
        G[b].push_back(a);
   }
   int answer = 0;
   rep(i, 1, N+1){
       int cnt = 0;
       for(int nx : G[i]){
           if(nx < i){
               cnt++;
           }
       }
       if(cnt == 1){
           answer++;
       }
   }
   cout << answer << endl;
   return 0;
}