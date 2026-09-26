from heapq import heappush, heappop

N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


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


G = [[] for _ in range(N + 1)]
for i in range(N):
    j = (i + 1) % N
    G[i].append((j, A[i]))
    G[j].append((i, A[i]))
for i in range(N):
    G[i].append((N, B[i]))
    G[N].append((i, B[i]))

dist = dijkstra(G, N)

cum = [0] * (N + 1)

for i in range(N):
    cum[i + 1] = cum[i] + A[i]

total = cum[N]

for _ in range(Q):
    S, T = map(int, input().split())
    S -= 1
    T -= 1

    if T == N:
        print(dist[S])
        continue

    d = cum[T] - cum[S]
    cycle = min(d, total - d)

    print(min(cycle, dist[S] + dist[T]))
