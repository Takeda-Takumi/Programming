#include <bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for (int i = s; i < (n); ++i)
using ll = long long;
using P = pair<int, int>;

ll base8_to_long(string N){
    ll res = 0;
    rep(i, 0, N.size()){
        res = res * 8 + int(N[i] - '0');
    }
    return res;
}

string long_to_base9(ll N){
    if(N == 0){
        return "0";
    }
    string res;
    while(N > 0){
        res = char(N%9 + '0') + res;
        N /= 9;
    }
    return res;
}

int main() {
   string N;
   int K;
   cin >> N >> K;
   rep(i,0,K){
       N = long_to_base9(base8_to_long(N));
       rep(j, 0, N.size()){
           if(N[j] == '8'){
               N[j] = '5';
           }
       }
   }
   cout << N << endl;
   return 0;
}
