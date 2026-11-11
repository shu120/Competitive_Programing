#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  string N;
  cin >> N;

  while (N.size() != 4)
    N = "0" + N;

  cout << N << endl;

  return 0;
}
