N, M, K = map(int, input().split())
S = list(map(int, input().split()))

for _ in range(M):
	P, V = map(int, input().split())
	S[P - 1] = V

ans = 0
for s in S:
	if s < K:
		ans += 1

print(ans)