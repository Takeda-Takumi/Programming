/**
*    author:  Takeda Takumi
*    created: 2021.05.01 21:06:12
**/

#include <bits/stdc++.h>
using namespace std;
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main()
{

    string s;
    cin >> s;
    int count = 0;
    rep(i, 0, s.size() - 3)
    {
        if (s[i] == 'Z')
        {
            if (s[i + 1] == 'O')
            {
                if (s[i + 2] == 'N')
                {
                    if (s[i + 3 == 'e'])
                    {
                        count++;
                    }
                }
            }
        }
    }
    cout << count << endl;

    return 0;
}