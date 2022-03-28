#include <bits/stdc++.h>
using namespace std;
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main()
{
    int N, P, Q;
    cin >> N >> P >> Q;
    int A[N];
    rep(i, 0, N)
    {
        cin >> A[i];
    }
    int ans = 0;
    rep(i, 0, N)
    {
        rep(j, i + 1, N)
        {
            rep(k, j + 1, N)
            {
                rep(l, k + 1, N)
                {
                    rep(m, l + 1, N)
                    {
                        // ll s = 1LL * A[i] * A[j] * A[k] * A[l] * A[m];
                        if (1LL * A[i] * A[j] % P * A[k] % P * A[l] % P * A[m] % P == Q)
                        {
                            ans++;
                        }
                    }
                }
            }
        }
    }
    cout << ans << endl;
    return 0;
}