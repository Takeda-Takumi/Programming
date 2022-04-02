#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main() {
    int x1, y1, x2, y2, x3, y3;
    cin >> x1 >> y1;
    cin >> x2 >> y2;
    cin >> x3 >> y3;

    int ans_x, ans_y;
    if (x1 == x2){
        ans_x = x3;
    } else if (x2 == x3) {
        ans_x = x1;
    } else {
        ans_x = x2;
    }

    if (y1 == y2){
        ans_y = y3;
    } else if (y2 == y3) {
        ans_y = y1;
    } else {
        ans_y = y2;
    }
    cout << ans_x << " " << ans_y << endl;
    return 0;
}