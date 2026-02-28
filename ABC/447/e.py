import sys
input = sys.stdin.readline
MOD = 998244353

class UnionFind:
	"""Union-Find（Disjoint Set Union）
	0-indexed / 連結判定・サイズ管理
	"""
	def __init__(self, n):
		"""n 要素の Union-Find を初期化"""
		self.par = [-1] * n
		self.siz = [1] * n
	def root(self, x):
		"""x が属する集合の根を返す"""
		if self.par[x] == -1:
			return x
		self.par[x] = self.root(self.par[x])
		return self.par[x]
	def issame(self, x, y):
		"""x と y が同じ集合に属するか判定"""
		return self.root(x) == self.root(y)
	def unite(self, x, y):
		"""x と y の属する集合を併合する（成功時 True）"""
		x = self.root(x)
		y = self.root(y)
		if x == y:
			return False
		if self.siz[x] < self.siz[y]:
			x, y = y, x
		self.par[y] = x
		self.siz[x] += self.siz[y]
		return True
	def size(self, x):
		"""x が属する集合の要素数を返す"""
		return self.siz[self.root(x)]

N, M = map(int, input().split())
U = [0] * (M + 1)
V = [0] * (M + 1)
for i in range(1, M + 1):
	u, v = map(int, input().split())
	U[i] = u - 1
	V[i] = v - 1

pow2 = [1] * (M + 1)
for i in range(1, M + 1):
	pow2[i] = (pow2[i - 1] * 2) % MOD

uf = UnionFind(N)
comp = N
for i in range(M, 0, -1):
	if comp == 2:
		break
	if uf.unite(U[i], V[i]):
		comp -= 1

ans = 0
for i in range(1, M + 1):
	if not uf.issame(U[i], V[i]):
		ans = (ans + pow2[i]) % MOD

print(ans)