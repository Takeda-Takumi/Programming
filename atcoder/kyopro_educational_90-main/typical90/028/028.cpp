#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int n;
int paper[1009][1009];
int main() {
    cin >> n;
    rep(i, 0, n){
        int lx, ly, rx, ry;
        cin >> lx >> ly >> rx >> ry;
        // paper[lx][ry] += 1;
        // paper[rx+1][ry] += -1;
        // paper[lx][ly-1] += -1;
        // paper[rx+1][ly-1] += 1;
        paper[lx][ly] += 1;
        paper[rx][ly] -= 1;
        paper[lx][ry] -= 1;
        paper[rx][ry] += 1;
    }
    rep(j, 0, 1000+9){
        rep(i, 1, 1000+9){
            paper[i][j] += paper[i-1][j];
        }
    }
    // for(int i=1; i < 1009; i++){
    //     for(int j=1008; j >= 2; j--){
    //         paper[i][j-1] += paper[i][j];
    //     }
    // }
    rep(i, 0, 1000+9){
        rep(j, 1, 1000+9){
            paper[i][j] += paper[i][j-1];
        }
    }

    vector<int> answer(n);
    rep(i, 0, 1000+9){
        rep(j, 0, 1000+9){
            if(paper[i][j] >= 1) answer[paper[i][j]] += 1;
        }
    }
    rep(i, 1, n+1) cout << answer[i] << endl;
    return 0;
}