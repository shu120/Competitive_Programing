#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int X;
  cin >> X;

  if (X == 0){
    cout << "No" << endl;
    return 0;
  }

  if (X % 100 == 0)
    cout << "Yes" << endl;
  else
    cout << "No" << endl;

  return 0;
}
