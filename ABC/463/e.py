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


N, M, Y = map(int, input().split())

hub = 0
G = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, t = map(int, input().split())
    G[u].append((v, t))
    G[v].append((u, t))

X = [0] + list(map(int, input().split()))

for i in range(1, N + 1):
    G[i].append((hub, X[i] + Y))
    G[hub].append((i, X[i]))

dist = dijkstra(G, 1)

print(*dist[2:])
