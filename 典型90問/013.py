#013 - Passing（★5）
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(G, start):
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

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
	A, B, C = map(int, input().split())
	A -= 1
	B -= 1
	G[A].append((B, C))
	G[B].append((A, C))

dist_from_1 = dijkstra(G, 0)
dist_from_N = dijkstra(G, N - 1)

for i in range(N):
	print(dist_from_1[i] + dist_from_N[i])