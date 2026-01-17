#C - Sake or Water
N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

ps = [0] * (N + 1)
for i in range(N):
	ps[i + 1] = ps[i] + A[i]

ans = -1
for m in range(1, N + 1):
	k = K - (N - m)
	if k <= 0:
		continue

	l = N - m
	r = l + k
	s = ps[r] - ps[l]

	if s >= X:
		ans = m
		break

print(ans)