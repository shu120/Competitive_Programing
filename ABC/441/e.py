#E - A > B substring
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

N = int(input())
S = input()

pf = [0] * (N + 1)
for i in range(N):
	if S[i] == 'A':
		pf[i + 1] = pf[i] + 1
	elif S[i] == 'B':
		pf[i + 1] = pf[i] - 1
	else:
		pf[i + 1] = pf[i]

val = list(set(pf))
val.sort()

idx = {}
for i in range(len(val)):
	idx[val[i]] = i + 1

fw = Fenwick_Tree(len(val))
ans = 0

for i in range(N + 1):
	p = idx[pf[i]]
	ans += fw.sum(p - 1)
	fw.add(p, 1)

print(ans)