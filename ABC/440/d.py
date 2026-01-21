#D - Forbidden List 2
import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

for _ in range(Q):
	X, Y = map(int, input().split())
	low = X
	high = X + Y + N
	lx = bisect_left(A, X)

	while low < high:
		mid = (low + high) // 2
		k = bisect_right(A, mid) - lx
		miss = (mid - X + 1) - k
		if miss >= Y:
			high = mid
		else:
			low = mid + 1
	
	print(low)