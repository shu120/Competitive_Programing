# D - Takahashi Tour
import sys

sys.setrecursionlimit(10**6)


def dfs(curr, pre):
    ans.append(curr + 1)

    for nxt in G[curr]:
        if nxt != pre:
            dfs(nxt, curr)
            ans.append(curr + 1)


N = int(input())

ans = []

G = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

for g in G:
    g.sort()

dfs(0, -1)

print(*ans)
