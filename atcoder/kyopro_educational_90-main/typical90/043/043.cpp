#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int h, w;
int dist[1009][1009][4];
int sx, sy, gx, gy;
char s[1009][1009];

const int inf = 1012345678;
const int dx[4] = {1, 0, -1, 0};
const int dy[4] = {0, 1, 0, -1};

struct state{
    int x, y, dir;
};

int main() {
    cin >> h >> w;
    cin >> sx >> sy;
    cin >> gx >> gy;
    --sx, --sy, --gx, --gy;
    rep(i, 0, h){
        cin >> s[i];
    }
    rep(i, 0, h){
        rep(j, 0, w){
            dist[i][j][0] = inf;
            dist[i][j][1] = inf;
            dist[i][j][2] = inf;
            dist[i][j][3] = inf;
        }
    }
    deque<state> deq;
    rep(i, 0, 4){
        dist[sx][sy][i] = 0;
        deq.push_back({sx, sy, i});
    }
    while (!deq.empty()) {
        state u = deq.front(); deq.pop_front();
        rep (i, 0, 4) {
            int tx = u.x + dx[i], ty = u.y + dy[i], cost = dist[u.x][u.y][u.dir] + (u.dir != i ? 1 : 0);
            if (0 <= tx && tx < h && 0 <= ty && ty < w && s[tx][ty] == '.' && dist[tx][ty][i] > cost){
                dist[tx][ty][i] = cost;
                if (u.dir != i) deq.push_back({tx, ty, i});
                else deq.push_front({tx, ty, i});
            }
        }
    }
    int answer = inf;
    rep (i, 0, 4) {
        answer = min(answer, dist[gx][gy][i]);
    }
    cout << answer << endl;
    return 0;
}