N, K = map(int, input().split())
pairs = []

for _ in range(N):
	a, b = map(int, input().split())
	pairs.append((a, b))

pairs.sort()

cum = 0
for a, b in pairs:
	cum += b
	if cum >= K:
		print(a)
		break