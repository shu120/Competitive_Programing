N, K, M = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
total = 0
r = 0

for l in range(N):
	while r < N and (r - l < K or total < M):
		total += A[r]
		r += 1

	if r - l < K or total < M:
		break

	ans += N - r + 1
	total -= A[l]

print(ans)