#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  string S;
  cin >> S;

  set<char> st(S.begin(), S.end());

  if (st.size() == 1)
    cout << 1 << endl;
  else if (st.size() == 2)
    cout << 3 << endl;
  else
    cout << 6 << endl;

  return 0;
}
