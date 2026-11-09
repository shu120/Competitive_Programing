#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
  int N, K, ans = 0;
  cin >> N >> K;
  vector<int> A(N);
  for (auto &x : A)
    cin >> x;

  for (int i = 0; i < N; i++) {
    if (A[i] == K)
      ans++;
  }
  for (int i = 0; i < N - 1; i++) {
    if ((A[i] < K && A[i + 1] > K) || (A[i] > K && A[i + 1] < K))
      ans++;
  }
  cout << ans << endl;

  return 0;
}
