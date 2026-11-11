#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  string S, T;
  cin >> S >> T;

  if (S < T)
    cout << "Yes" << endl;
  else
    cout << "No" << endl;

  return 0;
}
