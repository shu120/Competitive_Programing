# F - Blocked Roads
import sys
from collections import deque
input = sys.stdin.readline


def bfs(start, G, N, block=-1):
    """block番目の辺を使わないBFS"""
    dist = [-1] * N
    prev_edge = [-1] * N

    dist[start] = 0
    q = deque([start])

    while q:
        curr = q.popleft()

        for nxt, edge_id in G[curr]:
            if edge_id == block:
                continue

            if dist[nxt] == -1:
                dist[nxt] = dist[curr] + 1
                prev_edge[nxt] = edge_id
                q.append(nxt)

    return dist, prev_edge


N, M = map(int, input().split())

G = [[] for _ in range(N)]
edge = []

for i in range(M):
    s, t = map(int, input().split())
    s -= 1
    t -= 1

    G[s].append((t, i))
    edge.append((s, t))


dist, prev_edge = bfs(0, G, N)

if dist[N - 1] == -1:
    for _ in range(M):
        print(-1)

else:
    ans = [dist[N - 1]] * M

    path = []
    curr = N - 1

    while curr != 0:
        edge_id = prev_edge[curr]
        path.append(edge_id)

        s, _ = edge[edge_id]
        curr = s

    for edge_id in path:
        new_dist, _ = bfs(0, G, N, edge_id)
        ans[edge_id] = new_dist[N - 1]

    for x in ans:
        print(x)
