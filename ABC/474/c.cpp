#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
	int N, Q;
	cin >> N >> Q;
	vector<int>P(N);
	for(int i = 0; i <N; i++){
		cin >> P[i];
	}
	vector<int> X(N);
    for (int i = 0; i < N; i++) {
        P[i]--;
        X[P[i]] = i;
    }
    for (int i = 0; i < Q; i++) {
        int a;
        cin >> a;
        X[a - 1] = N + i;
    }
    vector<pair<int, int>> Y;
    for (int i = 0; i < N; i++) {
        Y.push_back({X[i], i});
    }
    sort(Y.begin(), Y.end());
    for (auto x : Y) {
        cout << x.second + 1 << ' ';
    }

	return 0;
}
