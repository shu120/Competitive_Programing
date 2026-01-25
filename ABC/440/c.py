#C - Striped Horse
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
	N, W = map(int, input().split())
	C = list(map(int, input().split()))

	mod = 2 * W

	grp = [0] * mod
	for i in range(N):
		p = (i + 1) % mod
		grp[p] += C[i]

	cir = grp + grp
	L = len(cir)

	S = [0] * (L + 1)
	for i in range(L):
		S[i + 1] = S[i] + cir[i]

	ans = 10 ** 30
	for s in range(mod):
		cost = S[s + W] - S[s]
		if cost < ans:
			ans = cost

	print(ans)
