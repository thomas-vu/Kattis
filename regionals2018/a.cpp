#include <bits/stdc++.h>

using namespace std;

int main(){
  vector<int> a;
  for(int i = 0; i < 3; i++){
    int b; cin >> b;
    a.push_back(b);
  }

  sort(a.begin(), a.end());

  int con = min(a[1]-a[0], a[2]-a[1]);

  int ans = INT_MAX;
  for(int i = 0; i < 2; i++){
    int diff = a[i+1] - a[i];
    if(diff != con){
      ans = a[i] + con;
    }
  }

  if(ans == INT_MAX)
    cout << a[2] + con << endl;
  else
    cout << ans << endl;



  

  
}
