/**
*    author:  Takeda Takumi
*    created: 06.04.2021 10:44:24
**/

#include <bits/stdc++.h>
using namespace std;
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;
using C = complex<double>;

C Cin()
{
    double a,b;
    cin >> a;
    cin >> b;

    C c = C(a,b);
    return c;
}


int main()
{
    int n;
    cin >> n;

    C c0 = Cin();
    C c1 = Cin();

    C center = (c0 + c1) / 2.0;

    //cout << c0 << c1 << endl;

    double PI = acos(-1);
    double arg = 2*PI / n;
    C r(cos(arg), sin(arg));
    
    C ans = center + (c0 - center) * r;

    printf("%.10f %.10f\n", ans.real(), ans.imag());

    return 0;
}