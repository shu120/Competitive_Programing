N, M = map(int, input().split())
counts = [0] * N

for _ in range(M):
	a, b = map(int, input().split())
	counts[a - 1] += 1
	counts[b - 1] += 1

for i in range(N):
	print(counts[i])