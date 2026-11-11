#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  string S;
  cin >> S;

  if (S.substr(S.size() - 2) == "er")
    cout << "er" << endl;
  else
    cout << "ist" << endl;

  return 0;
}
