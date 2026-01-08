#E(TLE ver.)
# import sys
# input = sys.stdin.readline

# N, Q = map(int, input().split())
# A = list(map(int, input().split()))
# ans = []

# for _ in range(Q):
# 	t, x, y = map(int, input().split())
# 	if t == 1:
# 		A[x - 1] = y
# 	else:
# 		l, r = x, y
# 		s = 0
# 		for v in A:
# 			s += max(l, min(r, v))
# 		ans.append(s)

# print("\n".join(map(str, ans)))

#E
import sys
input = sys.stdin.readline

class Fenwick_Tree:
	def __init__(self, n):
		self.n = n
		self.bit = [0] * (n+1)

	def add(self, i, v):
		n = self.n
		bit = self.bit
		while i <= n:
			bit[i] += v
			i += i & -i

	def sum(self, i):
		s = 0
		while i > 0:
			s += self.bit[i]
			i -= i & -i
		return s

MAX = 5 * (10 ** 5)
N, Q = map(int, input().split())
A = list(map(int, input().split()))
Fencnt = Fenwick_Tree(MAX + 1)
Fensum = Fenwick_Tree(MAX + 1)

for v in A:
	Fencnt.add(v + 1, 1)
	Fensum.add(v + 1, v)
a = []

for i in range(Q):
	t, x, y = map(int, input().split())
	if t == 1:
		index = x - 1
		old = A[index]
		Fencnt.add(old + 1, -1)
		Fensum.add(old + 1, -old)
		A[index] = y
		Fencnt.add(y + 1, 1)
		Fensum.add(y + 1, y)
	else:
		l, r = x, y
		if l > r:
			a.append(l * N)
			continue

		ll = l + 1
		rr = r + 1
		cnt_low = Fencnt.sum(ll)
		sum_mid = Fensum.sum(rr - 1) - Fensum.sum(ll)
		total = Fencnt.sum(MAX + 1)
		cnt_high = total - Fencnt.sum(rr -  1)

		s = l * cnt_low + sum_mid + r * cnt_high
		a.append(s)

print("\n".join(map(str, a)))