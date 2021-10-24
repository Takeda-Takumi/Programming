#include <bits/stdc++.h>
using namespace std;


bool isTriangel(int x1,int x2,int x3,int y1,int y2,int y3){
    return (((x1 - x2) * (y3 - y2) - (y1 - y2) * (x3 - x2)) != 0);
}

int main()
{
    int n;
    cin >> n;
    double x[600], y[600];
    for(int i = 0; i < n; i++){
        cin >> x[i] >> y[i];
    }

    int ans = 0;
    for(int i = 0; i < n; i++){
        for(int j = i+1; j < n; j++){
            for(int k = j+1; k < n; k++){
                if(isTriangel(x[i],x[j],x[k],y[i],y[j],y[k])){
                    ans++;
                }
            }
        }
    }

    cout << ans;

    return 0;
}