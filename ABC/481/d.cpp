#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int N, M, S, T;
  cin >> N >> M >> S >> T;

  S--;
  T--;

  vector<vector<int>> G(N);
  for (int i = 0; i < M; i++) {
    int a, b;
    cin >> a >> b;
    a--;
    b--;
    G[a].push_back(b);
  }
  vector<int> mn(N, -1);

  for (int v = 0; v < N; v++) {
    if (!G[v].empty())
      mn[v] = *min_element(G[v].begin(), G[v].end());
  }

  const int INF = 1e9;
  vector<int> dist(N, INF);
  deque<int> dq;

  dist[S] = 0;
  dq.push_back(S);

  while (!dq.empty()) {
    int v = dq.front();
    dq.pop_front();

    for (int to : G[v]) {
      int cost = (to == mn[v] ? 0 : 1);

      if (dist[to] > dist[v] + cost) {
        dist[to] = dist[v] + cost;

        if (cost == 0)
          dq.push_front(to);
        else
          dq.push_back(to);
      }
    }
  }

  if (dist[T] == INF)
    cout << -1 << endl;
  else
    cout << dist[T] << endl;

  return 0;
}
