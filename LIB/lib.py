
def dfs(start, G, N):
	"""DFS(stack): startからの各頂点への距離を返す（到達不能は-1）"""
	dist = [-1] * N
	dist[start] = 0
	stack = [start]
	while stack:
		curr = stack.pop()
		for nxt in G[curr]:
			if dist[nxt] == -1:
				dist[nxt] = dist[curr] + 1
				stack.append(nxt)
	return dist

from collections import deque
def bfs(start, G, N):
	"""BFS(queue): startからの各頂点への最短距離を返す（到達不能は-1）"""
	dist = [-1] * N
	dist[start] = 0
	q = deque([start])
	while q:
		curr = q.popleft()
		for nxt in G[curr]:
			if dist[nxt] == -1:
				dist[nxt] = dist[curr] + 1
				q.append(nxt)
	return dist

class Fenwick_Tree:
	"""Fenwick Tree (BIT)
	1-indexed / 点更新・前方和クエリ
	"""
	def __init__(self, n):
		self.n = n
		self.bit = [0] * (n + 1)
	def add(self, i, v):
		"""i番目に v を加算"""
		while i <= self.n:
			self.bit[i] += v
			i += i & -i
	def sum(self, i):
		"""[1, i] の和を返す"""
		s = 0
		while i > 0:
			s += self.bit[i]
			i -= i & -i
		return s

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

from heapq import heappush, heappop
def dijkstra(G, start):
	"""Dijkstra法"""
	N = len(G)
	inf = 1 << 62
	dist = [inf] * N
	dist[start] = 0
	q = [(0, start)]
	while q:
		dv, v = heappop(q)
		if dist[v] != dv:
			continue
		for u, cost in G[v]:
			du = dv + cost
			if du < dist[u]:
				dist[u] = du
				heappush(q, (du, u))
	return dist

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