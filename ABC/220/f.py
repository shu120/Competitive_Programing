# F - Distance Sums 2
import sys
sys.setrecursionlimit(10**7)

N = int(input())

G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

size = [1] * N
ans = [0] * N


def dfs(v, p, depth):
    ans[0] += depth

    for nv in G[v]:
        if nv == p:
            continue

        dfs(nv, v, depth + 1)
        size[v] += size[nv]


dfs(0, -1, 0)


def dfs2(v, p):
    for nv in G[v]:
        if nv == p:
            continue

        ans[nv] = ans[v] + N - 2 * size[nv]

        dfs2(nv, v)


dfs2(0, -1)

for x in ans:
    print(x)
