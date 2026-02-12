N, T = map(int, input().split())

ans = 0
for _ in range(N):
	A, B = map(int, input().split())
	ans += max(A - B * T, 0)

print(ans)