import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

N, S = map(int, input().split())
A = list(map(int, input().split()))

mid = N // 2
A1 = A[:mid]
A2 = A[mid:]

L = []
for mask in range(1 << len(A1)):
	s = 0
	for i in range(len(A1)):
		if mask & (1 << i):
			s += A1[i]
	L.append(s)
R = []
for mask in range(1 << len(A2)):
	s = 0
	for i in range(len(A2)):
		if mask & (1 << i):
			s += A2[i]
	R.append(s)

R.sort()

ans = 0
for i in L:
	need = S - i
	ans += bisect_right(R, need) - bisect_left(R, need)

print(ans)