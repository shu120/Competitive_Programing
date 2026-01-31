#003 - Longest Circular Road（★4）

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

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
	a, b = map(int, input().split())
	a, b = a - 1, b - 1
	G[a].append(b)
	G[b].append(a)

dist_0 = dfs(0, G, N)
u = dist_0.index(max(dist_0))

dist_u = dfs(u, G, N)
score = max(dist_u)

print(score + 1)