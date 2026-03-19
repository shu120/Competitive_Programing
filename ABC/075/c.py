#C - Bridge
N, M = map(int, input().split())
edges = []
for _ in range(M):
    A, B = map(int, input().split())
    edges.append((A - 1, B - 1))

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

ans = 0

for i in range(M):
    uf = UnionFind(N)
    for j in range(M):
        if i == j:
            continue
        A, B = edges[j]
        uf.unite(A, B)

    if uf.size(0) != N:
        ans += 1

print(ans)
