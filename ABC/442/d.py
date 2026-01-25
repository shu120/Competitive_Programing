import sys
input = sys.stdin.readline

class Fenwick_Tree:
	def __init__(self, n):
		self.n = n
		self.bit = [0] * (n + 1)

	def add(self, i, v):
		n = self.n
		bit = self.bit
		while i <= n:
			bit[i] += v
			i += i & -i

	def sum(self, i):
		s = 0
		bit = self.bit
		while i > 0:
			s += bit[i]
			i -= i & -i
		return s

N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))

bit = Fenwick_Tree(N)
for i in range(1, N + 1):
	bit.add(i, A[i])

out = []
for _ in range(Q):
	q = list(map(int, input().split()))
	if q[0] == 1:
		x = q[1]
		a = A[x]
		b = A[x + 1]
		if a != b:
			A[x], A[x + 1] = b, a
			bit.add(x, b - a)
			bit.add(x + 1, a - b)
	else:
		l = q[1]
		r = q[2]
		out.append(str(bit.sum(r) - bit.sum(l - 1)))

print("\n".join(out))