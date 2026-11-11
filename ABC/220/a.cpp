#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int A, B, C;
  cin >> A >> B >> C;

  for (int i = 1; C * i <= B; i++) {
    if (A <= C * i) {
      cout << C * i << endl;
      return 0;
    }
  }
  cout << -1 << endl;

  return 0;
}
