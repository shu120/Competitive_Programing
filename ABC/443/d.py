import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
	N = int(input())
	R = list(map(int, input().split()))

	L = [0] * N
	R2 = [0] * N

	L[0] = R[0]
	for i in range(1, N):
		L[i] = min(R[i], L[i - 1] + 1)

	R2[N - 1] = R[N - 1]
	for i in range(N - 2, -1, -1):
		R2[i] = min(R[i], R2[i + 1] + 1)

	ans = 0
	for i in range(N):
		x = min(L[i], R2[i])
		ans += R[i] - x

	print(ans)