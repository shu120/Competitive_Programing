#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
	int N;
	cin >> N;
	vector<int>P(N);
	for(int i = 0; i <N; i++){
		cin >> P[i];
	}

	bool ok = true;

	for(int i = 0; i < N; i++){
		if(i / 10 != (P[i] - 1) / 10){
			ok = false;
		}
	}

	if(ok){
		cout << "Yes";
	} else {
		cout << "No";
	}

	return 0;
}
