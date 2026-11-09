#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
  int Q;
  cin >> Q;

  map<string, int> mp;
  int ID = 1;

  for (int i = 0; i < Q; i++) {
    string s;
    cin >> s;
    if (mp.count(s)) {
      cout << mp[s] << endl;
    } else {
      mp[s] = ID;
      cout << ID << endl;
      ID++;
    }
  }
  return 0;
}
