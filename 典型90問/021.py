#021 - Come Back in One Piece（★5）
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())

G = [[] for _ in range(N)]
RG = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    RG[B].append(A)

visited = [False] * N
order = []

def dfs(v):
    visited[v] = True
    for to in G[v]:
        if not visited[to]:
            dfs(to)
    order.append(v)

for v in range(N):
    if not visited[v]:
        dfs(v)

visited = [False] * N

def rdfs(v):
    stack = [v]
    visited[v] = True
    size = 1
    while stack:
        cur = stack.pop()
        for to in RG[cur]:
            if not visited[to]:
                visited[to] = True
                stack.append(to)
                size += 1
    return size

ans = 0

for v in reversed(order):
    if not visited[v]:
        size = rdfs(v)
        ans += size * (size - 1) // 2

print(ans)
