// D - Teleportation
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
	int N;
	cin >> N;
    vector<ll> X(N), Y(N);
    for (int i = 0; i < N; i++) {
        cin >> X[i] >> Y[i];
    }

	set<pair<ll, ll>> st;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (i == j) continue;
			ll dx = X[j] - X[i];
			ll dy = Y[j] - Y[i];
			ll g = gcd(abs(dx), abs(dy));

			dx /= g;
			dy /= g;

			st.insert({dx, dy});
		}
	}
	cout << st.size();

	return 0;
}
