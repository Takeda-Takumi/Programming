/**
*    author:  Takeda Takumi
*    created: 2021.04.11 15:41:56
**/

#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

int main() {
   
   int a,b;
   cin >> a >> b;

   if((a*b) % 2){
       cout << "Odd" << endl;
   }else{
       cout << "Even" << endl;
   }
   
   return 0;
}