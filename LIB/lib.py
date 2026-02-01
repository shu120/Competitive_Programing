
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