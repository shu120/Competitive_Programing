import sys
input = sys.stdin.readline

class UnionFind:
	"""次に使える最小番号を管理するUnion-Find"""
	def __init__(self, n):
		self.par = list(range(n + 2))

	def find(self, x):
		while self.par[x] != x:
			self.par[x] = self.par[self.par[x]]
			x = self.par[x]
		return x

	def use(self, x):
		self.par[self.find(x)] = self.find(x + 1)

N, M = map(int, input().split())
cars = []

for _ in range(M):
	L, R = map(int, input().split())
	cars.append((R, L))

cars.sort()

uf = UnionFind(N)

for R, L in cars:
	pos = uf.find(L)
	
	if pos > R:
		print("No")
		exit()
	
	uf.use(pos)

print("Yes")