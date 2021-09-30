/**
*    author:  Takeda Takumi
*    created: 2021.05.01 21:06:12
**/

#include <bits/stdc++.h>
#include <cmath>
using namespace std;
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main()
{
    int N, D, H;
    vector<int> d(1000);
    vector<int> h(1000);

    cin >> N >> D >> H;
    rep(i, 0, N)
    {
        cin >> d[i] >> h[i];
    }

    /*

    vector<int>::iterator iter = max_element(h.begin(), h.end());
    size_t index = distance(h.begin(), iter);

    double ans = (double)(D*h[index] - d[index]*H) / (D - d[index]);

    */

    vector<double> rad;

    rep(i,0,N){
        rad.push_back(atan2(h[i],d[i]));
        //cout << rad[i] << endl;
    }
    //cout << endl;

    vector<double>::iterator rad_iter = max_element(rad.begin(), rad.end());
    size_t rad_index = distance(rad.begin(), rad_iter);

    double ufo_rad = atan2(H, D);

    double ans = 0.0;
    if (ufo_rad < rad[rad_index])
    {
        //cout << rad_index << endl;
        ans = (double)(D * h[rad_index] - d[rad_index] * H) / (D - d[rad_index]);
    }

    //cout << (double)(D * h[3] - d[3] * H) / (D - d[3]) << endl;
    //cout << ans << endl;
    printf("%.13f\n",ans);

    return 0;
}