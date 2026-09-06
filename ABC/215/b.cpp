#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N;
    cin >> N;
    int ans = 0;
    for (int k = 0; ; k++) {
        if ((1LL << k) <= N) {
            ans = k;
        } else {
            break;
        }
    }
    cout << ans;
}
