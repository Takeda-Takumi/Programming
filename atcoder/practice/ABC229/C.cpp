#include<bits/stdc++.h>
using namespace std;
int main(){
  long long n,w;
  cin >> n >> w;
  vector<pair<long long,long long>> v(n);
  for(auto &nx : v){
    cin >> nx.first >> nx.second;
  }
  cout << endl;
  sort(v.begin(),v.end());
  for(auto &nx : v){
      cout << nx.first  << " "<< nx.second << endl;
  }
  cout << '\n';
  reverse(v.begin(),v.end());

  for(auto &nx : v){
      cout << nx.first  << " "<< nx.second << endl;
  }
  cout << '\n';
  long long res=0;
  for(auto &nx : v){
    res+=nx.first*min(w,nx.second);
    w-=min(w,nx.second);
  }
  cout << res << '\n';
  return 0;
}