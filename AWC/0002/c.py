N, M = map(int, input().split())

ans = 0
for _ in range(N):
	A, B = map(int, input().split())
	if A < M:
		d = (M - A + B - 1) // B
		ans = max(ans, d)

print(ans)