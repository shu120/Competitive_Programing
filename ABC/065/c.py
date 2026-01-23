N, M = map(int, input().split())
MOD = 10 ** 9 + 7

if abs(N - M) >= 2:
	print(0)
else:
	ans = 1
	for i in range(1, N + 1):
		ans = (ans * i) % MOD
	for i in range(1, M + 1):
		ans = (ans * i) % MOD
	
	if N == M:
		ans = (2 * ans) % MOD
	print(ans)
