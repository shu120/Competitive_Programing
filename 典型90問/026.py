#026 - Independent Set on a Tree（★4）
import sys
input = sys.stdin.readline


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
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

dist = dfs(0, G, N)

group0 = []
group1 = []

for i in range(N):
    if dist[i] % 2 == 0:
        group0.append(i + 1)
    else:
        group1.append(i + 1)

if len(group0) >= N // 2:
    print(*group0[:N // 2])
else:
    print(*group1[:N // 2])

