#TLE
from bisect import bisect_left

def add(x, s):
	pos = bisect_left(s, x)
	s.insert(pos, x)
def remove(x, s):
	pos = bisect_left(s, x)
	s.pop(pos)

N, D = map(int, input().split())
A =list(map(int, input().split()))

s = []
ans = 0
R = 0

for L in range(N):
	while R < N:
		x = A[R]
		pos = bisect_left(s, x)

		if pos > 0 and x - s[pos-1] < D:
			break
		if pos < len(s) and s[pos] - x < D:
			break

		add(x, s)
		R += 1

	ans += R - L
	remove(A[L], s)

print(ans)