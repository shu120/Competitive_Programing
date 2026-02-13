N, K = map(int, input().split())
A = list(map(int, input().split()))

B = A[:]

for i in range(1, N):
	B[i] = max(B[i], B[i-1] - K)

for i in range(N - 2, -1, -1):
	B[i] = max(B[i], B[i+1] - K)

ans = 0
for i in range(N):
	ans += B[i] - A[i]

print(ans)