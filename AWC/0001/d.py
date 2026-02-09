import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [0] * (N + 1)
B = [0] * (N + 1)

for i in range(1, N + 1):
	A[i], B[i] = map(int, input().split())

dp = [[-1] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
	if B[i] <= M:
		dp[i][B[i]] = A[i]

for i in range(1, N + 1):
	for j in range(max(1, i - K), i):
		for c in range(M + 1):
			if dp[j][c] == -1:
				continue
			nc = c + B[i]
			if nc <= M:
				dp[i][nc] = max(dp[i][nc], dp[j][c] + A[i])

ans = 0
for i in range(1, N + 1):
	ans = max(ans, max(dp[i]))

print(ans)