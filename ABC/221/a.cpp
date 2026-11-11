#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int A, B, ans;
  cin >> A >> B;

  ans = std::pow(32, A - B);

  cout << ans << endl;

  return 0;
}
