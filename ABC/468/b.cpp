#include <bits/stdc++.h>
using namespace std;

int main(){
	int M, D;
	string S;
	cin >> M >> D >> S;
	int ans = 0;
	for(int x = 0; x < M; x++){
		bool watched = false;
		for(int i = 0; i < M; i++){
			if(S[i] == 'G' && abs(x - i) <= D){
				watched = true;
			}
		}
		if(watched == false){
			ans++;
		}
	}
	cout << ans;
}
