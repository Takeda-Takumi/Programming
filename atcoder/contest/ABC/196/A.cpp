/**
*    author:  Dooloper
*    created: 20.03.2021 20:53:11
**/

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a, b, c, d;
    cin >> a;
    cin >> b;
    cin >> c;
    cin >> d;
    /*
    cout << a;
    cout << b;
    cout << c;
    cout << d;
    */

    int max = -201;
    for (int x = a; x <= b; x++)
    {
        for (int y = c; y <= d; y++)
        {
            int tmp = x - y;
            if (max < tmp)
            {
                max = tmp;
            }
        }
    }

    cout << max;

    return 0;
}