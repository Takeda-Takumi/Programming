#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main() {
    int a, b;
    cin >> a >> b;

    double r = sqrt(a*a + b*b);
    
    cout << a/r << " " << b/r << endl;
    return 0;
}