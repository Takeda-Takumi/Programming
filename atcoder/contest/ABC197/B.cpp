/**
*    author:  Takeda Takumi
*    created: 27.03.2021 21:02:59
**/

#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int h, w;

ll find(int x, int y, int map[][101])
{
    ll res = 1;
    int i, j;

    i = x - 1;
    j = y;
    while (1 <= i && map[i][j] == 0)
    {
        res++;
        i--;
    }
    //cout << res << endl;

    i = x;
    j = y + 1;
    while (j <= w && map[i][j] == 0)
    {
        res++;
        j++;
    }
    //cout << res << endl;

    i = x + 1;
    j = y;
    while (i <= h && map[i][j] == 0)
    {
        res++;
        i++;
    }
    //cout << res << endl;

    i = x;
    j = y - 1;
    while (1 <= j && map[i][j] == 0)
    {
        res++;
        j--;
    }
    //cout << res << endl;

    return res;
}

int main()
{
    int x, y;
    cin >> h >> w >> x >> y;

    int map[101][101];
    for (int i = 1; i <= h; ++i)
    {
        for (int j = 1; j <= w; ++j)
        {
            map[i][j] = 0;
        }
    }
    for (int i = 1; i <= h; i++)
    {
        string s;
        cin >> s;
        for (int j = 1; j <= w; j++)
        {
            if (s[j - 1] == '#')
            {
                map[i][j] = 1;
            }
        }
    }
    /*
    for (int i = 1; i <= h; ++i)
    {
        for (int j = 1; j <= w; ++j)
        {
            cout << map[i][j];
        }
        cout << endl;
    }
    */
    cout << find(x, y, map) << endl;

    return 0;
}