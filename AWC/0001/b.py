N, L, R = map(int, input().split())
P = list(map(int, input().split()))

best = -1
ans = -1

for i, score in enumerate(P, start = 1):
	if L <= score <= R:
		if score > best:
			best = score
			ans = i

print(ans)