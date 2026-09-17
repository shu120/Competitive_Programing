# D - Restricted Permutation
import heapq
N, M = map(int, input().split())

G = [[] for _ in range(N)]
indeg = [0] * N
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    indeg[B] += 1

hq = []

for v in range(N):
    if indeg[v] == 0:
        heapq.heappush(hq, v)

ans = []

while hq:
    v = heapq.heappop(hq)
    ans.append(v)

    for nxt in G[v]:
        indeg[nxt] -= 1

        if indeg[nxt] == 0:
            heapq.heappush(hq, nxt)

if len(ans) != N:
    print(-1)
else:
    print(*(v + 1 for v in ans))
