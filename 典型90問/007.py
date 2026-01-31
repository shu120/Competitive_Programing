#007 - CP Classes（★3）
from bisect import bisect_left
N = int(input())
A = sorted(map(int, input().split()))
Q = int(input())

for _ in range(Q):
	B = int(input())
	idx = bisect_left(A, B)

	cand = []
	if idx < N:
		cand.append(abs(A[idx] - B))
	if idx > 0:
		cand.append(abs(A[idx - 1] - B))

	print(min(cand))