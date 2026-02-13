import sys
input = sys.stdin.readline

class SegTree:
	def __init__(self, A):
		n = len(A)
		self.size = 1
		while self.size < n:
			self.size <<= 1
		self.data = [0] * (2 * self.size)
		
		# 葉
		for i in range(n):
			self.data[self.size + i] = A[i]
		
		# 構築
		for i in range(self.size - 1, 0, -1):
			self.data[i] = max(self.data[2*i], self.data[2*i+1])

	def query(self, l, r):
		# [l, r] の最大値
		l += self.size
		r += self.size
		res = 0
		while l <= r:
			if l & 1:
				res = max(res, self.data[l])
				l += 1
			if not (r & 1):
				res = max(res, self.data[r])
				r -= 1
			l >>= 1
			r >>= 1
		return res


N, Q = map(int, input().split())
A = list(map(int, input().split()))

seg = SegTree(A)

for _ in range(Q):
	L, R = map(int, input().split())
	print(seg.query(L - 1, R - 1))