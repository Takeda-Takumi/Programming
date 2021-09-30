/**
*    author:  Takeda Takumi
*    created: 30.03.2021 16:14:34
**/

#include <bits/stdc++.h>
using namespace std;
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;
using C = complex<double>;
C inC(){
    double x, y;
    cin >> x >> y;
    return C(x,y);
}

int main()
{
    int n;
    cin >> n;
    C s = inC();
    C t = inC();
    C o = (s+t)/2.0;
    double PI = acos(-1);
    double rad = 2*PI/n;
    C r(cos(rad), sin(rad));
    C ans = o + (s-o)*r;
    printf("%.10f %.10f\n", ans.real(), ans.imag());
    return 0;

    

}