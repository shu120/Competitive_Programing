#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    int N;
    cin >> N;
    vector<ll> A(N), B(N);
    for (auto &x : A) cin >> x;
    for (auto &x : B) cin >> x;

    vector<ll> C(N, 1);
    for (int i = 0; i < N; i++) {
        if (A[i] > B[i]) {
            C[i] = 1'000'000'000'000'000'000LL;
        }
    }

    __int128 a = 0, b = 0;

    for (int i = 0; i < N; i++) {
        a += (__int128)A[i] * C[i];
        b += (__int128)B[i] * C[i];
    }

    if (a > b) {
        cout << "Yes" << '\n';
        for (auto x : C) {
            cout << x << ' ';
        }
    } else {
        cout << "No";
    }

    return 0;
}
