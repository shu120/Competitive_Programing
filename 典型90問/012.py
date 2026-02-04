#012 - Red Painting（★4）
import sys
input = sys.stdin.readline

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

H, W = map(int, input().split())
Q = int(input())

def idx(r, c):
	return r * W + c

UF = UnionFind(H * W)
red = [[False] * W for _ in range(H)]

for _ in range(Q):
	q = list(map(int, input().split()))
	if q[0] == 1:
		r, c = q[1] - 1, q[2] - 1
		red[r][c] = True
		for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
			nr, nc = r + dr, c + dc
			if 0 <= nr < H and 0 <= nc < W and red[nr][nc]:
				UF.unite(idx(r, c), idx(nr, nc))
	else:
		r1, c1, r2, c2 = q[1] - 1, q[2] - 1, q[3] - 1, q[4] - 1
		if red[r1][c1] and red[r2][c2] and UF.issame(idx(r1, c1), idx(r2, c2)):
			print("Yes")
		else:
			print("No")