N, K = map(int, input().split())

ans = 0
for _ in range(N):
	A, B = map(int, input().split())
	if A * B >= K:
		ans += 1

print(ans)