N = int(input())
A = list(map(int, input().split()))
A.sort()

maxA = A[-1]
cand = set()
cand.add(maxA)

for i in range(N):
	cand.add(maxA + A[i])

ans = []

for L in cand:
	l = 0
	r = N - 1
	ok = True

	while l <= r:
		if A[r] == L:
			r -= 1
		else:
			if l == r or A[l] + A[r] != L:
				ok = False
				break
			l += 1
			r -= 1

	if ok:
		ans.append(L)

print(*sorted(ans))