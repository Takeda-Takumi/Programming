#include<bits/stdc++.h>
using namespace std;

int main()
{
    int x = 0;
    char takahashi[5];

    std::cin >> takahashi;

    for (int i = 0; i < 4; i++)
    {
        if (takahashi[i] == '+')
        {
            x++;
        }
        else if (takahashi[i] == '-')
        {
            x--;
        }
    }
    printf("%d\n", x);
    return 0;
}