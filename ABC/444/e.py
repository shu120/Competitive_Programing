from sortedcontainers import SortedSet, SortedList, SortedDict # pyright: ignore[reportMissingImports]
from bisect import bisect_left

N, D = map(int, input().split())
A = list(map(int, input().split()))

s = SortedSet()
ans = 0
R = 0

for L in range(N):
	while R < N:
		x = A[R]
		i = s.bisect_left(x)

		if i > 0 and x - s[i - 1] < D:
			break
		if i < len(s) and s[i] - x < D:
			break

		s.add(x)
		R += 1

	ans += R - L
	s.remove(A[L])

print(ans)