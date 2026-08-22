import sys
sys.setrecursionlimit(10**6)

T = int(input())


def solve():
    N, M = map(int, input().split())

    G = [[] for _ in range(N)]

    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1

        G[A].append(B)
        G[B].append(A)

    def dfs(start):
        color = [-1] * N
        parent = [-1] * N
        depth = [0] * N

        color[start] = 0
        stack = [start]

        while stack:
            curr = stack.pop()

            for nxt in G[curr]:
                if color[nxt] == -1:
                    color[nxt] = color[curr] ^ 1
                    parent[nxt] = curr
                    depth[nxt] = depth[curr] + 1
                    stack.append(nxt)

                elif color[nxt] == color[curr]:
                    return curr, nxt, parent, depth

        return -1, -1, parent, depth

    start, goal, parent, depth = dfs(0)

    if start == -1:
        print(-1)
        return

    left = []
    right = []

    u = start
    v = goal

    while depth[u] > depth[v]:
        left.append(u)
        u = parent[u]

    while depth[v] > depth[u]:
        right.append(v)
        v = parent[v]

    while u != v:
        left.append(u)
        right.append(v)

        u = parent[u]
        v = parent[v]

    left.append(u)

    cycle = left + right[::-1]

    print(len(cycle))
    print(*[v + 1 for v in cycle])


for _ in range(T):
    solve()
