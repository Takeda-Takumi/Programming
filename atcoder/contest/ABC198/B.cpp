/**
*    author:  Takeda Takumi
*    created: 2021.04.11 20:54:40
**/

#include <bits/stdc++.h>
using namespace std;
#define rep(i, s, n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;


int main()
{
    string str;
    cin >> str;   
    int n = str.length();
    string s;

    rep(i,0,n)
    {
        if(str[i] != '0')
        {
            s = s + str[i];
        }else{
            break;
        }
    }

    //cout << s << endl;

    int size = s.length();
    bool f = false;
    
    rep(i, 0, size/2)
    {
        if(s[i] != s[size-i-1])
        {
            f = true;
            break;
        }
    }

    if(f){
        cout << "No" << endl;
    }else{
        cout << "Yes" << endl;
    }

    return 0;
}